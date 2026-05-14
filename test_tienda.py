from login_page import LoginPage
from selenium.webdriver.common.by import By

def test_login_exitoso(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url

def test_agregar_carrito(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    
    boton_agregar = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    boton_agregar.click()
    
    badge_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert badge_carrito == "1"

def test_login_fallido(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")
    error = login_page.get_error_message()
    assert "Sorry, this user has been locked out" in error
