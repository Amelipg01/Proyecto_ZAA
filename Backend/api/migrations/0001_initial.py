# Generated by Django 5.0.2 on 2024-04-18 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consumible',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unidad_medida', models.CharField(max_length=50)),
                ('fecha_de_vencimiento', models.DateField()),
                ('proveedor', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'consumibles',
            },
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripción', models.TextField()),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('especificaciones', models.TextField()),
                ('fotografía', models.CharField(max_length=100)),
                ('total_existencia', models.IntegerField()),
            ],
            options={
                'db_table': 'equipo',
            },
        ),
        migrations.CreateModel(
            name='EquipoExistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Equipo_ID', models.IntegerField()),
                ('Area_ID', models.IntegerField()),
                ('Color', models.CharField(max_length=50)),
                ('Estatus', models.CharField(max_length=50)),
                ('Fecha_Asignacion', models.DateField()),
            ],
            options={
                'db_table': 'equipos_existencias',
            },
        ),
        migrations.CreateModel(
            name='Mantenimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_del_trabajo_realizado', models.TextField()),
                ('fecha_de_mantenimiento', models.DateField()),
                ('estado_del_equipo_despues_del_mantenimiento', models.CharField(max_length=50)),
                ('Mantenimiento_ID', models.IntegerField()),
            ],
            options={
                'db_table': 'mantenimiento',
            },
        ),
        migrations.CreateModel(
            name='MiembroAdeudos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cliente', models.CharField(max_length=100)),
                ('recurso_prestado', models.CharField(max_length=100)),
                ('fecha_prestamo', models.DateField()),
                ('fecha_devolucion_estimada', models.DateField()),
                ('cantidad_prestada', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado_devolucion', models.CharField(max_length=50)),
                ('observaciones', models.TextField()),
            ],
            options={
                'db_table': 'miembros',
            },
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('cantidad_disponible', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado', models.CharField(max_length=50)),
                ('fecha_adquisicion', models.DateField()),
                ('proveedor', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'prestamos',
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('dirección', models.TextField()),
                ('responsable_id', models.IntegerField()),
                ('total_clientes_atendidos', models.IntegerField()),
                ('promedio_clientes_x_dia', models.DecimalField(decimal_places=2, max_digits=10)),
                ('capacidad_maxima', models.IntegerField()),
                ('total_empleados', models.IntegerField()),
                ('horario_disponibilidad', models.CharField(max_length=100)),
                ('estatus', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'sucursales',
            },
        ),
    ]
