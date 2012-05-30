# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Widget'
        db.create_table('formbuilder_widget', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('widget_type', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('formbuilder', ['Widget'])

        # Adding field 'Field.widget'
        db.add_column('formbuilder_field', 'widget',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['formbuilder.Widget'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Widget'
        db.delete_table('formbuilder_widget')

        # Deleting field 'Field.widget'
        db.delete_column('formbuilder_field', 'widget_id')


    models = {
        'formbuilder.choiceoption': {
            'Meta': {'object_name': 'ChoiceOption'},
            'field': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'choices'", 'to': "orm['formbuilder.Field']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'formbuilder.field': {
            'Meta': {'ordering': "('fieldset', 'sort_order')", 'unique_together': "(('form', 'key'),)", 'object_name': 'Field'},
            'field_type': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'fieldset': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['formbuilder.Fieldset']", 'null': 'True', 'blank': 'True'}),
            'form': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['formbuilder.Form']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'widget': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['formbuilder.Widget']", 'null': 'True', 'blank': 'True'})
        },
        'formbuilder.fieldset': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'Fieldset'},
            'form': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fieldsets'", 'to': "orm['formbuilder.Form']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legend': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'formbuilder.form': {
            'Meta': {'object_name': 'Form'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'formbuilder.widget': {
            'Meta': {'object_name': 'Widget'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'widget_type': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['formbuilder']