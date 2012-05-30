from django.contrib import admin

from orderable.admin import OrderableAdmin

from .models import Form, Fieldset, Field, ChoiceOption, Widget


class ChoiceOptionInline(admin.TabularInline):
    model = ChoiceOption


class FieldAdmin(OrderableAdmin):
    prepopulated_fields = {'key': ('name',)}
    list_display = ('name', 'form', 'fieldset', 'widget', 'sort_order_display')
    list_editable = ('fieldset', 'widget')
    inlines = [ChoiceOptionInline]


class FieldInline(admin.TabularInline):
    model = Field
    prepopulated_fields = {'key': ('name',)}


class FormAdmin(admin.ModelAdmin):
    inlines = [FieldInline]


admin.site.register(Form, FormAdmin)
admin.site.register(Fieldset)
admin.site.register(Field, FieldAdmin)
admin.site.register(ChoiceOption)
admin.site.register(Widget)
