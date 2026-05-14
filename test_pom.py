from selenium import webdriver
from login_page import LoginPage

def ejecutar_prueba_pom():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    try:
        print("Ejecutando prueba POM...")
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        assert "inventory.html" in driver.current_url
        print("✅ Prueba POM completada con éxito.")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    ejecutar_prueba_pom()
