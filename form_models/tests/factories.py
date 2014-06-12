from django.conf import settings
from django.template.defaultfilters import slugify

import factory

from form_models.models import Form, Field, ChoiceOption, Fieldset, Widget


class FormFactory(factory.Factory):
    FACTORY_FOR = Form

    name = 'Name'


class FieldFactory(factory.Factory):
    FACTORY_FOR = Field

    form = factory.SubFactory(FormFactory)
    name = 'Name'
    key = factory.LazyAttributeSequence(lambda a, n: slugify('{0}-{1}'.format(a.name, n)))
    field_type = 'number'


class ChoiceOptionFactory(factory.Factory):
    FACTORY_FOR = ChoiceOption

    field = factory.SubFactory(FieldFactory, field_type='choice')
    name = 'Name'


class FieldsetFactory(factory.Factory):
    FACTORY_FOR = Fieldset

    form = factory.SubFactory(FormFactory)
    legend = 'Legend'


class WidgetFactory(factory.Factory):
    FACTORY_FOR = Widget

    widget_type = settings.FORM_MODELS_WIDGETS[0][0]
