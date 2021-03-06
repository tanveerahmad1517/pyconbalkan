# Generated by Django 2.0.5 on 2018-06-11 21:43

from django.db import migrations, models


def update_weight_from_id(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Volunteer = apps.get_model("organizers", "Volunteer")
    for volunteer in Volunteer.objects.all():
        volunteer.weight = volunteer.id
        volunteer.save()

def remove_weight(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('organizers', '0006_volunteer_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='weight',
            field=models.IntegerField(null=True),
        ),
        migrations.RunPython(update_weight_from_id, remove_weight)
    ]
