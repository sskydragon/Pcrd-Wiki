# Generated by Django 2.0.3 on 2018-06-06 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcrd_unpack', '0012_solution_pub_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='solutioncomment',
            name='user',
            field=models.IntegerField(default=1),
        ),
    ]
