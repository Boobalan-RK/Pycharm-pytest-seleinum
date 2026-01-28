import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.guvi.in/")
driver.maximize_window()

time.sleep(8)

# 🔹 Function to hide SalesIQ chat (iframe + wrapper)
def hide_chat():
    driver.execute_script("""
    var iframe = document.getElementById('siq_chatwindow');
    if (iframe) {
        iframe.style.display = 'none';
    }
    var wrap = document.getElementById('zsiq_chat_wrap');
    if (wrap) {
        wrap.style.display = 'none';
    }
    """)

# Hide chat on home page
hide_chat()
time.sleep(2)

# Click Login (home page)
driver.find_element(By.ID, "login-btn").click()

time.sleep(8)
print("Current URL:", driver.current_url)

# Hide chat again on sign-in page
hide_chat()
time.sleep(2)

# Enter credentials
driver.find_element(By.ID, "email").send_keys("Boobalanrk211700051@gmail.com")
driver.find_element(By.ID, "password").send_keys("ShivRaji@2101")

# Hide chat before final submit
hide_chat()
time.sleep(1)

# Click Login (submit)
driver.find_element(By.ID, "login-btn").click()

time.sleep(5)
