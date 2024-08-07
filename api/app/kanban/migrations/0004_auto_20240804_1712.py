from django.db import migrations

def create_initial_columns(apps, schema_editor):
    Column = apps.get_model('kanban', 'Column')
    Column.objects.create(name='To Do')
    Column.objects.create(name='Up Next')
    Column.objects.create(name='In Progress')
    Column.objects.create(name='In Review')
    Column.objects.create(name='Done')

class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0003_card_column_delete_band_delete_listing_card_column'),  
    ]

    operations = [
        migrations.RunPython(create_initial_columns),
    ]
