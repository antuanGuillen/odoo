# Comandos útiles

```bash
# Estado
docker compose ps

# Registros de Odoo
docker compose logs --tail=100 odoo

# Reiniciar servicio
docker compose restart odoo

# Consola del contenedor
docker compose exec odoo bash

# Validar YAML
docker compose config

# Actualizar lista de aplicaciones: desde Odoo, modo desarrollador > Actualizar lista de aplicaciones.
```
