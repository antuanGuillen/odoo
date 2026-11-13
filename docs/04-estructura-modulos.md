# 4. Anatomía de un módulo

Un módulo de Odoo es un directorio Python con un `__manifest__.py` y los archivos que extienden el sistema.

Estructura típica:

```text
mi_modulo/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── elemento.py
├── security/
│   └── ir.model.access.csv
├── views/
│   └── elemento_views.xml
└── demo/
    └── demo.xml
```

## Manifest explicado
- `name`: nombre visible.
- `version`: versión del módulo.
- `depends`: módulos requeridos.
- `data`: archivos cargados al instalar/actualizar.
- `demo`: datos de demostración, si están habilitados.
- `installable`: permite instalarlo.

El ejemplo completo está en `addons/sge_biblioteca`.
