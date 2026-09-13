import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def setup():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Modo sin interfaz gráfica para ejecuciones CI/CD
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_tc001_login_exitoso(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    assert "inventory.html" in driver.current_url
    assert driver.find_element(By.CLASS_NAME, "title").text == "Products"

def test_tc004_flujo_checkout_completo(setup):
    driver = setup
    # 1. Login
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # 2. Agregar ítem al carrito
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    # 3. Checkout Step 1
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Juan")
    driver.find_element(By.ID, "last-name").send_keys("Hernandez")
    driver.find_element(By.ID, "postal-code").send_keys("49000")
    driver.find_element(By.ID, "continue").click()
    
    # 4. Checkout Step 2 & Finish
    driver.find_element(By.ID, "finish").click()
    
    header_text = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert header_text == "Thank you for your order!"
