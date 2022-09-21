# Generated by Django 3.2.5 on 2022-09-19 01:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0005_auto_20220914_1350'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='CommentBlog',
        ),
        migrations.CreateModel(
            name='CommentReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('dateTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.commentreview')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.reviewpost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
