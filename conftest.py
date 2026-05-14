import pytest
from selenium import webdriver
import os

@pytest.fixture(scope="function")
def driver(request):
    # Setup for headless mode (FASE 6)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    
    # Hacer el driver disponible en el test
    request.node.driver = driver
    
    yield driver
    
    # Teardown
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # Obtener el driver de Selenium
            driver = getattr(item, "driver", None)
            if driver:
                # Tomar captura de pantalla
                screenshot_dir = "screenshots"
                if not os.path.exists(screenshot_dir):
                    os.makedirs(screenshot_dir)
                file_name = f"{screenshot_dir}/{item.name}.png"
                driver.save_screenshot(file_name)
                # Añadir al reporte HTML
                if file_name:
                    html = f'<div><img src="{file_name}" alt="screenshot" style="width:304px;height:228px;" ' \
                           'onclick="window.open(this.src)" align="right"/></div>'
                    extra.append(pytest_html.extras.html(html))
        report.extra = extra
