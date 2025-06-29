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
# import re
# import time
#
# import traceback
# import pytest
# from selenium.common import NoSuchElementException, WebDriverException, TimeoutException
# from selenium.webdriver import ActionChains, Keys
#
#
# import homePage
# from Logger import BaseClass
# from homePage import HomePage1
#
#
# class TestTwo(BaseClass):
#     def test_VendorR(self):
#
#         try:
#             log = self.getLogger()
#             log.info("========== TEST STARTED ==========")
#
#             # Initialize page objects
#             homepage = HomePage1(self.driver)
#
#
#             # Execute test sections with safety wrappers
#             self._execute_section("Customer Login", self._customer_login, homepage)
#             self._execute_section("Vendor Request", self._vendor_request, homepage)
#
#             log.info("========== TEST COMPLETED SUCCESSFULLY ==========")
#
#
#
#         except BaseException as e:  # Catches ALL exceptions including KeyboardInterrupt
#             self._handle_critical_failure(e)
#
#
#             self._handle_critical_failure(e)
#
#             raise  # Re-raise to ensure pytest marks test as failed
#
#         finally:
#             print("\n" + "=" * 60)
#             print("Test execution reached completion point")
#             print("=" * 60 + "\n")
#             time.sleep(2)
#
#     def _customer_login(self, homepage):
#         """All customer login steps with validations"""
#         print("\nStarting Customer Login...")
#
#
#         # Test data
#         credentials = {
#             'username': "sagar.hingane+2@hypermatica.com",
#             'password': "Test@12345@"
#         }
#
#         # Email entry
#         if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", credentials['username']):
#             raise ValueError(f"Invalid email format: {credentials['username']}")
#         else:
#             homepage.getEmail().send_keys(credentials['username'])
#             print("Entered email:", credentials['username'])
#
#
#         # Password entry
#         if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", credentials['password']):
#             raise ValueError("Invalid password format")
#         else:
#             homepage.getPassword().send_keys(credentials['password'])
#             print("Valid password entered")
#
#         # Checkbox and submit
#         try:
#             homepage.getCheckBox().click()
#             print("CheckeBox Click Successfully!")
#         except AttributeError:
#             print("CheckBox Not Clicked")
#             raise NoSuchElementException("CheckBox was not found")
#
#
#
#         try:
#             homepage.getSignIn().click()
#             print("Sign-in button clicked successfully!")
#             print("Sign-in Successfully")
#         except AttributeError:
#             print("Sign in Failed")
#             raise NoSuchElementException("Sign-in button was not found")
#
#
#
#
# # New Vendor Request
#     def _vendor_request(self, homepage):
#         """All vendor request steps with validations"""
#         print("\nStarting Vendor Request...")
#
#         # Test data
#         vendor_data = {
#             'name': "jhon",
#             'business_case': "xyz",
#             'first_name': "brian",
#             'last_name': "lara",
#             'email2': "Hello@gmail.com",
#             'phone': "7218296837"
#         }
#
#         actions = ActionChains(self.driver)
#         homepage.getclick().click()
#         actions.send_keys(Keys.PAGE_DOWN).perform()
#
#         # Validate and enter all fields
#         if not re.match(r"^[a-zA-Z]+$", vendor_data['name']):
#             raise ValueError("Invalid Name Format!")
#         else:
#             homepage.getName().send_keys(vendor_data['name'])
#             print("You Entered Correct Vendor Name")
#         time.sleep(3)
#         homepage.getvendertype().click()
#         homepage.getvendertypeselect().click()
#         time.sleep(2)
#
#         homepage.getBusinessCase().send_keys(vendor_data['business_case'])
#
#         if not re.match(r"^[a-zA-Z]+$", vendor_data['first_name']):
#             raise ValueError("Invalid First Name Format!")
#         else:
#             homepage.getFirstName().send_keys(vendor_data['first_name'])
#
#         time.sleep(3)
#
#         if not re.match(r"^[a-zA-Z]+$", vendor_data['last_name']):
#             raise ValueError("Invalid Last Name Format!")
#         else:
#             homepage.getLastName().send_keys(vendor_data['last_name'])
#
#         time.sleep(3)
#
#         if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", vendor_data['email2']):
#             raise ValueError("Invalid Email Format!")
#         else:
#             homepage.getEmail2().send_keys(vendor_data['email2'])
#             print("Correct Email")
#
#         time.sleep(3)
#
#         if not re.match(r"^\d{10}$", vendor_data['phone']):
#             raise ValueError("Invalid Phone Number! Must be 10 digits.")
#
#         else:
#             homepage.getPhone().send_keys(vendor_data['phone'])
#             print("Correct Phone Number")
#
#         time.sleep(3)
#
#         homepage.getNext().click()
#         time.sleep(2)
#         print("Vendor request submitted successfully")
#
#     def _execute_section(self, section_name, section_function, *args):
#         """Wrapper to execute each test section with error handling"""
#         try:
#             section_function(*args)
#         except Exception as e:
#             print(f"\ncode fat gaya hai - {section_name} failed!")
#             print(f"Error Type: {type(e).__name__}")
#             print(f"Error Message: {str(e)}")
#             print("Stack Trace:")
#             traceback.print_exc()
#             pytest.fail(f"{section_name} failed: {str(e)}", pytrace=False)
#
#     def _handle_critical_failure(self, exception):
#         """Handle catastrophic failures"""
#         print("\ncode fat gaya hai - CRITICAL TEST FAILURE!")
#         print(f"Critical Error Type: {type(exception).__name__}")
#         print(f"Critical Error Message: {str(exception)}")
#         print("Full Stack Trace:")
#         traceback.print_exc()


#################################################for all Testcaes  but not add the code fat gaya hai#######################################################

# import rstr
# import re
# import time
# import traceback
# import pytest
# from selenium.webdriver import ActionChains, Keys
# from selenium.common.exceptions import NoSuchElementException
#
# import homePage
# from Logger import BaseClass
# from homePage import HomePage1
#
#
# class TestVendorRequest(BaseClass):
#
#     def test_valid_customer_login_and_vendor_request(self):
#
#
#         log = self.getLogger()
#         log.info("========== TEST STARTED ==========")
#
#         homepage = HomePage1(self.driver)
#
#         # Positive test data
#         username = "sagar.hingane+2@hypermatica.com"
#         password = "Test@12345@"
#         vendor_data = {
#             'name': "john",
#             'business_case': "xyz",
#             'first_name': "brian",
#             'last_name': "lara",
#             'email2': "Hello@gmail.com",
#             'phone': "7218296837"
#         }
#
#         # Customer Login
#         print("Executing customer login...")
#         self._customer_login(homepage, username, password)
#         print("Customer login successful!")
#
#         # Vendor Request
#         print("Executing vendor request...")
#         self._vendor_request(homepage, vendor_data)
#         print("Vendor request submitted successfully!")
#
#         log.info("✅ Positive test passed successfully!")
#
#     # Invalid email test cases with regex pattern generation
#     invalid_emails = [
#         rstr.xeger(r'^[a-zA-Z0-9._%+-]+[a-zA-Z0-9.-]+[a-zA-Z]{2,}$'),  # missing @
#         rstr.xeger(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+$'),  # missing TLD
#         rstr.xeger(r'^@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'),  # missing local part
#         rstr.xeger(r'^[a-zA-Z0-9._%+-]+@\.+[a-zA-Z]{2,}$')  # missing domain
#     ]
#
#     @pytest.mark.parametrize("invalid_email", invalid_emails)
#     # Update the email regex pattern in your test
#     # def test_invalid_email_format(self, invalid_email):
#     #     with pytest.raises(ValueError):
#     #         if not re.match(r"^[a-zA-Z0-9._%+-]{1,64}@[a-zA-Z0-9.-]{1,255}\.[a-zA-Z]{2,}$", invalid_email):
#     #             raise ValueError("Invalid email format")
#     def test_invalid_email_format(self, invalid_email):
#         with pytest.raises(ValueError):
#             print(f"Testing invalid email: {invalid_email}")
#             # More strict email pattern that doesn't allow consecutive dots
#             if not re.match(r"^[a-zA-Z0-9._%+-]{1,64}@(?!.*\.\.)[a-zA-Z0-9.-]{1,255}\.[a-zA-Z]{2,}$", invalid_email):
#                 raise ValueError("Invalid email format")
#
#     # Invalid password test cases with regex pattern generation
#     invalid_passwords = [
#         rstr.xeger(r'^[A-Za-z]{8,}$'),  # letters only
#         rstr.xeger(r'^\d{8,}$'),  # digits only
#         rstr.xeger(r'^[A-Za-z\d]{8,}$'),  # missing special char
#         rstr.xeger(r'^[A-Za-z@$!%*?&]{8,}$'),  # missing digit
#         rstr.xeger(r'^[\d@$!%*?&]{8,}$')  # missing letter
#     ]
#
#     @pytest.mark.parametrize("invalid_password", invalid_passwords)
#     def test_invalid_password_format(self, invalid_password):
#         with pytest.raises(ValueError):
#             print(f"Testing invalid password format: {invalid_password}")
#             if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", invalid_password):
#                 raise ValueError("Invalid password format")
#
#     # Invalid vendor name test cases
#     invalid_names = [
#         rstr.xeger(r'^\d+$'),  # numbers only
#         rstr.xeger(r'^[a-zA-Z]+\d+$'),  # letters with numbers
#         rstr.xeger(r'^[a-zA-Z]+[@#$%^&*]+$'),  # letters with special chars
#         rstr.xeger(r'^$')  # empty
#     ]
#
#     @pytest.mark.parametrize("invalid_name", invalid_names)
#     def test_invalid_vendor_name(self, invalid_name):
#         with pytest.raises(ValueError):
#             print(f"Testing invalid vendor name: {invalid_name}")
#             if not re.match(r"^[a-zA-Z]+$", invalid_name):
#                 raise ValueError("Invalid Name Format!")
#
#     # Invalid first name test cases
#     invalid_first_names = [
#         rstr.xeger(r'^\d+[a-zA-Z]+$'),  # starts with numbers
#         rstr.xeger(r'^[a-zA-Z]+\d+$'),  # ends with numbers
#         rstr.xeger(r'^[^a-zA-Z]+$'),  # no letters
#         rstr.xeger(r'^[a-zA-Z]+[^a-zA-Z0-9]+$')  # with special chars
#     ]
#
#     @pytest.mark.parametrize("invalid_first", invalid_first_names)
#     def test_invalid_first_name(self, invalid_first):
#         with pytest.raises(ValueError):
#             print(f"Testing invalid first name: {invalid_first}")
#             if not re.match(r"^[a-zA-Z]+$", invalid_first):
#                 raise ValueError("Invalid First Name Format!")
#
#     # Invalid last name test cases
#     invalid_last_names = [
#         rstr.xeger(r'^[a-zA-Z]+\d+$'),
#         rstr.xeger(r'^\d+[a-zA-Z]+$'),
#         rstr.xeger(r'^[a-zA-Z]+[@#$]+$'),
#         rstr.xeger(r'^$')
#     ]
#
#     @pytest.mark.parametrize("invalid_last", invalid_last_names)
#     def test_invalid_last_name(self, invalid_last):
#         with pytest.raises(ValueError):
#             print(f"Testing invalid last name: {invalid_last}")
#             if not re.match(r"^[a-zA-Z]+$", invalid_last):
#                 raise ValueError("Invalid Last Name Format!")
#
#     # Invalid vendor email test cases
#     invalid_vendor_emails = [
#         rstr.xeger(r'^[a-zA-Z0-9._%+-]+[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'),  # no @
#         rstr.xeger(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+$'),  # no TLD
#         rstr.xeger(r'^@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'),  # no local part
#         rstr.xeger(r'^[a-zA-Z0-9._%+-]+@\.[a-zA-Z]{2,}$')  # no domain
#     ]
#
#     @pytest.mark.parametrize("invalid_email2", invalid_vendor_emails)
#     def test_invalid_vendor_email(self, invalid_email2):
#         with pytest.raises(ValueError):
#             print(f"Testing invalid vendor email: {invalid_email2}")
#             if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", invalid_email2):
#                 raise ValueError("Invalid Email Format!")
#
#     # Invalid phone test cases (kept as you had them)
#     invalid_phones = [
#         rstr.xeger(r'^\d{1,9}$'),  # too short
#         rstr.xeger(r'^[a-zA-Z]+\d+$'),  # letters + digits
#         "",  # empty
#         rstr.xeger(r'^[\d]{9}$')  # exactly 9 digits
#     ]
#
#     @pytest.mark.parametrize("invalid_phone", invalid_phones)
#     def test_invalid_phone_number(self, invalid_phone):
#         with pytest.raises(ValueError):
#             print(f"Testing invalid phone number: {invalid_phone}")
#             if not re.match(r"^\d{10}$", invalid_phone):
#                 raise ValueError("Invalid Phone Number!")
#
#     def _customer_login(self, homepage, username, password):
#         print("\nStarting Customer Login...")
#         homepage.getEmail().send_keys(username)
#         homepage.getPassword().send_keys(password)
#
#         try:
#             homepage.getCheckBox().click()
#             print("Checkbox clicked successfully!")
#         except AttributeError:
#             raise NoSuchElementException("Checkbox was not found")
#
#         try:
#             homepage.getSignIn().click()
#             print("Sign-in clicked successfully!")
#         except AttributeError:
#             raise NoSuchElementException("Sign-in button was not found")
#
#     def _vendor_request(self, homepage, vendor_data):
#         print("\nStarting Vendor Request...")
#         actions = ActionChains(self.driver)
#         homepage.getclick().click()
#         actions.send_keys(Keys.PAGE_DOWN).perform()
#
#         print(
#             f"Entering vendor details: {vendor_data['name']}, {vendor_data['business_case']}, {vendor_data['first_name']}, {vendor_data['last_name']}, {vendor_data['email2']}, {vendor_data['phone']}")
#         homepage.getName().send_keys(vendor_data['name'])
#         homepage.getvendertype().click()
#         time.sleep(3)
#         homepage.getvendertypeselect().click()
#         time.sleep(3)
#         homepage.getBusinessCase().send_keys(vendor_data['business_case'])
#         homepage.getFirstName().send_keys(vendor_data['first_name'])
#         homepage.getLastName().send_keys(vendor_data['last_name'])
#         homepage.getEmail2().send_keys(vendor_data['email2'])
#         homepage.getPhone().send_keys(vendor_data['phone'])
#
#         homepage.getNext().click()
#         print("Vendor request submitted successfully")



#################################Testing testcases #################################

####Working Code
# import rstr
# import re
# import time
# import traceback
# import pytest
# from selenium.webdriver import ActionChains, Keys
# from selenium.common.exceptions import NoSuchElementException
#
# import homePage
# from Logger import BaseClass
# from homePage import HomePage1
#
#
# class TestVendorRequest(BaseClass):
#     def test_valid_customer_login_and_vendor_request(self):
#         try:
#             log = self.getLogger()
#             log.info("========== TEST STARTED ==========")
#
#             homepage = HomePage1(self.driver)
#
#             # Positive test data
#             username = "sagar.hingane+2@hypermatica.com"
#             password = "Test@12345@"
#             vendor_data = {
#                 'name': "john",
#                 'business_case': "xyz",
#                 'first_name': "brian",
#                 'last_name': "lara",
#                 'email2': "Hello@gmail.com",
#                 'phone': "7218296837"
#             }
#
#             # Execute test sections with safety wrappers
#             self._execute_section("Customer Login", self._customer_login, homepage, username, password)
#             self._execute_section("Vendor Request", self._vendor_request, homepage, vendor_data)
#
#             log.info("✅ Positive test passed successfully!")
#
#         except BaseException as e:  # Catches ALL exceptions including KeyboardInterrupt
#             self._handle_critical_failure(e)
#             raise  # Re-raise to ensure pytest marks test as failed
#
#         finally:
#             print("\n" + "=" * 60)
#             print("Test execution reached completion point")
#             print("=" * 60 + "\n")
#             time.sleep(2)
#
#     def _execute_section(self, section_name, section_function, *args):
#         """Wrapper to execute each test section with error handling"""
#         try:
#             section_function(*args)
#         except Exception as e:
#             print(f"\ncode fat gaya hai - {section_name} failed!")
#             print(f"Error Type: {type(e).__name__}")
#             print(f"Error Message: {str(e)}")
#             print("Stack Trace:")
#             traceback.print_exc()
#             pytest.fail(f"{section_name} failed: {str(e)}", pytrace=False)
#
#     def _handle_critical_failure(self, exception):
#         """Handle catastrophic failures"""
#         print("\ncode fat gaya hai - CRITICAL TEST FAILURE!")
#         print(f"Critical Error Type: {type(exception).__name__}")
#         print(f"Critical Error Message: {str(exception)}")
#         print("Full Stack Trace:")
#         traceback.print_exc()
#
#
#
#     ##Login Page
#     # Invalid email test cases with regex pattern generation
#     invalid_emails = [
#         rstr.xeger(r'^[a-zA-Z0-9._%+-]+[a-zA-Z0-9.-]+[a-zA-Z]{2,}$'),  # missing @
#         rstr.xeger(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+$'),  # missing TLD
#         rstr.xeger(r'^@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'),  # missing local part
#         rstr.xeger(r'^[a-zA-Z0-9._%+-]+@\.+[a-zA-Z]{2,}$')  # missing domain
#     ]
#
#     @pytest.mark.parametrize("invalid_email", invalid_emails)
#     def test_invalid_email_format(self, invalid_email):
#         with pytest.raises(ValueError):
#             print(f"Testing invalid email: {invalid_email}")
#             # More strict email pattern that doesn't allow consecutive dots
#             if not re.match(r"^[a-zA-Z0-9._%+-]{1,64}@(?!.*\.\.)[a-zA-Z0-9.-]{1,255}\.[a-zA-Z]{2,}$", invalid_email):
#                 raise ValueError("Invalid email format")
#
#     # Invalid password test cases with regex pattern generation
#     invalid_passwords = [
#         rstr.xeger(r'^[A-Za-z]{8,}$'),  # letters only
#         rstr.xeger(r'^\d{8,}$'),  # digits only
#         rstr.xeger(r'^[A-Za-z\d]{8,}$'),  # missing special char
#         rstr.xeger(r'^[A-Za-z@$!%*?&]{8,}$'),  # missing digit
#         rstr.xeger(r'^[\d@$!%*?&]{8,}$')  # missing letter
#     ]
#
#     @pytest.mark.parametrize("invalid_password", invalid_passwords)
#     def test_invalid_password_format(self, invalid_password):
#         with pytest.raises(ValueError):
#             print(f"Testing invalid password format: {invalid_password}")
#             if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", invalid_password):
#                 raise ValueError("Invalid password format")
#
#
#     ##New Vendor Create
#     # Invalid vendor name test cases
#     invalid_names = [
#         rstr.xeger(r'^\d+$'),  # numbers only
#         rstr.xeger(r'^[a-zA-Z]+\d+$'),  # letters with numbers
#         rstr.xeger(r'^[a-zA-Z]+[@#$%^&*]+$'),  # letters with special chars
#         rstr.xeger(r'^$')  # empty
#     ]
#
#     @pytest.mark.parametrize("invalid_name", invalid_names)
#     def test_invalid_vendor_name(self, invalid_name):
#         with pytest.raises(ValueError):
#             print(f"Testing invalid vendor name: {invalid_name}")
#             if not re.match(r"^[a-zA-Z]+$", invalid_name):
#                 raise ValueError("Invalid Name Format!")
#
#     # Invalid first name test cases
#     invalid_first_names = [
#         rstr.xeger(r'^\d+[a-zA-Z]+$'),  # starts with numbers
#         rstr.xeger(r'^[a-zA-Z]+\d+$'),  # ends with numbers
#         rstr.xeger(r'^[^a-zA-Z]+$'),  # no letters
#         rstr.xeger(r'^[a-zA-Z]+[^a-zA-Z0-9]+$')  # with special chars
#     ]
#
#     @pytest.mark.parametrize("invalid_first", invalid_first_names)
#     def test_invalid_first_name(self, invalid_first):
#         with pytest.raises(ValueError):
#             print(f"Testing invalid first name: {invalid_first}")
#             if not re.match(r"^[a-zA-Z]+$", invalid_first):
#                 raise ValueError("Invalid First Name Format!")
#
#     # Invalid last name test cases
#     invalid_last_names = [
#         rstr.xeger(r'^[a-zA-Z]+\d+$'),
#         rstr.xeger(r'^\d+[a-zA-Z]+$'),
#         rstr.xeger(r'^[a-zA-Z]+[@#$]+$'),
#         rstr.xeger(r'^$')
#     ]
#
#     @pytest.mark.parametrize("invalid_last", invalid_last_names)
#     def test_invalid_last_name(self, invalid_last):
#         with pytest.raises(ValueError):
#             print(f"Testing invalid last name: {invalid_last}")
#             if not re.match(r"^[a-zA-Z]+$", invalid_last):
#                 raise ValueError("Invalid Last Name Format!")
#
#     # Invalid vendor email test cases
#     invalid_vendor_emails = [
#         rstr.xeger(r'^[a-zA-Z0-9._%+-]+[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'),  # no @
#         rstr.xeger(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+$'),  # no TLD
#         rstr.xeger(r'^@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'),  # no local part
#         rstr.xeger(r'^[a-zA-Z0-9._%+-]+@\.[a-zA-Z]{2,}$')  # no domain
#     ]
#
#     @pytest.mark.parametrize("invalid_email2", invalid_vendor_emails)
#     def test_invalid_vendor_email(self, invalid_email2):
#         with pytest.raises(ValueError):
#             print(f"Testing invalid vendor email: {invalid_email2}")
#             if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", invalid_email2):
#                 raise ValueError("Invalid Email Format!")
#
#     # Invalid phone test cases (kept as you had them)
#     invalid_phones = [
#         rstr.xeger(r'^\d{1,9}$'),  # too short
#         rstr.xeger(r'^[a-zA-Z]+\d+$'),  # letters + digits
#         "",  # empty
#         rstr.xeger(r'^[\d]{9}$')  # exactly 9 digits
#     ]
#
#     @pytest.mark.parametrize("invalid_phone", invalid_phones)
#     def test_invalid_phone_number(self, invalid_phone):
#         with pytest.raises(ValueError):
#             print(f"Testing invalid phone number: {invalid_phone}")
#             if not re.match(r"^\d{10}$", invalid_phone):
#                 raise ValueError("Invalid Phone Number!")
#
#
#
#     ####LogIn Page
#     def _customer_login(self, homepage, username, password):
#         print("\nStarting Customer Login...")
#         homepage.getEmail().send_keys(username)
#         homepage.getPassword().send_keys(password)
#
#         try:
#             homepage.getCheckBox().click()
#             print("Checkbox clicked successfully!")
#         except AttributeError:
#             raise NoSuchElementException("Checkbox was not found")
#
#         try:
#             homepage.getSignIn().click()
#             print("Sign-in clicked successfully!")
#         except AttributeError:
#             raise NoSuchElementException("Sign-in button was not found")
#
#
#
#     ##New Vendor Create
#     def _vendor_request(self, homepage, vendor_data):
#         print("\nStarting Vendor Request...")
#         actions = ActionChains(self.driver)
#         homepage.getclick().click()
#         actions.send_keys(Keys.PAGE_DOWN).perform()
#
#         print(
#             f"Entering vendor details: {vendor_data['name']}, {vendor_data['business_case']}, {vendor_data['first_name']}, {vendor_data['last_name']}, {vendor_data['email2']}, {vendor_data['phone']}")
#         homepage.getName().send_keys(vendor_data['name'])
#         homepage.getvendertype().click()
#         time.sleep(3)
#         homepage.getvendertypeselect().click()
#         time.sleep(3)
#         homepage.getBusinessCase().send_keys(vendor_data['business_case'])
#         homepage.getFirstName().send_keys(vendor_data['first_name'])
#         homepage.getLastName().send_keys(vendor_data['last_name'])
#         homepage.getEmail2().send_keys(vendor_data['email2'])
#         homepage.getPhone().send_keys(vendor_data['phone'])
#
#
#         try:
#             homepage.getNext().click()
#             print("Next Button Clicked successfully")
#         except AttributeError:
#             raise NoSuchElementException("Next button was not found")
#

## ## ## Dependency checking checkbox and sign in button


### ### ###Current Working File
import rstr
import re
import time
import traceback
import pytest


from selenium.webdriver import ActionChains, Keys
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import homePage
from Logger import BaseClass
from homePage import HomePage1

from test_data import CUSTOMER_CREDENTIALS, VENDOR_DATA, ACCOUNT_INFORMATION
from customerLogin import perform_customer_login

class TestVendorRequest(BaseClass):
    # def test_valid_customer_login_and_vendor_request(self):
    def test_vendor_request(self):
        try:
            log = self.getLogger()
            log.info("========== TEST STARTED ==========")

            homepage = HomePage1(self.driver)


            self._execute_section("Customer Login", perform_customer_login,
                                  homepage,
                                  CUSTOMER_CREDENTIALS['username'],
                                  CUSTOMER_CREDENTIALS['password'],
                                  log)

            # Login and Vendor Request
            # self._execute_section("Customer Login", perform_customer_login, homepage, username, password, log)
            self._execute_section("Vendor Request", self._vendor_request, homepage, VENDOR_DATA)

            log.info("✅ Positive test passed successfully!")

        except BaseException as e:
            self._handle_critical_failure(e)
            raise

        finally:
            print("\n" + "=" * 60)
            print("Test execution reached completion point")
            print("=" * 60 + "\n")
            time.sleep(2)

    def _execute_section(self, section_name, section_function, *args):
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
        print("\ncode fat gaya hai - CRITICAL TEST FAILURE!")
        print(f"Critical Error Type: {type(exception).__name__}")
        print(f"Critical Error Message: {str(exception)}")
        print("Full Stack Trace:")
        traceback.print_exc()


    ##New Vendor Create
    # Invalid vendor name test cases
    invalid_names = [
        rstr.xeger(r'^\d+$'),  # numbers only
        rstr.xeger(r'^[a-zA-Z]+\d+$'),  # letters with numbers
        rstr.xeger(r'^[a-zA-Z]+[@#$%^&*]+$'),  # letters with special chars
        rstr.xeger(r'^$')  # empty
    ]

    @pytest.mark.parametrize("invalid_name", invalid_names)
    def test_invalid_vendor_name(self, invalid_name):
        with pytest.raises(ValueError):
            print(f"Testing invalid vendor name: {invalid_name}")
            if not re.match(r"^[a-zA-Z]+$", invalid_name):
                raise ValueError("Invalid Name Format!")

    # Invalid first name test cases
    invalid_first_names = [
        rstr.xeger(r'^\d+[a-zA-Z]+$'),  # starts with numbers
        rstr.xeger(r'^[a-zA-Z]+\d+$'),  # ends with numbers
        rstr.xeger(r'^[^a-zA-Z]+$'),  # no letters
        rstr.xeger(r'^[a-zA-Z]+[^a-zA-Z0-9]+$')  # with special chars
    ]

    @pytest.mark.parametrize("invalid_first", invalid_first_names)
    def test_invalid_first_name(self, invalid_first):
        with pytest.raises(ValueError):
            print(f"Testing invalid first name: {invalid_first}")
            if not re.match(r"^[a-zA-Z]+$", invalid_first):
                raise ValueError("Invalid First Name Format!")

    # Invalid last name test cases
    invalid_last_names = [
        rstr.xeger(r'^[a-zA-Z]+\d+$'),
        rstr.xeger(r'^\d+[a-zA-Z]+$'),
        rstr.xeger(r'^[a-zA-Z]+[@#$]+$'),
        rstr.xeger(r'^$')
    ]

    @pytest.mark.parametrize("invalid_last", invalid_last_names)
    def test_invalid_last_name(self, invalid_last):
        with pytest.raises(ValueError):
            print(f"Testing invalid last name: {invalid_last}")
            if not re.match(r"^[a-zA-Z]+$", invalid_last):
                raise ValueError("Invalid Last Name Format!")



    # Invalid vendor email test cases
    # invalid_vendor_emails = [
    #     rstr.xeger(r'^[a-zA-Z0-9._%+-]+[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'),  # no @
    #     rstr.xeger(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+$'),  # no TLD
    #     rstr.xeger(r'^@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'),  # no local part
    #     rstr.xeger(r'^[a-zA-Z0-9._%+-]+@\.[a-zA-Z]{2,}$')  # no domain
    # ]
    #
    # @pytest.mark.parametrize("invalid_email2", invalid_vendor_emails)
    # def test_invalid_vendor_email(self, invalid_email2):
    #     with pytest.raises(ValueError):
    #         print(f"Testing invalid vendor email: {invalid_email2}")
    #         if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", invalid_email2):
    #             raise ValueError("Invalid Email Format!")

    invalid_vendor_emails = [
        rstr.xeger(r'[a-zA-Z0-9._%+-]+[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'),  # missing '@'
        rstr.xeger(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+'),  # missing TLD (no .com)
        rstr.xeger(r'@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'),  # missing local part
        rstr.xeger(r'[a-zA-Z0-9._%+-]+@\.[a-zA-Z]{2,}'),  # domain starts with dot
        rstr.xeger(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{1}'),  # too short TLD
    ]

    @pytest.mark.parametrize("invalid_email2", invalid_vendor_emails)
    def test_invalid_vendor_email(self, invalid_email2):
        with pytest.raises(ValueError):
            print(f"Testing invalid vendor email: {invalid_email2}")
            if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", invalid_email2):
                raise ValueError("Invalid Email Format!")

    # Invalid phone test cases (kept as you had them)
    invalid_phones = [
        rstr.xeger(r'^\d{1,9}$'),  # too short
        rstr.xeger(r'^[a-zA-Z]+\d+$'),  # letters + digits
        "",  # empty
        rstr.xeger(r'^[\d]{9}$')  # exactly 9 digits
    ]

    @pytest.mark.parametrize("invalid_phone", invalid_phones)
    def test_invalid_phone_number(self, invalid_phone):
        with pytest.raises(ValueError):
            print(f"Testing invalid phone number: {invalid_phone}")
            if not re.match(r"^\d{10}$", invalid_phone):
                raise ValueError("Invalid Phone Number!")

    # --------------------------

    def _vendor_request(self, homepage, VENDOR_DATA):
        print("\nStarting Vendor Request...")
        actions = ActionChains(self.driver)
        homepage.getclick().click()
        actions.send_keys(Keys.PAGE_DOWN).perform()

        # print(
        #     f"Entering vendor details: {VENDOR_DATA['name']}, {VENDOR_DATA['business_case']}, {VENDOR_DATA['first_name']}, {VENDOR_DATA['last_name']}, {VENDOR_DATA['email2']}, {VENDOR_DATA['phone']}")
        homepage.getName().send_keys(VENDOR_DATA['name'])
        homepage.getvendertype().click()
        time.sleep(2)
        homepage.getvendertypeselect().click()
        time.sleep(2)
        homepage.getBusinessCase().send_keys(VENDOR_DATA['business_case'])
        homepage.getFirstName().send_keys(VENDOR_DATA['first_name'])
        homepage.getLastName().send_keys(VENDOR_DATA['last_name'])
        homepage.getEmail2().send_keys(VENDOR_DATA['email2'])
        homepage.getPhone().send_keys(VENDOR_DATA['phone'])

        try:
            homepage.getNext().click()
            print("Next Button Clicked successfully")
        except AttributeError:
            raise NoSuchElementException("Next button was not found")


    ###Second Page

        # homepage.getTypeAService().click()
        # time.sleep(3)
        # homepage.getServices().click()
        # homepage.getTypeALocation().click()
        # homepage.getLocations().click()
        # time.sleep(2)
        # homepage.getNext().click()
        # time.sleep(1)


        try:
            homepage.getTypeAService().click()
            time.sleep(3)
        except Exception as e:
            print("Error clicking Type A Service:")
            traceback.print_exc()
            raise

        try:
            homepage.getServices().click()
        except Exception as e:
            print("Error clicking Services:")
            traceback.print_exc()
            raise

        try:
            homepage.getTypeALocation().click()
        except Exception as e:
            print("Error clicking Type A Location:")
            traceback.print_exc()
            raise

        try:
            homepage.getLocations().click()
            time.sleep(2)
        except Exception as e:
            print("Error clicking Locations:")
            traceback.print_exc()
            raise

        try:
            homepage.getNext().click()
            time.sleep(1)
        except Exception as e:
            print("Error clicking Next:")
            traceback.print_exc()
            raise

        ##Third Page
        homepage.getRadio1().click()
        time.sleep(1)
        homepage.getRadio2().click()
        time.sleep(1)
        homepage.getRadio3().click()
        time.sleep(1)
        homepage.getRadio4().click()
        time.sleep(2)

        actions = ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()  # Scrolls down one page
        time.sleep(2)

        homepage.getSelectAnOption().click()
        time.sleep(2)
        homepage.getSelectAnOptionDropdown().click()
        time.sleep(2)
        homepage.getSave().click()
        time.sleep(10)

    ##New Vendor
        homepage.getAction().click()
        time.sleep(5)
        wait = WebDriverWait(self.driver, 10)
        approve_button = wait.until(EC.element_to_be_clickable(homePage.VendorActionLocators(self.driver).getApprove()))
        approve_button.click()
        # homePage.VendorActionLocators(self.driver).getApprove().click()
        time.sleep(10)
        homepage.getAction2().click()
        time.sleep(5)
        # homePage.VendorActionLocators(self.driver).getEdit().click()
        wait = WebDriverWait(self.driver, 10)
        edit_button = wait.until(EC.element_to_be_clickable(homePage.VendorActionLocators(self.driver).getEdit()))
        edit_button.click()
        time.sleep(5)

###Edit/Abou/Account Information####
        homepage.getLegal_Entity_Name().click()
        time.sleep(2)
        homepage.getLegal_Entity_Name().send_keys(ACCOUNT_INFORMATION['Legal_Entity_Name'])
        time.sleep(2)
        homepage.getParent_Account().click()
        time.sleep(3)
        homepage.getParent_Account_click().click()
        time.sleep(3)
        homepage.getPhone_No().click()
        time.sleep(2)
        homepage.getPhone_No().send_keys(ACCOUNT_INFORMATION['Phone_No'])
        time.sleep(2)
        homepage.getWebsite().click()
        time.sleep(2)
        homepage.getWebsite().send_keys(ACCOUNT_INFORMATION['Website'])
        time.sleep(2)
        homepage.getClient_Vendor_ID().click()
        time.sleep(2)
        homepage.getClient_Vendor_ID().send_keys(ACCOUNT_INFORMATION['Client Vendor ID'])
        time.sleep(2)
        homepage.getAccount_Information().click()
        time.sleep(5)








