# Generated by Django 4.1.1 on 2022-09-14 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cartproducts", "0003_alter_cartproducts_productvalue"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cartproducts",
            name="productValue",
        ),
    ]