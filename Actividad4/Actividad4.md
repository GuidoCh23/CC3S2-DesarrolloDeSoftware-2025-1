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
