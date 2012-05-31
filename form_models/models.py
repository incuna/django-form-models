from django.conf import settings
from django.db import models
from django import forms

from appconf import AppConf
from orderable.models import Orderable


class FormModelsAppConf(AppConf):
    WIDGETS = ()


class Form(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    def get_django_form_class(self, base_class=forms.Form, fields=None):
        if not fields:
            fields = self.field_set.all().select_related('widget')
        field_map = dict((f.key, f.get_django_field()) for f in fields)
        return type('DynamicForm%s' % self.pk, (base_class,), field_map)

    def get_layout(self, fields):
        from crispy_forms.layout import Fieldset as LayoutFieldset, Div
        layout = []
        used_fields = []
        for fieldset in self.fieldsets.all():
            fieldset_fields = []
            for field in fields:
                if field.fieldset_id == fieldset.pk:
                    fieldset_fields.append(field)
                    used_fields.append(field)

            widget = None
            for field in fieldset_fields:
                if field.widget and field.widget == widget:
                    # append to the previous widget
                    fieldset_fields[fieldset_fields.index(field) - 1].fields += (field.key,)
                    fieldset_fields[fieldset_fields.index(field)] = None
                elif not field.widget == widget:
                    # create the widget
                    widget = field.widget
                    if widget:
                        fieldset_fields[fieldset_fields.index(field)] = Div(field.key, css_class=field.widget.widget_type)
                    else:
                        fieldset_fields[fieldset_fields.index(field)] = field.key
                else:
                    # just swap in the key
                    fieldset_fields[fieldset_fields.index(field)] = field.key
            layout.append(LayoutFieldset(fieldset.legend, *filter(None, fieldset_fields)))
        layout = [field.key for field in fields if field not in used_fields] + layout
        return layout

    @property
    def num_fields(self):
        if not hasattr(self, '_num_fields'):
            self._num_fields = self.field_set.count()
        return self._num_fields


class Fieldset(Orderable):
    form = models.ForeignKey(Form, related_name='fieldsets')
    legend = models.CharField(max_length=200)

    def __unicode__(self):
        return self.legend


class Widget(models.Model):
    widget_type = models.CharField(max_length=200, choices=settings.FORM_MODELS_WIDGETS)

    def __unicode__(self):
        return u'Widget %d (%s)' % (self.pk, self.get_widget_type_display())


class Field(Orderable):
    FIELD_CHOICES = (
        ('number', 'Number'),
        ('percentage', 'Percentage'),
        ('choice', 'Choice'),
        ('free text', 'Free Text'),
    )
    DJANGO_FIELDS = {
        'number': forms.IntegerField,
        'percentage': forms.FloatField,
        'choice': forms.ChoiceField,
        'free text': forms.CharField,
    }
    form = models.ForeignKey(Form)
    fieldset = models.ForeignKey(Fieldset, blank=True, null=True)
    widget = models.ForeignKey(Widget, blank=True, null=True)
    name = models.CharField(max_length=200)
    key = models.SlugField()
    field_type = models.CharField(max_length=200, choices=FIELD_CHOICES)

    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = ('form', 'key')
        ordering = ('fieldset', 'sort_order')

    def get_django_field(self):
        field_class = self.DJANGO_FIELDS[self.field_type]
        kwargs = {
            'label': self.name,
            'required': False,
        }
        if self.field_type == 'choice':
            kwargs['choices'] = [(None, '-----')] + [(c.pk, c.name) for c in self.choices.all()]
        if self.field_type == 'percentage':
            kwargs['min_value'] = 0
            kwargs['max_value'] = 100
        field = field_class(**kwargs)
        return field


class ChoiceOption(models.Model):
    field = models.ForeignKey(Field, related_name='choices')
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name
