# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Fieldset'
        db.create_table('formbuilder_fieldset', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('form', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['formbuilder.Form'])),
            ('legend', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('formbuilder', ['Fieldset'])

        # Adding field 'Field.sort_order'
        db.add_column('formbuilder_field', 'sort_order', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True), keep_default=False)

        # Adding field 'Field.fieldset'
        db.add_column('formbuilder_field', 'fieldset', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['formbuilder.Fieldset'], null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'Fieldset'
        db.delete_table('formbuilder_fieldset')

        # Deleting field 'Field.sort_order'
        db.delete_column('formbuilder_field', 'sort_order')

        # Deleting field 'Field.fieldset'
        db.delete_column('formbuilder_field', 'fieldset_id')


    models = {
        'formbuilder.choiceoption': {
            'Meta': {'object_name': 'ChoiceOption'},
            'field': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'choices'", 'to': "orm['formbuilder.Field']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'formbuilder.field': {
            'Meta': {'unique_together': "(('form', 'key'),)", 'object_name': 'Field'},
            'field_type': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'fieldset': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['formbuilder.Fieldset']", 'null': 'True', 'blank': 'True'}),
            'form': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['formbuilder.Form']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'formbuilder.fieldset': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'Fieldset'},
            'form': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['formbuilder.Form']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legend': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'formbuilder.form': {
            'Meta': {'object_name': 'Form'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['formbuilder']
