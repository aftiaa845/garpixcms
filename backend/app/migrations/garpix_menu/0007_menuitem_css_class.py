# Generated by Django 3.2 on 2023-05-10 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garpix_menu', '0006_menuitem_subpage_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='css_class',
            field=models.CharField(blank=True, help_text='Можно задать, если пункту меню необходима особенная стилизация', max_length=100, null=True, verbose_name='CSS класс'),
        ),
    ]
