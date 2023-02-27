# Test-monet

Implementación de un sistema para manejar notas
de estudiantes, exámenes con sus preguntas y respuestas, y modificaciones en el django
Admin para mostrar las respuestas escogidas por un estudiante.

Para iniciar es necesario clonar el proyecto desde el repositorio. Posteriormente instale los requerimientos y luego realice las migraciones.
Pasado esto debe crear un super usuario con el cual primero registrara los datos de los estudiantes, por cada registro se creará un usuario con una contraseña por defecto que será la que asigne en el campo “code”. Además de ello este usuario se agregará automáticamente al Grupo “student” que tiene los permisos para ver las notas desde el admin de Django.

Luego debe crear el test y hecho esto debe crear las preguntas o questions relacionadas al test. En esta parte es importante registrar la respuesta y el puntaje de la pregunta , para que al momento que el estudiante registre su respuesta el sistema lo pueda comparar y asignar el puntaje correspondiente.

Por ejemplo:

Test: Examen-matemática.
Name: ¿Cuánto es 3 * 5?
Answer: 15
Points: 5

Una vez creado el Test con sus preguntas, el estudiante deberá acceder al link correspondiente con el numero de test para registrar sus respuestas:
http://127.0.0.1:8000/answer/test/<int:test_id>/

El envió de las respuestas deberá ser del siguiente modo:
[
  {
    "question": 1,
    "answer": "respuesta1"
  },
  {
    "question": 2,
    "answer": "respuesta2"
  },
  {
    "question": 3,
    "answer": "respuesta3"
  }
]

Al final el estudiante con su nombre y código podrá ingresar al sistema para poder revisar sus respuestas.

