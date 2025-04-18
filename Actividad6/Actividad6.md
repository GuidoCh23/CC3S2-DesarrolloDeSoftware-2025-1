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
2. Crea una rama `main` donde estará el código base.
3. Crea una rama por cada historia de usuario asignada al sprint, partiendo de la rama `main`.

**Comandos:**
```bash
$ mkdir scrum-project
$ cd scrum-project
$ git init
$ echo "# Proyecto Scrum" > README.md
$ git add README.md
$ git commit -m "Commit inicial en main"

# Crear ramas de historias de usuario
$ git checkout -b feature-user-story-1
$ git checkout -b feature-user-story-2
```

**Pregunta:** ¿Por qué es importante trabajar en ramas de funcionalidades separadas durante un sprint?


#### **Fase 2: Desarrollo del sprint (sprint execution)**

**Ejercicio 2: Integración continua con git rebase**

A medida que los desarrolladores trabajan en sus respectivas historias de usuario, pueden ocurrir cambios en main. Para mantener un historial lineal y evitar conflictos más adelante, se usa `git rebase` para integrar los últimos cambios de main en las ramas de funcionalidad antes de finalizar el sprint.

**Objetivo:** Mantener el código de la rama de funcionalidad actualizado con los últimos cambios de main durante el sprint.

**Instrucciones:**

1. Haz algunos commits en main.
2. Realiza un rebase de la rama `feature-user-story-1` para actualizar su base con los últimos cambios de main.

**Comandos:**
```bash
# Simula cambios en la rama main
$ git checkout main
$ echo "Actualización en main" > updates.md
$ git add updates.md
$ git commit -m "Actualizar main con nuevas funcionalidades"

# Rebase de la rama feature-user-story-1 sobre main
$ git checkout feature-user-story-1
$ git rebase main
```

**Pregunta:** ¿Qué ventajas proporciona el rebase durante el desarrollo de un sprint en términos de integración continua?


#### **Fase 3: Revisión del sprint (sprint review)**

**Ejercicio 3: Integración selectiva con git cherry-pick**

En esta fase, es posible que algunas funcionalidades estén listas para ser mostradas a los stakeholders, pero otras aún no están completamente implementadas. Usar `git cherry-pick` puede permitirte seleccionar commits específicos para mostrar las funcionalidades listas, sin hacer merge de ramas incompletas.

**Objetivo:** Mover commits seleccionados de una rama de funcionalidad (`feature-user-story-2`) a `main` sin integrar todos los cambios.

**Instrucciones:**

1. Realiza algunos commits en `feature-user-story-2`.
2. Haz cherry-pick de los commits que estén listos para mostrarse a los stakeholders durante la revisión del sprint.

**Comandos:**
```bash
$ git checkout feature-user-story-2
$ echo "Funcionalidad lista" > feature2.md
$ git add feature2.md
$ git commit -m "Funcionalidad lista para revisión"

$ echo "Funcionalidad en progreso" > progress.md
$ git add progress.md
$ git commit -m "Funcionalidad aún en progreso"

# Ahora selecciona solo el commit que esté listo
$ git checkout main
$ git cherry-pick <hash_del_commit_de_feature-lista>
```

**Pregunta:** ¿Cómo ayuda `git cherry-pick` a mostrar avances de forma selectiva en un sprint review?


#### **Fase 4: Retrospectiva del sprint (sprint retrospective)**

**Ejercicio 4: Revisión de conflictos y resolución**

Durante un sprint, pueden surgir conflictos al intentar integrar diferentes ramas de funcionalidades. Es importante aprender cómo resolver estos conflictos y discutirlos en la retrospectiva.

**Objetivo:** Identificar y resolver conflictos de fusión con `git merge` al intentar integrar varias ramas de funcionalidades al final del sprint.

**Instrucciones:**

1. Realiza cambios en `feature-user-story-1` y `feature-user-story-2` que resulten en conflictos.
2. Intenta hacer merge de ambas ramas con main y resuelve los conflictos.

**Comandos:**
```bash
$ git checkout feature-user-story-1
$ echo "Cambio en la misma línea" > conflicted-file.md
$ git add conflicted-file.md
$ git commit -m "Cambio en feature 1"

$ git checkout feature-user-story-2
$ echo "Cambio diferente en la misma línea" > conflicted-file.md
$ git add conflicted-file.md
$ git commit -m "Cambio en feature 2"

# Intentar hacer merge en main
$ git checkout main
$ git merge feature-user-story-1
$ git merge feature-user-story-2
```

**Pregunta**: ¿Cómo manejas los conflictos de fusión al final de un sprint? ¿Cómo puede el equipo mejorar la comunicación para evitar conflictos grandes?


#### **Fase 5: Fase de desarrollo, automatización de integración continua (CI) con git rebase**

**Ejercicio 5: Automatización de rebase con hooks de Git**

En un entorno CI, es común automatizar ciertas operaciones de Git para asegurar que el código se mantenga limpio antes de que pase a la siguiente fase del pipeline. Usa los hooks de Git para automatizar el rebase cada vez que se haga un push a una rama de funcionalidad.

**Objetivo:** Implementar un hook que haga automáticamente un rebase de `main` antes de hacer push en una rama de funcionalidad, asegurando que el historial se mantenga limpio.

**Instrucciones:**

1. Configura un hook `pre-push` que haga un rebase automático de la rama `main` sobre la rama de funcionalidad antes de que el push sea exitoso.
2. Prueba el hook haciendo push de algunos cambios en la rama `feature-user-story-1`.

**Comandos:**
```bash
# Dentro de tu proyecto, crea un hook pre-push
$ nano .git/hooks/pre-push

# Agrega el siguiente script para automatizar el rebase
#!/bin/bash
git fetch origin main
git rebase origin/main

# Haz el archivo ejecutable
$ chmod +x .git/hooks/pre-push

# Simula cambios y haz push
$ git checkout feature-user-story-1
$ echo "Cambios importantes" > feature1.md
$ git add feature1.md
$ git commit -m "Cambios importantes en feature 1"
$ git push origin feature-user-story-1
```

**Pregunta**: ¿Qué ventajas y desventajas observas al automatizar el rebase en un entorno de CI/CD?







