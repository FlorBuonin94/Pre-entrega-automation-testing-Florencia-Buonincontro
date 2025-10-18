from selenium import webdriver
from selenium.webdriver.common.by import By        #una parte del módulo que me permite hacer la selección de lo que quiero(ID, CLASS)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def setup_driver():
    options = Options()
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)                       #Espera implícita profesional

    return driver       #probar la ejecución de este return

def test_login_saucedemo():
    driver = setup_driver()
    driver.implicitly_wait(5)

    try:
        #1) Abrimos la página de inicio de sersión
        driver.get('https://saucedemo.com')

        #2) Esperamos a que se cargue el formulario
        WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.ID, "user-name")))

        #) Verificar título de sección página de login "Swag Labs"
        titulo_login = driver.find_element(By.CLASS_NAME, 'login_logo').text
        assert titulo_login == "Swag Labs"
        print(f'Título de login OK. {titulo_login}')
        print('----------------')

        #) Ingresar credenciales
        driver.find_element(By.ID, 'user-name').send_keys("standard_user")
        driver.find_element(By.ID, 'password').send_keys('secret_sauce')

        #) Hacemos clic en el botón de login
        driver.find_element(By.ID,'login-button').click()    

        WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
        print("¡Login exitoso!")
        print('----------------')

        #) Validar que estamos en inventario
        assert '/inventory.html' in driver.current_url
        print('Test de validación OK')
        print('----------------')

        #) Verificar título de sección de página de inicio "Products"
        titulo_inicio = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container span.title').text
        assert titulo_inicio == 'Products'
        print(f'Título de inicio OK. {titulo_inicio}')
        print('----------------')

        #) Contar productos visibles
        productos = driver.find_elements(By.CLASS_NAME, 'inventory_item')    #Guardo en una lista todos los elementos de la página
        print(f'Se encontraron {len(productos)} productos.')
        print('----------------')

        #) Añadir el primer producto al carrito
        productos[0].find_element(By.TAG_NAME, 'button').click()

        #) Mostrar nombre y precio del primer producto
        nombre = productos[0].find_element(By.CLASS_NAME, 'inventory_item_name').text
        precio = productos[0].find_element(By.CLASS_NAME, 'inventory_item_price').text
        print(f'Primer producto: {nombre} - Precio: {precio}')
        print('----------------')

        #) Confirmar que el badge del carrito muestra 1
        badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text  #me importa el texto
        assert badge == '1'
        print(f'Carrito OK {badge}')
        print('----------------')

        #) Ingresamos al carrito
        driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

        #) Verificamos que el producto añadido esté en la lista
        producto_en_carrito = driver.find_element(By.CLASS_NAME, 'inventory_item_name').text
        assert producto_en_carrito == nombre
        print(f'Carrito OK {producto_en_carrito}')
        print('----------------')

        print(f'Test Ok')
        print('----------------')

    finally:
        driver.quit()

if __name__ == "__main__":
    test_login_saucedemo()