from django import forms


class BaseField(object):

    def get_field_kwargs(self, instance):
        return {}


class CharField(BaseField):
    identifier = 'char'
    name = 'Character Field'
    django_field = forms.CharField


class NumberField(BaseField):
    identifier = 'number'
    name = 'Number Field'
    django_field = forms.IntegerField


class PercentageField(BaseField):
    identifier = 'percentage'
    name = 'Percentage Field'
    django_field = forms.FloatField

    def get_field_kwargs(self, instance):
        return {'min_value': 0, 'max_value': 100}


class ChoiceField(BaseField):
    identifier = 'choice'
    name = 'Choice Field'
    django_field = forms.ChoiceField

    def get_field_kwargs(self, instance):
        return {'choices': [(None, '-----')] + [(c.pk, c.name) for c in instance.choices.all()]}
