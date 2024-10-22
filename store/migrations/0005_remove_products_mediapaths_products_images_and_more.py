# Generated by Django 4.2 on 2024-10-22 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_orderstatus_alter_orders_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='mediaPaths',
        ),
        migrations.AddField(
            model_name='products',
            name='images',
            field=models.JSONField(blank=True, db_column='images', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='parentId',
            field=models.ForeignKey(db_column='parent_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.products'),
        ),
        migrations.RemoveField(
            model_name='products',
            name='categoryId',
        ),
        migrations.AddField(
            model_name='products',
            name='categoryId',
            field=models.ManyToManyField(blank=True, db_column='category_ids', db_index=True, to='store.categories'),
        ),
    ]
