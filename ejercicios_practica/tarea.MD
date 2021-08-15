![Inove banner](inove.jpg)
Inove Escuela de Código\
info@inove.com.ar\
Web: [Inove](http://inove.com.ar)

---
# Tarea: Django - Template Language

Al realizar esta tarea pondremos en práctica los conocimientos adquiridos en clase.
Una vez finalizada, el alumno debe subir el enlace a su repositorio "forkeado" el foro de tarea correspondiente -NO SE ADMITE LA DEVOLUCIÓN POR OTRO CANAL SALVO SE ESPECIFIQUE LO CONTRARIO- 

Recuerde que no debe subir la base de datos al sistema, para ello se encuentra el archivo .gitignore que especifica los archivos y directorios omitidos.

---

### 1. Completar el archivo base.html.
En la carpeta de templates/e-commerce/ se encuentra el template "base.html" vacío
Genere un template base para su aplicación, puede usar como base el utilizado en el ejemplo de clase.


### 2. Genere templates hijos y sus vistas.
Una vez generado el template base, genere templates hijos para su aplicación, remplazando los bloques que crea necesarios.

Debe generar como mínimo 5 templates para su aplicación, ellos serán para las páginas:
* login: para inicio de sesión del usuario (puede reutilizar el formulario de la tarea de la clase anterior)
* thanks: un mensaje de agradecimiento por su compra
* user: debe listar los datos del usuario logueado
* cart: debe listar los comics en el carrito de dicho usuario
* wish: debe listar los comics favoritos de dicho usuario

Para cada template debe generar una vista en donde recomendamos utilizar el método visto en clase **"get_context_data()"** para realizar la lógica de negocio (consultas, calculos, etc;).

### 3. Asignar las urls a las páginas creadas.
Debe asignar las urls para cada página, así mismo, debe asignarles un "name" para cada endpoint.

### 4. Personalice el estilo del sitio.
Modifique el archivo base.css brindado para personalizar el estilo del sitio a su gusto y suba una captura de pantalla al foro de tarea del campus.

---

## ¿Dudas?
Ante cualquier inquietud, debe referirse a los canales especificados para su trato en inove.