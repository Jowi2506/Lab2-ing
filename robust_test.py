from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuración inicial
driver = webdriver.Chrome()

def ejecutar_pruebas_robustas():
    try:
        print("Ejecutando Caso 1 con esperas explícitas...")
        driver.get("https://saucedemo.com")
        
        # Esperar hasta que el campo de usuario sea visible
        wait = WebDriverWait(driver, 10)
        user_input = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
        user_input.send_keys("standard_user")
        
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        
        # Esperar hasta que el botón sea clicable
        login_btn = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
        login_btn.click()
        
        # Esperar a que la URL cambie
        wait.until(EC.url_contains("inventory.html"))
        print("✅ Caso 1 completado con éxito (Robust).")
        
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    ejecutar_pruebas_robustas()
