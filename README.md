# Test Plan - Proyecto Listly

El software se va a usar desde el celular del vendedor, los artículos tienen su propio código, el formato de lista es el Excel (4 distintos).

---

## 1. Introduction

Listly será un proyecto que podrá ayudar a los vendedores ambulantes a tener al alcance de sus manos los precios actualizados de los productos que venden para poder hacer una venta más ágil.

### 1.1 Proposito

El propósito de este documento es dejar por escrito el Test Plan del producto de software **Listly**, desarrollado por **Santino Beltran, Franco Roldán, Dante Illescay, Francisco Merenda**. Este documento será usado por los stakeholders del proyecto, además de todos los miembros del equipo.

### 1.2 Scope

El alcance de este proyecto se limita a desarrollar y testear las características que describiremos más adelante en este documento.

- Las **pruebas de estrés y de rendimiento** no van a realizarse ya que los vendedores (los usuarios) serán pocos y no será necesario.
- Las **pruebas de automatización** tampoco estarán dentro del alcance del proyecto ya que no es lo que se busca en este caso.
- Las **pruebas de funcionalidad** sí estarán dentro del alcance del proyecto, al igual que las de **usabilidad**, **seguridad** y de **performance**.
- Las **pruebas de compatibilidad, UI y Hardware** no se realizarán ya que todos los vendedores van a contar con el mismo dispositivo.

### 1.3 Definitions, Acronyms, and Abbreviations

| Abbreviation | Word     |
|--------------|----------|
| A            | Admin    |
| V            | Vendedor |

---

## 2. Requerimientos Específicos

Listly tendrá **2 roles**:

- **Administrador**
- **Vendedor**

El rol de **vendedor** será un rol público. Debido a que no destinamos recursos a la seguridad, cualquiera podrá entrar a ver el listado de precios.

Generamos un apartado de **superusuario** el cual será capaz de loguearse y editar las listas de precios.

### Funcionalidades por rol

| Función                    | Admin | Vendedor |
|----------------------------|:-----:|:--------:|
| Cargar lista de precios    |  ✅   |          |
| Ver lista de precios       |  ✅   |    ✅    |
| Editar precio              |  ✅   |          |
| Búsqueda por nombre        |  ✅   |    ✅    |
| Borrar precio              |  ✅   |          |
| Cambiar contraseña         |  ✅   |          |
| Login y Logout             |  ✅   |          |
| Actualizar lista de precios|  ✅   |          |
| Gestión de artículos       |  ✅   |          |

---

## 2.2 Descripción de módulos

| Nombre del módulo          | Roles  | Descripción |
|----------------------------|--------|-------------|
| Cargar lista de precios    | Admin  | El administrador debe ser capaz de cargar las listas de precios al sistema cuando lo necesite. |
| Editar precio              | Admin  | El administrador puede editar los precios de todos los productos. |
| Borrar precio              | Admin  | El administrador puede borrar el precio de todos los productos. |
| Cambiar contraseña         | Admin  | El administrador puede cambiar la contraseña de ingreso. |
| Login y Logout             | Admin  | El administrador debe realizar un ingreso y salida del sistema de forma segura. |
| Actualizar lista de precios| Admin  | El administrador puede actualizar la lista de precios. |
| Gestión de artículos       | Admin  | El administrador puede dar de alta o baja a artículos que estén en el sistema. |
| Ver lista de precios       | Admin, Vendedor | Ambos pueden ver la lista de precios. |
| Búsqueda por nombre        | Admin, Vendedor | Ambos pueden buscar artículos por nombre. |

## 2.3 Historias de usuario

* Como administrador, quiero tener un login para poder acceder a la página y administrar las listas.
* Como vendedor, quiero poder ver las listas para ver los precios.
* Como vendedor, quiero poder buscar un artículo para ver el precio del mismo de una forma rápida y eficiente.
* Como administración, quiero cargar la lista de precios para actualizar la lista de precios. 
* Como administración, quiero cambiar la contraseña para generar una nueva en caso de olvido.
* Como administración, quiero borrar los artículos para dejar solo los que trabajamos.
* Como administración, quiero editar los datos para corregir los precios.

---

## 2.4 Casos de prueba

### 1. Login del Administrador
- ID: TC-ADM-001  
- Historia: Como administrador, quiero tener un login para poder acceder a la página y administrar las listas.  
- Pasos a seguir:
  1. Ir a la página de login.
  2. Ingresar usuario y contraseña válidos.
  3. Hacer clic en "Iniciar sesión".
- Datos esperados: Usuario y contraseña válidos.  
- Resultado esperado: Se accede al panel de administración.

---

### 2. Visualizar listas de precios (vendedor)
- ID: TC-VEND-001  
- Historia: Como vendedor, quiero poder ver las listas para ver los precios.  
- Pasos a seguir:
  1. Navegar a la sección de lista de precios.
- Datos esperados: Lista de precios actual.  
- Resultado esperado: Se visualizan los productos y sus precios correctamente.

---

### 3. Buscar artículo (vendedor)
- ID: TC-VEND-002  
- Historia: Como vendedor, quiero poder buscar un artículo para ver el precio del mismo de una forma rápida y eficiente.  
- Pasos a seguir:
  1. Ir a la sección de búsqueda.
  2. Ingresar el nombre del producto y buscar.
- Datos esperados: Nombre de un artículo existente.  
- Resultado esperado: Se muestra el artículo buscado junto a su precio.

---

### 4. Cargar lista de precios (administrador)
- ID: TC-ADM-002  
- Historia: Como administración, quiero cargar la lista de precios para actualizar la lista de precios.  
- Pasos a seguir:
  1. Iniciar sesión como administrador.
  2. Ir a la sección "Cargar lista de precios".
  3. Seleccionar archivo (Excel, PDF, etc.) válido.
  4. Confirmar la carga.
- Datos esperados: Archivo con estructura válida.  
- Resultado esperado: Se actualiza la lista de precios y se muestra mensaje de confirmación.

---

### 5. Cambiar contraseña (administrador)
- ID: TC-ADM-003  
- Historia: Como administración, quiero cambiar la contraseña para generar una nueva en caso de olvido.  
- Pasos a seguir:
  1. Iniciar sesión.
  2. Ir a "Configuración de cuenta".
  3. Seleccionar "Cambiar contraseña".
  4. Ingresar la contraseña actual, la nueva y confirmar.
- Datos esperados: Contraseña actual correcta, nueva válida.  
- Resultado esperado: La contraseña se actualiza correctamente.

---

### 6. Borrar artículo (administrador)
- ID: TC-ADM-004  
- Historia: Como administración, quiero borrar los artículos para dejar solo los que trabajamos.  
- Pasos a seguir:
  1. Iniciar sesión como administrador.
  2. Ir a la sección de artículos.
  3. Seleccionar un artículo.
  4. Hacer clic en "Eliminar".
- Datos esperados: Artículo existente y seleccionable.  
- Resultado esperado: El artículo se elimina y desaparece de la lista.

---

### 7. Editar artículo (administrador)
- ID: TC-ADM-005  
- Historia: Como administración, quiero editar los datos para corregir los precios.  
- Pasos a seguir:
  1. Iniciar sesión como administrador.
  2. Ir a la sección de productos.
  3. Seleccionar un producto.
  4. Modificar su precio o información.
  5. Guardar cambios.
- Datos esperados: Precio válido, artículo existente.  
- Resultado esperado: Se actualizan los datos y se reflejan en la lista de precios.

---

## 3. Especificaciones

### 3.1 Arquitectura

Arquitectura

La aplicación está diseñada bajo una arquitectura cliente-servidor, utilizando un servidor API REST que actúa como intermediario entre los clientes (vendedores) y la base de datos.  
El cliente realiza consultas, como búsqueda de productos o visualización de listas de precios, que son procesadas por el servidor y respondidas con los datos necesarios.

Por otro lado, el administrador accede a un panel de gestión desarrollado bajo el patrón MVC (Modelo-Vista-Controlador), que permite cargar listas de precios, editar o eliminar artículos y gestionar usuarios.

Tanto el cliente como el panel administrativo interactúan con una base de datos centralizada, donde se almacena toda la información del sistema.

## 3.2 Definicion de API

[Contrato](api_contract.yaml)