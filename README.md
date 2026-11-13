# Odoo SGE en español — Guía práctica para DAM

Material didáctico en español para aprender a administrar, configurar y desarrollar en Odoo 19 Community. Está organizado por objetivos, prácticas guiadas, ejemplos y retos.

> **Versión objetivo:** Odoo 19.0 Community. Algunas pantallas pueden variar según edición, módulos instalados y revisión exacta. Comprueba siempre la documentación oficial enlazada.

## Qué vas a aprender
1. Entorno, Docker Compose y primeros pasos.
2. Conceptos ERP, empresas, usuarios y permisos.
3. Aplicaciones funcionales: contactos, ventas, compras, inventario y facturación.
4. Estructura de módulos personalizados.
5. Python y ORM de Odoo.
6. Vistas XML, menús, acciones y datos de demostración.
7. Seguridad: grupos, ACL y reglas de registro.
8. Relaciones, campos calculados, restricciones y lógica de negocio.
9. Informes QWeb, pruebas y depuración.
10. Proyecto integrador y preparación de examen.

## Inicio rápido
Requisitos: Docker Engine y Docker Compose plugin.

```bash
docker compose up -d
docker compose ps
docker compose logs -f odoo
```

Abre `http://localhost:8069`. Para detener sin borrar datos:

```bash
docker compose down
```

**No ejecutes `docker compose down -v` salvo que quieras borrar los volúmenes y, con ellos, los datos persistentes.**

## Estructura
- `docs/`: teoría y prácticas paso a paso.
- `addons/`: módulos didácticos instalables.
- `docker-compose.yml`: entorno local de aprendizaje.
- `scripts/`: comandos útiles.

## Orden recomendado
Lee `docs/00-ruta-de-aprendizaje.md` y avanza en orden. Cada práctica incluye objetivo, pasos, comprobación y reto.

## Aviso
Este repositorio es un material educativo independiente, no oficial ni afiliado a Odoo S.A. Los ejemplos son deliberadamente pequeños para facilitar su comprensión. Haz copias de seguridad antes de probar en un servidor con datos reales.

## Documentación de referencia
-  https://antuanguillen.github.io/odoo/
