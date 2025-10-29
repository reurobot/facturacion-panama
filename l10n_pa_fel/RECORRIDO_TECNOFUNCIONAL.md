# RECORRIDO TECNO-FUNCIONAL

Documento realizado el 28 de octubre de 2025 a las 12:00 por Corporación Red Neural C.A.

## MÓDULO DE INTEGRACIÓN FACTURACIÓN ELECTRÓNICA (FEL) PARA ODOO

### Versión del Documento
1.0

### Fecha de Emisión
28 de octubre de 2025

### Propósito del Documento
Este documento describe el diseño tecno-funcional del módulo FEL, incluyendo arquitectura, componentes, flujos de proceso y consideraciones técnicas para la integración con el sistema de Facturación Electrónica de Panamá.

### Alcance
El recorrido cubre la implementación actual del módulo, enfocándose en la funcionalidad de envío de facturas. No incluye personalizaciones específicas del cliente.

### Audiencia
- Arquitectos de Software
- Desarrolladores Odoo
- Analistas Funcionales
- Equipos de QA

## 1. ARQUITECTURA GENERAL

### 1.1 Visión General
El módulo `l10n_pa_fel` es una extensión del modelo base `account.move` de Odoo, implementando integración con el Web Service FEL mediante protocolo SOAP. La arquitectura sigue patrones estándar de Odoo para extensiones de modelos y vistas.

### 1.2 Componentes Arquitectónicos
- **Capa de Presentación**: Vistas XML para configuración y visualización de estados FEL.
- **Capa de Lógica de Negocio**: Modelos Python extendiendo `account.move` y `fel.config`.
- **Capa de Integración**: Cliente SOAP utilizando librería `zeep` para comunicación con WS FEL.
- **Capa de Datos**: Campos adicionales en `account_move` para almacenamiento de metadatos FEL.

### 1.3 Dependencias Externas
- Librería `zeep` para manejo de servicios SOAP.
- Acceso a Web Service FEL de The Factory HKA.
- Módulo base `account` de Odoo.

## 2. COMPONENTES PRINCIPALES

### 2.1 Modelo `fel.config`
**Propósito**: Centralizar configuración de credenciales y parámetros FEL por compañía.

**Campos Principales**:
- `name`: Identificador de configuración.
- `token_empresa`: Credencial de autenticación empresa.
- `token_password`: Credencial de autenticación password.
- `wsdl_url`: Endpoint del servicio web.
- `company_id`: Asociación con compañía Odoo.

**Restricciones de Acceso**:
- Grupo: `account.group_account_manager`
- Permisos: Lectura, Escritura, Creación, Eliminación.

### 2.2 Extensión de `account.move`
**Herencia**: Modelo base `account.move` de Odoo.

**Campos Adicionales**:
- `fel_cufe`: Char - Código Único de Factura Electrónica.
- `fel_status`: Char - Estado del proceso FEL.

**Métodos Implementados**:
- `action_post()`: Sobrescrito para incluir envío FEL.
- `_send_to_fel()`: Ejecuta llamada al WS y actualización de campos.
- `_prepare_fel_data()`: Transforma datos Odoo a estructura FEL.

## 3. FLUJO FUNCIONAL DETALLADO

### 3.1 Diagrama de Secuencia
1. Usuario valida factura → `action_post()`
2. Verificación tipo documento → Si es `out_invoice`, continúa
3. Búsqueda configuración FEL → `fel.config` por compañía
4. Preparación datos → `_prepare_fel_data()`
5. Creación cliente SOAP → `zeep.Client(wsdl_url)`
6. Llamada WS → `client.service.Enviar(**datos)`
7. Procesamiento respuesta → Actualización `fel_cufe`, `fel_status`
8. Manejo excepciones → Registro error en `fel_status`

### 3.2 Puntos de Integración
- **Evento Gatillador**: Validación de factura (`action_post`).
- **Condición de Ejecución**: `move_type == 'out_invoice'`.
- **Transacción**: Sincronización con WS FEL.

## 4. MAPEO DE DATOS

### 4.1 Estructura de Datos FEL
La transformación sigue el esquema definido por The Factory HKA:

#### 4.1.1 Datos de Transacción
| Campo Odoo | Campo FEL | Descripción |
|------------|-----------|-------------|
| `name` | `numeroDocumentoFiscal` | Número de factura |
| `invoice_date` | `fechaEmision` | Fecha de emisión |
| `partner_id.vat` | `numeroRUC` | RUC del cliente |
| `partner_id.name` | `razonSocial` | Razón social cliente |

#### 4.1.2 Datos de Ítems
| Campo Odoo | Campo FEL | Descripción |
|------------|-----------|-------------|
| `product_id.name` | `descripcion` | Descripción producto |
| `quantity` | `cantidad` | Cantidad |
| `price_unit` | `precioUnitario` | Precio unitario |
| `price_subtotal` | `precioItem` | Subtotal ítem |
| `price_total` | `valorTotal` | Total con impuesto |

#### 4.1.3 Datos de Totales
| Campo Odoo | Campo FEL | Descripción |
|------------|-----------|-------------|
| `amount_untaxed` | `totalPrecioNeto` | Total sin impuestos |
| `amount_tax` | `totalITBMS` | Total ITBMS |
| `amount_total` | `totalFactura` | Total factura |

### 4.2 Reglas de Transformación
- Fechas: Formato ISO 8601 con zona horaria.
- Números: Separador decimal punto, sin separador miles.
- Campos opcionales: Omitidos si vacíos.

## 5. CONSIDERACIONES TÉCNICAS

### 5.1 Requisitos de Infraestructura
- **Python**: Versión 3.8+
- **Librerías**: `zeep` para SOAP
- **Conectividad**: HTTPS al WS FEL
- **Certificados**: SSL válidos

### 5.2 Seguridad
- **Almacenamiento**: Tokens en base de datos encriptada.
- **Transmisión**: HTTPS obligatorio.
- **Acceso**: Control por grupos de usuario Odoo.
- **Auditoría**: Logs de Odoo para operaciones FEL.

### 5.3 Rendimiento
- **Latencia**: Llamadas síncronas al WS (tiempo de respuesta ~2-5 seg).
- **Escalabilidad**: Una llamada por factura validada.
- **Manejo de Carga**: Sin límites específicos implementados.

### 5.4 Limitaciones Actuales
- Soporte limitado a facturas de venta estándar.
- Mapeo simplificado de impuestos (solo ITBMS básico).
- No implementa métodos adicionales FEL (EstadoDocumento, Anulacion).
- Falta validación previa de datos antes del envío.

## 6. ESTRATEGIA DE PRUEBAS

### 6.1 Entornos de Prueba
- **Demo**: https://demoemision.thefactoryhka.com.pa
- **Producción**: URL proporcionada por The Factory HKA

### 6.2 Casos de Prueba
- Envío exitoso de factura simple.
- Manejo de errores de conexión.
- Validación de tokens inválidos.
- Procesamiento de respuestas WS.

### 6.3 Herramientas de Prueba
- Tokens de demo proporcionados por The Factory HKA.
- Logs de Odoo para debugging.
- Herramientas de monitoreo de red.

## 7. PLAN DE MANTENIMIENTO

### 7.1 Monitoreo
- Estado de conectividad WS FEL.
- Tasa de éxito de envíos.
- Logs de errores recurrentes.

### 7.2 Actualizaciones
- Cambios en API FEL.
- Actualizaciones de librerías (`zeep`).
- Mejoras en mapeo de datos.

## 8. RIESGOS Y MITIGACIONES

### 8.1 Riesgos Identificados
- **Cambio de API**: Monitoreo continuo de documentación FEL.
- **Dependencia Externa**: Contrato SLA con The Factory HKA.
- **Volumen de Transacciones**: Implementar colas asíncronas si necesario.

### 8.2 Plan de Contingencia
- Modo offline para facturación local.
- Reintentos automáticos de envío.
- Alertas proactivas por fallos.

## 9. ANEXOS

### 9.1 Diagramas
- Diagrama de arquitectura (adjunto).
- Diagrama de flujo funcional (adjunto).

### 9.2 Referencias Técnicas
- Documentación Odoo: https://www.odoo.com/documentation
- Manual FEL: https://felwiki.thefactoryhka.com.pa
- Especificaciones SOAP: https://docs.python-zeep.org

---

**Nota**: Este documento es propiedad intelectual de Corporación Red Neural C.A. Queda prohibida su reproducción sin autorización expresa.
