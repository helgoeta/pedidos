# Generated by Django 2.2 on 2022-12-21 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_api', '0005_auto_20221221_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project_api.Cliente'),
        ),
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.DecimalField(decimal_places=2, max_digits=20)),
                ('total_item', models.DecimalField(decimal_places=2, max_digits=20)),
                ('preco_tabela', models.DecimalField(decimal_places=2, max_digits=20)),
                ('preco_liquido', models.DecimalField(decimal_places=2, max_digits=20)),
                ('ultima_alteracao', models.DateTimeField(auto_now=True)),
                ('produto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project_api.Produto')),
            ],
        ),
    ]
