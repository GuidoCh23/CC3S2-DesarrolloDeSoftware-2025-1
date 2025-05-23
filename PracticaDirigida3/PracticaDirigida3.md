## PRACTICA DIRIGIDA 3
Nombre: Guido Anthony Chipana Calderon

### Bash

> Guarda cada bloque en su correspondiente archivo, dale permisos con `chmod +x` y adáptalo a tu repositorio.

#### Paso 1 – Abrir la terminal y verificar Bash

1. Abre tu **Terminal** en Linux/macOS o Git Bash en Windows.  
2. Comprueba la versión de Bash:
   ```bash
   bash --version
   ```

   <div align="center">
      <img src="https://i.postimg.cc/tTg3dGrP/PD3-1-1.png" alt="PD3.1.1" width="600" />
   </div>

3. Asegúrate de usar la cabecera portable en tus scripts:
   ```bash
   #!/usr/bin/env bash
   ```

#### Paso 2 – "Hello, World!": tu primer script

1. Crea `hello.sh`:
   ```bash
   nano hello.sh
   ```
2. Escribe:
   ```bash
   #!/usr/bin/env bash
   echo "Hello, World!"
   ```

   <div align="center">
      <img src="https://i.postimg.cc/QdpJhb9B/PD3-1-2.png" alt="PD3.1.2" width="300" />
   </div>

3. Guarda y habilita:
   ```bash
   chmod +x hello.sh
   ```
4. Ejecútalo:
   ```bash
   ./hello.sh
   ```

   <div align="center">
      <img src="https://i.postimg.cc/8CNB56MZ/PD3-1-3.png" alt="PD3.1.3" width="600" />
   </div>

Al ejecutar nos sale el mensaje de `Hello, World!`
   
#### Paso 3 – Asignación de variables

```bash
#!/usr/bin/env bash
NOMBRE="Cesar"
readonly PI=3.14159
export ENV="producción"

echo "Usuario: $NOMBRE"
echo "PI vale: $PI"
echo "Entorno: $ENV"
```

- Usa siempre comillas al expandir: `"$VAR"`.  
- Activa `set -u` para error si variable no definida.

Cree `variable.sh` y escribi el script en bash que nos dan como ejemplo

   <div align="center">
      <img src="https://i.postimg.cc/nh8Gy5zb/PD3-1-4.png" alt="PD3.1.4" width="200" />
   </div>

Ejecuntado nos da el `Usuario`, el valor de `pi redondeado` y el `Entorno` o `ENV`

   <div align="center">
      <img src="https://i.postimg.cc/RVJTb9vL/PD3-1-5.png" alt="PD3.1.5" width="600" />
   </div>

#### Paso 4 – Parámetros posicionales

```bash
#!/usr/bin/env bash
# script_params.sh
echo "Script: $0"
echo "1er parámetro: $1"
echo "Todos: $@"
echo "Cantidad: $#"
shift 1
echo "Ahora \$1 es: $1"
```

Creamos el script en bash `parametros_posicionales.sh`

   <div align="center">
      <img src="https://i.postimg.cc/J72qqtCh/PD3-1-6.png" alt="PD3.1.6" width="300" />
   </div>

Ejecuta:

```bash
./script_params.sh f1 f2 f3
```

Ejecutamos el script `parametros_posicionales.sh` ejecutando el siguiente comando `./parametros_posicionales.sh` en la terminal

   <div align="center">
      <img src="https://i.postimg.cc/90KYFgY9/PD3-1-7.png" alt="PD3.1.7" width="700" />
   </div>

Vemos que se imprime el nombre del script, todos los paramaetro (f1, f2, f3), la cantidad total de parametros que se han pasado y finalmente vemos como con `shift 1`, `$S1` es ahora f2, osea que se corrio una variable a la derecha

#### Paso 5 – Arrays en Bash

```bash
#!/usr/bin/env bash
FRUTAS=(manzana banana cereza)
FRUTAS+=("durazno")

echo "Total frutas: ${#FRUTAS[@]}"
for f in "${FRUTAS[@]}"; do
  echo "Fruta: $f"
done

declare -A EDADES=([Alice]=28 [Kapu]=35)
echo "Kapu tiene ${EDADES[Kapu]} años"
```

Creamos el script en bash `arrays.sh`

   <div align="center">
      <img src="https://i.postimg.cc/D08ch3LF/PD3-1-8.png" alt="PD3.1.7" width="350" />
   </div>

Ejecutamos el script

   <div align="center">
      <img src="https://i.postimg.cc/W397x1DX/PD3-1-9.png" alt="PD3.1.7" width="600" />
   </div>

Vemos que nos muestra la cantidad de frutas, imprime todas las frutas iterando el array de frutas que se creo en el script y finalmente nos muestra cuando años tiene `kapu`

#### Paso 6 – Expansiones

#### Aritmética

```bash
a=7; b=3
echo "$a + $b = $((a + b))"
echo "$a ** $b = $((a ** b))"
```

Creamos el script en bash `aritmetica.sh`

   <div align="center">
      <img src="https://i.postimg.cc/mryjNwTx/PD3-1-10.png" alt="PD3.1.10" width="300" />
   </div>

Ejecutamos el script

   <div align="center">
      <img src="https://i.postimg.cc/V6sR7CNJ/PD3-1-11.png" alt="PD3.1.11" width="600" />
   </div>

Vemos que se efectua las operaciones aritmeticas entre `a` y `b` que son 2 variables numericas definidas en el script

#### Substitución de comandos

```bash
fecha=$(date +%Y-%m-%d)
archivos=$(ls | wc -l)
echo "Hoy: $fecha, Archivos: $archivos"
```

Creamos el script en bash `substitucion_comandos.sh`

   <div align="center">
      <img src="https://i.postimg.cc/fTVHnmfX/PD3-1-13.png" alt="PD3.1.12" width="300" />
   </div>

Ejecutamos el script

   <div align="center">
      <img src="https://i.postimg.cc/CKgJqtTH/PD3-1-12.png" alt="PD3.1.13" width="650" />
   </div>

Vemos que nos muestra la fecha actual y la cantidad de archivos

#### Otras

```bash
VAR=""
echo "${VAR:-default}"       # default si VAR vacío
txt="archivo.tar.gz"
echo "${txt%.tar.gz}"        # quita sufijo
```

Creamos el script en bash `otras.sh`

   <div align="center">
      <img src="https://i.postimg.cc/RZfXqm8Z/PD3-1-14.png" alt="PD3.1.14" width="400" />
   </div>

Ejecutamos el script

   <div align="center">
      <img src="https://i.postimg.cc/bN4mzrm5/PD3-1-15.png" alt="PD3.1.15" width="600" />
   </div>

Vemos que se imprime `default` ya que `VAR` dentro del script `otras.sh` esta vacio y tambien vemos que se imprime el nombre del archivo `archivo.tar.gz` pero sin el sufijo `.tar.gz`

#### Paso 7 – Pipes y redirección

```bash
# stdout a archivo
ls -l > listado.txt
# stderr
grep f1 *.log 2> errores.log
# ambos
make &> build.log
# pipe
ps aux | grep sshd | awk '{print $2}'
# process substitution
diff <(sort file1) <(sort file2)
```

Creamos el script en bash `pipes_redireccion.sh`

   <div align="center">
      <img src="https://i.postimg.cc/NGJNzpmB/PD3-1-16.png" alt="PD3.1.16" width="500" />
   </div>

Ejecutamos el script

   <div align="center">
      <img src="https://i.postimg.cc/yd8MBW1t/PD3-1-17.png" alt="PD3.1.17" width="650" />
   </div>

Vemos que se muestra el `ID` del proceso `ssh`que esta corriendo, pero luego nos salta un error, la cual sucede porque no existe `file 1` y `file2`. Ademas se al ejecutar este script se crearan los archivos `listado.txt`, `errores.log` y `buil.log`. En donde se guardara el listado de todos los archivos en `listado.txt`, se guardara los errores en `errores.log` y finalmente en `buil.log` se guardara ambos (informacion de archivos y errores)

#### Paso 8 – Condicionales

#### if

```bash
#!/usr/bin/env bash
num=$1
if [[ -z $num ]]; then
  echo "Pasa un número"
  exit 1
elif (( num % 2 == 0 )); then
  echo "$num es par"
else
  echo "$num es impar"
fi
```

Creamos el script en bash `condicionales.sh`

   <div align="center">
      <img src="https://i.postimg.cc/9Q02yqmQ/PD3-1-18.png" alt="PD3.1.18" width="300" />
   </div>

Ejecutamos el script

   <div align="center">
      <img src="https://i.postimg.cc/66VBKXbt/PD3-1-19.png" alt="PD3.1.19" width="650" />
   </div>

Hemos probado en el caso que no se le pasa nada, en la que se pasa un numero par y otro en el que se pasa un numero impar, y vemos que funciona correctamente

#### case

```bash
#!/usr/bin/env bash
ext="$1"
case "$ext" in
  txt) echo "Texto" ;;
  sh)  echo "Shell" ;;
  py)  echo "Python" ;;
  *)   echo "Desconocido" ;;
esac
```

Creamos el script en bash `case.sh`

   <div align="center">
      <img src="https://i.postimg.cc/1XKSrGVf/PD3-1-20.png" alt="PD3.1.20" width="300" />
   </div>

Ejecutamos el script

   <div align="center">
      <img src="https://i.postimg.cc/yxKBRQdM/PD3-1-21.png" alt="PD3.1.21" width="650" />
   </div>

Vemos que reconoce correctamente que tipo de archivo es, probando sin pasarle nada y cuando se le pasa txt nos dice que es `Texto`

#### Paso 9 – Bucles

```bash
# for clásico
for ((i=1;i<=3;i++)); do echo "Iter $i"; done

# for-in
for file in *.sh; do echo "Script: $file"; done

# while
count=3
while (( count>0 )); do echo "$count"; ((count--)); done

# until
until [[ -f resultado.txt ]]; do sleep 1; done
echo "resultado.txt listo"
```

Creamos el script en bash `bucles.sh`

   <div align="center">
      <img src="https://i.postimg.cc/YSJtrqwq/PD3-1-23.png" alt="PD3.1.23" width="400" />
   </div>

Ejecutamos el script

   <div align="center">
      <img src="https://i.postimg.cc/vBfbcFQ7/PD3-1-22.png" alt="PD3.1.22" width="550" />
   </div>

Vemos que itera en todos los bucles correctamente y tambien notaremos que el script esperara que exista el archivo `resultado.txt` para que finalize la ejecucion, por lo que cree paralelamente el archivo `resultado.txt` y por eso llega a terminar la ejecucion el script en bash `bucles.sh`

#### Paso 10 – Funciones

```bash
#!/usr/bin/env bash
saludar() {
  local name=$1
  echo "Hola, $name!"
}
saludar "Equipo"

dividir() {
  local a=$1 b=$2
  (( b==0 )) && return 1
  echo "$((a/b))"
}
if res=$(dividir 10 2); then
  echo "División: $res"
else
  echo "Error división"
fi
```

Creamos el script en bash `funciones.sh`

   <div align="center">
      <img src="https://i.postimg.cc/6QkYZG9D/PD3-1-24.png" alt="PD3.1.24" width="400" />
   </div>

Ejecutamos el script

   <div align="center">
      <img src="https://i.postimg.cc/t4gSGjSm/PD3-1-25.png" alt="PD3.1.25" width="650" />
   </div>

Vemos nos muestra el mensaje de saludo de la funcion `saludar` y tambien el resultado de la opercion de division dentro de la funcion `dividir`

#### Paso 11 – Depuración

```bash
set -xe  # traza + salir al error
export PS4='+ ${BASH_SOURCE}:${LINENO}:${FUNCNAME[0]}: '
trap 'echo "Error en línea $LINENO"; exit 1' ERR
```

Creamos el script en bash `depuracion.sh`

   <div align="center">
      <img src="https://i.postimg.cc/8P4KY5H6/PD3-1-26.png" alt="PD3.1.26" width="450" />
   </div>

Ejecutamos el script

   <div align="center">
      <img src="https://i.postimg.cc/ZqBw0Lh8/PD3-1-27.png" alt="PD3.1.27" width="650" />
   </div>

Vemos que se muestra solamente la definiciones que hicimos en el script `depuracion.sh`.
Para probarlo correctamente, le agregue el codigo del script de `funciones.sh`

   <div align="center">
      <img src="https://i.postimg.cc/RZbPMD2C/PD3-1-28.png" alt="PD3.1.28" width="450" />
   </div>

Ejecutamos el script modificado

   <div align="center">
      <img src="https://i.postimg.cc/CLSrJDj0/PD3-1-29.png" alt="PD3.1.29" width="650" />
   </div>

Y ahora vemos como se depura linea por linea, indicando de que script en bash viene (en este caso de `depuracion.sh`), nos muestra en que linea se encuentra y tambien de que funcion proviene

### **Ejercicios**


1 . Escribe funciones de Bash `marco` y `polo` que hagan lo siguiente: cada vez que ejecutes `marco`, debe guardarse de alguna manera el directorio de trabajo actual, luego, cuando ejecutes `polo`, sin importar en qué directorio te encuentres, `polo` te debe devolver (con `cd`) al directorio en el que ejecutaste `marco`.
   Para facilitar la depuración, puedes poner el código en un archivo `marco.sh` y recargarlo con `source marco.sh`.

2 . Tienes un comando que falla muy raramente. Para depurarlo necesitas capturar su salida, pero puede llevar tiempo que falle. Escribe un script de Bash que ejecute el siguiente fragmento **hasta que falle**, capture sus flujos de salida estándar y de error en archivos, y finalmente imprima todo:

```bash
#!/usr/bin/env bash

n=$(( RANDOM % 100 ))

if [[ n -eq 42 ]]; then
   echo "Algo esta pasando!"
   >&2 echo "El error fue por usar numero magicos"
   exit 1
fi

echo "Todo salio de acuerdo al plan"
```
Indica cuántas ejecuciones fueron necesarias para que ocurriera el fallo.

3 . El `-exec` de `find` puede ser muy poderoso para realizar operaciones sobre los archivos que encuentra. Sin embargo, ¿qué pasa si queremos hacer algo con **todos** los archivos, como crear un archivo ZIP? Algunos comandos leen de **STDIN**, pero otros (como `tar`) necesitan recibir la lista de archivos como argumentos. Para unir ambos mundos tenemos `xargs`, que ejecuta un comando tomando su **STDIN** como lista de argumentos. Por ejemplo:

```bash
ls | xargs rm
```

eliminará los archivos que `ls` lista.

**Tu tarea**: escribe un comando que encuentre **de manera recursiva** todos los archivos HTML en una carpeta y los comprima en un ZIP. Ten en cuenta que debe funcionar aunque los nombres de archivo contengan espacios (pista: revisa la opción `-d` o usa `-print0` en `find` junto con `-0` en `xargs`).

4 . Escribe un comando o script que, de forma recursiva, encuentre el archivo **más recientemente modificado** en un directorio. Y, más en general, ¿puedes listar todos los archivos por orden de recencia?

#### Paso 12 – Expresiones regulares en Bash

```bash
#!/usr/bin/env bash
email="$1"
re='^[[:alnum:]_.+-]+@[[:alnum:]-]+\.[[:alnum:].-]+$'
if [[ $email =~ $re ]]; then
  echo "Email válido"
  echo "Usuario: ${BASH_REMATCH[1]}"  # primer grupo
else
  echo "Email inválido"
fi
```
#### Paso 13 – Expresiones regulares en Python

Crea `extract_emails.py`:

```python
#!/usr/bin/env python3
import re, sys
texto=sys.stdin.read()
pat=re.compile(r'([A-Za-z0-9_.+-]+@[A-Za-z0-9-]+\.[A-Za-z0-9-.]+)')
for email in set(pat.findall(texto)):
    print(email)
```

Uso:
```bash
cat logs.txt | python3 extract_emails.py
```

**Validar nombre de rama**

```bash
#!/usr/bin/env bash
branch=$(git rev-parse --abbrev-ref HEAD)
# solo: feature/XYZ-123-descripcion o hotfix/XYZ-123
re='^(feature|hotfix)\/[A-Z]{2,5}-[0-9]+-[a-z0-9]+(-[a-z0-9]+)*$'
if [[ ! $branch =~ $re ]]; then
  echo "Nombre de rama inválido: $branch"
  echo "Formato correcto: feature/ABC-123-descripcion"
  exit 1
fi
```

**Validar mensaje de commit**

```bash
#!/usr/bin/env bash
msg_file=$1
# tipo(scope)!?: descripción de al menos 10 caracteres
re='^(feat|fix|docs|style|refactor|perf|test|chore)(\([a-z0-9_-]+\))?(!)?: .{10,}$'
if ! grep -Eq "$re" "$msg_file"; then
  echo "Mensaje de commit no cumple conventional commits"
  echo "Ej: fix(parser): manejar comillas dobles correctamente"
  exit 1
fi
```

**Validar formato de tag semántico**

```bash
#!/usr/bin/env bash
tag="$1"
# vX.Y.Z o X.Y.Z-prerelease+metadata
re='^v?[0-9]+\.[0-9]+\.[0-9]+(-[0-9A-Za-z.-]+)?(\+[0-9A-Za-z.-]+)?$'
if [[ ! $tag =~ $re ]]; then
  echo "Tag inválido: $tag"
  echo "Formato semver: 1.2.3, v1.2.3-beta+exp"
  exit 1
fi
```

**Extraer issue IDs de mensajes (`git log`)**

```bash
git log --oneline | \
  grep -Po '(?<=\[)[A-Z]{2,5}-[0-9]+(?=\])' | sort -u
# Explicación:
# (?<=\[)  ─ lookbehind para "["
# [A-Z]{2,5}-[0-9]+  ─ proyecto-1234
# (?=\])   ─ lookahead para "]"
```

**Detectar merges automáticos y extraer la rama objetivo**

```bash
git log --grep='^Merge branch' --pretty=format:'%s' | \
  grep -Po "(?<=Merge branch ')[^']+" 
# Captura el nombre de la rama tras "merge branch '<rama>'"
```
**Paso con grupo nombrado y alternancia**

```python
from behave import given

@given(r'^(?P<user>[A-Za-z0-9_]+) tiene (?P<count>[0-9]+) (artículos|productos)$')
def step_user_items(context, user, count):
    # user: nombre de usuario
    # count: número de artículos o productos
    context.user = user
    context.count = int(count)
```

**Paso con partes opcionales y lookahead**

```python
from behave import when

@when(r'^el usuario intenta(?: iniciar sesión(?: con contraseña "(?P<pw>[^"]+)")?)?$')
def step_login_optional_pw(context, pw=None):
    # El paso coincide con:
    #   "el usuario intenta"
    #   "el usuario intenta iniciar sesión"
    #   'el usuario intenta iniciar sesión con contraseña "abc"'
    context.pw = pw
```

**Validar formatos de fecha dentro de un paso**

```python
from behave import then

@then(r'^la fecha de entrega es (?P<date>\d{4}-\d{2}-\d{2})$')
def step_check_date(context, date):
    # date: "2025-04-16"
    import datetime
    datetime.datetime.strptime(date, '%Y-%m-%d')
```

**Step definition para comandos Git**

```python
from behave import given

@given(r'^estoy en la rama "(?P<branch>[a-z0-9/_-]+)"$')
def step_on_branch(context, branch):
    import subprocess
    current = subprocess.check_output(['git','rev-parse','--abbrev-ref','HEAD']).decode().strip()
    assert current == branch
```

**Capturar tablas Gherkin con regex dinámico**

```python
from behave import then
import re

@then(r'^los siguientes usuarios:$')
def step_table_users(context):
    # context.table tendrá filas:
    # | user   | age |
    # | alice  | 30  |
    # Validación adicional:
    for row in context.table:
        assert re.match(r'^[a-z]+$', row['user'])
        assert re.match(r'^[0-9]{1,3}$', row['age'])
```

**Scenario outline con ejemplos que usan regex**

```gherkin
Scenario Outline: Validación de correos
  Given el email "<email>"
  When valido el formato
  Then debe ser <valid>

Examples:
  | email                 | valid  |
  | user@example.com      | True   |
  | invalid-email@        | False  |
  | otra.cosa@dominio.org | True   |
```

```python
from behave import given, then
import re

EMAIL_RE = re.compile(r'^[[:alnum:]_.+-]+@[[:alnum:]-]+\.[[:alnum:].-]+$')

@given(r'el email "(?P<email>[^"]+)"')
def step_set_email(context, email):
    context.email = email

@then(r'debe ser (?P<valid>True|False)')
def step_check_email(context, valid):
    match = bool(EMAIL_RE.match(context.email))
    assert match == (valid == 'True')
```

#### Paso 14 – BDD con `behave`

1. **Feature** (`features/login.feature`):
   ```gherkin
   Feature: Login
     Scenario Outline: credenciales válidas
       Given el usuario "<user>" con contraseña "<pass>"
       When intenta iniciar sesión
       Then debe ver "Bienvenido, <user>"

     Examples:
       | user  | pass    |
       | alice | secret1 |
   ```
2. **Steps** (`features/steps/login_steps.py`):
   ```python
   from behave import given, when, then
   from myapp.auth import autenticar

   @given(r'el usuario "(?P<user>[^"]+)" con contraseña "(?P<pass>[^"]+)"')
   def step_user(c, user, pass_):
       c.user, c.passwd = user, pass_

   @when('intenta iniciar sesión')
   def step_try(c):
       c.result = autenticar(c.user, c.passwd)

   @then(r'debe ver "(?P<msg>[^"]+)"')
   def step_verify(c, msg):
       assert c.result == msg
   ```
3. Ejecuta:
   ```bash
   behave -q
   ```
#### Paso 15 – Pipelines CI

**GitHub actions** (`.github/workflows/ci.yml`):

```yaml
name: CI
on: [push,pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with: python-version: 3.10
      - run: pip install -r requirements.txt
      - run: pytest -q
      - run: behave -q
```

**Makefile local**:

```makefile
.PHONY: lint test bdd all
lint:
    flake8 src tests
test:
    pytest -q
bdd:
    behave -q
all: lint test bdd
```
