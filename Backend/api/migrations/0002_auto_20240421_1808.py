# Generated by Django 5.0.2 on 2024-04-22 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            '''
                DROP TRIGGER IF EXISTS adeudos_AFTER_INSERT;
                DROP TRIGGER IF EXISTS adeudos_AFTER_UPDATE;
                DROP TRIGGER IF EXISTS adeudos_AFTER_DELETE;
                DROP TRIGGER IF EXISTS consumibles_AFTER_INSERT;
                DROP TRIGGER IF EXISTS consumibles_AFTER_UPDATE;
                DROP TRIGGER IF EXISTS consumibles_AFTER_DELETE;
                DROP TRIGGER IF EXISTS equipos_AFTER_INSERT;
                DROP TRIGGER IF EXISTS equipos_BEFORE_UPDATE;
                DROP TRIGGER IF EXISTS equipos_AFTER_DELETE;
                DROP TRIGGER IF EXISTS equipos_existencias_AFTER_INSERT;
                DROP TRIGGER IF EXISTS equipos_existencias_AFTER_UPDATE;
                DROP TRIGGER IF EXISTS equipos_existencias_AFTER_DELETE;
                DROP TRIGGER IF EXISTS mantenimiento_AFTER_INSERT;
                DROP TRIGGER IF EXISTS mantenimiento_AFTER_UPDATE;
                DROP TRIGGER IF EXISTS mantenimiento_AFTER_DELETE;
                DROP TRIGGER IF EXISTS prestamos_AFTER_INSERT;
                DROP TRIGGER IF EXISTS prestamos_AFTER_UPDATE;
                DROP TRIGGER IF EXISTS prestamos_AFTER_DELETE;
                DROP TRIGGER IF EXISTS sucursales_AFTER_INSERT;
                DROP TRIGGER IF EXISTS sucursales_AFTER_UPDATE;
                DROP TRIGGER IF EXISTS sucursales_AFTER_DELETE;
            '''
            ),
        
        migrations.RunSQL(
            '''
CREATE DEFINER=`root`@`localhost` TRIGGER `adeudos_AFTER_INSERT` AFTER INSERT ON `adeudos` FOR EACH ROW BEGIN
    INSERT INTO bitacora values (
    default,
    user(),
		"Create",
		"adeudo",
        CONCAT_WS(" ","Se ha insertado un nuevo adeudo con el ID: ",NEW.ID, 
        "con los siguientes datos: NOMBRE=", NEW.nombre_cliente,
        "RECURSO_PRESTADO = ", NEW.recurso_prestado,
        "FECHA_PRESTAMO = ", NEW.fecha_prestamo,
        "FECHA_DEVOLUCION_ESTIMADA = ", NEW.fecha_devolucion_estimada, 
        "CANTIDAD_PRESTADA = ", NEW.cantidad_prestada,
        "ESTADO_DEVOLUCION = ", NEW.estado_devolucion, 
        "OBSERVACIONES = ", NEW.observaciones),
        NOW(),
        DEFAULT
    );
  
END
        
            '''
    ),
        migrations.RunSQL(
            '''
            CREATE DEFINER=`root`@`localhost` TRIGGER `adeudos_AFTER_UPDATE` AFTER UPDATE ON `adeudos` FOR EACH ROW BEGIN
INSERT INTO bitacora VALUES(
		DEFAULT,
        USER(),
        "Update",
        "adeudos",
        CONCAT_WS(" ","Se han actualizado los datos del adeudo con el ID: ",NEW.ID, 
        "con los siguientes datos:", "NOMBRE=", OLD.nombre_cliente, " cambio a " ,NEW.nombre_cliente,
        "RECURSO_PRESTADO = ", OLD.recurso_prestado, " cambio a " , NEW.recurso_prestado,
        "FECHA_PRESTAMO = ", OLD.fecha_prestamo, " cambio a " , NEW.fecha_prestamo,
        "FECHA_DEVOLUCION_ESTIMADA = ", OLD.fecha_devolucion_estimada, " cambio a " , NEW.fecha_devolucion_estimada, 
        "CANTIDAD_PRESTADA = ", OLD.cantidad_prestada, " cambio a " , NEW.cantidad_prestada,
        "ESTADO_DEVOLUCION = ", OLD.estado_devolucion, " cambio a " , NEW.estado_devolucion, 
        "OBSERVACIONES = ", OLD.observaciones, " cambio a " , NEW.observaciones),
        NOW(),
        DEFAULT
    );
END
            '''
        ),
        migrations.RunSQL(
            '''
            CREATE DEFINER=`root`@`localhost` TRIGGER `adeudos_AFTER_DELETE` AFTER DELETE ON `adeudos` FOR EACH ROW BEGIN
INSERT INTO bitacora VALUES(
		DEFAULT,
        USER(),
        "Delete",
        "adeudos",
        CONCAT_WS(" ","Se ha eliminado un adeudo con el ID: ", OLD.ID),
        now(),
        DEFAULT
    );
END
            '''
        ),
        migrations.RunSQL(
            '''
            CREATE DEFINER=`root`@`localhost` TRIGGER `consumibles_AFTER_INSERT` AFTER INSERT ON `consumibles` FOR EACH ROW BEGIN
    INSERT INTO bitacora values (
    default,
    user(),
		"Create",
		"consumibles",
        CONCAT_WS(" ","Se ha insertado un nuevo consumible con el ID: ",NEW.ID, 
        "con los siguientes datos: NOMBRE=", NEW.nombre,
        "CANTIDAD = ", NEW.cantidad,
        "UNIDAD_MEDIDA = ", NEW.unidad_medida,
        "FECHA_DE_VENCIMIENTO = ", NEW.fecha_de_vencimiento, 
        "PROVEEDOR = ", NEW.proveedor),
        NOW(),
        DEFAULT
    );
  
END
            '''
        ),
        migrations.RunSQL(
            '''
            CREATE DEFINER=`root`@`localhost` TRIGGER `consumibles_AFTER_UPDATE` AFTER UPDATE ON `consumibles` FOR EACH ROW BEGIN
 INSERT INTO bitacora VALUES(
		DEFAULT,
        USER(),
        "Update",
        "consumibles",
        CONCAT_WS(" ","Se han actualizado los datos del consumible con el ID: ",NEW.ID, 
        "con los siguientes datos:", "NOMBRE=", OLD.nombre, " cambio a " ,NEW.nombre,
		"CANTIDAD = ",OLD.cantidad, " cambio a " , NEW.cantidad,
        "UNIDAD_MEDIDA = ",OLD.unidad_medida, " cambio a " , NEW.unidad_medida,
        "FECHA_DE_VENCIMIENTO = ",OLD.fecha_de_vencimiento, " cambio a " , NEW.fecha_de_vencimiento, 
        "PROVEEDOR = ",OLD.proveedor, " cambio a " , NEW.proveedor),
        NOW(),
        DEFAULT
    );
END
            '''
        ),
        migrations.RunSQL(
            '''
            CREATE DEFINER=`root`@`localhost` TRIGGER `consumibles_AFTER_DELETE` AFTER DELETE ON `consumibles` FOR EACH ROW BEGIN
INSERT INTO bitacora VALUES(
		DEFAULT,
        USER(),
        "Delete",
        "consumibles",
        CONCAT_WS(" ","Se ha eliminado un consumible con el ID: ", OLD.ID),
        now(),
        DEFAULT
    );
END
            '''
        ),
        migrations.RunSQL(
            '''
            CREATE DEFINER=`root`@`localhost` TRIGGER `equipos_AFTER_INSERT` AFTER INSERT ON `equipos` FOR EACH ROW BEGIN
	INSERT INTO bitacora VALUES(
		DEFAULT,
        USER(),
        "Create",
        "equipos",
        CONCAT_WS(" ","Se ha insertado un nuevo equipo con el ID: ",NEW.ID, 
        "con los siguientes datos: NOMBRE=", NEW.nombre,
        "DESCRIPCION = ", NEW.descripcion,
        "MARCA = ", NEW.marca,
        "MODELO = ", NEW.modelo, 
        "ESPECIFICACIONES = ", NEW.especificaciones,
        "FOTOGRAFIA = ", NEW.fotografia, 
        "TOTAL_EXISTENCIA = ", NEW.total_existencia),
        NOW(),
        DEFAULT
    );
END
            '''
        ),
        migrations.RunSQL(
            '''
            CREATE DEFINER=`root`@`localhost` TRIGGER `equipos_BEFORE_UPDATE` BEFORE UPDATE ON `equipos` FOR EACH ROW BEGIN
INSERT INTO bitacora VALUES(
		DEFAULT,
        USER(),
        "Update",
        "equipos",
        CONCAT_WS(" ","Se han actualizado los datos del equipo con el ID: ",NEW.ID, 
        "con los siguientes datos:", "NOMBRE=", OLD.nombre, " cambio a " ,NEW.nombre,
        "DESCRIPCION = ", OLD.descripcion, " cambio a " , NEW.descripcion,
        "MARCA = ", OLD.marca, " cambio a " , NEW.marca, 
        "MODELO = ",  OLD.modelo, " cambio a " ,NEW.modelo, 
        "ESPECIFICACIONES = ", OLD.especificaciones, " cambio a " , NEW.especificaciones,
        "FOTOGRAFIA = ",  OLD.fotografia, " cambio a " ,NEW.fotografia, 
        "TOTAL_EXISTENCIA = ", OLD.total_existencia, " cambio a " , NEW.total_existencia),
        NOW(),
        DEFAULT
    );
END
            '''
        ),
        migrations.RunSQL(
            '''
            CREATE DEFINER=`root`@`localhost` TRIGGER `equipos_AFTER_DELETE` AFTER DELETE ON `equipos` FOR EACH ROW BEGIN
INSERT INTO bitacora VALUES(
		DEFAULT,
        USER(),
        "Delete",
        "equipos",
        CONCAT_WS(" ","Se ha eliminado un equipo con el ID: ", OLD.ID),
        now(),
        DEFAULT
    );
END
            '''
        ),
        migrations.RunSQL(
            '''
    CREATE DEFINER=`root`@`localhost` TRIGGER `equipos_existencias_AFTER_INSERT` AFTER INSERT ON `equipos_existencias` FOR EACH ROW BEGIN
	-- Declaración de variables
    DECLARE v_nombre_equipo varchar(60) default null;
    DECLARE v_nombre_area varchar(60) default null;

    -- Iniciación de las variables
    if new.equipo_id is not null then
        -- En caso de tener el id del equipo
        set v_nombre_equipo = (SELECT CONCAT_WS(" ", e.nombre, e.marca, e.modelo) FROM equipos e WHERE id = NEW.equipo_id);
    else
        SET v_nombre_equipo = "Sin equipo asignado";
    end if;

    if new.area_id is not null then
        -- En caso de tener el id del area
        set v_nombre_area = (SELECT nombre FROM areas WHERE id = NEW.area_id);
    else
        SET v_nombre_area = "Sin area asignada";
    end if;

    -- Insertar en la bitacora
    INSERT INTO bitacora VALUES(
        DEFAULT,
        USER(),
        "Create",
        "equipos_existencias",
        CONCAT_WS(" ","Se ha insertado una nueva relación de EQUIPOS EXISTENCIAS con el ID: ",NEW.ID, 
        "con los siguientes datos: ",
        "EQUIPO ID = ", v_nombre_equipo,
        "AREA ID = ",  v_nombre_area,
        "COLOR = ", NEW.color, 
        "ESTATUS = ", NEW.estatus,
        "FECHA DE ASIGNACIÓN = ", NEW.fecha_asignacion),
        NOW(),
        DEFAULT
    );
END

            '''
        ),
        migrations.RunSQL(
            '''
            CREATE DEFINER=`root`@`localhost` TRIGGER `equipos_existencias_AFTER_UPDATE` AFTER UPDATE ON `equipos_existencias` FOR EACH ROW BEGIN
	-- Declaración de variables
    DECLARE v_nombre_equipo VARCHAR(100) DEFAULT NULL;
    DECLARE v_nombre_equipo2 VARCHAR(100) DEFAULT NULL;
    DECLARE v_nombre_area VARCHAR(60) DEFAULT NULL;
    DECLARE v_nombre_area2 VARCHAR(60) DEFAULT NULL;

    -- Inicialización de las variables
    IF NEW.equipo_id IS NOT NULL THEN 
		-- En caso de tener el id del equipo
		SET v_nombre_equipo = (SELECT CONCAT_WS(" ", e.nombre, e.marca, e.modelo) FROM equipos e WHERE id = NEW.equipo_id);
    ELSE
		SET v_nombre_equipo = "Sin equipo asignado.";
    END IF;
    
    IF OLD.equipo_id IS NOT NULL THEN 
		-- En caso de tener el id del equipo
		SET v_nombre_equipo2 =(SELECT CONCAT_WS(" ", e.nombre, e.marca, e.modelo) FROM equipos e WHERE id = OLD.equipo_id);
    ELSE
		SET v_nombre_equipo2 = "Sin equipo asignado.";
    END IF;

    IF NEW.area_id IS NOT NULL THEN 
		-- En caso de tener el id del area
		SET v_nombre_area = (SELECT nombre FROM areas WHERE id = NEW.area_id);
    ELSE
		SET v_nombre_area = "Sin area asignada.";
    END IF;

    IF OLD.area_id IS NOT NULL THEN 
		-- En caso de tener el id del area
		SET v_nombre_area2 = (SELECT nombre FROM areas WHERE id = OLD.area_id);
    ELSE
		SET v_nombre_area2 = "Sin area asignada.";
    END IF;
    
    INSERT INTO bitacora VALUES(
        DEFAULT,
        USER(),
        "Update",
        "equipos_exixstencias",
        CONCAT_WS(" ","Se han actualizado los datos de la relación EQUIPOS EXISTENCIAS con el ID: ",NEW.ID, 
        "con los siguientes datos:",
        "EQUIPO ID = ", v_nombre_equipo2, "cambio a", v_nombre_equipo,
        "AREA ID =",v_nombre_area2,"cambio a", v_nombre_area,
        "COLOR = ", OLD.color, "cambio a", NEW.color ,
        "ESTATUS = ", OLD.estatus, "cambio a", NEW.estatus,
        "FECHA DE ASIGNACIÓN = ", OLD.fecha_asignacion , "cambio a", NEW.fecha_asignacion ),
        NOW(),
        DEFAULT       
    );
END

            '''
        ),
        migrations.RunSQL(
            '''
        CREATE DEFINER=`root`@`localhost` TRIGGER `equipos_existencias_AFTER_DELETE` AFTER DELETE ON `equipos_existencias` FOR EACH ROW BEGIN
	INSERT INTO bitacora VALUES(
		DEFAULT,
        USER(),
        "Delete",
        "equipos_existencias",
        CONCAT_WS(" ","Se ha eliminado una relación EUIPOS EXISTENCIAS con los IDs: ", OLD.ID),
        now(),
        DEFAULT
    );
END 
            '''
        ),
        migrations.RunSQL(
            '''
            CREATE DEFINER=`root`@`localhost` TRIGGER `mantenimiento_AFTER_INSERT` AFTER INSERT ON `mantenimiento` FOR EACH ROW BEGIN
INSERT INTO bitacora values (
    default,
    user(), 
		"Create",
		"mantenimiento",
        CONCAT_WS(" ","Se ha insertado un nuevo mantenimiento con el ID: ",NEW.ID, 
        "con los siguientes datos: DESCRIPCION_DEL_TRABAJO_REALIZADO = ", NEW.descripcion_del_trabajo_realizado,
        "FECHA_DE_MANTENIMIENTO = ", NEW.fecha_de_mantenimiento,
        "ESTADO_DEL_EQUIPO_DESPUES_DEL_MANTENIMIENTO = ", NEW.estado_del_equipo_despues_del_mantenimiento),
        NOW(),
        DEFAULT
    );
  
END
            '''
        ),
        migrations.RunSQL(
            '''
        CREATE DEFINER=`root`@`localhost` TRIGGER `mantenimiento_AFTER_UPDATE` AFTER UPDATE ON `mantenimiento` FOR EACH ROW BEGIN
 INSERT INTO bitacora VALUES(
		DEFAULT,
        USER(),
        "Update",
        "mantenimiento",
        CONCAT_WS(" ","Se han actualizado los datos del mantenimiento con el ID: ",NEW.ID, 
         "con los siguientes datos: DESCRIPCION_DEL_TRABAJO_REALIZADO = ", OLD.descripcion_del_trabajo_realizado, " cambio a " , NEW.descripcion_del_trabajo_realizado,
        "FECHA_DE_MANTENIMIENTO = ", OLD.fecha_de_mantenimiento, " cambio a " , NEW.fecha_de_mantenimiento,
        "ESTADO_DEL_EQUIPO_DESPUES_DEL_MANTENIMIENTO = ", OLD.estado_del_equipo_despues_del_mantenimiento, " cambio a " , NEW.estado_del_equipo_despues_del_mantenimiento),
        NOW(),
        DEFAULT
    );
  
END  
            '''
        ),
        migrations.RunSQL(
            '''
        CREATE DEFINER=`root`@`localhost` TRIGGER `mantenimiento_AFTER_DELETE` AFTER DELETE ON `mantenimiento` FOR EACH ROW BEGIN
 INSERT INTO bitacora VALUES(
		DEFAULT,
        USER(),
        "Delete",
        "mantenimiento",
        CONCAT_WS(" ","Se ha eliminado un mantenimiento con el ID: ", OLD.ID),
        now(),
        DEFAULT
    );
END   
            '''
        ),
        migrations.RunSQL(
            '''
        CREATE DEFINER=`root`@`localhost` TRIGGER `prestamos_AFTER_INSERT` AFTER INSERT ON `prestamos` FOR EACH ROW BEGIN
    INSERT INTO bitacora values (
    default,
    user(),
		"Create",
		"prestamos",
        CONCAT_WS(" ","Se ha insertado un nuevo prestamo con el ID: ",NEW.ID, 
        "con los siguientes datos: DECRIPCION=", NEW.descripcion,
        "CANTIDAD_DISPONIBLE = ", NEW.cantidad_disponible,
        "CANTIDAD_TOTAL = ", NEW.cantidad_total,
        "ESTADO = ", NEW.estado, 
		"FECHA_ADQUISICION = ", NEW.fecha_adquisicion, 
        "PROVEEDOR = ", NEW.proveedor),
        NOW(),
        DEFAULT
    );
  
END   
            '''
        ),
        migrations.RunSQL(
            '''
            REATE DEFINER=`root`@`localhost` TRIGGER `prestamos_AFTER_UPDATE` AFTER UPDATE ON `prestamos` FOR EACH ROW BEGIN
 INSERT INTO bitacora VALUES(
		DEFAULT,
        USER(),
        "Update",
        "prestamos",
        CONCAT_WS(" ","Se han actualizado los datos del prestamo con el ID: ",NEW.ID, 
        "con los siguientes datos: DECRIPCION=",OLD.descripcion, " cambio a " , NEW.descripcion,
        "CANTIDAD_DISPONIBLE = ",OLD.cantidad_disponible, " cambio a " , NEW.cantidad_disponible,
        "CANTIDAD_TOTAL = ",OLD.cantidad_total, " cambio a " , NEW.cantidad_total,
        "ESTADO = ",OLD.estado, " cambio a " , NEW.estado, 
		"FECHA_ADQUISICION = ",OLD.fecha_adquisicion, " cambio a " , NEW.fecha_adquisicion, 
        "PROVEEDOR = ",OLD.proveedor, " cambio a " , NEW.proveedor),
        NOW(),
        DEFAULT
    );
  
END

            '''
        ),
        migrations.RunSQL(
            '''
        CREATE DEFINER=`root`@`localhost` TRIGGER `prestamos_AFTER_DELETE` AFTER DELETE ON `prestamos` FOR EACH ROW BEGIN
 INSERT INTO bitacora VALUES(
		DEFAULT,
        USER(),
        "Delete",
        "prestamos",
        CONCAT_WS(" ","Se ha eliminado un recurso prestable con el ID: ", OLD.ID),
        now(),
        DEFAULT
    );
END
            '''
        ),
        migrations.RunSQL(
            '''
        CREATE DEFINER=`root`@`localhost` TRIGGER `sucursales_AFTER_INSERT` AFTER INSERT ON `sucursales` FOR EACH ROW BEGIN
-- Declaración de variables
	DECLARE v_cadena_estatus varchar(15) default null;
    DECLARE v_nombre_responsable varchar(60) default null;
-- Iniciación de las variables
-- El estatus de la sucursal se almacena en un dato del tipo BIT, por
-- cuestiones de memoria, pero para registrar eventos en bitacora
-- se requiere ser más descriptivo con la redacción de los eventos
IF new.estatus = b'1' then
	set v_cadena_estatus = "Activa";
else
	set v_cadena_estatus = "Inactiva";
end if;

if new. responsable_id is not null then
-- En caso de tener el id del empleado responsable debemos recuperar su nombre
-- 
	set v_nombre_responsable = (SELECT CONCAT_WS(" ", p.titulo_cortesia, p.nombre, p.primer_apellido, p.segundo_Apellido) FROM personas p WHERE id = NEW.responsable_id);
else
	SET v_nombre_responsable = "Sin responsable asignado";
end if;
-- Insertar en la bitacora
INSERT INTO bitacora VALUES(
		DEFAULT,
        USER(),
        "Create",
        "sucursales",
        CONCAT_WS(" ","Se ha insertado una nueva SUCURSAL con el ID: ",NEW.ID, 
        "con los siguientes datos: ",
        "NOMBRE=", NEW.nombre,
        "DIRECCION = ", NEW.direccion,
        "RESPONSABLE ID = ", v_nombre_responsable,
        "TOTAL CLIENTES ATENDIDOS = ",  NEW.total_clientes_atendidos,
        "PROMEDIO CLIENTES POR DIA = ", NEW.promedio_clientes_x_dia, 
        "CAPACIDAD MAXIMA = ", NEW.capacidad_maxima, 
        "TOTAL EMPLEADOS = ", NEW.total_empleados,
        "HORARIO DISPONIBILIDAD = ", NEW.horario_disponibilidad,
        "ESTATUS = ",  v_cadena_estatus),
        NOW(),
        DEFAULT
    );
END   
            '''
        ),
        migrations.RunSQL(
            '''
            CREATE DEFINER=`root`@`localhost` TRIGGER `sucursales_AFTER_UPDATE` AFTER UPDATE ON `sucursales` FOR EACH ROW BEGIN
	-- Declaración de variables
    DECLARE v_cadena_estatus VARCHAR(15) DEFAULT NULL;
    DECLARE v_nombre_responsable VARCHAR(100) DEFAULT NULL;
    DECLARE v_cadena_estatus2 VARCHAR(15) DEFAULT NULL;
    DECLARE v_nombre_responsable2 VARCHAR(100) DEFAULT NULL;

    -- Inicialización de las variables
    -- El estatus de la sucursa se almacena en un dato del tipo BIT, por
    -- cuestiones de memorìa, pero para registrar eventos en bitacora
    -- se requiere ser más descriptivo con las readcción de los eventos. 
    IF NEW.estatus = b'1' THEN
     SET v_cadena_estatus= "Activa";
	ELSE
	 SET v_cadena_estatus= "Inactiva";
    END IF; 
    
    IF OLD.estatus = b'1' THEN
     SET v_cadena_estatus2= "Activa";
	ELSE
	 SET v_cadena_estatus2= "Inactiva";
    END IF; 
          
	IF NEW.responsable_id IS NOT NULL THEN 
    -- En caso de tener el id del empleado responsable debemos recuperar su nombre
    -- para ingresarlo en la bitacora.
	SET v_nombre_responsable = (SELECT CONCAT_WS(" ", p.titulo_cortesia, p.nombre, p.primer_apellido,
    p.segundo_apellido) FROM personas p WHERE id = NEW.responsable_id);
	ELSE
    SET v_nombre_responsable = "Sin responsable asingado.";
    END IF;
    
    IF OLD.responsable_id IS NOT NULL THEN 
    -- En caso de tener el id del empleado responsable debemos recuperar su nombre
    -- para ingresarlo en la bitacora.
	SET v_nombre_responsable2 = (SELECT CONCAT_WS(" ", p.titulo_cortesia, p.nombre, p.primer_apellido,
    p.segundo_apellido) FROM personas p WHERE id = OLD.responsable_id);
	ELSE
    SET v_nombre_responsable2 = "Sin responsable asingado.";
    END IF;
    
    
    INSERT INTO bitacora VALUES(
		DEFAULT,
		USER(),
        "Update",
        "sucursales",
        CONCAT_WS(" ","Se ha modificado una SUCURSAL  existente con el ID: ",
        NEW.ID, "con los siguientes datos: NOMBRE =", OLD.nombre,"cambio a",NEW.nombre,
        "DIRECCION =", OLD.direccion,"cambio a",NEW.direccion,
        "RESPONSABLE = ", v_nombre_responsable2, "cambio a", v_nombre_responsable,
        "TOTAL CLIENTES ATENDIDOS  =",OLD.total_clientes_atendidos,"cambio a", NEW.total_clientes_atendidos,
        "PROMEDIO DE CLIENTES POR DIA =", OLD.promedio_clientes_x_dia,"cambio a",NEW.promedio_clientes_x_dia, 
        "CAPACIDAD MÀXIMA =", OLD.capacidad_maxima,"cambio a", NEW.capacidad_maxima,
        "TOTAL EMPLEADOS =", OLD.total_empleados, "cambio a", NEW.total_empleados,
        "HORARIO_DISPONIBILIDAD =", OLD.horario_disponibilidad, "cambio a", NEW.horario_disponibilidad, 
        "ESTATUS = ", v_cadena_estatus2, "cambio a", v_cadena_estatus),
        NOW(),
        DEFAULT       
    );
END

            '''
        ),
        migrations.RunSQL(
            '''
        
CREATE DEFINER=`root`@`localhost` TRIGGER `sucursales_AFTER_DELETE` AFTER DELETE ON `sucursales` FOR EACH ROW BEGIN
	INSERT INTO bitacora VALUES(
		DEFAULT,
        USER(),
        "Delete",
        "sucursales",
        CONCAT_WS(" ","Se ha eliminado una SUCURSAL con el ID: ", OLD.ID),
        now(),
        DEFAULT
    );
END
            '''
        ),
    ]
