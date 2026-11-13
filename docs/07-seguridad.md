# 7. Seguridad

Hay tres conceptos que no debes confundir:
- **Grupo:** conjunto de usuarios con una función.
- **ACL (ir.model.access):** permisos de lectura, escritura, creación y borrado sobre un modelo.
- **Regla de registro:** limita qué registros puede ver o modificar un usuario.

Ejemplo didáctico de ACL:
```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_sge_libro_user,sge.libro user,model_sge_libro,base.group_user,1,1,1,0
```

No uses permisos amplios por comodidad en producción. La seguridad debe probarse con usuarios reales de cada grupo.
