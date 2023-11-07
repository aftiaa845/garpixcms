# Generated by Django 3.2 on 2023-11-07 08:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('garpix_user', '0004_auto_20230510_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='GarpixUserPasswordConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_length', models.PositiveIntegerField(default=12, verbose_name='Минимальная длина пароля')),
                ('min_digits', models.PositiveIntegerField(default=2, verbose_name='Минимальное количество цифр')),
                ('min_chars', models.PositiveIntegerField(default=2, verbose_name='Минимальное количество букв')),
                ('min_uppercase', models.PositiveIntegerField(default=1, verbose_name='Минимальное количество заглавных букв')),
                ('min_special_symbols', models.PositiveIntegerField(default=1, verbose_name='Минимальное количество спец.символов')),
                ('available_attempt', models.IntegerField(default=-1, help_text='-1 если ограничение не требуется', verbose_name='Количество допустимых неуспешных попыток входа')),
                ('password_history', models.IntegerField(default=-1, help_text='-1 если ограничение не требуется', verbose_name='Количество последних паролей, которые нельзя использовать при смене')),
                ('password_validity_period', models.IntegerField(default=-1, help_text='-1 если ограничение не требуется', verbose_name='Срок действия пароля (в днях)')),
                ('password_first_change', models.BooleanField(default=False, verbose_name='Обязательная смена пароля при первом входе')),
            ],
            options={
                'verbose_name': 'Настройки безопасности входа',
                'verbose_name_plural': 'Настройки безопасности входа',
            },
        ),
        migrations.CreateModel(
            name='PasswordHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='пароль')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'История паролей',
                'verbose_name_plural': 'История паролей',
            },
        ),
    ]
