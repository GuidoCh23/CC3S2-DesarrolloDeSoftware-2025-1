## ACTIVIDAD 6
Nombre: Guido Anthony Chipana Calderon

### Objetivo de aprendizaje:  

Aprender a usar los comandos `git rebase` y `git cherry-pick` para mantener un historial de commits limpio y manejable en proyectos colaborativos.  También explorarás cuándo y por qué utilizar estos comandos en lugar de los merges regulares.

#### **Parte 1: git rebase para mantener un historial lineal**

1. **Escenario de ejemplo:**

   - Crea un nuevo repositorio Git y dos ramas, main y new-feature:
     ```bash
     $ mkdir prueba-git-rebase
     $ cd prueba-git-rebase
     $ git init
     $ echo "# Mi Proyecto de Rebase" > README.md
     $ git add README.md
     $ git commit -m "Commit inicial en main"
     ```

   <div align="center">
      <img src="https://i.postimg.cc/mDPJs6nw/Act6-Ejercicio1-1.png" alt="act6Ejer1.1" width="700" />
   </div>

   - Crea y cambia a la rama new-feature:
     ```bash
     $ git checkout -b new-feature
     $ echo "Esta es una nueva característica." > NewFeature.md
     $ git add NewFeature.md
     $ git commit -m "Agregar nueva característica"
     ```

    Presenta el historial de ramas obtenida hasta el momento.

   <div align="center">
      <img src="https://i.postimg.cc/4NY61R9w/Act6-Ejercicio1-2.png" alt="act6Ejer1.2" width="750" />
   </div>

   Ahora, digamos que se han agregado nuevos commits a main mientras trabajabas en new-feature:

   ```bash
   # Cambiar de nuevo a 'main' y agregar nuevos commits
   $ git checkout main
   $ echo "Updates to the project." >> Updates.md
   $ git add Updates.md
   $ git commit -m "Update main"
   ```

   <div align="center">
      <img src="https://i.postimg.cc/nrFxqtc1/Act6-Ejercicio1-3.png" alt="act6Ejer1.3" width="700" />
   </div>

   Tu gráfico de commits ahora diverge

   <div align="center">
      <img src="https://i.postimg.cc/bNdcPgGd/Act6-Ejercicio1-4.png" alt="act6Ejer1.4" width="700" />
   </div>

   Realiza el rebase de `new-feature` sobre `main` con los siguientes comandos:
   ```bash
   $ git checkout new-feature
   $ git rebase main
   ```

   <div align="center">
      <img src="https://i.postimg.cc/TPPfyx1q/Act6-Ejercicio1-5.png" alt="act6Ejer1.5" width="700" />
   </div>

2. **Revisión:**

   Después de realizar el rebase, visualiza el historial de commits con:
   ```bash
   $ git log --graph –oneline
   ```

   <div align="center">
      <img src="https://i.postimg.cc/hvNfsjzB/Act6-Ejercicio1-6.png" alt="act6Ejer1.6" width="700" />
   </div>

3. **Momento de fusionar y completar el proceso de git rebase:**
   ```bash
   # Cambiar a 'main' y realizar una fusión fast-forward
   $ git checkout main
   $ git merge new-feature
   ```

   <div align="center">
      <img src="https://i.postimg.cc/hGg8qCCd/Act6-Ejercicio1-7.png" alt="act6Ejer1.7" width="650" />
   </div>

   Cuando se realiza una fusión *fast-forward*, las HEADs de las ramas main y new-feature serán los commits correspondientes.

#### Parte 2: **git cherry-pick para la integración selectiva de commit**

1. **Escenario de ejemplo:**

   ```bash
   # Inicializar un nuevo repositorio
   $ mkdir prueba-cherry-pick
   $ cd prueba-cherry-pick
   $ git init

   # Agregar y commitear README.md inicial a main
   $ echo "# Mi Projecto" > README.md
   $ git add README.md
   $ git commit -m "Commit inicial"

   # Crear y cambiar a una nueva rama 'add-base-documents'
   $ git checkout -b add-base-documents

   # Hacer cambios y commitearlos
   # Agregar CONTRIBUTING.md
   $ echo "# CONTRIBUTING" >> CONTRIBUTING.md
   $ git add CONTRIBUTING.md
   $ git commit -m "Se agrega CONTRIBUTING.md"

   # Agregar LICENSE.txt
   $ echo "LICENSE" >> LICENSE.txt
   $ git add LICENSE.txt
   $ git commit -m "Agrega LICENSE.txt"

   # Echa un vistazo al log de la rama 'add-base-documents'
   $ git log add-base-documents --graph --oneline
   ```

   <div align="center">
      <img src="https://i.postimg.cc/Mpq8HRrk/Act6-Ejercicio2-1.png" alt="act6Ejer2.1" width="800" />
   </div>

   Muestra un diagrama de como se ven las ramas en este paso.

   <div align="center">
      <img src="https://i.postimg.cc/28xKHtTJ/Act6-Ejercicio2-2.png" alt="act6Ejer2.2" width="500" />
   </div>

2. **Tarea: Haz cherry-pick de un commit de add-base-documents a main:**
   ```bash
   $ git checkout main
   $ git cherry-pick a80e8ad  # Reemplaza con el hash real del commit de tu log
   ```

   <div align="center">
      <img src="https://i.postimg.cc/YqVWwrXm/Act6-Ejercicio2-3.png" alt="act6Ejer2.3" width="650" />
   </div>

3. **Revisión:**  
   Revisa el historial nuevamente:
   ```bash
   $ git log --graph --oneline
   ```

   <div align="center">
      <img src="https://i.postimg.cc/yNhjdg5G/Act6-Ejercicio2-4.png" alt="act6Ejer2.4" width="650" />
   </div>
   
   Después de que hayas realizado con éxito el cherry-pick del commit, se agregará un nuevo commit a tu rama actual (main en este ejemplo) y contendrá los cambios del commit cherry-picked.  

   Ten en cuenta que el nuevo commit tiene los mismos cambios pero un valor de hash de commit diferente. !Comprueba esto!.

   El commit donde se agrega LICENSE.txt en la rama add-base-documents, su hash es fbb60b6 pero vemos que despues del cherry-pick en main su hash es 16981e4. 

#### **Preguntas de discusión:**

1. ¿Por qué se considera que rebase es más útil para mantener un historial de proyecto lineal en comparación con merge?

Porque reubica los commits como si todos provinieran directamente de la rama principal, evitando los commits de fusion. Esto hace que la historia del proyecto sea mas clara, facil de seguir y limpia.

2. ¿Qué problemas potenciales podrían surgir si haces rebase en una rama compartida con otros miembros del equipo?

Puede causar muchos problemas, porque estaremos reescribiendo un historial que ellos ya tienen. Por ejemplo si otros miembros del equipo ya han hecho pull de esa rama y tu haces rebase y luego haces push, las versiones locales de los otros miembros ya no coincidiran con la nueva historia lo que puede generar conflictos al hacer pull, confusion y riesgo de perdida de trabajo si no resolvemos los conflictos correctamente

3. ¿En qué se diferencia cherry-pick de merge, y en qué situaciones preferirías uno sobre el otro?

La diferencia entre cherry-pick y merge es que el primero copia uno o varios commits especificos de otra rama mientras que el segundo trae todo el historial de esa rama. Usaria cherry-pick cuando solo necesite aplicar un cambio puntual como un bugfix, sin mezclar el resto del trabajo de la rama original.

4. ¿Por qué es importante evitar hacer rebase en ramas públicas?

Porque al modificar el historial podemos complicarle la vida a los demas colaboradores. Ellos ya podrian haber hecho cambios basados en ese historial y si nosotros lo reescribimos, su version quedara desactualizada lo que generara conflictos, errores y una perdida innecesaria de tiempo para arreglarlo todo.

### **Ejercicios teóricos**

1. **Diferencias entre git merge y git rebase**  
   **Pregunta**: Explica la diferencia entre git merge y git rebase y describe en qué escenarios sería más adecuado utilizar cada uno en un equipo de desarrollo ágil que sigue las prácticas de Scrum.

La diferencia clave es que git merge une ramas preservando todo el historial original y crea un merge commit que señala el punto de fusion mientras que git rebase “reescala” tus commits sobre la rama main o base, como si los hubieras hecho a partir del ultimo estado de main o base, lo que da un historial mas limpio y lineal. En un equipo Scrum conviene usar merge porque al finalizar una feature queda reflejada en un unico commit de merge, mostrando con claridad cuando y como se integro. Y usaria rebase para las propias ramas de trabajo de los desarrolladores antes de subirlas, de modo que al revisarlas parezca que siempre partieron de la última version estable de main.

2. **Relación entre git rebase y DevOps**  
   **Pregunta**: ¿Cómo crees que el uso de git rebase ayuda a mejorar las prácticas de DevOps, especialmente en la implementación continua (CI/CD)? Discute los beneficios de mantener un historial lineal en el contexto de una entrega continua de código y la automatización de pipelines.

En un flujo DevOps con CI/CD, un historial lineal facilita muchisimo la automatizacion, los pipelines de CI/CD detectan cambios mas facilmente, los diffs son mas pequeños y claros, y herramientas como git bisect funcionan sin interferencias de merges innecesarios. Ademas al mantener una secuencia ordenada de commits es mas sencillo generar changelogs automaticos, acelerando el ciclo de feedback y reduciendo la posibilidad de errores en el despliegue.

3. **Impacto del git cherry-pick en un equipo Scrum**  
   **Pregunta**: Un equipo Scrum ha finalizado un sprint, pero durante la integración final a la rama principal (main) descubren que solo algunos commits específicos de la rama de una funcionalidad deben aplicarse a producción. ¿Cómo podría ayudar git cherry-pick en este caso? Explica los beneficios y posibles complicaciones.

Por ejemplo al final del sprint descubrimos que solo dos correcciones criticas deben ir a produccion y el resto de la feature aun no esta lista. Con cherry-pick podemos seleccionar esos dos commits puntuales y aplicarlos en main sin arrastrar el resto del trabajo incompleto. Asi garantizamos que en produccion solo llegue lo probado y aprobado. Pero tendriamos posibles complicaciones como manejar posibles conflictos y en que como esos commits podrian aparecer “duplicados” en la historia, uno en el main y el otro de la otra rama "feature" lo que podria producir confucion de cual commir es el orginal por lo que hay que procurar documentar bien que se aplico y no perder el hilo de quien hizo que y cuando.

### **Ejercicios prácticos**

1. **Simulación de un flujo de trabajo Scrum con git rebase y git merge**

   **Contexto:**  
   Tienes una rama `main` y una rama `feature` en la que trabajas. Durante el desarrollo del sprint, se han realizado commits tanto en `main` como en `feature`.  

   Tu objetivo es integrar los cambios de la rama `feature` en `main` manteniendo un historial limpio.

   **Instrucciones:**

   - Crea un repositorio y haz algunos commits en la rama main.

   <div align="center">
      <img src="https://i.postimg.cc/sxwTLtnP/Act6-Ejercicio3-1.png" alt="act6Ejer3.4" width="700" />
   </div>

   - Crea una rama feature, agrega nuevos commits, y luego realiza algunos commits adicionales en main.

   <div align="center">
      <img src="https://i.postimg.cc/sgtwbPJL/Act6-Ejercicio3-2.png" alt="act6Ejer3.4" width="700" />
   </div>

   - Realiza un rebase de feature sobre main.

   <div align="center">
      <img src="https://i.postimg.cc/FFDGhXZ3/Act6-Ejercicio3-3.png" alt="act6Ejer3.4" width="650" />
   </div>
     
   - Finalmente, realiza una fusión fast-forward de feature con main.
  
   <div align="center">
      <img src="https://i.postimg.cc/vTkVDhDF/Act6-Ejercicio3-4.png" alt="act6Ejer3.4" width="650" />
   </div>

   **Preguntas:**

   - ¿Qué sucede con el historial de commits después del rebase?<br>
Después de realizar un git rebase de la rama feature sobre main, el historial de commits cambia de forma que los commits de feature se reescriben y se colocan "encima" de los commits mas recientes de main. Esto hace que la historia parezca lineal como si los cambios en feature hubieran ocurrido despues de los de main aunque originalmente hayan sido paralelos en diferentes ramas.

   - ¿En qué situación aplicarías una fusión fast-forward en un proyecto ágil?<br>
Lo usaria cuando la rama de desarrollo (por ejemplo feature) esta completamente actualizada respecto a main es decir cuando main no ha tenido cambios nuevos desde que se creo feature. En este caso al fusionar, Git simplemente "avanza" el puntero de main hacia el ultimo commit de feature sin crear un commit extra de fusion. En un proyecto agil esto lo aplicariamos al final de un sprint si los cambios en feature ya fueron probados y revisados y se quiere integrar de forma limpia ya que fast-forward preserva una linea de tiempo clara y continua que refleje bien la evolucion del proyecto.

2. **Cherry-pick para integración selectiva en un pipeline CI/CD**

   **Contexto:**  
   Durante el desarrollo de una funcionalidad, te das cuenta de que solo ciertos cambios deben ser integrados en la rama de producción, ya que el resto aún está en desarrollo. Para evitar fusionar toda la rama, decides hacer cherry-pick de los commits que ya están listos para producción.

   **Instrucciones:**

   - Crea un repositorio con una rama main y una rama feature.
  
   <div align="center">
      <img src="https://i.postimg.cc/bJvbphnd/Act6-Ejercicio4-1.png" alt="act6Ejer4.1" width="650" />
   </div>

   - Haz varios commits en la rama feature, pero solo selecciona uno o dos commits específicos que consideres listos para producción.
  
   <div align="center">
      <img src="https://i.postimg.cc/PxLzsw0P/Act6-Ejercicio4-2.png" alt="act6Ejer4.2" width="690" />
   </div>

   - Realiza un cherry-pick de esos commits desde feature a main.
  
   <div align="center">
      <img src="https://i.postimg.cc/Prnb9Ny5/Act6-Ejercicio4-3.png" alt="act6Ejer4.3" width="670" />
   </div>

   - Verifica que los commits cherry-picked aparezcan en main.
  
   <div align="center">
      <img src="https://i.postimg.cc/DwBqS6TS/Act6-Ejercicio4-4.png" alt="act6Ejer4.4" width="650" />
   </div>


   **Preguntas:**

   - ¿Cómo utilizarías cherry-pick en un pipeline de CI/CD para mover solo ciertos cambios listos a producción?<br>
Lo utilizaria cuando necesito pasar rapidamente ciertos cambios especificos como una correccion urgente o una mejora puntual, desde una rama de desarrollo a la rama de produccion sin tener que fusionar toda la rama. Asi podemos hacer despliegues mas seguros sin detener el avance del resto del equipo en otras funcionalidades.

   - ¿Qué ventajas ofrece cherry-pick en un flujo de trabajo de DevOps?<br>
Una de las mayores ventajas de usar cherry-pick en un flujo de trabajo DevOps es que nos da un control muy preciso sobre que cambios se integran en produccion. No siempre todo lo que se desarrolla esta listo para desplegarse, asi que poder elegir exactamente que commit llevar sin tener que fusionar toda una rama es realmente muy util. Por ejemplo si estamos trabajando en una nueva funcionalidad pero solo una parte de ella ya paso las pruebas y esta aprobada, con cherry-pick podemos mover solo ese fragmento sin afectar lo demas.

### **Git, Scrum y Sprints**

#### **Fase 1: Planificación del sprint (sprint planning)**

**Ejercicio 1: Crear ramas de funcionalidades (feature branches)**

En esta fase del sprint, los equipos Scrum deciden qué historias de usuario van a trabajar. Cada historia de usuario puede representarse como una rama de funcionalidad.

**Objetivo:** Crear ramas para cada historia de usuario y asegurar que el trabajo se mantenga aislado.

**Instrucciones:**

1. Crea un repositorio en Git.

   <div align="center">
      <img src="https://i.postimg.cc/P5k7scBs/Act6-Ejercicio5-1.png" alt="act6Ejer5.1" width="500" />
   </div>
   
3. Crea una rama `main` donde estará el código base.

   <div align="center">
      <img src="https://i.postimg.cc/MH7yystV/Act6-Ejercicio5-2.png" alt="act6Ejer5.2" width="650" />
   </div>

4. Crea una rama por cada historia de usuario asignada al sprint, partiendo de la rama `main`.

   <div align="center">
      <img src="https://i.postimg.cc/9QM7MF3G/Act6-Ejercicio5-3.png" alt="act6Ejer5.3" width="630" />
   </div>

**Pregunta:** ¿Por qué es importante trabajar en ramas de funcionalidades separadas durante un sprint?<br>
Trabajar en ramas de funcionalidades separadas durante un sprint es importante porque nos permite que cada desarrollador o equipo trabaje de forma aislada en una tarea especifica sin interferir con el trabajo de los demas.

#### **Fase 2: Desarrollo del sprint (sprint execution)**

**Ejercicio 2: Integración continua con git rebase**

A medida que los desarrolladores trabajan en sus respectivas historias de usuario, pueden ocurrir cambios en main. Para mantener un historial lineal y evitar conflictos más adelante, se usa `git rebase` para integrar los últimos cambios de main en las ramas de funcionalidad antes de finalizar el sprint.

**Objetivo:** Mantener el código de la rama de funcionalidad actualizado con los últimos cambios de main durante el sprint.

**Instrucciones:**

1. Haz algunos commits en main.

   <div align="center">
      <img src="https://i.postimg.cc/gjfXx33Q/Act6-Ejercicio5-4.png" alt="act6Ejer5.4" width="700" />
   </div>

2. Realiza un rebase de la rama `feature-user-story-1` para actualizar su base con los últimos cambios de main.

   <div align="center">
      <img src="https://i.postimg.cc/xCLT6Bmx/Act6-Ejercicio5-5.png" alt="act6Ejer5.5" width="630" />
   </div>

**Pregunta:** ¿Qué ventajas proporciona el rebase durante el desarrollo de un sprint en términos de integración continua?<br>
Ofrece como ventaja que el historial de cambios se mantiene limpio y ordenado, lo que nos facilita mucho el seguimiento del trabajo durante el sprint. Ademas al usar rebase podemos asegurarnos de que la rama en la que estamos trabajando este siempre actualizada con los ultimos cambios de main, sin necesidad de generar commits de merge que ensucien el historial. Esto hace que la integracion continua sea mas fluida ya que se reducen los conflictos y el codigo se puede probar y desplegar con mayor confianza.

#### **Fase 3: Revisión del sprint (sprint review)**

**Ejercicio 3: Integración selectiva con git cherry-pick**

En esta fase, es posible que algunas funcionalidades estén listas para ser mostradas a los stakeholders, pero otras aún no están completamente implementadas. Usar `git cherry-pick` puede permitirte seleccionar commits específicos para mostrar las funcionalidades listas, sin hacer merge de ramas incompletas.

**Objetivo:** Mover commits seleccionados de una rama de funcionalidad (`feature-user-story-2`) a `main` sin integrar todos los cambios.

**Instrucciones:**

1. Realiza algunos commits en `feature-user-story-2`.

   <div align="center">
      <img src="https://i.postimg.cc/Gpw5RfVn/Act6-Ejercicio5-6.png" alt="act6Ejer5.6" width="630" />
   </div>

2. Haz cherry-pick de los commits que estén listos para mostrarse a los stakeholders durante la revisión del sprint.

   <div align="center">
      <img src="https://i.postimg.cc/fyr2dBKw/Act6-Ejercicio5-7.png" alt="act6Ejer5.7" width="630" />
   </div>

**Pregunta:** ¿Cómo ayuda `git cherry-pick` a mostrar avances de forma selectiva en un sprint review?<br>
git cherry-pick nos ayuda seleccionando solo los commits que estan completamente listos y funcionales para llevarlos a la rama principal antes del sprint review. Esto es nos es muy util porque a veces estamos trabajando en varias partes de una funcionalidad pero no todas estan terminadas o probadas. Con cherry-pick podemos mostrar solo los avances que si estan listos sin tener que fusionar toda la rama lo cual nos da una imagen mas clara y controlada del progreso real del equipo durante la revision del sprint.

#### **Fase 4: Retrospectiva del sprint (sprint retrospective)**

**Ejercicio 4: Revisión de conflictos y resolución**

Durante un sprint, pueden surgir conflictos al intentar integrar diferentes ramas de funcionalidades. Es importante aprender cómo resolver estos conflictos y discutirlos en la retrospectiva.

**Objetivo:** Identificar y resolver conflictos de fusión con `git merge` al intentar integrar varias ramas de funcionalidades al final del sprint.

**Instrucciones:**

1. Realiza cambios en `feature-user-story-1` y `feature-user-story-2` que resulten en conflictos.

   <div align="center">
      <img src="https://i.postimg.cc/d0PpQsn4/Act6-Ejercicio5-8.png" alt="act6Ejer5.8" width="800" />
   </div>

2. Intenta hacer merge de ambas ramas con main y resuelve los conflictos.

   <div align="center">
      <img src="https://i.postimg.cc/tTrB6pt0/Act6-Ejercicio5-9.png" alt="act6Ejer5.9" width="750" />
   </div>

   <div align="center">
      <img src="https://i.postimg.cc/BQJx0dxH/Act6-Ejercicio5-10.png" width="500" />
      <img src="https://i.postimg.cc/6QZ7R0rB/Act6-Ejercicio5-11.png" alt="act6Ejer5.11" width="400" />
   </div>

**Pregunta**: 
- ¿Cómo manejas los conflictos de fusión al final de un sprint?<br>
Cuando hay conflictos de fusion al final del sprint hay que manejarlo comparando cuidadosamente los cambios en cada archivo entendiendo que aporto cada parte y hablando con el autor del otro cambio, asi para tener una fusion existosa y correcta.
  
- ¿Cómo puede el equipo mejorar la comunicación para evitar conflictos grandes?<br>
Para evitar conflictos grandes el equipo puede comunicarse mejor informando cuando estan trabajando en los mismos archivos o funcionalidades. Tambien ayudaria hacer pull mas seguido, usar ramas pequeñas y revisar los cambios entre todos los miembros del equipo con regularidad.

#### **Fase 5: Fase de desarrollo, automatización de integración continua (CI) con git rebase**

**Ejercicio 5: Automatización de rebase con hooks de Git**

En un entorno CI, es común automatizar ciertas operaciones de Git para asegurar que el código se mantenga limpio antes de que pase a la siguiente fase del pipeline. Usa los hooks de Git para automatizar el rebase cada vez que se haga un push a una rama de funcionalidad.

**Objetivo:** Implementar un hook que haga automáticamente un rebase de `main` antes de hacer push en una rama de funcionalidad, asegurando que el historial se mantenga limpio.

**Instrucciones:**

1. Configura un hook `pre-push` que haga un rebase automático de la rama `main` sobre la rama de funcionalidad antes de que el push sea exitoso.

   <div align="center">
      <img src="https://i.postimg.cc/ZnZ26pRW/Act6-Ejercicio5-12.png" alt="act6Ejer5.12" width="700" />
   </div>

2. Prueba el hook haciendo push de algunos cambios en la rama `feature-user-story-1`.

   <div align="center">
      <img src="https://i.postimg.cc/J0P6JFvF/Act6-Ejercicio5-13.png" alt="act6Ejer5.13" width="700" />
   </div>

**Pregunta**: ¿Qué ventajas y desventajas observas al automatizar el rebase en un entorno de CI/CD?<br>
Automatizar el rebase en un entorno CI/CD tiene como ventaja que nos asegura que las ramas esten siempre actualizadas con la ultima version de main lo que reduce conflictos y mantiene el historial limpio. Ademas nos ahorra tiempo al no tener que hacerlo manualmente. La desventaja es que si ocurre un conflicto durante el rebase automatico puede detener el pipeline y requerir intervencion manual lo que nos puede complicar un poco el flujo si no se gestiona bien.

### **Navegando conflictos y versionado en un entorno devOps**

**Objetivo:**  
Gestionar conflictos en Git, realizar fusiones complejas, utilizar herramientas para comparar y resolver conflictos, aplicar buenas prácticas en el manejo del historial de versiones  y usar el versionado semántico en un entorno de integración continua (CI).

**Herramientas:**

- Git  
- Un entorno de desarrollo (Visual Studio Code, terminal, etc.)  
- Un repositorio en GitHub o GitLab (opcional, puede ser local)

**Contexto:**  
En un entorno de desarrollo colaborativo, los conflictos son inevitables cuando varios desarrolladores trabajan en la misma base de código. Resolver estos conflictos es crucial para mantener un flujo de trabajo eficiente en DevOps.

Los conflictos ocurren cuando dos ramas modifican la misma línea de un archivo y luego se intenta fusionarlas. Git no puede decidir qué cambio priorizar, por lo que la resolución manual es necesaria.

#### **Ejemplo:**

1. **Inicialización del proyecto y creación de ramas**

   - **Paso 1**: Crea un nuevo proyecto en tu máquina local.
     ```bash
     $ mkdir proyecto-colaborativo
     $ cd proyecto-colaborativo
     ```

   <div align="center">
      <img src="https://i.postimg.cc/SK3HXbTd/Act6-Ejercicio6-1.png" alt="act6Ejer1.1" width="700" />
   </div>

   - **Paso 2**: Inicializa Git en tu proyecto.
     ```bash
     $ git init
     ```

   <div align="center">
      <img src="https://i.postimg.cc/Lsc09B50/Act6-Ejercicio6-2.png" alt="act6Ejer6.1" width="700" />
   </div>

   - **Paso 3**: Crea un archivo de texto llamado `archivo_colaborativo.txt` y agrega algún contenido inicial.
     ```bash
     $ echo "Este es el contenido inicial del proyecto" > archivo_colaborativo.txt
     ```

   <div align="center">
      <img src="https://i.postimg.cc/GtQMxWQZ/Act6-Ejercicio6-3.png" alt="act6Ejer6.2" width="900" />
   </div>

   - **Paso 4**: Agrega el archivo al área de staging y haz el primer commit.
     ```bash
     $ git add .
     $ git commit -m "Commit inicial con contenido base"
     ```

   <div align="center">
      <img src="https://i.postimg.cc/L68vM0v8/Act6-Ejercicio6-4.png" alt="act6Ejer6.3" width="700" />
   </div>

   - **Paso 5**: Crea dos ramas activas: main y feature-branch.
     ```bash
     $ git branch feature-branch  # Crear una nueva rama
     ```
     
   <div align="center">
      <img src="https://i.postimg.cc/tJwswT2P/Act6-Ejercicio6-5.png" alt="act6Ejer6.4" width="750" />
   </div>

   - **Paso 6**: Haz checkout a la rama feature-branch y realiza un cambio en el archivo `archivo_colaborativo.txt`.
     ```bash
     $ git checkout feature-branch
     $ echo "Este es un cambio en la feature-branch" >> archivo_colaborativo.txt
     $ git add .
     $ git commit -m "Cambios en feature-branch"
     ```

   <div align="center">
      <img src="https://i.postimg.cc/vTJmXKZt/Act6-Ejercicio6-6.png" alt="act6Ejer6.5" width="900" />
   </div>

   - **Paso 7**: Regresa a la rama main y realiza otro cambio en la misma línea del archivo `archivo_colaborativo.txt`.
     ```bash
     $ git checkout main
     $ echo "Este es un cambio en la rama main" >> archivo_colaborativo.txt
     $ git add .
     $ git commit -m "Cambios en main"
     ```

   <div align="center">
      <img src="https://i.postimg.cc/DztnnWty/Act6-Ejercicio6-7.png" alt="act6Ejer6.6" width="700" />
   </div>

2. **Fusión y resolución de conflictos**

   - **Paso 1**: Intenta fusionar feature-branch en main. Se espera que surjan conflictos de fusión.
     ```bash
     $ git merge feature-branch
     ```

   <div align="center">
      <img src="https://i.postimg.cc/vH3yD2pK/Act6-Ejercicio6-8.png" alt="act6Ejer6.8" width="700" />
   </div>

   - **Paso 2**: Usa `git status` para identificar los archivos en conflicto. Examina los archivos afectados y resuelve manualmente los conflictos, conservando las líneas de código más relevantes para el proyecto.
     ```bash
     $ git status
     $ git checkout --theirs <archivo>  # Si decides aceptar los cambios de feature-branch
     $ git checkout --ours <archivo>    # Si decides aceptar los cambios de main
     ```
git checkout --ours <archivo> / --theirs Nos permite elegir que version del archivo conservar en caso de conflictos. Esto nos ayuda a tomar decisiones rapidas.

   <div align="center">
      <img src="https://i.postimg.cc/d0TcHsLM/Act6-Ejercicio6-9.png" alt="act6Ejer6.9" width="650" />
   </div>

   - **Paso 3**: Una vez resueltos los conflictos, commitea los archivos y termina la fusión
     ```bash
     $ git add .
     $ git commit -m "Conflictos resueltos"
     ```

   <div align="center">
      <img src="https://i.postimg.cc/x1cw8fGk/Act6-Ejercicio6-10.png" alt="act6Ejer6.10" width="700" />
   </div>

3. **Simulación de fusiones y uso de git diff**

   - **Paso 1**: Simula una fusión usando `git merge --no-commit --no-ff` para ver cómo se comportarían los cambios antes de realizar el commit.
     ```bash
     $ git merge --no-commit --no-ff feature-branch
     $ git diff --cached  # Ver los cambios en el área de staging
     $ git merge --abort  # Abortar la fusión si no es lo que se esperaba
     ```

   <div align="center">
      <img src="https://i.postimg.cc/kX5ZYJpj/Act6-Ejercicio6-11.png" alt="act6Ejer6.11" width="900" />
   </div>

git merge --no-commit --no-ff nos permite visualizar como afectaria una fusion sin aplicar el commit. Nos es util para verificar cambios antes de integrarlos minimizando errores. git diff --cached nos muestra los cambios preparados para el commit, es ideal para revisar lo que vamos a guardar antes de hacerlo. Y git merge --abort que cancela la fusion en curso es util cuando detectas que la integracion no es adecuada o que hay conflictos complejos.

4. **Uso de git mergetool**

   - **Paso 1**: Configura git mergetool con una herramienta de fusión visual (puedes usar meld, vimdiff, o Visual Studio Code).
     ```bash
     $ git config --global merge.tool <nombre-herramienta>
     $ git mergetool
     ```

   <div align="center">
      <img src="https://i.postimg.cc/DZgj5Hdk/Act6-Ejercicio6-12.png" alt="act6Ejer6.12" width="900" />
   </div>

git config --global merge.tool configura una herramienta visual para ayudarnos a resolver conflictos, esto mejora la comprension y facilita las decisiones en fusiones complejas.

   - **Paso 2**: Usa la herramienta gráfica para resolver un conflicto de fusión.

   <div align="center">
      <img src="https://i.postimg.cc/3NyKTXwR/Act6-Ejercicio6-13.png" alt="act6Ejer6.13" width="900" />
   </div>
   <div align="center">
      <img src="https://i.postimg.cc/Gp23Kn1G/Act6-Ejercicio6-14.png" width="500" />
      <img src="https://i.postimg.cc/fLSz47yb/Act6-Ejercicio6-15.png" alt="act6Ejer6.15" width="500" />
   </div>


5. **Uso de git revert y git reset**

   - **Paso 1**: Simula la necesidad de revertir un commit en main debido a un error. Usa `git revert` para crear un commit que deshaga los cambios.
     ```bash
     $ git revert <commit_hash>
     ```

   <div align="center">
      <img src="https://i.postimg.cc/252bjxCF/Act6-Ejercicio6-16.png" alt="act6Ejer6.16" width="900" />
   </div>

git revert crea un nuevo commit que deshace los efectos de un commit anterior, esto es seguro porque mantiene el historial y es ideal para entornos colaborativos o produccion.

   - **Paso 2**: Realiza una prueba con `git reset --mixed` para entender cómo reestructurar el historial de commits sin perder los cambios no commiteados.
     ```bash
     $ git reset --mixed <commit_hash>
     ```

   <div align="center">
      <img src="https://i.postimg.cc/XvHf1WBb/Act6-Ejercicio6-17.png" alt="act6Ejer6.17" width="700" />
   </div>

git reset --mixed vuelve a un estado anterior del historial pero conserva los cambios en el directorio de trabajo, es util para corregir errores sin perder codigo.

2. **Versionado semántico y etiquetado**

   - **Paso 1**: Aplica versionado semántico al proyecto utilizando tags para marcar versiones importantes.
     ```bash
     $ git tag -a v1.0.0 -m "Primera versión estable"
     $ git push origin v1.0.0
     ```

   <div align="center">
      <img src="https://i.postimg.cc/x8yq7Gpz/Act6-Ejercicio6-18.png" alt="act6Ejer6.18" width="700" />
   </div>

git tag marca versiones importantes del proyecto no permite identificar puntos clave del desarrollo, facilitando despliegues o entregas.

3. **Aplicación de git bisect para depuración**

   - **Paso 1**: Usa `git bisect` para identificar el commit que introdujo un error en el código.
     ```bash
     $ git bisect start
     $ git bisect bad   # Indica que la versión actual tiene un error
     $ git bisect good <último_commit_bueno>
     # Continúa marcando como "good" o "bad" hasta encontrar el commit que introdujo el error
     $ git bisect reset  # Salir del modo bisect
     ```

   <div align="center">
      <img src="https://i.postimg.cc/25s6S9PW/Act6-Ejercicio6-19.png" alt="act6Ejer6.19" width="650" />
   </div>

git bisect nos permite encontrar el commit exacto que introdujo un error mediante busqueda binaria. Es muy util para encontrar en que commit ocurre el primer error, encontradolo de forma optima.

4. **Documentación y reflexión**

   - **Paso 1**: Documenta todos los comandos usados y los resultados obtenidos en cada paso.<br>
     Se adjuntaron los comandos usados y resultado por medio de imagenes en cada proceso del proyecto de ejemplo.
     
   - **Paso 2**: Reflexiona sobre la utilidad de cada comando en un flujo de trabajo de DevOps.<br>
     Se redacto las reflexiones de los comandos hechos en cada punto del proceso del proyecto de ejemplo

### **Preguntas**

1. **Ejercicio para git checkout --ours y git checkout --theirs**

   **Contexto**: En un sprint ágil, dos equipos están trabajando en diferentes ramas. Se produce un conflicto de fusión en un archivo de configuración crucial. El equipo A quiere mantener sus cambios mientras el equipo B solo quiere conservar los suyos. El proceso de entrega continua está detenido debido a este conflicto.

   **Pregunta**:  
   ¿Cómo utilizarías los comandos `git checkout --ours` y `git checkout --theirs` para resolver este conflicto de manera rápida y eficiente? Explica cuándo preferirías usar cada uno de estos comandos y cómo impacta en la pipeline de CI/CD. ¿Cómo te asegurarías de que la resolución elegida no comprometa la calidad del código?

En nuestro sprint agil al enfrentar un conflicto entre los equipos A y B por cambios en el mismo archivo de configuracion usariamos git checkout --ours cuando creamos que los cambios de nuestro equipo (A) son los que deben prevalecer. Por el contrario usariamos git checkout --theirs cuando los cambios del equipo B sean mas importantes o correctos para el proyecto. La decision de cualquiera de estas, impacta directamente en nuestra pipeline de CI/CD ya que elegir incorrectamente podria introducir errores o retrasar entregas. Para asegurar la calidad antes de confirmar cualquier resolucion hariamos una reunion rapida entre ambos equipos para revisar los cambios y ejecutariamos pruebas locales completas, asegurando que la solucion elegida mantenga la integridad del sistema.

2. **Ejercicio para git diff**

   **Contexto**: Durante una revisión de código en un entorno ágil, se observa que un pull request tiene una gran cantidad de cambios, muchos de los cuales no están relacionados con la funcionalidad principal. Estos cambios podrían generar conflictos con otras ramas en la pipeline de CI/CD.

   **Pregunta**:  
   Utilizando el comando `git diff`, ¿cómo compararías los cambios entre ramas para identificar diferencias específicas en archivos críticos? Explica cómo podrías utilizar `git diff feature-branch..main` para detectar posibles conflictos antes de realizar una fusión y cómo esto contribuye a mantener la estabilidad en un entorno ágil con CI/CD.

Durante nuestra revision de codigo usariamos git diff feature-branch..main para identificar especificamente que archivos criticos han cambiado entre ramas. Ahora si queremos enfocarnos en un archivo particular podriamos ejecutar git diff feature-branch..main archivo_especifico, esto nos ayuda a detectar posibles conflictos antes de intentar la fusion. En nuestro entorno agil con CI/CD esta practica nos ahorra tiempo  al evitar fusiones problematicas que podrian romper el pipeline, permitiendonos identificar tempranamente cambios que necesitan coordinacion entre equipos.

3. **Ejercicio para git merge --no-commit --no-ff**

   **Contexto**: En un proyecto ágil con CI/CD, tu equipo quiere simular una fusión entre una rama de desarrollo y la rama principal para ver cómo se comporta el código sin comprometerlo inmediatamente en el repositorio. Esto es útil para identificar posibles problemas antes de completar la fusión.

   **Pregunta**:  
   Describe cómo usarías el comando `git merge --no-commit --no-ff` para simular una fusión en tu rama local. ¿Qué ventajas tiene esta práctica en un flujo de trabajo ágil con CI/CD, y cómo ayuda a minimizar errores antes de hacer commits definitivos? ¿Cómo automatizarías este paso dentro de una pipeline CI/CD?

Para simular una fusion sin comprometerla inmediatamente ejecutariamos git merge --no-commit --no-ff feature-branch desde nuestra rama principal, esto nos permite ver exactamente como quedarian los archivos despues de la fusion y ejecutar pruebas locales para verificar que todo funciona correctamente. Si en el caso detectamos problemas simplemente hacemos git merge --abort y no hay daño, esta practica es invaluable en nuestro flujo de trabajo agil ya que nos da la oportunidad de detectar problemas antes de que afecten al resto del equipo o interrumpan el pipeline de CI/CD. Para automatizar esto podriamos añadir un paso de pre-merge en nuestro pipeline que simule la fusion y ejecute las pruebas, enviando alertas si detecta posibles problemas.

4. **Ejercicio para git mergetool**

   **Contexto**: Tu equipo de desarrollo utiliza herramientas gráficas para resolver conflictos de manera colaborativa. Algunos desarrolladores prefieren herramientas como vimdiff o Visual Studio Code. En medio de un sprint, varios archivos están en conflicto y los desarrolladores prefieren trabajar en un entorno visual para resolverlos.

   **Pregunta**:  
   Explica cómo configurarías y utilizarías `git mergetool` en tu equipo para integrar herramientas gráficas que faciliten la resolución de conflictos. ¿Qué impacto tiene el uso de `git mergetool` en un entorno de trabajo ágil con CI/CD, y cómo aseguras que todos los miembros del equipo mantengan consistencia en las resoluciones?

En nuestro equipo hay que configurar git mergetool eligiendo una herramienta comun como Visual Studio Code con git config --global merge.tool vscode, cuando enfrentemos conflictos durante el sprint simplemente ejecutamos git mergetool para abrir la interfaz grafica que nos muestra claramente las diferencias entre versiones, facilitando la toma de decisiones informando sobre que codigo mantener. git mergetool mejorara notablemente nuestro flujo agil al reducir el tiempo dedicado a resolver conflictos complejos y disminuir errores que podrian afectar el pipeline. Y para mantener la consistencia entre el equipo tenemos que documentar nuestras preferencias de configuracion y ocasionalmente hacemos sesiones cuando lidiamos con conflictos especialmente complicados.

5. **Ejercicio para git reset**

   **Contexto**: En un proyecto ágil, un desarrollador ha hecho un commit que rompe la pipeline de CI/CD. Se debe revertir el commit, pero se necesita hacerlo de manera que se mantenga el código en el directorio de trabajo sin deshacer los cambios.

   **Pregunta**:  
   Explica las diferencias entre `git reset --soft`, `git reset --mixed` y `git reset --hard`. ¿En qué escenarios dentro de un flujo de trabajo ágil con CI/CD utilizarías cada uno? Describe un caso en el que usarías `git reset --mixed` para corregir un commit sin perder los cambios no commiteados y cómo afecta esto a la pipeline.

git reset --soft mueve el puntero de la rama (HEAD) a un commit anterior y conserva tanto los cambios en el area de staging como en el directorio de trabajo, es util cuando solo quieres rehacer el ultimo commit. git reset --mixed tambien mueve HEAD pero limpia el area de staging dejando los cambios en el directorio de trabajo sin perderse ideal cuando quieres reorganizar los cambios antes de volver a hacer commit. git reset --hard descarta todo, tanto staging y el directorio de trabajo, volviendo al estado exacto del commit anterior lo cual es peligroso si no has guardado tus cambios. En un flujo agil con CI/CD, git reset --mixed es util cuando se detecta que un commit rompio el pipeline, ya que te permite corregir el codigo sin perder el trabajo realizado, podemos hacer git reset --mixed HEAD~1, ajustar el error y luego hacer un nuevo commit limpio que no cause fallos en la integracion continua. Esto evitando que cambios defectuosos lleguen al repositorio remoto o afecten al equipo.

6. **Ejercicio para git revert**

   **Contexto**: En un entorno de CI/CD, tu equipo ha desplegado una característica a producción, pero se ha detectado un bug crítico. La rama principal debe revertirse para restaurar la estabilidad, pero no puedes modificar el historial de commits debido a las políticas del equipo.

   **Pregunta**:  
   Explica cómo utilizarías `git revert` para deshacer los cambios sin modificar el historial de commits. ¿Cómo te aseguras de que esta acción no afecte la pipeline de CI/CD y permita una rápida recuperación del sistema? Proporciona un ejemplo detallado de cómo revertirías varios commits consecutivos.

Utilizaria git revert para crear un nuevo commit que deshace los cambios problematicos sin alterar el historial. Por ejemplo si ejecutamos git revert abc1234 (hash del commit problematico) esto generara un nuevo commit con los cambios invertidos. Ahora para revertir varios commits consecutivos se puede usar el comando git revert con el rango de commits en orden inverso. Por ejemplo si queremos revertir los tres ultimos commits, ejecutariamos git revert HEAD~2..HEAD (esto aplica los reverts en orden desde el mas antiguo al mas reciente). Esto nos asegura que la rama principal se mantenga estable sin eliminar la evidencia de los cambios previos, permitiendonos que el pipeline procese los nuevos commits como parte del flujo normal. Ademas que se puede verificar que todo funcione correctamente ejecutando pruebas locales o usando entornos de staging antes de hacer git push asi garantizando asi una recuperacion rapida y segura en produccion.

7. **Ejercicio para git stash**

   **Contexto**: En un entorno ágil, tu equipo está trabajando en una corrección de errores urgente mientras tienes cambios no guardados en tu directorio de trabajo que aún no están listos para ser committeados. Sin embargo, necesitas cambiar rápidamente a una rama de hotfix para trabajar en la corrección.

   **Pregunta**:  
   Explica cómo utilizarías `git stash` para guardar temporalmente tus cambios y volver a ellos después de haber terminado el hotfix. ¿Qué impacto tiene el uso de `git stash` en un flujo de trabajo ágil con CI/CD cuando trabajas en múltiples tareas? ¿Cómo podrías automatizar el proceso de *stashing* dentro de una pipeline CI/CD?

git stash es una herramienta util para guardar temporalmente los cambios del directorio de trabajo que aun no estan listos para ser committeados. Si surge una urgencia como un hotfix en produccion podemos ejecutar git stash para guardar nuestros cambios actuales y dejar nuestra area de trabajo limpia, luego podemos cambiar a la rama del hotfix con git checkout hotfix-rama y realizar la correccion. Una vez completado y desplegado el hotfix podemos volver a nuestra rama original con git checkout mi-rama y recuperar nuestros cambios con git stash pop. Este flujo propuesto evita la perdida de trabajo y permite una rapida reaccion ante urgencias sin contaminar el codigo en produccion. En un flujo CI/CD git stash no afecta directamente al pipeline ya que los cambios no estan committeados pero es util para desarrolladores que alternan tareas locales. Para automatizarlo podemos incluir un script en el pipeline (por ejemplo en hooks) que haga git stash push -m "stash-auto" antes de hacer checkout a otra rama y luego git stash pop cuando se regrese permitiendo asi una gestion mas fluida del contexto en entornos colaborativos.

8. **Ejercicio para .gitignore**

   **Contexto**: Tu equipo de desarrollo ágil está trabajando en varios entornos locales con configuraciones diferentes (archivos de logs, configuraciones personales). Estos archivos no deberían ser parte del control de versiones para evitar confusiones en la pipeline de CI/CD.

   **Pregunta**:  
   Diseña un archivo `.gitignore` que excluya archivos innecesarios en un entorno ágil de desarrollo. Explica por qué es importante mantener este archivo actualizado en un equipo colaborativo que utiliza CI/CD y cómo afecta la calidad y limpieza del código compartido en el repositorio.

Ejemplo de archivo .gitignore que excluye archivos innecesarios:

```gitignore
# Entorno virtual
venv/

# Archivos compilados
*.pyc
__pycache__/

# Configuración de editor
.vscode/
.idea/

# Archivos temporales y de logs
*.log
*.tmp
```

Es importante mantener el archivo .gitignore actualizado en un equipo colaborativo con CI/CD porque nos asegura que solo los archivos relevantes para el proyecto se incluyan en el repositorio. Esto permite evita subir archivos innecesarios como configuraciones personales, archivos temporales o generados automaticamente, que podrian causar errores en la integracion continua. Un .gitignore bien gestionado nos contribuye a mantener la limpieza, organizacion y calidad del codigo compartido permitiendo un flujo de trabajo mas agil y eficiente.



