from django import forms
from django.test import TestCase

from tools import assert_equal, assert_true

from factories import FormFactory, FieldFactory, ChoiceOptionFactory


class BasicModelLayoutTest(TestCase):

    def test_basic_model_creation(self):
        """You should be able to add a form."""
        form = FormFactory.create()
        field = FieldFactory.create()
        choice = ChoiceOptionFactory.create()


class TestFields(TestCase):

    def test_number_field(self):
        field = FieldFactory.build(field_type='number')
        assert_true(isinstance(field.get_django_field(), forms.IntegerField))

    def test_percentage_field(self):
        field = FieldFactory.build(field_type='percentage')
        assert_true(isinstance(field.get_django_field(), forms.FloatField))

    def test_free_text_field(self):
        field = FieldFactory.build(field_type='free text')
        assert_true(isinstance(field.get_django_field(), forms.CharField))

    def test_choice_field(self):
        # Have to use create here because of how field generation works
        choice = ChoiceOptionFactory.create()
        field = choice.field
        dj_field = field.get_django_field()
        assert_true(isinstance(dj_field, forms.ChoiceField))
        assert_equal(choice.name, dj_field.choices[-1][1])


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
