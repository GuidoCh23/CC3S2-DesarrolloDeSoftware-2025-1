## ACTIVIDAD 7
Nombre: Guido Anthony Chipana Calderon

### Inicializacion
Clonamos el repositorio donde esta el proyecto base de la actividad 7

   <div align="center">
      <img src="https://i.postimg.cc/GtNnz3ZV/Act7-0-1.png" alt="act7.0.1" width="750" />
   </div>

Creamos nuestro entorno virtual y lo inicializamos o activamos

   <div align="center">
      <img src="https://i.postimg.cc/nz9LJ5py/Act7-0-2.png" alt="act7.0.2" width="750" />
   </div>

Instalamos los requisitos del proyecto

   <div align="center">
      <img src="https://i.postimg.cc/BQmt22Yw/Act7-0-3.png" alt="act7.0.3" width="750" />
   </div>

Ahora ya tenemos listo el proyecto para comenzar a realizar los ejercicios

### Estructura del proyecto

El proyecto tiene la siguiente estructura de directorios:

```
.
├── features
│   ├── belly.feature
│   ├── environment.py
│   └── steps
│       └── steps.py
├── src
│   └── belly.py
└── README.md
```

- **features**: Contiene los archivos relacionados con Behave.
  - **belly.feature**: Archivo que describe las características y escenarios en lenguaje Gherkin.
  - **environment.py**: Archivo de configuración para inicializar el contexto de Behave.
  - **steps**: Carpeta que contiene las definiciones de los pasos.
    - **steps.py**: Implementación de los pasos definidos en `belly.feature`.
- **src**: Contiene el código fuente del proyecto.
  - **belly.py**: Implementación de la clase `Belly`.
- **README.md**: Este archivo de documentación.

### Ejercicio 1: **Añadir soporte para minutos y segundos en tiempos de espera**

**Objetivo**  
- Ampliar la funcionalidad para reconocer tiempos de espera expresados en horas, minutos y segundos.

**Instrucciones**  
1. **Modifica** la función que maneja el tiempo de espera en `steps.py` (o donde parsees el tiempo) para que acepte:
   - "1 hora y 30 minutos"
   - "90 minutos"
   - "3600 segundos"
   - **Variaciones** que incluyan segundos (por ejemplo, `"1 hora, 30 minutos y 45 segundos"`).
2. **Implementa** un escenario de prueba en Gherkin (`belly.feature`) que valide que el estómago gruñe o no según estas variaciones de tiempo.
3. **Considera** también crear pruebas unitarias con Pytest para la lógica de parsing (función que convierte el texto de tiempo en horas decimales).
4. **En un entorno DevOps**:
   - Agrega la ejecución de `behave` y `pytest` en tu *pipeline* de CI/CD, de modo que al hacer push de los cambios se ejecuten automáticamente las pruebas.

**Ejemplo Gherkin**:
```gherkin
Escenario: Comer pepinos y esperar en minutos y segundos
  Dado que he comido 35 pepinos
  Cuando espero "1 hora y 30 minutos y 45 segundos"
  Entonces mi estómago debería gruñir
```
**Solucion**:

1. He modificado `step_when_wait_time_description` para que acepte los siguiente formatos:
	- "1 hora y 30 minutos"
   - "90 minutos"
   - "3600 segundos"
   - Y variaciones que incluyan segundos (por ejemplo, `"1 hora, 30 minutos y 45 segundos"`).
 
   <div align="center">
      <img src="https://i.postimg.cc/QtZQ9v03/Act7-1-1.png" alt="act7.1.1" width="700" />
   </div>

En `step_when_wait_time_description` agregue una nueva linea en la que se elimina las `,` de `time_description` para el caso en que la descripcion tenga una similar estructura a esta `"1 hora, 30 minutos y 45 segundos"`

```python
time_description = time_description.replace(',',' ')
```

Tambien para que `step_when_wait_time_description` acepte segundos, modifique la expresion regular para que tome en cuenta los segundos

```python
pattern = re.compile(r'(?:(\w+)\s*horas?)?\s*(?:(\w+)\s*minutos?)?\s*(?:(\w+)\s*segundos?)?')
```

Y finalmente agregue nuevas lineas para que obtenga los segundo de `time_description`, convertir la palabra en numero, en el caso que el numero de segundo esta escrito texto y no en numeros, y modifique el calculo de `total_time_in_hours` para que tome en cuenta los segundos

```python
	if match:
            hours_word = match.group(1) or "0"
            minutes_word = match.group(2) or "0"
            seconds_word = match.group(3) or "0" #obtiene los segundos

            hours = convertir_palabra_a_numero(hours_word)
            minutes = convertir_palabra_a_numero(minutes_word)
            seconds = convertir_palabra_a_numero(seconds_word) #pasa la palabra a numero
			
	    #calcula el tiempo en horas, tomando en cuenta los segundos
            total_time_in_hours = hours + (minutes / 60) + (seconds / 3600) 
```

2. Añadi 5 escenarios Gherkin en `belly.feature` para probar las nuevas funcionalidades

   <div align="center">
      <img src="https://i.postimg.cc/Gp21ZhDM/Act7-1-2.png" alt="act7.1.2" width="450" />
   </div>

Agregue diferente escenarios Gherkin, como por ejemplo donde solo hay segundos, los numeros son textos, usando horas, minutos y segundos, etc.

3. Añadi pruebas unitarias Pytest para testear la funcion que convierte texto de tiempo a horas decimales

   <div align="center">
      <img src="https://i.postimg.cc/C5QgMyVG/Act7-1-5.png" alt="act7.1.5" width="650" />
   </div>

Usando `@pytest.mark.parametrize` pude agregar varias pruebas en la que se incluyen segundos

4. Cree un archivo `ci.yml` en `.github/workflows` para `CI/CD`

   <div align="center">
      <img src="https://i.postimg.cc/3J0Ry1b8/Act7-1-4.png" width="260" />
      <img src="https://i.postimg.cc/26tv46Qg/Act7-1-3.png" alt="act7.1.4" width="307" />
   </div>

En el archivo `ci.yml` defini que se activaria cuando se pushee a la rama `main` o `features/ejercicio-*` ya que trabajare con rama `feature/ejercicio-1`, `feature/ejercicio-2`, ... , `feature/ejercicio-*`. Tambien se activara cuando vea un pull request a la rama main, todo esto con el fin de evitar agregar scripts con errores u otros problemas y asi mantener una healthy branch

```python
on:
  push:
    branches:  
      - main
      - 'features/ejercicio-*'
  pull_request:
    branches: 
      - main
```

En la parte de `jobs`, agregue un job llamado `test` que se encargara de correr las pruebas pytest y behave

5. Corramos manualmente los tests, ejecutando en la terminal `pytest --cov` y `behave`

   <div align="center">
      <img src="https://i.postimg.cc/yxvmrHZz/Act7-1-6.png" alt="act7.1.6" width="1000" />
   </div>

Hemos corrido `pytest --cov` y vemos que paso todas las pruebas

   <div align="center">
      <img src="https://i.postimg.cc/HnDWDcbw/Act7-1-7.png" alt="act7.1.7" width="500" />
   </div>
   
Tambien hemos corrido `pytest --cov`y vemos que tambien pasa todas las pruebas, por lo que todo esta correctamente funcionando

6. Probemos haciendo un push a la rama `feature/actividad-1`

   <div align="center">
      <img src="https://i.postimg.cc/L5Pdt2QN/Act7-1-8.png" alt="act7.1.8" width="450" />
   </div>

Ahora como hemos pusheamos al repositorio, se activo el job `test` y vemos que paso todas la pruebas, por lo que todo esta correcto

### Ejercicio 2: **Manejo de cantidades fraccionarias de pepinos**

**Objetivo**  
- Permitir que el sistema acepte cantidades fraccionarias de pepinos (decimales).

**Instrucciones**  
1. **Modifica** el sistema (la clase `Belly` y los steps en Behave) para que acepte entradas como `"0.5"`, `"2.75"`.
2. **Implementa** un nuevo escenario en Gherkin donde se ingiera una cantidad fraccionaria y verifica el comportamiento.
3. **Valida** que el sistema lance una excepción o error si se ingresa una cantidad negativa de pepinos.
4. **Pruebas unitarias**:  
   - Cubre el caso de pepinos fraccionarios en `test_belly.py`.
   - Cubre también el caso de pepinos negativos (se espera un error).

**Ejemplo Gherkin**:
```gherkin
Escenario: Comer una cantidad fraccionaria de pepinos
  Dado que he comido 0.5 pepinos
  Cuando espero 2 horas
  Entonces mi estómago no debería gruñir
```

**En un entorno DevOps**:
- Asegúrate de que la falla (excepción por valor negativo) sea reportada como *falla de build* si ocurre.  
- Configura notificaciones (por correo/Slack/Teams) si alguna de las pruebas falla.

**Solucion**:

1. Modifique la clase `Belly` para que acepte cantidades fraccionarias de pepinos

   <div align="center">
      <img src="https://i.postimg.cc/W3f14Nx3/Act7-2-1.png" alt="act7.2.1" width="500" />
   </div>

Cree una nueva funcion `number_validator` para validar si podemos pasar el numero a float y si lo era que lo pase a float, tambien registramos esta funcion como `Number`

   <div align="center">
      <img src="https://i.postimg.cc/NFqRdvkd/Act7-2-2.png" alt="act7.2.2" width="450" />
   </div>

Hemos implementado `Number` en cukes, para que cukes pase como un numero float al metodo `comer` de `belly`

2. Implemente 1 escenario Gherkin para probar la nueva funcionalidad

   <div align="center">
      <img src="https://i.postimg.cc/KzvYFqvm/Act7-2-3.png" alt="act7.2.3" width="450" />
   </div>

3. Modifique la clase `Belly` para que no acepte cantidades negativas de pepinos

   <div align="center">
      <img src="https://i.postimg.cc/rm3zJGMc/Act7-2-4.png" alt="act7.2.3" width="500" />
   </div>

Agregue un una condicion `if` si en el caso que los pepinos comidos son negativos salte una excepción y en el caso que son positivos que continue normalmente

4. Agregue nuevas pruebas unitarias para estos casos

   <div align="center">
      <img src="https://i.postimg.cc/K8tGSSb6/Act7-2-5.png" alt="act7.2.5" width="500" />
   </div>

Agregue en  `tets_belly.py` el test  `test_eat_fractional_cucumber` para testear que se pueda agregar cantidades fraccionarias de pepinos

   <div align="center">
      <img src="https://i.postimg.cc/hjRg22NS/Act7-2-6.png" alt="act7.2.6" width="600" />
   </div>

Tambien agregue otro test llamado `tets_eat_negative_cucumber` para testear que salte una excepción en el caso se agregue valores negativos de pepinos

5. Probemos los tests ejecutando en la terminal `pytest --cov` y `behave`

   <div align="center">
      <img src="https://i.postimg.cc/90qns29K/Act7-2-7.png" alt="act7.2.7" width="1000" />
   </div>

Vemos que los test `pytest` pasan todas las pruebas correctamente

   <div align="center">
      <img src="https://i.postimg.cc/MZVks0YT/Act7-2-8.png" alt="act7.2.8" width="600" />
   </div>

Tambien el test `behave` pasa correctamente

### Ejercicio 3: **Soporte para idiomas múltiples (Español e Inglés)**

**Objetivo**  
- Aceptar descripciones de tiempo en distintos idiomas (español e inglés).

**Instrucciones**  
1. **Modifica** el parsing de tiempo para que reconozca palabras clave en inglés, además de español (por ejemplo, `"two hours"`, `"thirty minutes"`).
2. **Escribe** al menos dos escenarios de prueba en Gherkin que usen tiempos en inglés.
3. **Implementa** una función que convierta las palabras en inglés a valores numéricos (similar a la que se usa para el español).
4. **En un pipeline DevOps**, podrías:
   - Dividir los escenarios en distintos *tags* (`@spanish`, `@english`) y ejecutar cada conjunto en etapas diferentes, o en paralelo.

**Ejemplo Gherkin**:
```gherkin
Escenario: Esperar usando horas en inglés
  Dado que he comido 20 pepinos
  Cuando espero "two hours and thirty minutes"
  Entonces mi estómago debería gruñir
```

**Solucion**

1. He modificado `convertir_palabra_a_numero` para que reconozca palabras numericas en ingles como `"two"`, `"thirty"`, etc

   <div align="center">
      <img src="https://i.postimg.cc/GtvmdHs1/Act7-3-1.png" alt="act7.3.1" width="600" />
   </div>

Agregue palabras de numero en ingles para que pueda reconocer palabras numericas en ingles

2. Tambien he modificado `step_when_wait_time_description` para que acepte palabra en ingles como  `"hours"`, `"minutes"` y `"seconds"`

   <div align="center">
      <img src="https://i.postimg.cc/fRppj5rB/Act7-3-2.png" alt="act7.3.2" width="900" />
   </div>

Modifique la expresion regular para que acepte tambien palabra en ingles

3. Añadi 3 escenarios Gherkin que usen tiempo en ingles

   <div align="center">
      <img src="https://i.postimg.cc/k5MsSSnf/Act7-3-3.png" alt="act7.3.3" width="500" />
   </div>

Agregue 3 diferentes escenarios Gherkin, usando palabras numericas como `two` y usando palabras claves en ingles como `"hours"`, `and`, etc.

4. Añadi tags (@spanish y @english) en los escenarios Gherkin, lo que divide que escenario Gherkin es en español o ingles

   <div align="center">
      <img src="https://i.postimg.cc/1XyDxhfM/Act7-3-4.png" alt="act7.3.4" width="500" />
   </div>

Agregue tags (@spanish y @english) para separar que escenarios son en ingles y cuales son en español

### Ejercicio 4: **Manejo de tiempos aleatorios**

**Objetivo**  
- Permitir ingresar rangos de tiempo (por ejemplo, "entre 1 y 3 horas") y escoger un tiempo aleatorio dentro de ese rango.

**Instrucciones**  
1. **Crea** una función que, dada una expresión como "entre 1 y 3 horas", devuelva un valor aleatorio entre 1 y 3 horas.
2. **Implementa** un escenario en Gherkin que verifique que, tras comer pepinos y esperar un tiempo aleatorio, el estómago puede gruñir.
3. **Imprime** (en consola o logs) el tiempo aleatorio elegido para que el resultado sea rastreable en tu pipeline.
4. **En un pipeline DevOps**:  
   - Considera utilizar un *seed* de aleatoriedad fijo para evitar *flakiness* (tests intermitentes).  
   - O, si manejas aleatoriedad real, acepta el riesgo de pruebas no deterministas y monitorea cuidadosamente.

**Ejemplo Gherkin**:
```gherkin
Escenario: Comer pepinos y esperar un tiempo aleatorio
  Dado que he comido 25 pepinos
  Cuando espero un tiempo aleatorio entre 1 y 3 horas
  Entonces mi estómago debería gruñir
```

**Solucion**

1. Cree una funcion llamada `range_time_description` para que acepte expresione como `entre 1 y 3 horas` y nos devuelva un valor aleatorio entre 1 y 3 en este caso

   <div align="center">
      <img src="https://i.postimg.cc/fLHtt3Hn/Act7-4-1.png" alt="act7.4.1" width="700" />
   </div>

2. Añadi un nuevo escenario Gherkin para probar esta nueva funcionalidad

   <div align="center">
      <img src="https://i.postimg.cc/x8zffqhP/Act7-4-2.png" alt="act7.4.2" width="500" />
   </div>

3. En la funcion `range_time_description` se agrego una linea que imprime el tiempo aleatorio que elige

```python
print(f'Tiempo aleatorio generado: {random_time_hours:.2f} horas (entre {lower} y {higher})')
```

4. Tambien en la funcion `range_time_description` se agrego una seed de aleatoridad fijo para evitar flakiness (tests intermitentes)

```python
seed_value = 42
random.seed(seed_value)
```

### Ejercicio 5: **Validación de cantidades no válidas**

**Objetivo**  
- Manejar y reportar adecuadamente errores al ingresar cantidades no válidas.

**Instrucciones**  
1. **Añade** validaciones para evitar que el usuario ingrese < 0 pepinos o > 100 pepinos.
2. **Modifica** la lógica para arrojar un error (excepción) si la cantidad no es válida.
3. **Implementa** un escenario de prueba que verifique el comportamiento de error.
4. **En tu pipeline**, verifica que la excepción se maneje y el test falle de manera controlada si el sistema no lanza la excepción esperada.

**Ejemplo Gherkin**:
```gherkin
Escenario: Manejar una cantidad no válida de pepinos
  Dado que he comido -5 pepinos
  Entonces debería ocurrir un error de cantidad negativa.
```

**Solucion:**

1. Añadi una nueva validacion en la clase `Belly` para que no acepte pepino `< 0` o `> 100`

   <div align="center">
      <img src="https://i.postimg.cc/0ypxJ38d/Act7-5-1.png" alt="act7.5.1" width="500" />
   </div>

Agregue una condicion `elif` en el caso el numero de pepinos es `> 100` nos salte una excepción

2. Probamos agregando un escenario Gherkin en la que los numeros de pepinos es `> 100`

   <div align="center">
      <img src="https://i.postimg.cc/cHNcLFsz/Act7-5-2.png" alt="act7.5.2" width="450" />
   </div>

3. Verificamos que en nuestra pipeline salte esta expecion o error

   <div align="center">
      <img src="https://i.postimg.cc/bvfnxdKD/Act7-5-3.png" alt="act7.5.3" width="700" />
   </div>

Vemos que hubo un failed, la cual es el escenario Gherkin que hemos agregado, en la que comia 102 pepinos. Por lo que funciona correctamente las condiciones que hemos implementado
