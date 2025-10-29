# Proyecto de Integración FEL para Odoo

Este proyecto contiene la implementación de integración con el sistema de Facturación Electrónica (FEL) de Panamá para Odoo.

## Estructura del Proyecto

- `l10n_pa_fel/`: Módulo de Odoo para integración FEL
  - `MANUAL_USUARIO.md`: Manual de usuario del módulo
  - `RECORRIDO_TECNOFUNCIONAL.md`: Recorrido tecno-funcional
- `fel_examples/`: Ejemplos y scripts auxiliares
  - `MetodosPython/`: Scripts Python para métodos FEL
  - `fel_integration.py`: Script de integración básico

## Diagrama de Flujo Funcional

```mermaid
graph TD
    A[Usuario valida factura] --> B[action_post()]
    B --> C{¿Es out_invoice?}
    C -->|Sí| D[Buscar config FEL]
    C -->|No| E[Fin]
    D --> F[_prepare_fel_data()]
    F --> G[Crear cliente SOAP]
    G --> H[Llamar Enviar()]
    H --> I{¿Éxito?}
    I -->|Sí| J[Actualizar CUFE y status]
    I -->|No| K[Registrar error]
    J --> L[Fin]
    K --> L
```

## Instalación

1. Copie el módulo `l10n_pa_fel` a su directorio de addons de Odoo.
2. Instale dependencias: `pip install zeep`
3. Instale el módulo en Odoo.

## Documentación

- **[Manual de Usuario](l10n_pa_fel/MANUAL_USUARIO.md)**: Guía completa para instalación, configuración y uso.
- **[Recorrido Tecno-Funcional](l10n_pa_fel/RECORRIDO_TECNOFUNCIONAL.md)**: Detalles técnicos de la implementación.


