# 2. Entorno de desarrollo con Docker

## Arrancar
Desde la raíz del repositorio:

```bash
docker compose up -d
docker compose ps
```

## Ver registros
```bash
docker compose logs -f odoo
docker compose logs -f db
```

Salir de los registros: `Ctrl+C` (no detiene los contenedores).

## Entrar en el contenedor
```bash
docker compose exec odoo bash
```

## Reiniciar solo Odoo
```bash
docker compose restart odoo
```

## Parar conservando datos
```bash
docker compose down
```

## Precauciones
- `docker compose down -v` elimina volúmenes: puede borrar la base de datos.
- Los nombres `container_name` deben ser únicos en el host Docker. Si ya existe `sge_odoo`, cambia el nombre o elimina/renombra el contenedor antiguo después de verificarlo.
- No publiques PostgreSQL en Internet.
- Cambia las contraseñas de ejemplo para cualquier entorno compartido.

## Diagnóstico rápido
| Síntoma | Comprobación |
|---|---|
| Puerto 8069 ocupado | `docker ps` y `ss -ltnp` |
| Contenedor reiniciándose | `docker compose logs --tail=100 odoo` |
| No conecta a PostgreSQL | `docker compose logs db` y variables HOST/USER/PASSWORD |
| Módulo no aparece | Comprueba `addons_path`, montaje y actualización de lista de aplicaciones |
