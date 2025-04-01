#
###original
# import pytest
#
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# chromeoptions = Options()
# chromeoptions.headless = True
# chromeoptions.add_argument("--headless")
# chromeoptions.add_argument("--no-sandbox")
# chromeoptions.add_argument("--disable-dev-shm-usage")
# chromeoptions.add_argument("--disable-gpu")
#
# driver = webdriver.Chrome( options= chromeoptions)
#
# @pytest.fixture(scope="class")
# def setup(request):
#     driver =webdriver.Chrome()
#     driver.get("https://venlink--dev3.sandbox.my.site.com/customer/login")
#     print("Browser successfully launched")
#     print("Current URL :",driver.current_url)
#     driver.maximize_window()
#     driver.implicitly_wait(5)
#     request.cls.driver = driver
#     yield driver
#     driver.quit()












####current Working File
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import os
#
#
# @pytest.fixture(scope="class")
# def setup(request):
#     chromeoptions = Options()
#     chromeoptions.add_argument("--headless")  # Run in headless mode
#     chromeoptions.add_argument("--no-sandbox")
#     chromeoptions.add_argument("--disable-dev-shm-usage")
#     chromeoptions.add_argument("--disable-gpu")
#
#     # Set a unique user data directory to prevent conflicts
#     user_data_dir = f"/tmp/chrome-user-data-{os.getpid()}"
#     chromeoptions.add_argument(f"--user-data-dir={user_data_dir}")
#
#     driver = webdriver.Chrome(options=chromeoptions)
#     driver.get("https://venlink--dev3.sandbox.my.site.com/customer/login")
#
#     print("Browser successfully launched")
#     print("Current URL:", driver.current_url)
#
#     driver.maximize_window()
#     driver.implicitly_wait(5)
#
#     request.cls.driver = driver
#     yield driver
#     driver.quit()





















######For testing
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

@pytest.fixture(scope="class")
def setup(request):
    chromeoptions = Options()
    chromeoptions.add_argument("--headless")
    chromeoptions.add_argument("--no-sandbox")
    chromeoptions.add_argument("--disable-dev-shm-usage")
    chromeoptions.add_argument("--disable-gpu")

    # Set unique user data directory
    user_data_dir = f"/tmp/chrome-user-data-{os.getpid()}"
    chromeoptions.add_argument(f"--user-data-dir={user_data_dir}")

    driver = webdriver.Chrome(options=chromeoptions)
    driver.get("https://venlink--dev3.sandbox.my.site.com/customer/login")
    print("Browser successfully launched")
    print("Current URL:", driver.current_url)

    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield driver
    driver.quit()