## ACTIVIDAD 4
Nombre: Guido Anthony Chipana Calderon

### Ejercicio 1: Manejo avanzado de ramas y resolución de conflictos

**Objetivo:** Practicar la creación, fusión y eliminación de ramas, así como la resolución de conflictos que puedan surgir durante la fusión.

**Instrucciones:**

1. **Crear una nueva rama para una característica:**
   - Crea una nueva rama llamada `feature/advanced-feature` desde la rama `main`:
     
     ```bash
     $ git branch feature/advanced-feature
     $ git checkout feature/advanced-feature
      ```
     
      <div align="center">
        <img src="https://i.postimg.cc/PxXpjs6f/Act4-Ejercicio1-1.png" alt="act4Ejer1.1" width="700" />
      </div>

2. **Modificar archivos en la nueva rama:**
   - Edita el archivo `main.py` para incluir una función adicional:
     ```python
     def greet():
         print('Hello from advanced feature')

     greet()
     ```

      <div align="center">
        <img src="https://i.postimg.cc/dDPJJGqR/Act4-Ejercicio1-2.png" alt="act4Ejer1.2" width="500" />
      </div>

   - Añade y confirma estos cambios en la rama `feature/advanced-feature`:

     ```bash
     $ git add main.py
     $ git commit -m "Add greet function in advanced feature"
     ```
     
<div align="center">
  <img src="https://i.postimg.cc/x1gq3FfW/Act4-Ejercicio1-3.png" alt="act4Ejer1.3" width="700" />
</div>

3. **Simular un desarrollo paralelo en la rama main:**
   - Cambia de nuevo a la rama `main`:

     ```bash
     $ git checkout main
     ```

      <div align="center">
        <img src="https://i.postimg.cc/4NgdkTnD/Act4-Ejercicio1-4.png" alt="act4Ejer1.4" width="700" />
      </div>

   - Edita el archivo `main.py` de forma diferente (por ejemplo, cambia el mensaje del print original):
     ```python
     print('Hello World - updated in main')
     ```

      <div align="center">
        <img src="https://i.postimg.cc/GpVLXWZS/Act4-Ejercicio1-5.png" alt="act4Ejer1.5" width="400" />
      </div>

   - Añade y confirma estos cambios en la rama `main`:

     ```bash
     $ git add main.py
     $ git commit -m "Update main.py message in main branch"
     ```
     
      <div align="center">
        <img src="https://i.postimg.cc/y6F1Trnv/Act4-Ejercicio1-6.png" alt="act4Ejer1.6" width="700" />
      </div>

4. **Intentar fusionar la rama feature/advanced-feature en main:**
   - Fusiona la rama `feature/advanced-feature` en `main`:

     ```bash
     $ git merge feature/advanced-feature
     ```
     
      <div align="center">
        <img src="https://i.postimg.cc/9FCWgtnV/Act4-Ejercicio1-7.png" alt="act4Ejer1.7" width="700" />
      </div>

5. **Resolver el conflicto de fusión:**
   - Git generará un conflicto en `main.py`. Abre el archivo y resuelve el conflicto manualmente, eligiendo cómo combinar las dos versiones.
     
      <div align="center">
        <img src="https://i.postimg.cc/FKdmkP7b/Act4-Ejercicio1-8.png" width="400" />
        <img src="https://i.postimg.cc/XJ9bQpKp/Act4-Ejercicio1-9.png" alt="act4Ejer1.8" width="400" />
      </div>

   - Después de resolver el conflicto, añade el archivo resuelto y completa la fusión:

     ```bash
     $ git add main.py
     $ git commit -m "Resolve merge conflict between main and feature/advanced-feature"
     ```
     
      <div align="center">
        <img src="https://i.postimg.cc/Z5gzmrVW/Act4-Ejercicio1-10.png" alt="act4Ejer1.10" width="900" />
      </div>

6. **Eliminar la rama fusionada:**
   - Una vez que hayas fusionado con éxito y resuelto los conflictos, elimina la rama `feature/advanced-feature`:

     ```bash
     $ git branch -d feature/advanced-feature
     ```
     
      <div align="center">
        <img src="https://i.postimg.cc/cCTPbYv4/Act4-Ejercicio1-11.png" alt="act4Ejer1.11" width="700" />
      </div>

### Ejercicio 2: Exploración y manipulación del historial de commits

**Objetivo:** Aprender a navegar y manipular el historial de commits usando comandos avanzados de Git.

**Instrucciones:**

1. **Ver el historial detallado de commits:**
   - Usa el comando `git log` para explorar el historial de commits, pero esta vez con más detalle:

     ```bash
     $ git log -p
     ```

      <div align="center">
        <img src="https://i.postimg.cc/gcvMkvkx/Act4-Ejercicio2-1.png" alt="act4Ejer2.1" width="650" />
      </div>
      
   - Examina las diferencias introducidas en cada commit. ¿Qué cambios fueron realizados en cada uno?

      Vemos que hay muchos commits que detallan el autor del commit, cuando fue hecho y cual fue el cambio hecho.

2. **Filtrar commits por autor:**
   - Usa el siguiente comando para mostrar solo los commits realizados por un autor específico:

     ```bash
     $ git log --author="TuNombre"
     ```

      <div align="center">
        <img src="https://i.postimg.cc/Jh5nz6gT/Act4-Ejercicio2-2.png" alt="act4Ejer2.2" width="500" />
      </div>
      
3. **Revertir un commit:**
   - Imagina que el commit más reciente en `main.py` no debería haberse hecho. Usa `git revert` para revertir ese commit:

     ```bash
     $ git revert HEAD
     ```
     
      <div align="center">
        <img src="https://i.postimg.cc/x1Kj6p00/Act4-Ejercicio2-3.png" width="450" />
        <img src="https://i.postimg.cc/rpjVkd03/Act4-Ejercicio2-4.png" alt="act4Ejer2.4" width="500" />
      </div>

   - Verifica que el commit de reversión ha sido añadido correctamente al historial.

      <div align="center">
        <img src="https://i.postimg.cc/kG6qKf1P/Act4-Ejercicio2-5.png" alt="act4Ejer2.5" width="700" />
      </div>
      
4. **Rebase interactivo:**
   - Realiza un rebase interactivo para combinar varios commits en uno solo. Esto es útil para limpiar el historial de commits antes de una fusión.
   - Usa el siguiente comando para empezar el rebase interactivo:

     ```bash
     $ git rebase -i HEAD~3
     ```

      <div align="center">
        <img src="https://i.postimg.cc/s24YCJJz/Act4-Ejercicio2-10.png" alt="act4Ejer2.10" width="500" />
      </div>
     
   - En el editor que se abre, combina los últimos tres commits en uno solo utilizando la opción `squash`.

      <div align="center">
        <img src="https://i.postimg.cc/SKCZ2871/Act4-Ejercicio2-6.png" width="400" />
        <img src="https://i.postimg.cc/tTDNWz1k/Act4-Ejercicio2-8.png" width="400" />
        <img src="https://i.postimg.cc/RV2Q7h0k/Act4-Ejercicio2-9.png" alt="act4Ejer2.9" width="400" />
      </div>

5. **Visualización gráfica del historial:**
   - Usa el siguiente comando para ver una representación gráfica del historial de commits:

     ```bash
     $ git log --graph --oneline --all
     ```

      <div align="center">
        <img src="https://i.postimg.cc/T1FmJNTV/Act4-Ejercicio2-11.png" alt="act4Ejer2.11" width="700" />
      </div>
     
   - Reflexiona sobre cómo el historial de tu proyecto se visualiza en este formato. ¿Qué información adicional puedes inferir?

      Puedo ver que los commits son representados en forma de asteriscos (*) y que estas tienen cada un hash unico como tambien el comentario de que es ese commit, tambien que los commits que agregue en rebase ya no se encuentran por separado sino que todo esta junto en un solo commit.

### Ejercicio 3: Creación y gestión de ramas desde commits específicos

**Objetivo:** Practicar la creación de ramas desde commits específicos y comprender cómo Git maneja las referencias históricas.

**Instrucciones:**

1. **Crear una nueva rama desde un commit específico:**
   - Usa el historial de commits (`git log --oneline`) para identificar un commit antiguo desde el cual crear una nueva rama:

     ```bash
     $ git log --oneline
     ```

      <div align="center">
        <img src="https://i.postimg.cc/xdy55QJ9/Act4-Ejercicio3-1.png" alt="act4Ejer3.1" width="650" />
      </div>
      
   - Crea una nueva rama `bugfix/rollback-feature` desde ese commit:

     ```bash
     $ git branch bugfix/rollback-feature <commit-hash>
     $ git checkout bugfix/rollback-feature
     ```

      <div align="center">
        <img src="https://i.postimg.cc/1RYHJJtV/Act4-Ejercicio3-2.png" alt="act4Ejer3.2" width="700" />
      </div>

2. **Modificar y confirmar cambios en la nueva rama:**
   - Realiza algunas modificaciones en `main.py` que simulen una corrección de errores:
     ```python
     def greet():
         print('Fixed bug in feature')
     ```
     
      <div align="center">
        <img src="https://i.postimg.cc/FKZbcx8R/Act4-Ejercicio3-3.png" alt="act4Ejer3.3" width="500" />
      </div>
      
   - Añade y confirma los cambios en la nueva rama:

     ```bash
     $ git add main.py
     $ git commit -m "Fix bug in rollback feature"
     ```

      <div align="center">
        <img src="https://i.postimg.cc/W3YMY12c/Act4-Ejercicio3-4.png" alt="act4Ejer3.4" width="700" />
      </div>

3. **Fusionar los cambios en la rama principal:**
   - Cambia de nuevo a la rama `main` y fusiona la rama `bugfix/rollback-feature`:

     ```bash
     $ git checkout main
     $ git merge bugfix/rollback-feature
     ```

      <div align="center">
        <img src="https://i.postimg.cc/NFrrN8JR/Act4-Ejercicio3-5.png" alt="act4Ejer3.5" width="650" />
      </div>

   - Arreglamos los conflictos manualmente:
  
      <div align="center">
        <img src="https://i.postimg.cc/t4zDtyVp/Act4-Ejercicio3-6.png" width="400" />
        <img src="https://i.postimg.cc/rsWNdLk6/Act4-Ejercicio3-7.png" alt="act4Ejer3.7" width="400" />
      </div>

   - Añade el archivo resuelto y completamos el merge

     ```bash
     $ git add main.py
     $ git commit -m “resolve marge and fix bug in rollback feature”
     ```

      <div align="center">
        <img src="https://i.postimg.cc/cLTMtmVJ/Act4-Ejercicio3-8.png" alt="act4Ejer3.8" width="900" />
      </div>
      
4. **Explorar el historial después de la fusión:**
   - Usa `git log` y `git log --graph` para ver cómo se ha integrado el commit en el historial:

     ```bash
     $ git log --graph --oneline
     ```

      <div align="center">
        <img src="https://i.postimg.cc/Kz3nVy4K/Act4-Ejercicio3-9.png" alt="act4Ejer3.9" width="600" />
      </div>

5. **Eliminar la rama bugfix/rollback-feature:**
   - Una vez fusionados los cambios, elimina la rama `bugfix/rollback-feature`:

     ```bash
     $ git branch -d bugfix/rollback-feature
     ```

      <div align="center">
        <img src="https://i.postimg.cc/8PmLx4kb/Act4-Ejercicio3-10.png" alt="act4Ejer3.10" width="700" />
      </div>

### Ejercicio 4: Manipulación y restauración de commits con git reset y git restore

**Objetivo:** Comprender cómo usar `git reset` y `git restore` para deshacer cambios en el historial y en el área de trabajo.

**Instrucciones:**

1. **Hacer cambios en el archivo main.py:**
   - Edita el archivo `main.py` para introducir un nuevo cambio:
     ```python
     print('This change will be reset')
     ```

      <div align="center">
        <img src="https://i.postimg.cc/Twmc1Wg2/Act4-Ejercicio4-1.png" alt="act4Ejer4.1" width="450" />
      </div>
      
   - Añade y confirma los cambios:

     ```bash
     $ git add main.py
     $ git commit -m "Introduce a change to be reset"
     ```

      <div align="center">
        <img src="https://i.postimg.cc/Hn944D6f/Act4-Ejercicio4-2.png" alt="act4Ejer4.2" width="700" />
      </div>
      
2. **Usar git reset para deshacer el commit:**
   - Deshaz el commit utilizando `git reset` para volver al estado anterior:

     ```bash
     $ git reset --hard HEAD~1
     ```
     
   - Verifica que el commit ha sido eliminado del historial y que el archivo ha vuelto a su estado anterior.

      <div align="center">
        <img src="https://i.postimg.cc/RVvTChF9/Act4-Ejercicio4-3.png" alt="act4Ejer4.3" width="800" />
      </div>

3. **Usar git restore para deshacer cambios no confirmados:**
   - Realiza un cambio en `README.md` y no lo confirmes:

     ```bash
     $ echo "Another line in README" >> README.md
     $ git status
     ```

      <div align="center">
        <img src="https://i.postimg.cc/DZVq9yD9/Act4-Ejercicio4-4.png" alt="act4Ejer4.4" width="700" />
      </div>
      
   - Usa `git restore` para deshacer este cambio no confirmado:

     ```bash
     $ git restore README.md
     ```
      
   - Verifica que el cambio no confirmado ha sido revertido.

      <div align="center">
        <img src="https://i.postimg.cc/ZnHpvPRm/Act4-Ejercicio4-5.png" alt="act4Ejer4.5" width="700" />
      </div>

### Ejercicio 5: Trabajo colaborativo y manejo de Pull Requests

**Objetivo:** Simular un flujo de trabajo colaborativo utilizando ramas y pull requests.

**Instrucciones:**

1. **Crear un nuevo repositorio remoto:**
   - Usa GitHub o GitLab para crear un nuevo repositorio remoto y clónalo localmente:

     ```bash
     $ git clone <URL-del-repositorio>
     ```

      <div align="center">
        <img src="https://i.postimg.cc/652wbWrV/Act4-Ejercicio5-1.png" alt="act4Ejer5.1" width="750" />
      </div>

2. **Crear una nueva rama para desarrollo de una característica:**
   - En tu repositorio local, crea una nueva rama `feature/team-feature`:

     ```bash
     $ git branch feature/team-feature
     $ git checkout feature/team-feature
     ```

      <div align="center">
        <img src="https://i.postimg.cc/fLRQcDW9/Act4-Ejercicio5-2.png" alt="act4Ejer5.2" width="700" />
      </div>

3. **Realizar cambios y enviar la rama al repositorio remoto:**
   - Realiza cambios en los archivos del proyecto y confírmalos:

     ```bash
     $ echo "print('Collaboration is key!')" > collaboration.py
     $ git add .
     $ git commit -m "Add collaboration script"
     ```

      <div align="center">
        <img src="https://i.postimg.cc/fy64Qdcc/Act4-Ejercicio5-3.png" alt="act4Ejer5.3" width="800" />
      </div>

   - Envía la rama al repositorio remoto:

     ```bash
     $ git push origin feature/team-feature
     ```

      <div align="center">
        <img src="https://i.postimg.cc/tRfGxKKs/Act4-Ejercicio5-4.png" alt="act4Ejer5.4" width="700" />
      </div>

4. **Abrir un Pull Request:**
   - Abre un Pull Request (PR) en la plataforma remota (GitHub/GitLab) para fusionar `feature/team-feature` con la rama `main/master`.
   - Añade una descripción detallada del PR, explicando los cambios realizados y su propósito.

      <div align="center">
        <img src="https://i.postimg.cc/7LqF4w2W/Act4-Ejercicio5-5.png" alt="act4Ejer5.5" width="700" />
      </div>

5. **Revisar y fusionar el Pull Request:**
   - Simula la revisión de código, comenta en el PR y realiza cualquier cambio necesario basado en la retroalimentación.

      <div align="center">
        <img src="https://i.postimg.cc/kGRZs50B/Act4-Ejercicio5-6.png" alt="act4Ejer5.6" width="700" />
      </div>
   
   - Una vez aprobado, fusiona el PR en la rama `main/master`.

      <div align="center">
        <img src="https://i.postimg.cc/rwTVd64S/Act4-Ejercicio5-7.png" width="550" />
        <img src="https://i.postimg.cc/zvWNBpXt/Act4-Ejercicio5-8.png" alt="act4Ejer5.8" width="500" />
      </div>

6. **Eliminar la rama remota y local:**
   - Después de la fusión, elimina la rama tanto local como remotamente:

     ```bash
     $ git branch -d feature/team-feature
     $ git push origin --delete feature/team-feature
     ```

      <div align="center">
        <img src="https://i.postimg.cc/SN6qbZPj/Act4-Ejercicio5-9.png" alt="act4Ejer5.9" width="800" />
      </div>

### Ejercicio 6: Cherry-Picking y Git Stash

**Objetivo:** Aprender a aplicar commits específicos a otra rama utilizando `git cherry-pick` y a guardar temporalmente cambios no confirmados utilizando `git stash`.

**Instrucciones:**

1. **Hacer cambios en main.py y confirmarlos:**
   - Realiza y confirma varios cambios en `main.py` en la rama `main`:

     ```bash
     $ echo "print('Cherry pick this!')" >> main.py
     $ git add main.py
     $ git commit -m "Add cherry-pick example"
     ```

2. **Crear una nueva rama y aplicar el commit específico:**
   - Crea una nueva rama `feature/cherry-pick` y aplícale el commit específico:

     ```bash
     $ git branch feature/cherry-pick
     $ git checkout feature/cherry-pick
     $ git cherry-pick <commit-hash>
     ```

3. **Guardar temporalmente cambios no confirmados:**
   - Realiza algunos cambios en `main.py` pero no los confirmes:

     ```bash
     $ echo "This change is stashed" >> main.py
     $ git status
     ```
   - Guarda temporalmente estos cambios utilizando `git stash`:

     ```bash
     $ git stash
     ```

4. **Aplicar los cambios guardados:**
   - Realiza otros cambios y confírmalos si es necesario.
   - Luego, recupera los cambios guardados anteriormente:

     ```bash
     $ git stash pop
     ```

5. **Revisar el historial y confirmar la correcta aplicación de los cambios:**
   - Usa `git log` para revisar el historial de commits y verificar que todos los cambios se han aplicado correctamente.
