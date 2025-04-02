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
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import os

# @pytest.fixture(scope="class")
# def setup(request):
#     chromeoptions = Options()
#     chromeoptions.add_argument("--headless")
#     chromeoptions.add_argument("--no-sandbox")
#     chromeoptions.add_argument("--disable-dev-shm-usage")
#     chromeoptions.add_argument("--disable-gpu")

#     # Set unique user data directory
#     user_data_dir = f"/tmp/chrome-user-data-{os.getpid()}"
#     chromeoptions.add_argument(f"--user-data-dir={user_data_dir}")

#     driver = webdriver.Chrome(options=chromeoptions)
#     driver.get("https://venlink--dev3.sandbox.my.site.com/customer/login")
#     print("Browser successfully launched")
#     print("Current URL:", driver.current_url)

#     driver.maximize_window()
#     driver.implicitly_wait(5)
#     request.cls.driver = driver
#     yield driver
#     driver.quit()











###Use For AWS SNS
import pytest
import boto3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

# AWS SNS Configuration
SNS_TOPIC_ARN = "arn:aws:sns:eu-north-1:203918861989:Demo"
sns_client = boto3.client("sns", region_name="eu-north-1")


def send_sns_notification():
    message = "Test execution completed successfully. Check the report for details."
    subject = "Test Execution Report"

    try:
        response = sns_client.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=message,
            Subject=subject
        )
        print("SNS Notification Sent! Message ID:", response["MessageId"])
    except Exception as e:
        print("Failed to send SNS notification:", str(e))


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


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    print("All tests completed. Sending SNS notification...")
    send_sns_notification()
