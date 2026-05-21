from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Chrome setup
options = Options()
options.add_argument("--start-maximized")

# Launch browser
driver = webdriver.Chrome(options=options)

# Open Amazon
driver.get("https://www.amazon.in")

time.sleep(3)

# Find search box
search_box = driver.find_element(By.ID, "twotabsearchtextbox")

# Search product
search_box.send_keys("laptop")
search_box.send_keys(Keys.RETURN)

time.sleep(5)

# Get product titles
titles = driver.find_elements(By.CSS_SELECTOR, "h2 span")

# Get prices
prices = driver.find_elements(By.CLASS_NAME, "a-price-whole")

print("\n--- AMAZON PRODUCT DATA ---\n")

# Print first 5 products
for i in range(5):
    try:
        title = titles[i].text
        price = prices[i].text

        print(f"{i+1}. Product: {title}")
        print(f"   Price: ₹{price}\n")

    except:
        pass

# Close browser
driver.quit()