# Pre-entrega-automation-testing-Florencia-Buonincontro

Este proyecto implementa una automatización de pruebas para el sitio SauceDemo, utilizando Selenium WebDriver y Python.

🎯 **Propósito del Proyecto**
El objetivo es automatizar los siguientes flujos en la aplicación SauceDemo:

* Login con credenciales válidas e inválidas
* Verificación del catálogo de productos
* Interacción con el carrito de compras (añadir productos y verificar su contenido)
* Cierre de sesión

🛠️ **Tecnologías Utilizadas**
* Python: Lenguaje de programación principal
* Pytest: Framework de testing para estructurar y ejecutar pruebas
* Selenium WebDriver: Para la automatización de la interfaz web
* Git/GitHub: Para control de versiones y compartir el código

⚙️ **Instalación de Dependencias**
* Asegúrate de tener Python 3.7 o superior instalado.

Instala las dependencias necesarias:
pip install selenium pytest pytest-html

* Descarga el WebDriver correspondiente a tu navegador:

ChromeDriver

* Asegúrate de que el WebDriver esté en tu PATH o especifica su ubicación en el código.

▶️ **Ejecución de las Pruebas Para ejecutar todas las pruebas: python3 -m pytest pre_entrega_modelo/test_saucedemo.py -v**

Para generar un reporte HTML: python3 -m pytest pre_entrega_final/test_saucedemo.py -v --html=reporte.html

✅ **Funcionalidades Implementadas**

Automatización de Login Caso de éxito con credenciales válidas
Caso de fallo con credenciales inválidas

Verificación del Catálogo Comprobación del título de la página
Verificación de presencia de productos

Interacción con el Carrito Añadir producto al carrito
Verificar que el contador se incremente

Navegar al carrito

Comprobar que el producto añadido aparezca correctamente

Cierre de Sesión Verificar que el usuario pueda cerrar sesión correctamente
✨ Características Adicionales Capturas de pantalla automáticas: Se toman cuando un test falla.
