# # original File
#
# import re
# import time
#
# from selenium.common import NoSuchElementException
# from selenium.webdriver import ActionChains, Keys
#
# from Logger import BaseClass
# from homePage import HomePage1
#
#
# class TestTwo(BaseClass):
#
#     def test_VendorR(self):
#         time.sleep(5)
#
#
#         # customer login page
#         homepage = HomePage1(self.driver)
#         # homepage.getEmail().send_keys("john.doe@hypermatica.com.dev3")
#         username = "john.doe@hypermatica.com.dev3"  # Change this for testing
#         # Regular expression for email validation
#         email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
#
#         if re.match(email_regex, username):
#             homepage.getEmail().send_keys(username)
#             print("Entered email:", username)
#         else:
#             print("Incorrect username")
#
#         # homepage.getPassword().send_keys("Test@1234")
#         password = "Test@1234"
#         password_regex = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
#         if re.match(password_regex, password):
#             homepage.getPassword().send_keys(password)
#             print("Valid password entered")
#         else:
#             print("Invalid password! (Must be at least 8 characters, include letters, numbers, and a special character)")
#
#         homepage.getCheckBox().click()
#
#         try:
#             sign_in_button = homepage.getSignIn()  # Using the method from homePage.pygibe
#             sign_in_button.click()
#             time.sleep(3)  # Wait for any response
#             print("Sign-in button clicked successfully!")
#         except NoSuchElementException:
#             print("Sign-in button not found!")
#         print("Sign in successfully")
#         time.sleep(3)
#
#         # vendor request page
#
#         actions = ActionChains(self.driver)
#
#         # Test Data
#         name = "jhon"
#         vendor_type = "Some Vendor Type"
#         business_case = "xyz"
#         first_name = "brian"
#         last_name = "lara"
#         email2 = "Hello@gmail.com"
#         phone = "7218296837"
#
#         # Validation regex
#         email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
#         phone_regex = r"^\d{10}$"
#         name_regex = r"^[a-zA-Z]+$"
#
#         # Click and scroll
#         homepage.getclick().click()
#         actions.send_keys(Keys.PAGE_DOWN).perform()
#
#         # Validate and enter Name
#         if re.match(name_regex, name):
#             homepage.getName().send_keys(name)
#             print("You Entered Correct Vendor Name")
#         else:
#             print("Invalid Name Format!")
#
#         # Click Vendor Type
#         homepage.getvendertype().click()
#         homepage.getvendertypeselect().click()
#
#         time.sleep(2)
#
#         # Enter Business Case
#         homepage.getBusinessCase().send_keys(business_case)
#
#         # Validate and enter First Name
#         if re.match(name_regex, first_name):
#             homepage.getFirstName().send_keys(first_name)
#
#         else:
#             print("Invalid First Name Format!")
#
#         time.sleep(2)
#
#         # Validate and enter Last Name
#         if re.match(name_regex, last_name):
#             homepage.getLastName().send_keys(last_name)
#         else:
#             print("Invalid Last Name Format!")
#
#         # Validate and enter Email
#         if re.match(email_regex, email2):
#             homepage.getEmail2().send_keys(email2)
#             print("Correct Email")
#         else:
#             print("Invalid Email Format!")
#
#         time.sleep(2)
#
#         # Validate and enter Phone Number
#         if re.match(phone_regex, phone):
#             homepage.getPhone().send_keys(phone)
#             print("Correct Phone Number")
#         else:
#             print("Invalid Phone Number! Must be 10 digits.")
#
#         # Click Next
#         homepage.getNext().click()
#         time.sleep(2)
#
# time.sleep(10)


#


















#
######For testing
import re
import time

import traceback
import pytest
from selenium.common import NoSuchElementException, WebDriverException, TimeoutException
from selenium.webdriver import ActionChains, Keys


import homePage
from Logger import BaseClass
from homePage import HomePage1


class TestTwo(BaseClass):
    def test_VendorR(self):
        try:
            log = self.getLogger()
            log.info("========== TEST STARTED ==========")

            # Initialize page objects
            homepage = HomePage1(self.driver)


            # Execute test sections with safety wrappers
            self._execute_section("Customer Login", self._customer_login, homepage)
            self._execute_section("Vendor Request", self._vendor_request, homepage)

            log.info("========== TEST COMPLETED SUCCESSFULLY ==========")



        except BaseException as e:  # Catches ALL exceptions including KeyboardInterrupt
            self._handle_critical_failure(e)


            self._handle_critical_failure(e)

            raise  # Re-raise to ensure pytest marks test as failed

        finally:
            print("\n" + "=" * 60)
            print("Test execution reached completion point")
            print("=" * 60 + "\n")
            time.sleep(2)

    def _customer_login(self, homepage):
        """All customer login steps with validations"""
        print("\nStarting Customer Login...")


        # Test data
        credentials = {
            'username': "john.doe@hypermatica.com.dev3",
            'password': "Test@1234"
        }

        # Email entry
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", credentials['username']):
            raise ValueError("Invalid email format")
        else:
            homepage.getEmail().send_keys(credentials['username'])
            print("Entered email:", credentials['username'])


        # Password entry
        if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", credentials['password']):
            raise ValueError("Invalid password format")
        else:
            homepage.getPassword().send_keys(credentials['password'])
            print("Valid password entered")

        # Checkbox and submit
        homepage.getCheckBox().click()
        # homepage.getSignIn().click()
        # time.sleep(3)
        # print("Sign-in button clicked successfully!")
        # print("Sign in successfully")
        #
        try:
            homepage.getSignIn().click()
            print("Sign-in button clicked successfully!")
            print("Sign-in Successfully")
        except AttributeError:
            print("Sign in Failed")
            raise NoSuchElementException("Sign-in button was not found")




# New Vendor Request
    def _vendor_request(self, homepage):
        """All vendor request steps with validations"""
        print("\nStarting Vendor Request...")

        # Test data
        vendor_data = {
            'name': "jhon",
            'business_case': "xyz",
            'first_name': "brian",
            'last_name': "lara",
            'email2': "Hello@gmail.com",
            'phone': "7218296837"
        }

        actions = ActionChains(self.driver)
        homepage.getclick().click()
        actions.send_keys(Keys.PAGE_DOWN).perform()

        # Validate and enter all fields
        if not re.match(r"^[a-zA-Z]+$", vendor_data['name']):
            raise ValueError("Invalid Name Format!")
        else:
            homepage.getName().send_keys(vendor_data['name'])
            print("You Entered Correct Vendor Name")
        time.sleep(3)
        homepage.getvendertype().click()
        homepage.getvendertypeselect().click()
        time.sleep(2)

        homepage.getBusinessCase().send_keys(vendor_data['business_case'])

        if not re.match(r"^[a-zA-Z]+$", vendor_data['first_name']):
            raise ValueError("Invalid First Name Format!")
        else:
            homepage.getFirstName().send_keys(vendor_data['first_name'])

        time.sleep(3)

        if not re.match(r"^[a-zA-Z]+$", vendor_data['last_name']):
            raise ValueError("Invalid Last Name Format!")
        else:
            homepage.getLastName().send_keys(vendor_data['last_name'])

        time.sleep(3)

        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", vendor_data['email2']):
            raise ValueError("Invalid Email Format!")
        else:
            homepage.getEmail2().send_keys(vendor_data['email2'])
            print("Correct Email")

        time.sleep(3)

        if not re.match(r"^\d{10}$", vendor_data['phone']):
            raise ValueError("Invalid Phone Number! Must be 10 digits.")

        else:
            homepage.getPhone().send_keys(vendor_data['phone'])
            print("Correct Phone Number")

        time.sleep(3)

        homepage.getNext().click()
        time.sleep(2)
        print("Vendor request submitted successfully")

    def _execute_section(self, section_name, section_function, *args):
        """Wrapper to execute each test section with error handling"""
        try:
            section_function(*args)
        except Exception as e:
            print(f"\ncode fat gaya hai - {section_name} failed!")
            print(f"Error Type: {type(e).__name__}")
            print(f"Error Message: {str(e)}")
            print("Stack Trace:")
            traceback.print_exc()
            pytest.fail(f"{section_name} failed: {str(e)}", pytrace=False)

    def _handle_critical_failure(self, exception):
        """Handle catastrophic failures"""
        print("\ncode fat gaya hai - CRITICAL TEST FAILURE!")
        print(f"Critical Error Type: {type(exception).__name__}")
        print(f"Critical Error Message: {str(exception)}")
        print("Full Stack Trace:")
        traceback.print_exc()


