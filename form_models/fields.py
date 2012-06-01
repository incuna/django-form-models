from django import forms


class BaseField(object):

    def get_field_kwargs(self, instance):
        return {}


class CharField(BaseField):
    identifier = 'char'
    django_field = forms.CharField


class NumberField(BaseField):
    identifier = 'number'
    django_field = forms.IntegerField


class PercentageField(BaseField):
    identifier = 'percentage'
    django_field = forms.FloatField

    def get_field_kwargs(self, instance):
        return {'min_value': 0, 'max_value': 100}


class ChoiceField(BaseField):
    identifier = 'choice'
    django_field = forms.ChoiceField

    def get_field_kwargs(self, instance):
        return {'choices': [(None, '-----')] + [(c.pk, c.name) for c in instance.choices.all()]}
