## ACTIVIDAD 9
Nombre: Guido Anthony Chipana Calderon

### Objetivo de aprendizaje:  
El objetivo de este proyecto es desarrollar una clase ShoppingCart que permita gestionar de forma eficiente un carrito de compras. La clase debe soportar las siguientes funcionalidades:

- **Agregar artículos al carrito:** Permitir añadir productos especificando nombre, cantidad y precio unitario, gestionando la posibilidad de agregar múltiples cantidades del mismo producto.
- **Eliminar artículos del carrito:** Remover productos previamente agregados.
- **Calcular el total del carrito:** Sumar el costo total de los artículos en el carrito, considerando la cantidad y precio unitario de cada uno.
- **Aplicar descuentos:** Permitir la aplicación de un descuento porcentual sobre el total del carrito, con validación de rango y redondeo a dos decimales.
- **Procesar pagos a través de un servicio externo:** Integrar un gateway de pago mediante inyección de dependencias para facilitar pruebas utilizando mocks y stubs, permitiendo simular el procesamiento de pagos sin realizar llamadas a servicios externos reales.

El proyecto se desarrollará de forma incremental utilizando el proceso RGR (Red, Green, Refactor) y pruebas unitarias con pytest para asegurar la correcta implementación de cada funcionalidad.

### La estructura del proyecto

```
├── pytest.ini
├── src
│   └── shopping_cart.py
└── tests
    └── test_shopping_cart.py

```

### Ejercicio

Desarrolla las 6 iteraciones de Desarrollo Guiado por Pruebas (TDD) (Red-Green-Refactor) aplicadas a la clase `UserManager`, incluyendo casos de mocks, stubs, fakes, spies e inyección de dependencias. Cada iteración presenta un escenario diferente para ilustrar cómo podrías usar estas técnicas. 

#### Iteración 1: Agregar usuario (Básico)

#### Paso 1 (Red): Escribimos la primera prueba

Creamos la prueba que verifica que podemos agregar un usuario con éxito. Para mantenerlo simple, no usamos aún ninguna inyección de dependencias ni mocks.

**Archivo:** `tests/test_user_manager.py`

```python
import pytest
from user_manager import UserManager, UserAlreadyExistsError

def test_agregar_usuario_exitoso():
    # Arrange
    manager = UserManager()
    username = "kapu"
    password = "securepassword"

    # Act
    manager.add_user(username, password)

    # Assert
    assert manager.user_exists(username), "El usuario debería existir después de ser agregado."
```

   <div align="center">
      <img src="https://i.postimg.cc/vZP5hnQs/AC9-1-1.png" alt="AC.1.1" width="600" />
   </div>

Si ejecutamos `pytest`, la prueba fallará porque aún no hemos implementado la clase `UserManager`.

   <div align="center">
      <img src="https://i.postimg.cc/hjmxK3VD/AC9-1-2.png" alt="AC.1.2" width="900" />
   </div>

#### Paso 2 (Green): Implementamos lo mínimo para que pase la prueba

**Archivo:** `user_manager.py`

```python
class UserAlreadyExistsError(Exception):
    pass

class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            raise UserAlreadyExistsError(f"El usuario '{username}' ya existe.")
        self.users[username] = password

    def user_exists(self, username):
        return username in self.users
```

   <div align="center">
      <img src="https://i.postimg.cc/8CjM0C5r/AC9-1-3.png" alt="AC.1.3" width="500" />
   </div>

Volvemos a ejecutar `pytest` y ahora la prueba pasan correctamente.

   <div align="center">
      <img src="https://i.postimg.cc/vmkfFdg2/AC9-1-4.png" alt="AC.1.4" width="900" />
   </div>

#### Paso 3 (Refactor)

Revisamos que el código sea claro y conciso. Por ahora, el diseño es simple y cumple su función.


### Iteración 2: Autenticación de usuario (Introducción de una dependencia para Hashing)

Ahora queremos asegurar contraseñas usando *hashing*. Para ello, introduciremos **inyección de dependencias**: crearemos una interfaz (o protocolo) para un "servicio de hashing", de modo que `UserManager` no dependa directamente de la implementación de hashing.

#### Paso 1 (Red): Escribimos la prueba

Queremos verificar que `UserManager` autentica correctamente a un usuario con la contraseña adecuada. Asumiremos que la contraseña se almacena en hash.

**Archivo:** `tests/test_user_manager.py`

```python
import pytest
from user_manager import UserManager, UserNotFoundError, UserAlreadyExistsError

class FakeHashService:
    """
    Servicio de hashing 'falso' (Fake) que simplemente simula el hashing
    devolviendo la cadena con un prefijo "fakehash:" para fines de prueba.
    """
    def hash(self, plain_text: str) -> str:
        return f"fakehash:{plain_text}"

    def verify(self, plain_text: str, hashed_text: str) -> bool:
        return hashed_text == f"fakehash:{plain_text}"

def test_autenticar_usuario_exitoso_con_hash():
    # Arrange
    hash_service = FakeHashService()
    manager = UserManager(hash_service=hash_service)

    username = "usuario1"
    password = "mypassword123"
    manager.add_user(username, password)

    # Act
    autenticado = manager.authenticate_user(username, password)

    # Assert
    assert autenticado, "El usuario debería autenticarse correctamente con la contraseña correcta."
```

   <div align="center">
      <img src="https://i.postimg.cc/NFYyBGgD/AC9-2-1.png" alt="AC.2.1" width="600" />
   </div>

Notar que hemos creado un `FakeHashService` que actúa como un **Fake**: se comporta como un servicio “real”, pero su lógica es simplificada para pruebas (no usa un algoritmo de hashing real).

Si ejecutamos la prueba, fallará porque no hemos implementado ni `authenticate_user` ni la inyección de `hash_service`.

   <div align="center">
      <img src="https://i.postimg.cc/xjyJgmR4/AC9-2-2.png" alt="AC.2.2" width="900" />
   </div>

#### Paso 2 (Green): Implementamos la funcionalidad y la DI

Modificamos `user_manager.py` para inyectarle un servicio de hashing:

```python
class UserNotFoundError(Exception):
    pass

class UserAlreadyExistsError(Exception):
    pass

class UserManager:
    def __init__(self, hash_service=None):
        """
        Si no se provee un servicio de hashing, se asume un hash trivial por defecto
        (simplemente para no romper el código).
        """
        self.users = {}
        self.hash_service = hash_service
        if not self.hash_service:
            # Si no pasamos un hash_service, usamos uno fake por defecto.
            # En producción, podríamos usar bcrypt o hashlib.
            class DefaultHashService:
                def hash(self, plain_text: str) -> str:
                    return plain_text  # Pésimo, pero sirve de ejemplo.

                def verify(self, plain_text: str, hashed_text: str) -> bool:
                    return plain_text == hashed_text

            self.hash_service = DefaultHashService()

    def add_user(self, username, password):
        if username in self.users:
            raise UserAlreadyExistsError(f"El usuario '{username}' ya existe.")
        hashed_pw = self.hash_service.hash(password)
        self.users[username] = hashed_pw

    def user_exists(self, username):
        return username in self.users

    def authenticate_user(self, username, password):
        if not self.user_exists(username):
            raise UserNotFoundError(f"El usuario '{username}' no existe.")
        stored_hash = self.users[username]
        return self.hash_service.verify(password, stored_hash)
```

   <div align="center">
      <img src="https://i.postimg.cc/pXW9SdcX/AC9-2-3.png" alt="AC.2.3" width="550" />
   </div>

Ejecutamos `pytest` y la prueba debería pasar. Nuestra inyección de dependencias nos permite cambiar la lógica de hashing sin modificar `UserManager`.

   <div align="center">
      <img src="https://i.postimg.cc/Y03v9c0H/AC9-2-4.png" alt="AC.2.4" width="900" />
   </div>

#### Paso 3 (Refactor)

Podemos refactorizar si lo consideramos necesario, pero por ahora la estructura cumple el propósito.


#### Iteración 3: Uso de un Mock para verificar llamadas (Spy / Mock)

Ahora queremos asegurarnos de que, cada vez que llamamos a `add_user`, se invoque el método `hash` de nuestro servicio de hashing. Para ello, usaremos un **mock** que “espía” si se llamó el método y con qué parámetros. Esto sería un caso de **Spy o Mock**.

#### Paso 1 (Red): Escribimos la prueba de "espionaje"

Instalaremos e importaremos `unittest.mock` (incluido con Python 3) para crear un mock:

```python
from unittest.mock import MagicMock

def test_hash_service_es_llamado_al_agregar_usuario():
    # Arrange
    mock_hash_service = MagicMock()
    manager = UserManager(hash_service=mock_hash_service)
    username = "spyUser"
    password = "spyPass"

    # Act
    manager.add_user(username, password)

    # Assert
    mock_hash_service.hash.assert_called_once_with(password)
```

   <div align="center">
      <img src="https://i.postimg.cc/gJw9j30k/AC9-2-5.png" alt="AC.2.5" width="450" />
   </div>

Esta prueba verificará que, después de llamar a `add_user`, efectivamente el método `hash` se llamó **exactamente una vez** con `password` como argumento.

#### Paso 2 (Green): Probar que todo pasa

Realmente, nuestro código ya llama a `hash_service.hash`. Si ejecutamos `pytest`, la prueba debería pasar de inmediato, pues la implementación actual ya cumple la expectativa.

   <div align="center">
      <img src="https://i.postimg.cc/gJ1CZrwy/AC9-2-6.png" alt="AC.2.6" width="900" />
   </div>

#### Paso 3 (Refactor)

No hay cambios adicionales. El uso de Mocks/Spies simplemente corrobora el comportamiento interno.


#### Iteración 4: Excepción al agregar usuario existente (Stubs/más pruebas negativas)

En esta iteración, reforzamos la prueba para el caso de usuario duplicado. Ya tenemos la excepción `UserAlreadyExistsError`, pero vamos a hacer una **prueba un poco más compleja** usando *stubs* si quisiéramos aislar ciertos comportamientos.

Realmente, podemos considerar un “stub” si quisiéramos forzar que `user_exists` devuelva `True`. Sin embargo, nuestra lógica interna ya está implementada. Mostraremos un stub parcial:

#### Paso 1 (Red): Prueba

```python
def test_no_se_puede_agregar_usuario_existente_stub():
    # Este stub forzará que user_exists devuelva True
    class StubUserManager(UserManager):
        def user_exists(self, username):
            return True

    stub_manager = StubUserManager()
    with pytest.raises(UserAlreadyExistsError) as exc:
        stub_manager.add_user("cualquier", "1234")

    assert "ya existe" in str(exc.value)
```

   <div align="center">
      <img src="https://i.postimg.cc/XvtWwsmy/AC9-2-7.png" alt="AC.2.7" width="420" />
   </div>

Aquí forzamos con una subclase `StubUserManager` que devuelva `True` en `user_exists`, simulando que el usuario “ya existe”. Así aislamos el comportamiento sin importar lo que pase dentro.

#### Paso 2 (Green)

Modificaremos la clase `UserManager`, especificamente el metodo `add_user` para que use `user_exists` y devuelva `True`

   <div align="center">
      <img src="https://i.postimg.cc/hPNkj2zJ/AC9-2-9.png" alt="AC.2.9" width="600" />
   </div>

#### Paso 3 (Refactor)

Nada adicional por el momento. Todas las pruebas pasan

   <div align="center">
      <img src="https://i.postimg.cc/FRc4GjXC/AC9-2-8.png" alt="AC.2.8" width="900" />
   </div>

#### Iteración 5: Agregar un "Fake" repositorio de datos (Inyección de Dependencias)

Hasta ahora, `UserManager` guarda los usuarios en un diccionario interno (`self.users`). Supongamos que queremos que en producción se use una base de datos, pero en pruebas se use un repositorio en memoria. Esto es un uso típico de **Fake** o **InMemory** repos.

#### Paso 1 (Red): Nueva prueba

Creamos una prueba que verifique que podemos inyectar un repositorio y que `UserManager` lo use.

```python
class InMemoryUserRepository:
    """Fake de un repositorio de usuarios en memoria."""
    def __init__(self):
        self.data = {}

    def save_user(self, username, hashed_password):
        if username in self.data:
            raise UserAlreadyExistsError(f"'{username}' ya existe.")
        self.data[username] = hashed_password

    def get_user(self, username):
        return self.data.get(username)

    def exists(self, username):
        return username in self.data

def test_inyectar_repositorio_inmemory():
    repo = InMemoryUserRepository()
    manager = UserManager(repo=repo)  # inyectamos repo
    username = "fakeUser"
    password = "fakePass"

    manager.add_user(username, password)
    assert manager.user_exists(username)
```
   <div align="center">
      <img src="https://i.postimg.cc/2SvPBnh0/AC9-2-10.png" alt="AC.2.10" width="500" />
   </div>

Como vemos, ahora `UserManager` debería aceptar un `repo` para almacenar y consultar usuarios, en vez de usar un diccionario interno.

   <div align="center">
      <img src="https://i.postimg.cc/R0B21qT4/AC9-2-11.png" alt="AC.2.11" width="900" />
   </div>
   
Al ejecutar los test vemos que no pasa, porque `repo` aun no esta definida en la clase `UserManager`

#### Paso 2 (Green): Implementación

Modificamos `UserManager` para recibir un `repo`:

```python
class UserManager:
    def __init__(self, hash_service=None, repo=None):
        self.hash_service = hash_service or self._default_hash_service()
        self.repo = repo
        if not self.repo:
            # Si no se inyecta repositorio, usamos uno interno por defecto
            self.repo = self._default_repo()
    
    def _default_hash_service(self):
        class DefaultHashService:
            def hash(self, plain_text: str) -> str:
                return plain_text
            def verify(self, plain_text: str, hashed_text: str) -> bool:
                return plain_text == hashed_text
        return DefaultHashService()

    def _default_repo(self):
        # Un repositorio en memoria muy básico
        class InternalRepo:
            def __init__(self):
                self.data = {}
            def save_user(self, username, hashed_password):
                if username in self.data:
                    raise UserAlreadyExistsError(f"'{username}' ya existe.")
                self.data[username] = hashed_password
            def get_user(self, username):
                return self.data.get(username)
            def exists(self, username):
                return username in self.data
        return InternalRepo()

    def add_user(self, username, password):
        hashed = self.hash_service.hash(password)
        self.repo.save_user(username, hashed)

    def user_exists(self, username):
        return self.repo.exists(username)

    def authenticate_user(self, username, password):
        stored_hash = self.repo.get_user(username)
        if stored_hash is None:
            raise UserNotFoundError(f"El usuario '{username}' no existe.")
        return self.hash_service.verify(password, stored_hash)
```

   <div align="center">
      <img src="https://i.postimg.cc/fyz8k9Zg/AC9-2-12.png" alt="AC.2.12" width="500" />
   </div>

Volvemos a correr los tests. Ahora los test pasan.

   <div align="center">
      <img src="https://i.postimg.cc/J7xTvP5w/AC9-2-13.png" alt="AC.2.13" width="900" />
   </div>

#### Paso 3 (Refactor)

El código quedó un poco más ordenado; `UserManager` no depende directamente de la estructura interna de almacenamiento.


#### Iteración 6: Introducir un “Spy” de notificaciones (Envío de correo)

Finalmente, agregaremos una funcionalidad que, cada vez que se agrega un usuario, se envíe un correo de bienvenida. Para probar este envío de correo sin mandar correos reales, usaremos un **Spy** o **Mock** que verifique que se llamó al método `send_welcome_email` con los parámetros correctos.

#### Paso 1 (Red): Prueba

```python
from unittest.mock import MagicMock

def test_envio_correo_bienvenida_al_agregar_usuario():
    # Arrange
    mock_email_service = MagicMock()
    manager = UserManager(email_service=mock_email_service)
    username = "nuevoUsuario"
    password = "NuevaPass123!"

    # Act
    manager.add_user(username, password)

    # Assert
    mock_email_service.send_welcome_email.assert_called_once_with(username)
```

   <div align="center">
      <img src="https://i.postimg.cc/4d79P4PN/AC9-3-1.png" alt="AC.3.1" width="550" />
   </div>

Esta prueba fallará al inicio porque `UserManager` aún no llama a ningún `send_welcome_email`.

   <div align="center">
      <img src="https://i.postimg.cc/8kvvr5sZ/AC9-3-2.png" alt="AC.3.2" width="900" />
   </div>

#### Paso 2 (Green): Implementamos la llamada al servicio de correo

Modificamos `UserManager`:

```python
class UserManager:
    def __init__(self, hash_service=None, repo=None, email_service=None):
        self.hash_service = hash_service or self._default_hash_service()
        self.repo = repo or self._default_repo()
        self.email_service = email_service  # <--- nuevo

    # ... resto de métodos ...

    def add_user(self, username, password):
	    if self.user_exists(username):
		    raise UserAlreadyExistsError(f"El usuario '{username}' ya existe. ")
        hashed = self.hash_service.hash(password)
        self.repo.save_user(username, hashed)
        if self.email_service:
            self.email_service.send_welcome_email(username)
```

   <div align="center">
      <img src="https://i.postimg.cc/QCcWL6v2/AC9-3-3.png" alt="AC.3.3" width="550" />
   </div>

Ejecutamos de nuevo `pytest`. Ahora la prueba debe pasar, ya que llamamos al `email_service`.

   <div align="center">
      <img src="https://i.postimg.cc/63kGmsbV/AC9-3-4.png" alt="AC.3.4" width="900" />
   </div>

#### Paso 3 (Refactor)

Podríamos refactorizar lo que queramos, pero la lógica principal es clara: si se inyecta `email_service`, se usa; si no, no se hace nada especial.

---

