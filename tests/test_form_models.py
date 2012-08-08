from django import forms
from django.test import TestCase

from crispy_forms.layout import Div, Fieldset as LayoutFieldset

from form_models.models import Widget, FormModelsAppConf

from factories import FormFactory, FieldFactory, ChoiceOptionFactory, WidgetFactory, FieldsetFactory
from tools import assert_equal, assert_true


class TestFields(TestCase):

    def test_number_field(self):
        field = FieldFactory.build(field_type='number')
        assert_true(isinstance(field.get_django_field(), forms.IntegerField))

    def test_percentage_field(self):
        field = FieldFactory.build(field_type='percentage')
        assert_true(isinstance(field.get_django_field(), forms.FloatField))

    def test_choice_field(self):
        field = FieldFactory.build(field_type='char')
        assert_true(isinstance(field.get_django_field(), forms.CharField))

    def test_choice_field(self):
        # Have to use create here because of how field generation works
        choice = ChoiceOptionFactory.create()
        field = choice.field
        dj_field = field.get_django_field()
        assert_true(isinstance(dj_field, forms.ChoiceField))
        assert_equal(choice.name, dj_field.choices[-1][1])

    def test_no_slug_provided(self):
        field = FieldFactory.create(name='hello', key='')
        assert_equal(field.key, 'hello')


class TestFormGeneration(TestCase):

    def test_simple_form(self):
        form = FormFactory.build()
        dj_form = form.get_django_form_class()
        assert_true(issubclass(dj_form, forms.Form))

    def test_field_in_form(self):
        form = FormFactory.build()
        field = FieldFactory.build(form=form)
        dj_form = form.get_django_form_class(fields=[field])
        assert_equal(len(dj_form.base_fields), 1)
        assert_equal(type(dj_form.base_fields.values()[0]), type(field.get_django_field()))


class TestWidgets(TestCase):

    def test_settings(self):
        assert_equal(Widget._meta.get_field_by_name('widget_type')[0].choices, FormModelsAppConf.WIDGETS)

    def test_widget_layout(self):
        widget = WidgetFactory.create()
        field1 = FieldFactory.create(widget=widget)
        field2 = FieldFactory.create(widget=widget, form=field1.form)
        layout = field1.form.get_layout()
        assert_equal(len(layout), 1)
        assert_true(isinstance(layout[0], Div))
        assert_equal(layout[0].css_class, widget.widget_type)
        assert_true(field1.key in layout[0].fields)
        assert_true(field2.key in layout[0].fields)

    def test_widgets_in_fieldsets(self):
        widget = WidgetFactory.create()
        fieldset = FieldsetFactory.create()
        field1 = FieldFactory.create(fieldset=fieldset, widget=widget, form=fieldset.form)
        field2 = FieldFactory.create(fieldset=fieldset, widget=widget, form=fieldset.form)
        layout = fieldset.form.get_layout()
        assert_equal(len(layout), 1)
        assert_true(isinstance(layout[0], LayoutFieldset))
        assert_equal(len(layout[0].fields), 1)
        layout_widget = layout[0].fields[0]
        assert_true(isinstance(layout_widget, Div))
        assert_equal(layout_widget.css_class, widget.widget_type)
        assert_true(field1.key in layout_widget.fields)
        assert_true(field2.key in layout_widget.fields)
