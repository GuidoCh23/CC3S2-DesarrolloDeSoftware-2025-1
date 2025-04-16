## ACTIVIDAD 5
Nombre: Guido Anthony Chipana Calderon

### Ejercicio 1: Clona un repositorio Git con múltiples ramas.
   Clonamos un repositorio Git que tenga multiples ramas
   
   <div align="center">
      <img src="https://i.postimg.cc/2503dhBr/Act5-Ejercicio11-1.png" width="800" />
      <img src="https://i.postimg.cc/63SSDWmF/Act5-Ejercicio11-2.png" alt="act5Ejer11.2" width="600" />
   </div>

   Identifica dos ramas que puedas fusionar utilizando `git merge --ff`.  

   <div align="center">
      <img src="https://i.postimg.cc/PJncXtmc/Act5-Ejercicio11-6.png" alt="act5Ejer11.3" width="500" />
   </div>

   Existen cambios en la rama colaboracion que no esta en develop, por lo que haremos el marge desde develop.
   
   Haz el proceso de fusión utilizando `git merge --ff`.  

   <div align="center">
      <img src="https://i.postimg.cc/7ZjjsM5w/Act5-Ejercicio11-7.png" alt="act5Ejer11.4" width="650" />
   </div>
   
   Verifica el historial con `git log --graph --oneline`.  

   <div align="center">
      <img src="https://i.postimg.cc/9MH0h7nj/Act5-Ejercicio11-8.png" alt="act5Ejer11.5" width="650" />
   </div>

   **Pregunta:** ¿En qué situaciones recomendarías evitar el uso de `git merge --ff`? Reflexiona sobre las desventajas de este método.

Evitaria usar git merge --ff cuando queramos que este claro en el historial que hubo una rama con una funcionalidad o cambio especifico. Si usamos fast-forward se pierde ese commit de que algo vino de otra rama y eso puede complicar revisar el historial mas adelante.

### Ejercicio 2: Simula un flujo de trabajo de equipo.  
   Trabaja en dos ramas independientes, creando diferentes cambios en cada una.  

   <div align="center">
      <img src="https://i.postimg.cc/T15yz7B2/Act5-Ejercicio2-1.png" alt="act5Ejer2.1" width="800" />
   </div>
   
   Fusiona ambas ramas con `git merge --no-ff` para ver cómo se crean los commits de fusión.  

   <div align="center">
      <img src="https://i.postimg.cc/bN8DCT3P/Act5-Ejercicio2-2.png" width="800" />
      <img src="https://i.postimg.cc/B6H5DvQB/Act5-Ejercicio2-3.png" width="400" />
      <img src="https://i.postimg.cc/0jZwdKgD/Act5-Ejercicio2-4.png" alt="act5Ejer2.4" width="400" />
   </div>
   
   Observa el historial utilizando `git log --graph --oneline`.  

   <div align="center">
      <img src="https://i.postimg.cc/mgWsNXw3/Act5-Ejercicio2-5.png" alt="act5Ejer2.5" width="700" />
   </div>

   **Pregunta:** 
   - **¿Cuáles son las principales ventajas de utilizar `git merge --no-ff` en un proyecto en equipo?**

El merge --no-ff nos permite mantener un historial mas claro y estructurado. Todos los cambios hechos en una rama queda registrado como una fusion distinta lo que facilita revisar el historial y entender que se hizo y cuando, sobre todo si muchas personas estan trabajando en paralelo.

   - **¿Qué problemas podrían surgir al depender excesivamente de commits de fusión?**

Podriamos tener el problema que el historial puede volverse muy ruidoso y dificil, y aun mas si se hacen muchos merges sin control.

### Ejercicio 3: Crea múltiples commits en una rama.  
   Haz varios cambios y commits en una rama feature.

   <div align="center">
      <img src="https://i.postimg.cc/rFtF55Zw/Act5-Ejercicio1-1.png" alt="act5Ejer1.1" width="800" />
   </div>
   
   Fusiona la rama con `git merge --squash` para aplanar todos los commits en uno solo.  

   <div align="center">
      <img src="https://i.postimg.cc/Sx3PCz5k/Act5-Ejercicio1-2.png" alt="act5Ejer1.2" width="630" />
   </div>

   Verifica el historial de commits antes y después de la fusión para ver la diferencia.  

   <div align="center">
      <img src="https://i.postimg.cc/T1jyqmQS/Act5-Ejercicio1-3.png" alt="act5Ejer1.3" width="750" />
   </div>

   **Preguntas:** 
   - **¿Cuándo es recomendable utilizar una fusión squash?** 
   
   Es recomendable cuando tienes muchos commits pequeños o experimentales que no merecen estar en el historial principal. Hay que usar squash cuando tenemos caracteristicas que pasaron por varias revisiones dejando solo      un commit limpio y descriptivo en main.
   
   - **¿Qué ventajas ofrece para proyectos grandes en comparación con fusiones estándar?**
   
   En proyectos grandes, el squash merge tiene como ventaja que mantiene el historial principal limpio y navegable ya que evita la acumulacion de muchos commits pequeños ya que todo estos commits pequeños lo agrupa en un     solo commit, simplificando la revision del codigo y mejora la legibilidad del historial.

### Ejercicio 4: Resolver conflictos en una fusión non-fast-forward

En algunos casos, las fusiones no son tan sencillas y pueden surgir conflictos que necesitas resolver manualmente. Este ejercicio te guiará a través del proceso de manejo de conflictos.

1. Inicializa un nuevo repositorio:
   ```bash
   mkdir prueba-merge-conflict
   cd prueba-merge-conflict
   git init
   ```

   <div align="center">
      <img src="https://i.postimg.cc/ZKt0KXf6/Act5-Ejercicio4-1.png" alt="act5Ejer4.1" width="600" />
   </div>

2. Crea un archivo index.html y realiza un commit en la rama main:
   ```bash
   echo "<html><body><h1>Proyecto inicial CC3S2</h1></body></html>" > index.html
   git add index.html
   git commit -m "commit inicial del  index.html en main"
   ```

   <div align="center">
      <img src="https://i.postimg.cc/zBZ4Rw42/Act5-Ejercicio4-2.png" alt="act5Ejer4.2" width="900" />
   </div>

3. Crea y cambia a una nueva rama feature-update:
   ```bash
   git checkout -b feature-update
   ```

   <div align="center">
      <img src="https://i.postimg.cc/9QBBBd4N/Act5-Ejercicio4-3.png" alt="act5Ejer4.3" width="750" />
   </div>

4. Edita el archivo y realiza un commit en la rama feature-update:
   ```bash
   echo "<p>.....</p>" >> index.html
   git add index.html
   git commit -m "Actualiza ..."
   ```

   <div align="center">
      <img src="https://i.postimg.cc/QCkBrbZ2/Act5-Ejercicio4-4.png" alt="act5Ejer4.4" width="750" />
   </div>

5. Regresa a la rama main y realiza una edición en el mismo archivo:
   ```bash
   git checkout main
   echo "<footer>Contacta aquí example@example.com</footer>" >> index.html
   git add index.html
   git commit -m "....index.html"
   ```

   <div align="center">
      <img src="https://i.postimg.cc/L5XdH9cm/Act5-Ejercicio4-5.png" alt="act5Ejer4.5" width="900" />
   </div>

6. Fusiona la rama feature-update con --no-ff y observa el conflicto:
   ```bash
   git merge --no-ff feature-update
   ```

   <div align="center">
      <img src="https://i.postimg.cc/6pCPx48d/Act5-Ejercicio4-6.png" alt="act5Ejer4.6" width="700" />
   </div>

7. Git detectará un conflicto en index.html. Abre el archivo y resuelve el conflicto. Elimina las líneas de conflicto generadas por Git (`<<<<<<<`, `=======`, `>>>>>>>`) y crea la versión final del archivo con ambos cambios:

   ```html
   <html>
     <body>
       <h1>....</h1>
       <p>....</p>
       <footer>...example@example.com</footer>
     </body>
   </html>
   ```

   <div align="center">
      <img src="https://i.postimg.cc/DZSDDjLz/Act5-Ejercicio4-7.png" width="450" />
      <img src="https://i.postimg.cc/T32tFNXX/Act5-Ejercicio4-8.png" alt="act5Ejer4.8" width="450" />
   </div>


8. Agrega el archivo corregido y completa la fusión:
   ```bash
   git add index.html
   git commit
   ```

   <div align="center">
      <img src="https://i.postimg.cc/cHf7rfNm/Act5-Ejercicio4-9.png" alt="act5Ejer4.9" width="900" />
   </div>

9. Verifica el historial para confirmar la fusión y el commit de resolución de conflicto:
   ```bash
   git log --graph --oneline
   ```

   <div align="center">
      <img src="https://i.postimg.cc/Pr7LnNgr/Act5-Ejercicio4-10.png" alt="act5Ejer4.10" width="700" />
   </div>

**Preguntas:**
- **¿Qué pasos adicionales tuviste que tomar para resolver el conflicto?**

Tuve que abrir los archivos en conflicto, revisar linea por linea, decidir que parte del codigo mantener y luego hacer un commit despues de resolver todo.

- **¿Qué estrategias podrías emplear para evitar conflictos en futuros desarrollos colaborativos?**

Implementaria trabajar en ramas bien separadas y comunicarnos mejor con el equipo sobre que partes del codigo esta tocando cada uno. Tambien nos ayudaria dividir bien las tareas para que no editemos los mismos archivos al mismo tiempo.

### Ejercicio 5: Comparar los historiales con git log después de diferentes fusiones

Este ejercicio te permitirá observar las diferencias en el historial generado por fusiones fast-forward, non-fast-forward y squash.

1. Crea un nuevo repositorio y realiza varios commits en dos ramas:
   ```bash
   mkdir prueba-compare-merge
   cd prueba-compare-merge
   git init
   echo "Version 1.0" > version.txt
   git add version.txt
   git commit -m "...."
   git checkout -b feature-1
   echo "Caracteristica 1 agregada" >> version.txt
   git add version.txt
   git commit -m "Agregar caracteristica 1"
   git checkout main
   git checkout -b feature-2
   echo "Caracteristica 2 agregada" >> version.txt
   git add version.txt
   git commit -m "Se agrega caracteristica 2"
   ```

   <div align="center">
      <img src="https://i.postimg.cc/KzgYgVNB/Act5-Ejercicio5-1.png" alt="act5Ejer5.1" width="900" />
   </div>

2. Fusiona feature-1 usando fast-forward:
   ```bash
   git checkout main
   git merge feature-1 --ff
   ```

   <div align="center">
      <img src="https://i.postimg.cc/dV1wypQ3/Act5-Ejercicio5-2.png" alt="act5Ejer15.2" width="700" />
   </div>

3. Fusiona feature-2 usando non-fast-forward:
   ```bash
   git merge feature-2 --no-ff
   ```

   <div align="center">
      <img src="https://i.postimg.cc/SKC52f9j/Act5-Ejercicio5-3.png" width="750" />
      <img src="https://i.postimg.cc/1tyWghPY/Act5-Ejercicio5-4.png" width="300" />
      <img src="https://i.postimg.cc/x84gFXmW/Act5-Ejercicio5-5.png" alt="act5Ejer5.5" width="300" />
   </div>

4. Realiza una nueva rama feature-3 con múltiples commits y fusiónala con squash:
   ```bash
   git checkout -b feature-3
   echo "Caracteristica 3 paso 1" >> version.txt
   git add version.txt
   git commit -m "Caracteristica 3 paso 1"
   echo "Caracteristica 3 paso 2" >> version.txt
   git add version.txt
   git commit -m "Caracteristica 3 paso 2"
   git checkout main
   git merge --squash feature-3
   git commit -m "Agregar caracteristica 3 en un commit"
   ```

   <div align="center">
      <img src="https://i.postimg.cc/G23QLFJW/Act5-Ejercicio5-6.png" alt="act5Ejer5.6" width="900" />
   </div>

4. Compara el historial de Git:
   - Historial Fast-forward:
     ```bash
     git log --graph --oneline --first-parent
     ```
     
   <div align="center">
      <img src="https://i.postimg.cc/QM8Y69nd/Act5-Ejercicio5-7.png" alt="act5Ejer5.7" width="800" />
   </div>

   - Historial Non-fast-forward:
     ```bash
     git log --graph --oneline –merges
     ```

   <div align="center">
      <img src="https://i.postimg.cc/V6SRTj9m/Act5-Ejercicio5-8.png" alt="act5Ejer5.8" width="800" />
   </div>

   - Historial con Squash:
     ```bash
     git log --graph --oneline --decorate --all
     ```

   <div align="center">
      <img src="https://i.postimg.cc/t452VRCQ/Act5-Ejercicio5-9.png" alt="act5Ejer5.9" width="800" />
   </div>

**Preguntas:**
- **¿Cómo se ve el historial en cada tipo de fusión?**

En el caso de Non-fast-forward y Squash se ve como un commit aparte para la fusion, pero en el caso de Fast Forward se funsiona sin agregar un commit extra para la fusion

- **¿Qué método prefieres en diferentes escenarios y por qué?**

Fast-forward lo prefiero para cambios pequeños y lineales para mantener un historial limpio. Non-fast-forward para caracteristicas mas complejas que requieren documentar detalladamente su integracion mediante commits de merge. Y Squash para limpiar ramas con muchos commits pequeños dejando solo un commit limpio y descriptivo en main.

### Ejercicio 6: Usando fusiones automáticas y revertir fusiones

En este ejercicio, aprenderás cómo Git puede fusionar automáticamente cambios cuando no hay conflictos y cómo revertir una fusión si cometes un error.

1. Inicializa un nuevo repositorio y realiza dos commits en main:
   ```bash
   mkdir prueba-auto-merge
   cd prueba-auto-merge
   git init
   echo "Linea 1" > file.txt
   git add file.txt
   git commit -m "Agrega linea 1"
   echo "Linea 2" >> file.txt
   git add file.txt
   git commit -m "...linea 2"
   ```

   <div align="center">
      <img src="https://i.postimg.cc/8cy3mGMK/Act5-Ejercicio6-1.png" alt="act5Ejer6.1" width="600" />
   </div>


2. Crea una nueva rama auto-merge y realiza otro commit en file.txt:
   ```bash
   git checkout -b auto-merge
   echo "Linea 3" >> file.txt
   git add file.txt
   git commit -m "... linea 3"
   ```

   <div align="center">
      <img src="https://i.postimg.cc/WbFSH0vb/Act5-Ejercicio6-2.png" alt="act5Ejer6.2" width="600" />
   </div>


3. Vuelve a main y realiza cambios no conflictivos en otra parte del archivo:
   ```bash
   git checkout main
   echo "Footer: Fin del archivo" >> file.txt
   git add file.txt
   git commit -m "Add footer al archivo file.txt"
   ```

   <div align="center">
      <img src="https://i.postimg.cc/rpnQHjKs/Act5-Ejercicio6-3.png" alt="act5Ejer6.3" width="800" />
   </div>


4. Fusiona la rama auto-merge con main:
   ```bash
   git merge auto-merge
   ```

   <div align="center">
      <img src="https://i.postimg.cc/02VMDB3z/Act5-Ejercicio6-4.png" alt="act5Ejer6.4" width="600" />
   </div>


5. Git debería fusionar los cambios automáticamente sin conflictos.

   <div align="center">
      <img src="https://i.postimg.cc/HsnsDsZL/Act5-Ejercicio6-5.png" alt="act5Ejer5.9" width="600" />
   </div>

6. Revertir la fusión: Si decides que la fusión fue un error, puedes revertirla:
   ```bash
   git revert -m 1 HEAD
   ```

   <div align="center">
      <img src="https://i.postimg.cc/q7k5Sgwb/Act5-Ejercicio6-6.png" alt="act5Ejer6.6" width="650" />
   </div>


7. Verifica el historial:
   ```bash
   git log --graph --oneline
   ```

   <div align="center">
      <img src="https://i.postimg.cc/K8Q6Zn1S/Act5-Ejercicio6-7.png" alt="act5Ejer6.7" width="600" />
   </div>


**Preguntas:**
- **¿Cuándo usarías un comando como git revert para deshacer una fusión?**

Lo usaria si la fusion ya se hizo en la rama principal y resulto en errores o rompio algo, git revert permite deshacer los cambios sin perder el rastro de lo que paso.

- **¿Qué tan útil es la función de fusión automática en Git?**

Es muy util, la mayoria de veces Git resuelve todo solo y eso ahorra tiempo. Pero cuando hay conflictos igual toca revisarlo manualmente.

### Ejercicio 7: Fusión remota en un repositorio colaborativo

Este ejercicio te permitirá practicar la fusión de ramas en un entorno remoto colaborativo, simulando un flujo de trabajo de equipo.

1. Clona un repositorio remoto desde GitHub o crea uno nuevo:
   ```bash
   git clone https://github.com/tu-usuario/nombre-del-repositorio.git
   cd nombre-del-repositorio
   ```

   <div align="center">
      <img src="https://i.postimg.cc/RF0806cD/Act5-Ejercicio7-1.png" alt="act5Ejer7.1" width="800" />
   </div>

2. Crea una nueva rama colaboracion y haz algunos cambios:
   ```bash
   git checkout -b colaboracion
   echo "Colaboración remota" > colaboracion.txt
   git add colaboracion.txt
   git commit -m "...."
   ```

   <div align="center">
      <img src="https://i.postimg.cc/ZK3Tm2Yy/Act5-Ejercicio7-2.png" alt="act5Ejer7.2" width="800" />
   </div>

3. Empuja los cambios a la rama remota:
   ```bash
   git push origin colaboracion
   ```

   <div align="center">
      <img src="https://i.postimg.cc/fbWZxbcx/Act5-Ejercicio7-3.png" alt="act5Ejer7.3" width="800" />
   </div>

4. Simula una fusión desde la rama colaboracion en la rama main de otro colaborador. (Puedes usar la interfaz de GitHub para crear un Pull Request y realizar la fusión).

   <div align="center">
      <img src="https://i.postimg.cc/bNRB193B/Act5-Ejercicio7-4.png" width="700" />
      <img src="https://i.postimg.cc/mrKXTXgt/Act5-Ejercicio7-5.png" width="500" />
      <img src="https://i.postimg.cc/x83ty9yz/Act5-Ejercicio7-6.png" alt="act5Ejer7.6" width="450" />
   </div>

**Preguntas:**
- **¿Cómo cambia la estrategia de fusión cuando colaboras con otras personas en un repositorio remoto?**

La estrategia cambia porque ya no decides solo, hay que adaptarse a las politicas del equipo sobre usar algun tipo de estrategia de fusion. Ahora importa mas la comunicacion y las politicas del equipo.

- **¿Qué problemas comunes pueden surgir al integrar ramas remotas?**

Podemos tener problemas como conflictos de fusion cuando hay varias modificaciones en el mismo archivo y tambien podemos tener commits desordenados que son dificiles de revisar.

### Ejercicio 8 y final: flujo de trabajo completo

Configura un proyecto simulado:

- Crea un proyecto con tres ramas: main, feature1, y feature2.

   <div align="center">
      <img src="https://i.postimg.cc/qqrVLKQ1/Act5-Ejercicio8-1.png" alt="act5Ejer8.1" width="700" />
   </div>
  
- Realiza varios cambios en feature1 y feature2 y simula colaboraciones paralelas.

   <div align="center">
      <img src="https://i.postimg.cc/mkVZJ4Xf/Act5-Ejercicio8-2.png" alt="act5Ejer8.2" width="700" />
   </div>

- Realiza fusiones utilizando diferentes métodos:
  - Fusiona feature1 con main utilizando `git merge --ff`.

   <div align="center">
      <img src="https://i.postimg.cc/rsYX5wZm/Act5-Ejercicio8-3.png" alt="act5Ejer8.3" width="600" />
   </div>

  - Fusiona feature2 con main utilizando `git merge --no-ff`.
 
   <div align="center">
      <img src="https://i.postimg.cc/vmXP4SN8/Act5-Ejercicio8-4.png" alt="act5Ejer8.4" width="900" />
   </div>

  - Haz una rama adicional llamada feature3 y aplasta sus commits utilizando `git merge --squash`.

   <div align="center">
      <img src="https://i.postimg.cc/3JgzK9YN/Act5-Ejercicio8-5.png" alt="act5Ejer8.5" width="800" />
   </div>

Analiza el historial de commits:

- Revisa el historial para entender cómo los diferentes métodos de fusión afectan el árbol de commits.

   <div align="center">
      <img src="https://i.postimg.cc/mZ3Sknzv/Act5-Ejercicio8-6.png" alt="act5Ejer8.6" width="600" />
   </div>

- Compara los resultados y discute con tus compañeros de equipo cuál sería la mejor estrategia de fusión para proyectos más grandes.

Para proyectos mas grandes creo que seria mejor usar la fusion de no-fast-forward ya que nos permite crear un commit de merge/fusion al fusionar dos ramas, esto es util para identificar en que momento se hizo la fusion y con que rama, pero siempre hay que usarlo con criterio, porque si hacemos varias fusiones no-fast-forward saturara el historial de commits de merges lo que complica el entendimiento de los cambios hechos en el proyecto.
