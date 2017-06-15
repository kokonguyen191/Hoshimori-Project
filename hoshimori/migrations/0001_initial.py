# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings
import hoshimori.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation', models.DateTimeField(auto_now_add=True, verbose_name='Join Date')),
                ('start_date', models.DateField(help_text='When you started playing with this account.', null=True, verbose_name='Start Date')),
                ('level', models.PositiveIntegerField(null=True, verbose_name='Level', db_index=True)),
                ('nickname', models.CharField(max_length=100, verbose_name='Nickname')),
                ('game_id', models.CharField(max_length=8, verbose_name='Game ID')),
                ('device', models.CharField(max_length=150, verbose_name='Device')),
                ('i_os', models.PositiveIntegerField(default=0, verbose_name='Operating System', choices=[(0, b'iOs'), (1, b'Android')])),
                ('i_player_type', models.PositiveIntegerField(default=0, verbose_name='Player type', choices=[(0, b'Free-to-play'), (1, b'Pay-to-win'), (2, b'FTP PTW Hybrid')])),
                ('owner', models.ForeignKey(related_name='accounts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.PositiveIntegerField(unique=True, serialize=False, verbose_name='ID', primary_key=True, db_index=True)),
                ('i_rarity', models.PositiveIntegerField(verbose_name='Rarity', choices=[(0, '\u2605'), (1, '\u2605\u2605'), (2, '\u2605\u2605\u2605'), (3, '\u2605\u2605\u2605\u2605')])),
                ('i_weapon', models.PositiveIntegerField(verbose_name='Weapon', choices=[(0, 'Sword'), (1, 'Spear'), (2, 'Hammer'), (3, 'Gun'), (4, 'Rod'), (5, 'Gunblade'), (6, 'Twin Barrett')])),
                ('name', models.CharField(max_length=100, verbose_name='Title')),
                ('japanese_name', models.CharField(max_length=100, verbose_name='Title (Japanese)')),
                ('image', models.ImageField(upload_to=hoshimori.models.uploadItem(b'c'), verbose_name='Image')),
                ('art', models.ImageField(upload_to=hoshimori.models.uploadItem(b'c/art'), verbose_name='Art')),
                ('transparent', models.ImageField(upload_to=hoshimori.models.uploadItem(b'c/transparent'), verbose_name='Transparent')),
                ('subcard_effect', models.BooleanField(default=False, verbose_name='Subcard Effect')),
                ('card_type', models.PositiveIntegerField(verbose_name='Card Type', choices=[(0, 'Normal'), (1, 'Extra'), (2, 'Subcard')])),
                ('hp_1', models.PositiveIntegerField(default=0, verbose_name='HP (Level 1)')),
                ('hp_50', models.PositiveIntegerField(default=0, verbose_name='HP (Level 50)')),
                ('hp_70', models.PositiveIntegerField(default=0, verbose_name='HP (Level 70)')),
                ('sp_1', models.PositiveIntegerField(default=0, verbose_name='SP (Level 1)')),
                ('sp_50', models.PositiveIntegerField(default=0, verbose_name='SP (Level 50)')),
                ('sp_70', models.PositiveIntegerField(default=0, verbose_name='SP (Level 70)')),
                ('atk_1', models.PositiveIntegerField(default=0, verbose_name='ATK (Level 1)')),
                ('atk_50', models.PositiveIntegerField(default=0, verbose_name='ATK (Level 50)')),
                ('atk_70', models.PositiveIntegerField(default=0, verbose_name='ATK (Level 70)')),
                ('def_1', models.PositiveIntegerField(default=0, verbose_name='DEF (Level 1)')),
                ('def_50', models.PositiveIntegerField(default=0, verbose_name='DEF (Level 50)')),
                ('def_70', models.PositiveIntegerField(default=0, verbose_name='DEF (Level 70)')),
                ('skill_name', models.CharField(max_length=100, verbose_name='Skill name')),
                ('japanese_skill_name', models.CharField(max_length=100, verbose_name='Skill name (Japanese)')),
                ('skill_SP', models.PositiveIntegerField(default=0, verbose_name='Skill SP')),
                ('skill_combo', models.PositiveIntegerField(default=13, verbose_name='Skill combo')),
                ('skill_hits', models.PositiveIntegerField(default=0, verbose_name='Skill hits')),
                ('skill_damage', models.CharField(max_length=300, verbose_name='Skill damage')),
                ('skill_range', models.CharField(max_length=300, verbose_name='Skill range')),
                ('skill_comment', models.CharField(max_length=1000, verbose_name='Skill comment')),
                ('evolved_skill_combo', models.PositiveIntegerField(verbose_name='Evolved Skill combo')),
                ('evolved_skill_damage', models.CharField(max_length=300, verbose_name='Evolved Skill damage')),
                ('max_damage', models.PositiveIntegerField(default=0, verbose_name='Max damage')),
                ('nakayoshi_title', models.CharField(max_length=100, verbose_name='Passive Skill')),
                ('japanese_nakayoshi_title', models.CharField(max_length=100, verbose_name='Passive Skill (Japanese)')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Irousu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Nakayoshi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('i_name', models.PositiveIntegerField(null=True, verbose_name='Nakayoshi skill', choices=[(0, 'ATK'), (1, 'HP'), (2, 'SP'), (3, 'Damage'), (4, 'Combo Damage'), (5, 'SP Consumption'), (6, 'Skill Combo'), (7, 'Movement Rate'), (8, 'Dodge'), (9, 'Auto Reload'), (10, 'Bullet'), (11, 'Item Recovery Range'), (12, 'Item Drop Quantity'), (13, 'Coin'), (14, 'Cheerpoint'), (15, 'EXP'), (16, 'Bond Point'), (17, 'Guard Penetration'), (18, 'Received Damage'), (19, 'Null SP Damage'), (20, 'Null Slow'), (21, 'Null Paralysis'), (22, 'Null Skill Seal'), (23, 'Null Poison')])),
                ('positive_effect', models.BooleanField(default=True, verbose_name='Positive Effect')),
                ('effect_level', models.PositiveIntegerField(default=None, null=True, verbose_name='Effect level', blank=True, choices=[(0, b'Small'), (1, b'Medium'), (2, b'Large'), (3, b'Super')])),
                ('bonus_value', models.PositiveIntegerField(null=True, verbose_name='Effect Value')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Stage')),
                ('episode', models.PositiveIntegerField(null=True, verbose_name='Episode')),
                ('number', models.PositiveIntegerField(null=True, verbose_name='Stage number')),
                ('irousu', models.CharField(max_length=200, verbose_name='Irousu')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StageDifficulty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('difficulty', models.PositiveIntegerField(null=True, verbose_name='Difficulty', choices=[(0, b'Easy'), (1, b'Normal'), (2, b'Hard')])),
                ('level', models.PositiveIntegerField(null=True, verbose_name='Level')),
                ('exp', models.PositiveIntegerField(null=True, verbose_name='EXP')),
                ('coins', models.PositiveIntegerField(null=True, verbose_name='Coins')),
                ('cheerpoints', models.PositiveIntegerField(null=True, verbose_name='Cheerpoints')),
                ('objectives', models.CharField(max_length=200, verbose_name='Objectives')),
                ('stage', models.ForeignKey(related_name='difficulties', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Stage', to='hoshimori.Stage', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='Name (romaji)')),
                ('japanese_name', models.CharField(max_length=100, verbose_name='Name (Japanese)')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('i_school_year', models.PositiveIntegerField(null=True, verbose_name='School year', choices=[(0, 'Middle School Year 1'), (1, 'Middle School Year 2'), (2, 'Middle School Year 3'), (3, 'High School Year 1'), (4, 'High School Year 2'), (5, 'High School Year 3')])),
                ('birthday', models.DateField(null=True, verbose_name='Birthday')),
                ('i_star_sign', models.PositiveIntegerField(null=True, verbose_name='Star sign', choices=[(0, 'Leo'), (1, 'Aries'), (2, 'Libra'), (3, 'Virgo'), (4, 'Scorpio'), (5, 'Capricorn'), (6, 'Pisces'), (7, 'Gemini'), (8, 'Cancer'), (9, 'Sagittarius'), (10, 'Aquarius'), (11, 'Taurus')])),
                ('i_blood_type', models.PositiveIntegerField(null=True, verbose_name='Blood type', choices=[(0, b'O'), (1, b'A'), (2, b'B'), (3, b'AB')])),
                ('extra_activity', models.CharField(max_length=100, verbose_name='Extracurricular activity')),
                ('catchphrase_1', models.CharField(max_length=100, verbose_name='Catchphrase 1')),
                ('catchphrase_2', models.CharField(max_length=100, verbose_name='Catchphrase 2')),
                ('height', models.PositiveIntegerField(help_text=b'in cm', null=True, verbose_name='Height')),
                ('weight', models.PositiveIntegerField(help_text=b'in kg', null=True, verbose_name='Weight')),
                ('bust', models.PositiveIntegerField(help_text=b'in cm', null=True, verbose_name='Bust')),
                ('waist', models.PositiveIntegerField(help_text=b'in cm', null=True, verbose_name='Waist')),
                ('hip', models.PositiveIntegerField(help_text=b'in cm', null=True, verbose_name='Hip')),
                ('hobby_1', models.CharField(max_length=100, verbose_name='Hobby 1')),
                ('hobby_2', models.CharField(max_length=100, verbose_name='Hobby 2')),
                ('hobby_3', models.CharField(max_length=100, verbose_name='Hobby 3')),
                ('food_likes', models.CharField(max_length=100, verbose_name='Liked food')),
                ('food_dislikes', models.CharField(max_length=100, verbose_name='Disliked food')),
                ('family', models.CharField(max_length=100, verbose_name='Family members')),
                ('dream', models.CharField(max_length=100, verbose_name='Dream job')),
                ('ideal_1', models.CharField(max_length=100, verbose_name='Ideal person 1')),
                ('ideal_2', models.CharField(max_length=100, verbose_name='Ideal person 2')),
                ('ideal_3', models.CharField(max_length=100, verbose_name='Ideal person 3')),
                ('pastime', models.CharField(max_length=100, verbose_name='Pastime')),
                ('destress', models.CharField(max_length=100, verbose_name='Destress')),
                ('fav_memory', models.CharField(max_length=100, verbose_name='Favorite memory')),
                ('fav_phrase', models.CharField(max_length=100, verbose_name='Favorite phrase')),
                ('secret', models.CharField(max_length=5000, verbose_name='Secret')),
                ('CV', models.CharField(help_text=b'In Japanese characters.', max_length=100, verbose_name='CV')),
                ('romaji_CV', models.CharField(help_text=b'In romaji.', max_length=100, verbose_name='CV')),
                ('image', models.ImageField(upload_to=hoshimori.models.uploadItem(b'i'), verbose_name='Image')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('japanese_name', models.CharField(max_length=100, verbose_name='Name (Japanese)')),
                ('image', models.ImageField(upload_to=hoshimori.models.uploadItem(b'w'), verbose_name='Icon')),
                ('rhythm', models.ImageField(upload_to=hoshimori.models.uploadItem(b'w/rhythm'), verbose_name='Rhythm')),
                ('i_weapon', models.PositiveIntegerField(verbose_name='Weapon', choices=[(0, 'Sword'), (1, 'Spear'), (2, 'Hammer'), (3, 'Gun'), (4, 'Rod'), (5, 'Gunblade'), (6, 'Twin Barrett')])),
                ('owner', models.ForeignKey(related_name='added_weapons', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WeaponUpgrade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.PositiveIntegerField(default=0, verbose_name='Upgrade Level', choices=[(0, b''), (1, 'Alpha'), (2, 'Beta'), (3, 'Gamma')])),
                ('i_rarity', models.PositiveIntegerField(default=0, verbose_name='Rarity', choices=[(0, '\u2605'), (1, '\u2605\u2605'), (2, '\u2605\u2605\u2605'), (3, '\u2605\u2605\u2605\u2605')])),
                ('atk_min', models.PositiveIntegerField(default=0, verbose_name='Weapon ATK (Minimum)')),
                ('atk_max', models.PositiveIntegerField(default=0, verbose_name='Weapon ATK (Maximum)')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Price')),
                ('origin', models.ForeignKey(related_name='upgrade', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Weapon', to='hoshimori.Weapon', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='card',
            name='evolved_nakayoshi_skills',
            field=models.ManyToManyField(related_name='card_with_nakayoshi_evolved', to='hoshimori.Nakayoshi'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='nakayoshi_skills',
            field=models.ManyToManyField(related_name='card_with_nakayoshi', to='hoshimori.Nakayoshi'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='owner',
            field=models.ForeignKey(related_name='added_cards', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='student',
            field=models.ForeignKey(related_name='cards', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Student', to='hoshimori.Student', null=True),
            preserve_default=True,
        ),
    ]
