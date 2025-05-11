## PRACTICA DIRIGIDA 2
Nombre: Guido Anthony Chipana Calderon

### Instrucciones previas

1. **Descarga y guarda el script:**
   - Copia el contenido del script proporcionado (el ejemplo extendido) y guárdalo en un archivo llamado `git_avanzado.sh`.

   <div align="center">
      <img src="https://i.postimg.cc/7YGHpm08/PD2-0-1.png" alt="PD2.0.1" width="300" />
   </div>

2. **Asignar permisos de ejecución:**
   - Abre la terminal en el directorio donde guardaste el archivo y ejecuta:
     ```bash
     chmod +x git_avanzado.sh
     ```

   <div align="center">
      <img src="https://i.postimg.cc/y6JWH1Cb/PD2-0-2.png" alt="PD2.0.2" width="550" />
   </div>

Le damos permisos a `git_avanzado.sh`

3. **Ubicación:**
   - Asegúrate de ejecutar el script dentro de la raíz de un repositorio Git, ya que el script interactúa con el entorno Git.

   <div align="center">
      <img src="https://i.postimg.cc/bY2Y5mQX/PD2-0-3.png" alt="PD2.0.3" width="550" />
   </div>

Inicializamos un repositorio git en la carpete `PD2_software`

### Procedimiento de la actividad

A continuación se muestra un ejemplo de uso que ilustra una sesión interactiva con el script. Este ejemplo simula cómo un usuario podría interactuar con algunas de las opciones del menú. Recuerda que, al ejecutarlo, verás mensajes en tiempo real en la terminal y deberás ingresar las opciones y datos solicitados.

1. **Inicio del script**

   Tras darle permisos de ejecución y ejecutar el script desde la raíz de un repositorio Git, se muestra el siguiente menú en la terminal:

   ```
   ====== Menú avanzado de Git ======
   1) Listar reflog y restaurar un commit
   2) Agregar un submódulo
   3) Agregar un subtree
   4) Gestión de ramas
   5) Gestión de stashes
   6) Mostrar estado y últimos commits
   7) Gestión de tags
   8) Gestión de Git Bisect
   9) Gestión de Git Diff
   10) Gestión de Hooks
   11) Salir
   Seleccione una opción:
   ```

   <div align="center">
      <img src="https://i.postimg.cc/PrTWrvfq/PD2-1-1.png" alt="PD2.0.3" width="550" />
   </div>


2. **Opción: agregar un submódulo (Opción 2)**

   - **Usuario:** Ingresa `2` y presiona Enter.
   - El script pide:
     ```
     Ingrese la URL del repositorio para el submódulo:
     ```

   <div align="center">
      <img src="https://i.postimg.cc/PrTWrvfq/PD2-1-1.png" alt="PD2.1,1" width="530" />
   </div>

   - **Usuario:** Escribe, por ejemplo:  
     `https://github.com/usuario/repositorio-submodulo.git`
   - El script solicita:
     ```
     Ingrese el directorio donde se ubicará el submódulo:
     ```

   <div align="center">
      <img src="https://i.postimg.cc/MpHH5VmX/PD2-1-2.png" alt="PD2.1.2" width="500" />
   </div>

   - **Usuario:** Escribe, por ejemplo:  
     `libs/submodulo`

   <div align="center">
      <img src="https://i.postimg.cc/YCLkj3xN/PD2-1-3.png" alt="PD2.1.3" width="650" />
   </div>

   - **Script:** Ejecuta:
     ```bash
     git submodule add https://github.com/usuario/repositorio-submodulo.git libs/submodulo
     git submodule update --init --recursive
     ```
   - **Salida esperada:**  
     El mensaje confirmando que el submódulo ha sido agregado:
     ```
     Submódulo agregado en: libs/submodulo
     ```

   <div align="center">
      <img src="https://i.postimg.cc/qqcw190c/PD2-1-4.png" alt="PD2.1.4" width="500" />
   </div>

3. **Opción: Gestión de ramas (Opción 4)**

   - **Usuario:** Regresa al menú principal y escoge la opción `4`.
   - El script despliega un submenú:
     ```
     === Gestión de ramas ===
     a) Listar ramas
     b) Crear nueva rama y cambiar a ella
     c) Cambiar a una rama existente
     d) Borrar una rama
     e) Volver al menú principal
     Seleccione una opción:
     ```

   <div align="center">
      <img src="https://i.postimg.cc/PqyNtyyX/PD2-2-1.png" alt="PD2.2.1" width="350" />
   </div>

   - **Ejemplo A: Listar ramas (Opción a)**
     - **Usuario:** Ingresa `a` y presiona Enter.
     - **Script:** Ejecuta `git branch` y muestra la lista de ramas:
 
       ```
         master
       * feature/nueva-funcionalidad
       ```

   <div align="center">
      <img src="https://i.postimg.cc/rwQKTgQ8/PD2-2-2.png" alt="PD2.2.2" width="350" />
   </div>

Notemos que no aparece ninguna rama, esto es porque no hemos hecho ningun commit inicial, por lo que ahora haremos nuestro primer commit 

   <div align="center">
      <img src="https://i.postimg.cc/zDxWwnsH/PD2-2-3.png" alt="PD2.2.3" width="600" />
   </div>

Ahora volvemos a ejecutar `./git_avanzado.sh`, elegimos la opcion 4 (Gestion de ramas) y seleccionamos la opcion a (Listar ramas)

   <div align="center">
      <img src="https://i.postimg.cc/NGKJHfVt/PD2-2-4.png" alt="PD2.2.4" width="500" />
   </div>

Ahora ya aparece la rama main, que es la unica rama que tenemos por el momento

   - **Ejemplo B: Crear una nueva rama (Opción b)**
     - **Usuario:** Ingresa `b`, luego el script pregunta:
       
       ```
       Ingrese el nombre de la nueva rama:
       ```

   <div align="center">
      <img src="https://i.postimg.cc/L8THcTmm/PD2-3-1.png" alt="PD2.3.1" width="350" />
   </div>

- **Usuario:** Escribe `feature/login`.
- **Script:** Ejecuta `git checkout -b feature/login` y confirma:

  ```
  Rama 'feature/login' creada y activada.
  ```

   <div align="center">
      <img src="https://i.postimg.cc/hjmNBDVV/PD2-3-2.png" alt="PD2.3.2" width="350" />
   </div>

4. **Opción: Gestión de git diff (Opción 9)**

   - **Usuario:** Selecciona la opción `9` del menú principal.
   - El submenú de diff se muestra:
     ```
     === Gestión de git diff ===
     a) Mostrar diferencias entre el working tree y el área de staging (git diff)
     b) Mostrar diferencias entre el área de staging y el último commit (git diff --cached)
     c) Comparar diferencias entre dos ramas o commits
     d) Volver al menú principal
     Seleccione una opción:
     ```

   <div align="center">
      <img src="https://i.postimg.cc/SsNjwTXh/PD2-4-1.png" alt="PD2.4.1" width="500" />
   </div>

   - **Ejemplo:**  
     - **Usuario:** Ingresa `c` para comparar dos revisiones.  
       El script solicita:
       ```
       Ingrese el primer identificador (rama o commit):
       ```
     - **Usuario:** Escribe `master`.
     - El script luego pregunta:
       ```
       Ingrese el segundo identificador (rama o commit):
       ```
     - **Usuario:** Escribe `feature/login`.
     - **Script:** Ejecuta `git diff master feature/login` y muestra las diferencias entre ambas ramas en la terminal.

   <div align="center">
      <img src="https://i.postimg.cc/YSVqsrw1/PD2-4-2.png" alt="PD2.4.2" width="600" />
   </div>

Notamos que no muestra ninguna diferencia, ya que no existe aun diferencia entre ambas ramas.
Entonces haremos cambios en la rama `feature/login` para poder ver los camibios en `git_avanzado`

   <div align="center">
      <img src="https://i.postimg.cc/Hxttdhss/PD2-4-3.png" alt="PD2.4.3" width="600" />
   </div>

Ahora ya tenemos cambios hechos, volvemos a ejecutar `./git_avanzado.sh`, seleccionamos opcion `9` (Gestion de git diff) y elegimos la opcion `c` (Comparar diferencias entre dos ramas o commits)

   <div align="center">
      <img src="https://i.postimg.cc/d31GvQx4/PD2-4-4.png" alt="PD2.4.4" width="600" />
   </div>

Observamos las diferencias entre ambas ramas, la cual es la `linea 1`

5. **Opción: Gestión de hooks (Opción 10)**

   - **Usuario:** Escoge la opción `10` para gestionar hooks.
   - Se despliega el submenú de hooks:
     ```
     === Gestión de hooks ===
     a) Listar hooks disponibles
     b) Crear/instalar un hook (ej. pre-commit)
     c) Editar un hook existente
     d) Borrar un hook
     e) Volver al menú principal
     Seleccione una opción:
     ```

   <div align="center">
      <img src="https://i.postimg.cc/QC5C20GN/PD2-5-1.png" alt="PD2.5.1" width="350" />
   </div>

   - **Ejemplo:** Crear un hook pre-commit.
     - **Usuario:** Ingresa `b`.
     - El script pregunta:
       ```
       Ingrese el nombre del hook a instalar (por ejemplo, pre-commit):
       ```
   
     - **Usuario:** Escribe Cpre-commit`.
     - Luego el script solicita:
       ```
       Ingrese el contenido del hook (una línea, se agregará '#!/bin/bash' al inicio):
       ```
   
     - **Usuario:** Escribe una línea, por ejemplo:
       `echo "Ejecutando pre-commit hook..." && exit 0`
     - **Script:** Crea el archivo `.git/hooks/pre-commit`, lo hace ejecutable y confirma:
       ```
       Hook 'pre-commit' instalado.
       ```

   <div align="center">
      <img src="https://i.postimg.cc/c1TbYZVm/PD2-5-2.png" alt="PD2.5.2" width="700" />
   </div>

Vemos que se crea correctamente el hook `pre-commit`

6. **Finalizar la sesión**

   - **Usuario:** Cuando termine de utilizar las opciones deseadas, regresa al menú principal y selecciona `11` para salir:
     ```
     Saliendo del script.
     ```

   <div align="center">
      <img src="https://i.postimg.cc/wvnZtktm/PD2-5-3.png" alt="PD2.5.3" width="500" />
   </div>

### Preguntas

- **¿Qué diferencias observas en el historial del repositorio después de restaurar un commit mediante reflog?**

Al restaurar un commit con reflog, veo que el historial retrocede a ese punto específico. Los commits posteriores quedan temporalmente sin conexión aunque Git los mantiene accesibles por si se necesita recuperarlos más tarde

- **¿Cuáles son las ventajas y desventajas de utilizar submódulos en comparación con subtrees?**

Los submódulos mantienen repositorios independientes y es ideal para proyectos separados pero son más complejos de gestionar. Los subtrees en cambio integran todo en un solo repositorio es más simple para colaboradores pero pueden llegar a aumentar el tamaño del proyecto y mezclar historiales

- **¿Cómo impacta la creación y gestión de hooks en el flujo de trabajo y la calidad del código?**

Los hooks automatizan verificaciones por ejemplo antes de commits, lo que mejora la calidad del código. Aunque puede parecer ralentizar el proceso a largo plazo logra evitar errores y ahorran tiempo de depuración (búsqueda de errores).

- **¿De qué manera el uso de `git bisect` puede acelerar la localización de un error introducido recientemente?**

Sabemos que `git bisect` usa búsqueda binaria para encontrar el commit problemático. Por ejemplo en lugar de revisar 100 commits uno por uno, `git bisect` lo encuentro en aproximadamente 7 pasos, marcando cada commit como bueno o malo.

- **¿Qué desafíos podrías enfrentar al administrar ramas y stashes en un proyecto con múltiples colaboradores?**

Con` ramas` podriamos enfrentar conflictos de fusión (merge) y multiplicacion de ramas "olvidadas". Con `stashes` podriamos tener un problema ya que los `stashes` son locales y pueden perderse si alguien se olvida de ellos o deja el proyecto.

