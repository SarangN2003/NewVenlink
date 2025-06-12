
#######################Final Screenshots Conftest.py
# import pytest
# import boto3
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import os
# import datetime
# from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
# from PIL import Image
# from fpdf import FPDF
# import glob
#
# # AWS SNS Configuration
# SNS_TOPIC_ARN = "arn:aws:sns:eu-north-1:203918861989:Demo"
# sns_client = boto3.client("sns", region_name="eu-north-1")
#
# # Screenshot directory setup
# SCREENSHOT_DIR = "screenshots"
# PDF_REPORT = "test_execution_report.pdf"
# if not os.path.exists(SCREENSHOT_DIR):
#     os.makedirs(SCREENSHOT_DIR)
#
# # Counter for sequential numbering
# screenshot_counter = 1
#
#
# class ScreenshotListener(AbstractEventListener):
#     """Listener to take screenshots on various actions with sequential numbering"""
#
#     def after_click(self, element, driver):
#         self._take_screenshot(driver, "click")
#
#     def after_change_value_of(self, element, driver):
#         self._take_screenshot(driver, "change_value")
#
#     def after_send_keys(self, element, driver):
#         self._take_screenshot(driver, "send_keys")
#
#     def after_navigate_to(self, url, driver):
#         self._take_screenshot(driver, "navigate")
#
#     def _take_screenshot(self, driver, action):
#         """Helper method to take screenshots with sequential numbering"""
#         global screenshot_counter
#         timestamp = datetime.datetime.now().strftime("%H%M%S_%f")
#         filename = f"{SCREENSHOT_DIR}/{screenshot_counter:03d}_{action}_{timestamp}.png"
#         driver.save_screenshot(filename)
#         print(f"Screenshot saved: {filename}")
#         screenshot_counter += 1
#
#
# def create_pdf_report():
#     """Create a PDF report with all screenshots in sequence and save it in the screenshots folder"""
#     print("\nCreating PDF report...")
#     pdf = FPDF()
#     pdf.set_auto_page_break(auto=True, margin=15)
#
#     # Get all screenshots sorted by their sequence number
#     screenshot_files = sorted(glob.glob(f"{SCREENSHOT_DIR}/*.png"))
#
#     if not screenshot_files:
#         print("No screenshots found to include in PDF")
#         return None
#
#     # Define PDF path inside the screenshots folder with the new name
#     pdf_path = os.path.join(SCREENSHOT_DIR, "screenshots.pdf")
#
#     for screenshot in screenshot_files:
#         # Add a new page for each screenshot
#         pdf.add_page()
#
#         # Extract action name from filename for the title
#         action = os.path.basename(screenshot).split('_')[1].capitalize()
#         step_number = os.path.basename(screenshot).split('_')[0]
#
#         # Add title
#         pdf.set_font("Arial", 'B', 12)
#         pdf.cell(0, 10, f"Step {step_number}: {action}", 0, 1, 'C')
#         pdf.ln(5)
#
#         # Add the screenshot
#         try:
#             with Image.open(screenshot) as img:
#                 width, height = img.size
#
#             max_width = 180  # mm
#             scale_factor = max_width / (width / 3.78)
#             new_width = max_width
#             new_height = (height / 3.78) * scale_factor
#
#             pdf.image(screenshot, x=(210 - new_width) / 2, w=new_width, h=new_height)
#             pdf.ln(10)
#
#             pdf.set_font("Arial", 'I', 8)
#             timestamp = ' '.join(os.path.basename(screenshot).split('_')[2:]).replace('.png', '')
#             pdf.cell(0, 5, f"Timestamp: {timestamp}", 0, 1, 'C')
#
#         except Exception as e:
#             print(f"Failed to add {screenshot} to PDF: {str(e)}")
#
#     # Save the PDF in the screenshots folder with the new name
#     pdf.output(pdf_path)
#     print(f"PDF report created: {pdf_path}")
#     return pdf_path
#
#
# def send_sns_notification(status, report_path=None):
#     """Send SNS notification with both report links"""
#     try:
#         s3 = boto3.client("s3", region_name="eu-north-1")
#
#         # Generate presigned URLs for both reports
#         report_url = s3.generate_presigned_url(
#             "get_object",
#             Params={"Bucket": "venlinkfargatereport", "Key": "reports/report.pdf"},
#             ExpiresIn=3600
#         )
#
#         screenshots_url = s3.generate_presigned_url(
#             "get_object",
#             Params={"Bucket": "venlinkfargatereport", "Key": "reports/screenshots.pdf"},
#             ExpiresIn=3600
#         )
#
#         if status == "success":
#             message = (
#                 "✅ Test script executed successfully!\n\n"
#                 "📊 Test Report:\n"
#                 f"{report_url}\n\n"
#                 "📸 Screenshots Report:\n"
#                 f"{screenshots_url}"
#             )
#             subject = "✅ Script Run Successfully"
#         else:
#             message = (
#                 "❌ Test script execution failed!\n\n"
#                 "📊 Test Report:\n"
#                 f"{report_url}\n\n"
#                 "📸 Screenshots Report:\n"
#                 f"{screenshots_url}"
#             )
#             subject = "❌ Script Failed"
#
#         response = sns_client.publish(
#             TopicArn=SNS_TOPIC_ARN,
#             Message=message,
#             Subject=subject
#         )
#         print("Notification sent with both report links")
#
#     except Exception as e:
#         print("Failed to send SNS notification:", str(e))
#
#
# @pytest.fixture(scope="class")
# def setup(request):
#     global screenshot_counter
#     screenshot_counter = 1  # Reset counter for each test class
#
#     chromeoptions = Options()
#     chromeoptions.add_argument("--headless")
#     chromeoptions.add_argument("--no-sandbox")
#     chromeoptions.add_argument("--disable-dev-shm-usage")
#     chromeoptions.add_argument("--disable-gpu")
#
#     # Set unique user data directory
#     user_data_dir = f"/tmp/chrome-user-data-{os.getpid()}"
#     chromeoptions.add_argument(f"--user-data-dir={user_data_dir}")
#
#     # Create regular driver
#     driver = webdriver.Chrome(options=chromeoptions)
#
#     # Wrap the driver with event listener for screenshots
#     event_driver = EventFiringWebDriver(driver, ScreenshotListener())
#
#     event_driver.get("https://venlink--dev3.sandbox.my.site.com/customer/login")
#     print("Browser successfully launched")
#     print("Current URL:", event_driver.current_url)
#
#     event_driver.maximize_window()
#     event_driver.implicitly_wait(5)
#
#     # Take initial screenshot
#     timestamp = datetime.datetime.now().strftime("%H%M%S_%f")
#     event_driver.save_screenshot(f"{SCREENSHOT_DIR}/{screenshot_counter:03d}_initial_{timestamp}.png")
#     screenshot_counter += 1
#
#     request.cls.driver = event_driver
#     yield event_driver
#     event_driver.quit()
#
#
# @pytest.hookimpl(tryfirst=True)
# def pytest_sessionfinish(session, exitstatus):
#     """Send notification after all tests complete"""
#     print("\nAll tests completed. Determining status...")
#
#     # Create PDF report
#     report_path = create_pdf_report()
#
#     # Send notification with report link
#     if exitstatus == 0:  # success
#         send_sns_notification("success", report_path)
#     else:  # failure
#         send_sns_notification("failure", report_path)
#
#     # Clean up screenshots (optional)
#     for file in glob.glob(f"{SCREENSHOT_DIR}/*.png"):
#         try:
#             os.remove(file)
#         except Exception as e:
#             print(f"Failed to delete {file}: {str(e)}")




##############
import pytest
import boto3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import datetime
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from PIL import Image
from fpdf import FPDF
import glob

# AWS SNS Configuration
SNS_TOPIC_ARN = "arn:aws:sns:eu-north-1:203918861989:Demo"
sns_client = boto3.client("sns", region_name="eu-north-1")

# Screenshot directory setup
SCREENSHOT_DIR = "screenshots"
PDF_REPORT = "test_execution_report.pdf"
if not os.path.exists(SCREENSHOT_DIR):
    os.makedirs(SCREENSHOT_DIR)

# Counter for sequential numbering
screenshot_counter = 1


class ScreenshotListener(AbstractEventListener):
    """Listener to take screenshots on various actions with sequential numbering"""

    def after_click(self, element, driver):
        self._take_screenshot(driver, "click")

    def after_change_value_of(self, element, driver):
        self._take_screenshot(driver, "change_value")

    def after_send_keys(self, element, driver):
        self._take_screenshot(driver, "send_keys")

    def after_navigate_to(self, url, driver):
        self._take_screenshot(driver, "navigate")

    def _take_screenshot(self, driver, action):
        """Helper method to take screenshots with sequential numbering"""
        global screenshot_counter
        timestamp = datetime.datetime.now().strftime("%H%M%S_%f")
        filename = f"{SCREENSHOT_DIR}/{screenshot_counter:03d}_{action}_{timestamp}.png"
        driver.save_screenshot(filename)
        print(f"Screenshot saved: {filename}")
        screenshot_counter += 1


def create_pdf_report():
    """Create a PDF report with all screenshots in sequence and save it in the screenshots folder"""
    print("\nCreating PDF report...")
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Get all screenshots sorted by their sequence number
    screenshot_files = sorted(glob.glob(f"{SCREENSHOT_DIR}/*.png"))

    if not screenshot_files:
        print("No screenshots found to include in PDF")
        return None

    # Define PDF path inside the screenshots folder with the new name
    pdf_path = os.path.join(SCREENSHOT_DIR, "screenshots.pdf")

    for screenshot in screenshot_files:
        # Add a new page for each screenshot
        pdf.add_page()

        # Extract action name from filename for the title
        action = os.path.basename(screenshot).split('_')[1].capitalize()
        step_number = os.path.basename(screenshot).split('_')[0]

        # Add title
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, f"Step {step_number}: {action}", 0, 1, 'C')
        pdf.ln(5)

        # Add the screenshot
        try:
            with Image.open(screenshot) as img:
                width, height = img.size

            max_width = 180  # mm
            scale_factor = max_width / (width / 3.78)
            new_width = max_width
            new_height = (height / 3.78) * scale_factor

            pdf.image(screenshot, x=(210 - new_width) / 2, w=new_width, h=new_height)
            pdf.ln(10)

            pdf.set_font("Arial", 'I', 8)
            timestamp = ' '.join(os.path.basename(screenshot).split('_')[2:]).replace('.png', '')
            pdf.cell(0, 5, f"Timestamp: {timestamp}", 0, 1, 'C')

        except Exception as e:
            print(f"Failed to add {screenshot} to PDF: {str(e)}")

    # Save the PDF in the screenshots folder with the new name
    pdf.output(pdf_path)
    print(f"PDF report created: {pdf_path}")
    return pdf_path


def send_sns_notification(status, report_path=None):
    """Send SNS notification with both report links"""
    try:
        s3 = boto3.client("s3", region_name="eu-north-1")

        # Generate presigned URLs for both reports
        report_url = s3.generate_presigned_url(
            "get_object",
            Params={"Bucket": "venlinkfargatereport", "Key": "reports/report.pdf"},
            ExpiresIn=3600
        )

        screenshots_url = s3.generate_presigned_url(
            "get_object",
            Params={"Bucket": "venlinkfargatereport", "Key": "reports/screenshots.pdf"},
            ExpiresIn=3600
        )

        if status == "success":
            message = (
                "✅ Test script executed successfully!\n\n"
                "📊 Test Report:\n"
                f"{report_url}\n\n"
                "📸 Screenshots Report:\n"
                f"{screenshots_url}"
            )
            subject = "✅ Script Run Successfully"
        else:
            message = (
                "❌ Test script execution failed!\n\n"
                "📊 Test Report:\n"
                f"{report_url}\n\n"
                "📸 Screenshots Report:\n"
                f"{screenshots_url}"
            )
            subject = "❌ Script Failed"

        response = sns_client.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=message,
            Subject=subject
        )
        print("Notification sent with both report links")

    except Exception as e:
        print("Failed to send SNS notification:", str(e))


@pytest.fixture(scope="class")
def setup(request):
    global screenshot_counter
    screenshot_counter = 1  # Reset counter for each test class

    chromeoptions = Options()
    chromeoptions.add_argument("--headless")
    chromeoptions.add_argument("--no-sandbox")
    chromeoptions.add_argument("--disable-dev-shm-usage")
    chromeoptions.add_argument("--disable-gpu")

    # Set unique user data directory
    user_data_dir = f"/tmp/chrome-user-data-{os.getpid()}"
    chromeoptions.add_argument(f"--user-data-dir={user_data_dir}")

    # Create regular driver
    driver = webdriver.Chrome(options=chromeoptions)

    # Wrap the driver with event listener for screenshots
    event_driver = EventFiringWebDriver(driver, ScreenshotListener())

    event_driver.get("https://venlink--dev3.sandbox.my.site.com/customer/login")
    print("Browser successfully launched")
    print("Current URL:", event_driver.current_url)


    event_driver.maximize_window()
    event_driver.implicitly_wait(5)

    # Take initial screenshot
    timestamp = datetime.datetime.now().strftime("%H%M%S_%f")
    event_driver.save_screenshot(f"{SCREENSHOT_DIR}/{screenshot_counter:03d}_initial_{timestamp}.png")
    screenshot_counter += 1

    request.cls.driver = event_driver
    yield event_driver
    event_driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    """Send notification after all tests complete"""
    print("\nAll tests completed. Determining status...")

    # Create PDF report
    report_path = create_pdf_report()

    # Send notification with report link
    if exitstatus == 0:  # success
        send_sns_notification("success", report_path)
    else:  # failure
        send_sns_notification("failure", report_path)

    # Clean up screenshots (optional)
    for file in glob.glob(f"{SCREENSHOT_DIR}/*.png"):
        try:
            os.remove(file)
        except Exception as e:
            print(f"Failed to delete {file}: {str(e)}")

