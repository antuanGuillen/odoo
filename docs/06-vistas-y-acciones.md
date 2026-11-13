# 6. Vistas, acciones y menús

Las vistas XML definen cómo se muestran y editan los registros. En versiones recientes de Odoo se utiliza la etiqueta `<list>` para las vistas de lista.

Ejemplo mínimo:
```xml
<record id="sge_libro_view_list" model="ir.ui.view">
    <field name="name">sge.libro.list</field>
    <field name="model">sge.libro</field>
    <field name="arch" type="xml">
        <list>
            <field name="name"/>
            <field name="paginas"/>
            <field name="disponible"/>
        </list>
    </field>
</record>
```

Una acción de ventana abre un modelo y un menú permite llegar a esa acción. Consulta `addons/sge_biblioteca/views/libro_views.xml` para el ejemplo integrado.
