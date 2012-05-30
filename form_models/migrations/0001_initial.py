# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Form'
        db.create_table('formbuilder_form', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('formbuilder', ['Form'])

        # Adding model 'Field'
        db.create_table('formbuilder_field', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('form', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['formbuilder.Form'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('key', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('field_type', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('formbuilder', ['Field'])

        # Adding unique constraint on 'Field', fields ['form', 'key']
        db.create_unique('formbuilder_field', ['form_id', 'key'])

        # Adding model 'ChoiceOption'
        db.create_table('formbuilder_choiceoption', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('field', self.gf('django.db.models.fields.related.ForeignKey')(related_name='choices', to=orm['formbuilder.Field'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('formbuilder', ['ChoiceOption'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Field', fields ['form', 'key']
        db.delete_unique('formbuilder_field', ['form_id', 'key'])

        # Deleting model 'Form'
        db.delete_table('formbuilder_form')

        # Deleting model 'Field'
        db.delete_table('formbuilder_field')

        # Deleting model 'ChoiceOption'
        db.delete_table('formbuilder_choiceoption')


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
            'form': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['formbuilder.Form']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'formbuilder.form': {
            'Meta': {'object_name': 'Form'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['formbuilder']
