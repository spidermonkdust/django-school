# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Variant'
        db.delete_table('school_variant')

        # Deleting model 'AnswerableQuestion'
        db.delete_table('school_answerablequestion')

        # Deleting model 'VariantQuestion'
        db.delete_table('school_variantquestion')

        # Adding field 'Question.variants'
        db.add_column('school_question', 'variants', self.gf('django.db.models.fields.TextField')(default=0), keep_default=False)

        # Adding field 'Question.answer'
        db.add_column('school_question', 'answer', self.gf('django.db.models.fields.SmallIntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Adding model 'Variant'
        db.create_table('school_variant', (
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school.VariantQuestion'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('right', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('school', ['Variant'])

        # Adding model 'AnswerableQuestion'
        db.create_table('school_answerablequestion', (
            ('answer', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('question_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['school.Question'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('school', ['AnswerableQuestion'])

        # Adding model 'VariantQuestion'
        db.create_table('school_variantquestion', (
            ('question_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['school.Question'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('school', ['VariantQuestion'])

        # Deleting field 'Question.variants'
        db.delete_column('school_question', 'variants')

        # Deleting field 'Question.answer'
        db.delete_column('school_question', 'answer')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'school.announcement': {
            'Meta': {'object_name': 'Announcement'},
            'assignment': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.Course']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'school.assignment': {
            'Meta': {'object_name': 'Assignment'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.Course']"}),
            'due': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'school.attempt': {
            'Meta': {'object_name': 'Attempt'},
            'assignment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.Assignment']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'points': ('django.db.models.fields.FloatField', [], {}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.Student']"})
        },
        'school.course': {
            'Meta': {'object_name': 'Course'},
            'faq': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.Faq']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'schedule': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.Schedule']"})
        },
        'school.exercises': {
            'Meta': {'object_name': 'Exercises', '_ormbases': ['school.Assignment']},
            'assignment_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['school.Assignment']", 'unique': 'True', 'primary_key': 'True'})
        },
        'school.faq': {
            'Meta': {'object_name': 'Faq'},
            'html': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'school.lecture': {
            'Meta': {'object_name': 'Lecture'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.Course']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'school.material': {
            'Meta': {'object_name': 'Material'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lecture': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.Lecture']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '300'})
        },
        'school.question': {
            'Meta': {'object_name': 'Question'},
            'answer': ('django.db.models.fields.SmallIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quiz': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.Quiz']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'variants': ('django.db.models.fields.TextField', [], {})
        },
        'school.quiz': {
            'Meta': {'object_name': 'Quiz', '_ormbases': ['school.Assignment']},
            'assignment_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['school.Assignment']", 'unique': 'True', 'primary_key': 'True'})
        },
        'school.schedule': {
            'Meta': {'object_name': 'Schedule'},
            'html': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'school.student': {
            'Meta': {'object_name': 'Student'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['school']
