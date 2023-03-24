## 📌Python-GPT-CodeReview

## 🚀 Comenzando

Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

Para clonar el repositorio de GitHub, sigue estos pasos:

1. Abre la página del repositorio en GitHub.
2. Haz clic en el botón "Code" verde en la esquina derecha.
3. Copia la URL del repositorio haciendo clic en el icono del portapapeles.
4. Abre tu terminal y navega hasta la carpeta donde deseas clonar el repositorio.
5. Ejecuta el comando `git clone` seguido de la URL que copiaste en el paso 3.

Por ejemplo:

```
git clone <https://github.com/fecork/Python-GPT-CodeReview.git>

```

Esto clonará el repositorio en tu máquina local.

### 📋 Pre-requisitos

- kedro==0.18.1
- openai
- tenacity
- numpy
- python-dotenv
- rich

### 🔧 Instalación

1. Clonar el repositorio
2. Ejecutar `pip install -r requirements.txt`
3. Configurar las variables de entorno en el archivo .env
4. Ejecutar `python review.py -t "best" -p "archivo.py"`

La opción `-t` se utiliza para seleccionar una tarea específica a realizar dentro del script `review.py`. A continuación, se describen las tareas disponibles:

- `best`: Ejecuta las mejores prácticas para el código especificado en la opción `p`.
- `improve`: Mejora el código especificado en la opción `p`.
- `security`: Verifica la seguridad del código especificado en la opción `p`.
- `create`: Crea un nuevo código para cumplir con los requisitos especificados en la opción `n`.
- `rebuild`: Reconstruye el código especificado en la opción `p` teniendo en cuenta el error especificado en la opción `e`.
- `explain`: Explica el código especificado en la opción `p`.
- `pytest`: Genera las pruebas unitarias utilizando pytest en el código especificado en la opción `p`.
- `audit`: Genera el reporte de auditoría en el código especificado en la opción `p`.

## 🛠️ Construido con

- [kedro](https://kedro.readthedocs.io/en/stable/) - El framework utilizado
- [openai](https://beta.openai.com/docs/api-reference/introduction/) - Para realizar la auditoría de código
- [tenacity](https://tenacity.readthedocs.io/en/latest/) - Para reintentar las solicitudes de conexión
- [numpy](https://numpy.org/) - Para realizar cálculos matemáticos
- [python-dotenv](https://pypi.org/project/python-dotenv/) - Para cargar las variables de entorno
- [rich](https://rich.readthedocs.io/) - Para mostrar mensajes en la consola con estilo

## 🖇️ Contribuyendo

Por favor lee el [CONTRIBUTING.md](https://gist.github.com/villanuevand/xxxxxx) para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.

## 📖 Wiki

Puedes encontrar más información sobre el uso de este proyecto en nuestra [Wiki](https://github.com/tu/proyecto/wiki)

## 📌 Versionado

Usamos [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/tu/proyecto/tags).

## ✒️ Autores

- **Ferney Córdoba Canchala** - *Trabajo Inicial* - [fecork](https://github.com/fecork)

## 📄 Licencia

Este proyecto está bajo la Licencia (Tu Licencia) - mira el archivo [LICENSE.md](notion://www.notion.so/fecork/LICENSE.md) para detalles

## 🎁 Expresiones de Gratitud

- Comenta a otros sobre este proyecto 📢
- Invita una cerveza 🍺 o un café ☕ a alguien del equipo.
- Da las gracias públicamente 🤓.
- etc.