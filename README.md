# 📌GPT-CodeReview-Python

Este es un POC en construcción.

Utilizando GPT, podemos realizar el análisis de un código para poder saber que buenas prácticas podemos aplicar, si estámos aplicando de manera corecta el PEP-8, para re escribir un código o mejorar el que tenemos.

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

Para configurar las variables de entorno en el archivo `.env`, sigue estos pasos:

1. Crea un archivo llamado `.env` en la raíz del proyecto.
2. Abre el archivo `.env` en un editor de texto.
3. Agrega las variables de entorno necesarias en el formato `VARIABLE=valor`.
4. Guarda el archivo `.env`.

A continuación, se describen las variables de entorno utilizadas en el proyecto:
para este caso usamos el servicio de GPT proporcionado por Microsoft Azure.

- `AZOPENAIKEY`: Clave de API de OpenAI para acceder a la API de GPT.
- `AZOPENAIENDPOINT`: Punto final de la API de OpenAI para acceder a la API de GPT.
- `AZOPENAITYPE`: Tipo de modelo de GPT a utilizar (p. ej., `davinci`).
- `AZOPENAIVERSION`: Versión de GPT a utilizar (p. ej., `2020-05-03`). Si no se especifica, se utilizará la versión más reciente.
- `RETRYATTEMPTS`: Número de intentos de reintentar la conexión si falla.

Por ejemplo:

```
AZOPENAIKEY=XXXXXXXXXXXXXXXXXXXXX
AZOPENAIENDPOINT=https://api.openai.com/v1
AZOPENAITYPE=davinci

```

## repositorio

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
- `tdt`: aplica tdt basado en una descripción y guarda las pruebas generadas en  `p`.

### Ejemplos

suponiendo que `p=RR`

TDT de un código para limpiar carácteres especiales

    python review.py -n "eliminar carácteres especiales de un string que no son UTF8" -p "../RR/" -t "tdt"

salida:

    import pytest
    import re

    def remove_non_utf8_chars(input_string):
        #elimina caracteres especiales de un string que no son UTF8
        return re.sub(r'[^\x00-\x7F]+','', input_string)

    @pytest.mark.parametrize("input_string, expected_output", [
        ("Hola! 🤗", "Hola!"),
        ("¿Cómo estás? 🤔", "Cmo ests?"),
        ("Muy bien, gracias 🙏", "Muy bien, gracias"),
    ])
    def test_remove_non_utf8_chars(input_string, expected_output, capsys):
        # Comprueba que la función elimina los caracteres especiales
        remove_non_utf8_chars(input_string)
        out, err = capsys.readouterr()
        assert out == expected_output

    def test_remove_non_utf8_chars_type_error(monkeypatch):
        # Comprueba que la función arroja un TypeError cuando el parámetro
        # no es una cadena de caracteres
        monkeypatch.setattr(remove_non_utf8_chars, "input_string", 123456)
        with pytest.raises(TypeError):
            remove_non_utf8_chars(input_string)

___

Pedir que codifique la función que detecta esdrujulas en un texto

    python review.py -n "hacer una función en python aplicando buenas prácticas que detecte en un texto si hay palabras esdrujulas, retornarlas en una lista" -p "../RR/" -t "ask"

salida:

    def detectar_palabras_esdrujulas(texto):
        resultado = []
        palabras = texto.split()  # separa el texto en palabras

        for palabra in palabras:
            if palabra.endswith("í") or palabra.endswith("ó"):
                resultado.append(palabra)

        return resultado

Revisar si hay malas prácticas en el código
    
    python review.py -p "../RR/example_.py" -t "best"

salida:

    1. [E]Error: Usar el método split() de cadenas sin especificar el argumento del caracter de separación. 
    [S]Sugerencia: Utilizar el argumento del carácter de separación para mejorar la legibilidad del código.

    2. [E]Error: El nombre de la variable resultado no es descriptivo.
    [S]Sugerencia: Usar nombres más descriptivos para las variables como palabras_esdrujulas_encontradas.

    3. [E]Error: Utilizar índices de iteración en lugar de iterar sobre los elementos de la lista.
    [S]Sugerencia: Utilizar iteración directa sobre los elementos de la lista para simplificar el código.

Rehacer el código basado en las sugerencias de buenas prácticas de la tarea "best"

     python review.py -p "../RR/example_.py" -t "rebuild"

salida:

     def encontrar_palabras_esdrujulas(texto):
        palabras_esdrujulas_encontradas = []

        for palabra in texto.split():
            if palabra.endswith(('í', 'ó')):
            palabras_esdrujulas_encontradas.append(palabra)

        return palabras_esdrujulas_encontradas
___

Mejorar el código de acuerdo al Zen de Python

    python review.py -p "../RR/example_.py" -t "improve"

salida:

    def detectar_palabras_esdrujulas(texto: str) -> list:
    """
    Esta función detecta todas las palabras esdrújulas dentro de un
    texto dado y devuelve una lista con ellas.
    """
    palabras = texto.split()  # separa el texto en palabras
    return

___

Pedir explicación de lo que hace un código

    python review.py -p "../RR/example_.py" -t "explain"

salida:

    Línea 1 a 5: Esta función recibe una cadena de texto como argumento y devuelve una lista con todas las palabras que terminen con "í" o "ó". Para hacer esto, primero usa una comprensión de listas para separar el texto en palabras individuales. Luego, usa un bucle for para recorrer cada palabra y comprobar si termina con "í" o "ó" usando el método de cadena ".endswith()". Si la palabra cumple esta condición, se agrega a la lista de resultados. Finalmente, la función devuelve la lista de palabras esdrújulas
    encontradas.

___

Auditar un código

    python review.py -p "../RR/example_.py" -t "auditoria"

salida:

    Error: El código no sigue las convenciones PEP 8.
    Ejemplo de código correcto:

    def detectar_palabras_esdrujulas(texto):
        resultado = []
        palabras = texto.split()  # separa el texto en palabras

        for palabra in palabras:
            if palabra.endswith("í") or palabra.endswith("ó"):
                resultado.append(palabra)

        return resultado

___

Revisar si hay vulnerabilidades o porblemas de seguridad

    python review.py -p "../RR/example_.py" -t "security

salida:

    Problemática:
    1. Inyección de código: el texto proporcionado por el usuario podría contener código malicioso que podría ser ejecutado por el programa.
    2. Deserialización insegura: el texto proporcionado por el usuario podría contener información maliciosa en formato de serialización que podría ser ejecutada por el programa.
    3. Uso de componentes con vulnerabilidades conocidas: si el programa está utilizando componentes con vulnerabilidades conocidas, es posible que los usuarios puedan explotar esas vulnerabilidades para obtener acceso no autorizado.

    Sugerencia:
    1. Utilizar una función de filtro para verificar si el texto proporcionado contiene caracteres no permitidos.
    2. Utilizar una función de deserialización segura para verificar que el texto proporcionado no está en formato de serialización.
    3. Asegurarse de que todos los componentes utilizados en el programa estén actualizados y no tengan vulnerabilidades conocidas.

    Código reescrito:
    def detectar_palabras_esdrujulas(texto):
        resultado = []
        palabras = filter(lambda x: not set('<>{}[]()=+-*/\|&^%$#@!`~').intersection(x), texto.split())  # filtra el texto para eliminar caracteres no permitidos

        for palabra in palabras:
            if palabra.endswith("í") or palabra.endswith("ó"):
                resultado.append(palabra)

        return resultado

___

Crear pruebas unitarias de un código

    python review.py -p "../RR/example_.py" -t "pytest"

salida:

    @pytest.mark.parametrize("texto, esdrujulas", [
        ("Hola mundo", []),
        ("Hola trabají", ["trabají"]),
        ("Tengó que trabajar", ["Tengó"]),
        ("No me gusta leer", []),
    ])
    def test_detectar_palabras_esdrujulas(texto, esdrujulas):
        assert detectar_palabras_esdrujulas(texto) == esdrujulas


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