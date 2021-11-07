# Generated by Django 3.2.8 on 2021-11-07 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('address', models.TextField()),
                ('Admin', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'My Business',
                'verbose_name_plural': 'Business',
            },
        ),
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=250)),
                ('id_name', models.IntegerField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('Admin', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'My Neighbourhood',
                'verbose_name_plural': 'Neighbourhoods',
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('picture', models.ImageField(blank=True, default='profile_pics/default.jpg', upload_to='profile_pics/')),
                ('neighbourhood', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='occupant', to='blog.neighbourhood')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='neibav',
            name='author',
        ),
        migrations.RemoveField(
            model_name='neibav',
            name='neiba',
        ),
        migrations.RemoveField(
            model_name='profileview',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-pub_date'], 'verbose_name': 'My Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='date',
            new_name='pub_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user_location',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user_name',
        ),
        migrations.AddField(
            model_name='post',
            name='Author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='post',
            field=models.TextField(null=True),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='NeibaV',
        ),
        migrations.DeleteModel(
            name='ProfileView',
        ),
        migrations.AddField(
            model_name='business',
            name='admin_profile',
            field=models.ForeignKey(blank=True, default='1', on_delete=django.db.models.deletion.CASCADE, to='blog.profile'),
        ),
        migrations.AddField(
            model_name='business',
            name='neighbourhood',
            field=models.ForeignKey(blank=True, default='1', on_delete=django.db.models.deletion.CASCADE, to='blog.neighbourhood'),
        ),
        migrations.AddField(
            model_name='post',
            name='author_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.profile'),
        ),
        migrations.AddField(
            model_name='post',
            name='neighbourhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.neighbourhood'),
        ),
    ]