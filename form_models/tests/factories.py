from django.conf import settings
from django.template.defaultfilters import slugify

import factory

from form_models.models import Form, Field, ChoiceOption, Fieldset, Widget


class FormFactory(factory.DjangoModelFactory):
    class Meta:
        model = Form

    name = 'Name'


class FieldFactory(factory.DjangoModelFactory):
    class Meta:
        model = Field

    form = factory.SubFactory(FormFactory)
    name = 'Name'
    key = factory.LazyAttributeSequence(lambda a, n: slugify('{0}-{1}'.format(a.name, n)))
    field_type = 'number'


class ChoiceOptionFactory(factory.DjangoModelFactory):
    class Meta:
        model = ChoiceOption

    field = factory.SubFactory(FieldFactory, field_type='choice')
    name = 'Name'


class FieldsetFactory(factory.DjangoModelFactory):
    class Meta:
        model = Fieldset

    form = factory.SubFactory(FormFactory)
    legend = 'Legend'


class WidgetFactory(factory.DjangoModelFactory):
    class Meta:
        model = Widget

    widget_type = settings.FORM_MODELS_WIDGETS[0][0]
