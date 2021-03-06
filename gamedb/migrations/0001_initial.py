# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GameBase'
        db.create_table('gamedb_gamebase', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('added_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('gamedb', ['GameBase'])

        # Adding M2M table for field owners on 'GameBase'
        db.create_table('gamedb_gamebase_owners', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('gamebase', models.ForeignKey(orm['gamedb.gamebase'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('gamedb_gamebase_owners', ['gamebase_id', 'user_id'])

        # Adding M2M table for field disposers on 'GameBase'
        db.create_table('gamedb_gamebase_disposers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('gamebase', models.ForeignKey(orm['gamedb.gamebase'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('gamedb_gamebase_disposers', ['gamebase_id', 'user_id'])

        # Adding M2M table for field rules_known_by on 'GameBase'
        db.create_table('gamedb_gamebase_rules_known_by', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('gamebase', models.ForeignKey(orm['gamedb.gamebase'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('gamedb_gamebase_rules_known_by', ['gamebase_id', 'user_id'])

        # Adding model 'Game'
        db.create_table('gamedb_game', (
            ('gamebase_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['gamedb.GameBase'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('gamedb', ['Game'])

        # Adding M2M table for field similar_games on 'Game'
        db.create_table('gamedb_game_similar_games', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_game', models.ForeignKey(orm['gamedb.game'], null=False)),
            ('to_game', models.ForeignKey(orm['gamedb.game'], null=False))
        ))
        db.create_unique('gamedb_game_similar_games', ['from_game_id', 'to_game_id'])

        # Adding model 'GameExpansion'
        db.create_table('gamedb_gameexpansion', (
            ('gamebase_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['gamedb.GameBase'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('gamedb', ['GameExpansion'])

        # Adding M2M table for field expands on 'GameExpansion'
        db.create_table('gamedb_gameexpansion_expands', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('gameexpansion', models.ForeignKey(orm['gamedb.gameexpansion'], null=False)),
            ('game', models.ForeignKey(orm['gamedb.game'], null=False))
        ))
        db.create_unique('gamedb_gameexpansion_expands', ['gameexpansion_id', 'game_id'])


    def backwards(self, orm):
        # Deleting model 'GameBase'
        db.delete_table('gamedb_gamebase')

        # Removing M2M table for field owners on 'GameBase'
        db.delete_table('gamedb_gamebase_owners')

        # Removing M2M table for field disposers on 'GameBase'
        db.delete_table('gamedb_gamebase_disposers')

        # Removing M2M table for field rules_known_by on 'GameBase'
        db.delete_table('gamedb_gamebase_rules_known_by')

        # Deleting model 'Game'
        db.delete_table('gamedb_game')

        # Removing M2M table for field similar_games on 'Game'
        db.delete_table('gamedb_game_similar_games')

        # Deleting model 'GameExpansion'
        db.delete_table('gamedb_gameexpansion')

        # Removing M2M table for field expands on 'GameExpansion'
        db.delete_table('gamedb_gameexpansion_expands')


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
        'gamedb.game': {
            'Meta': {'ordering': "['name']", 'object_name': 'Game', '_ormbases': ['gamedb.GameBase']},
            'gamebase_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['gamedb.GameBase']", 'unique': 'True', 'primary_key': 'True'}),
            'similar_games': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'similar_games_rel_+'", 'null': 'True', 'to': "orm['gamedb.Game']"})
        },
        'gamedb.gamebase': {
            'Meta': {'object_name': 'GameBase'},
            'added_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'disposers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'games_disposed'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owners': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'games_owned'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'rules_known_by': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'game_rules_known'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'updated_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'gamedb.gameexpansion': {
            'Meta': {'ordering': "['name']", 'object_name': 'GameExpansion', '_ormbases': ['gamedb.GameBase']},
            'expands': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'expansions'", 'symmetrical': 'False', 'to': "orm['gamedb.Game']"}),
            'gamebase_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['gamedb.GameBase']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['gamedb']