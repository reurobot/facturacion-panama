# MANUAL DE USUARIO

## MÓDULO DE INTEGRACIÓN FACTURACIÓN ELECTRÓNICA (FEL) PARA ODOO

### Versión del Documento
1.0

### Fecha de Emisión
[28-10-2025]

### Propósito del Documento
El presente manual tiene como objetivo proporcionar las instrucciones necesarias para la instalación, configuración y uso del módulo de integración FEL en el sistema ERP Odoo, cumpliendo con las normativas de Facturación Electrónica en Panamá.

### Alcance
Este manual aplica a usuarios administradores, contadores y personal técnico responsable de la implementación y operación del módulo FEL en entornos Odoo.

### Responsabilidades
- **Administrador del Sistema**: Instalación y configuración inicial.
- **Usuario Contable**: Configuración de parámetros FEL y validación de facturas.
- **Desarrollador**: Personalización y mantenimiento técnico.

## 1. INTRODUCCIÓN AL MÓDULO

El módulo "Panama Electronic Invoicing (FEL)" permite la integración automática entre Odoo y el sistema de Facturación Electrónica de Panamá, facilitando el cumplimiento legal de emisión de facturas electrónicas.

### 1.1 Funcionalidades Principales
- Envío automático de facturas al FEL al validar en Odoo.
- Almacenamiento de códigos CUFE y estados de envío.
- Configuración centralizada de credenciales FEL.

## 2. REQUISITOS PREVIOS

### 2.1 Requisitos del Sistema
- Instancia de Odoo versión 15.0 o superior.
- Acceso administrativo al servidor Odoo.
- Conexión a internet para comunicación con servicios FEL.

### 2.2 Requisitos de Software
- Python 3.8 o superior.
- Librería `zeep` instalada en el entorno Python de Odoo.

## 3. INSTALACIÓN DEL MÓDULO

### 3.1 Procedimiento de Instalación
1. Ubique el directorio de addons de su instancia Odoo.
2. Copie la carpeta `l10n_pa_fel` al directorio de addons.
3. Ejecute el comando: `pip install zeep` en el entorno Python de Odoo.
4. Inicie sesión en Odoo como administrador.
5. Navegue a **Aplicaciones > Actualizar Lista de Aplicaciones**.
6. Busque el módulo "Panama Electronic Invoicing (FEL)".
7. Haga clic en "Instalar".

### 3.2 Verificación de Instalación
- El módulo aparecerá en la lista de aplicaciones instaladas.
- Verifique que no haya errores en el log de Odoo.

## 4. CONFIGURACIÓN DEL MÓDULO

### 4.1 Acceso a Configuración FEL
1. Inicie sesión en Odoo.
2. Navegue a **Contabilidad > FEL Config**.
3. Haga clic en "Crear" para nueva configuración.

### 4.2 Parámetros de Configuración
Complete los siguientes campos obligatorios:
- **Nombre**: Identificador descriptivo de la configuración.
- **Token Empresa**: Credencial proporcionada por The Factory HKA.
- **Token Password**: Contraseña asociada al token.
- **WSDL URL**: URL del servicio web FEL (demo: https://demoemision.thefactoryhka.com.pa/ws/obj/v1.0/Service.svc?singleWsdl).
- **Compañía**: Compañía de Odoo asociada.

### 4.3 Validación de Configuración
- Guarde la configuración.
- Verifique que los tokens sean válidos contactando al proveedor FEL.

## 5. OPERACIÓN DEL MÓDULO

### 5.1 Creación de Facturas
1. Cree una factura de venta estándar en Odoo.
2. Complete todos los campos requeridos (cliente, productos, impuestos).

### 5.2 Validación y Envío FEL
1. Haga clic en "Confirmar" para validar la factura.
2. El sistema automáticamente enviará la factura al FEL.
3. Espere la confirmación del envío.

### 5.3 Verificación del Estado FEL
1. Abra la factura validada.
2. Navegue a la pestaña "Otra Información".
3. Revise los campos:
   - **CUFE**: Código único de factura electrónica.
   - **Estado FEL**: Estado del proceso (Enviado, Error: [detalle]).

## 6. SOLUCIÓN DE PROBLEMAS

### 6.1 Problemas Comunes
- **Error de Conexión**: Verifique conectividad a internet y URL WSDL.
- **Tokens Inválidos**: Confirme credenciales con The Factory HKA.
- **Datos Incorrectos**: Valide información de cliente y productos.

### 6.2 Diagnóstico
- Revise el campo "Estado FEL" para mensajes de error específicos.
- Consulte los logs de Odoo para detalles técnicos.

### 6.3 Procedimiento de Recuperación
1. Corrija el problema identificado.
2. Reintente la validación de la factura.
3. Si persiste, contacte soporte técnico.

## 7. SOPORTE TÉCNICO

### 7.1 Canales de Soporte
- **Proveedor FEL**: The Factory HKA - fel@thefactoryhka.com.pa
- **Desarrollador del Módulo**: Corporación Red Neural C.A

### 7.2 Información Requerida para Soporte
- Versión de Odoo.
- Logs de error relevantes.
- Configuración FEL (sin tokens sensibles).

## 8. ANEXOS

### 8.1 Glosario de Términos
- **FEL**: Facturación Electrónica de Panamá.
- **CUFE**: Código Único de Factura Electrónica.
- **WSDL**: Web Services Description Language.

### 8.2 Referencias
- Manual de Integración FEL: https://felwiki.thefactoryhka.com.pa
- Documentación Odoo: https://www.odoo.com/documentation

---

**Nota**: Este documento es propiedad intelectual de Corporación Red Neural C.A. Queda prohibida su reproducción sin autorización expresa.
