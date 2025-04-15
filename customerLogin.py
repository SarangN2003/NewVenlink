# # customerLogin.py
#
# from selenium.common.exceptions import NoSuchElementException
#
# username = "sagar.hingane+2@hypermatica.com"
# password = "Test@12345@"
#
# def perform_customer_login(homepage, username, password, logger):
#     logger.info("Starting Customer Login...")
#     homepage.getEmail().send_keys(username)
#     homepage.getPassword().send_keys(password)
#
#     checkbox_success = False
#
#     try:
#         homepage.getCheckBox().click()
#         logger.info("Checkbox clicked successfully.")
#         checkbox_success = True
#     except AttributeError:
#         raise NoSuchElementException("Checkbox was not found.")
#     except Exception as e:
#         logger.error(f"Checkbox click failed: {str(e)}")
#         raise
#
#     if checkbox_success:
#         try:
#             homepage.getSignIn().click()
#             logger.info("Sign-in clicked successfully.")
#         except AttributeError:
#             raise NoSuchElementException("Sign-in button was not found.")
#         except Exception as e:
#             logger.error(f"Sign-in click failed: {str(e)}")
#             raise
#     else:
#         raise Exception("Sign-in skipped because checkbox operation failed.")

# customerLogin.py

# import pytest
# import rstr
# from selenium.common.exceptions import NoSuchElementException
# import re
#
#
# # Test credentials
# username = "sagar.hingane+2@hypermatica.com"
# password = "Test@12345@"
#
# def perform_customer_login(homepage, username, password, logger):
#     logger.info("Starting Customer Login...")
#
#     homepage.getEmail().send_keys(username)
#     logger.info(f"Entered email: {username}")
#
#     homepage.getPassword().send_keys(password)
#     logger.info("Entered password")
#
#     checkbox_success = False
#
#     try:
#         homepage.getCheckBox().click()
#         logger.info("Checkbox clicked successfully.")
#         checkbox_success = True
#     except AttributeError:
#         raise NoSuchElementException("Checkbox was not found.")
#     except Exception as e:
#         logger.error(f"Checkbox click failed: {str(e)}")
#         raise
#
#     if checkbox_success:
#         try:
#             homepage.getSignIn().click()
#             logger.info("Sign-in clicked successfully.")
#         except AttributeError:
#             raise NoSuchElementException("Sign-in button was not found.")
#         except Exception as e:
#             logger.error(f"Sign-in click failed: {str(e)}")
#             raise
#     else:
#         raise Exception("Sign-in skipped because checkbox operation failed.")
#
#
#
#
# invalid_emails = [
#     rstr.xeger(r'^[a-zA-Z0-9._%+-]+[a-zA-Z0-9.-]+[a-zA-Z]{2,}$'),
#     rstr.xeger(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+$'),
#     rstr.xeger(r'^@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'),
#     rstr.xeger(r'^[a-zA-Z0-9._%+-]+@\.+[a-zA-Z]{2,}$')
# ]
#
# @pytest.mark.parametrize("invalid_email", invalid_emails)
# def test_invalid_email_format(invalid_email):
#     with pytest.raises(ValueError):
#         print(f"Testing invalid email: {invalid_email}")
#         if not re.match(r"^[a-zA-Z0-9._%+-]{1,64}@(?!.*\.\.)[a-zA-Z0-9.-]{1,255}\.[a-zA-Z]{2,}$", invalid_email):
#             raise ValueError("Invalid email format")
#
#
# invalid_passwords = [
#     rstr.xeger(r'^[A-Za-z]{8,}$'),
#     rstr.xeger(r'^\d{8,}$'),
#     rstr.xeger(r'^[A-Za-z\d]{8,}$'),
#     rstr.xeger(r'^[A-Za-z@$!%*?&]{8,}$'),
#     rstr.xeger(r'^[\d@$!%*?&]{8,}$')
# ]
#
# @pytest.mark.parametrize("invalid_password", invalid_passwords)
# def test_invalid_password_format(invalid_password):
#     with pytest.raises(ValueError):
#         print(f"Testing invalid password format: {invalid_password}")
#         if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", invalid_password):
#             raise ValueError("Invalid password format")



#####Current Working File
import pytest
import rstr
from selenium.common.exceptions import NoSuchElementException
import re
from test_data import CUSTOMER_CREDENTIALS  # Import from centralized test data

# Use credentials from test_data.py
username = CUSTOMER_CREDENTIALS['username']
password = CUSTOMER_CREDENTIALS['password']

def perform_customer_login(homepage, username, password, logger):
    logger.info("Starting Customer Login...")

    homepage.getEmail().send_keys(username)
    logger.info(f"Entered email: {username}")

    homepage.getPassword().send_keys(password)
    logger.info("Entered password")

    checkbox_success = False

    try:
        homepage.getCheckBox().click()
        logger.info("Checkbox clicked successfully.")
        checkbox_success = True
    except AttributeError:
        raise NoSuchElementException("Checkbox was not found.")
    except Exception as e:
        logger.error(f"Checkbox click failed: {str(e)}")
        raise

    if checkbox_success:
        try:
            homepage.getSignIn().click()
            logger.info("Sign-in clicked successfully.")
        except AttributeError:
            raise NoSuchElementException("Sign-in button was not found.")
        except Exception as e:
            logger.error(f"Sign-in click failed: {str(e)}")
            raise
    else:
        raise Exception("Sign-in skipped because checkbox operation failed.")

invalid_emails = [
    rstr.xeger(r'^[a-zA-Z0-9._%+-]+[a-zA-Z0-9.-]+[a-zA-Z]{2,}$'),
    rstr.xeger(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+$'),
    rstr.xeger(r'^@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'),
    rstr.xeger(r'^[a-zA-Z0-9._%+-]+@\.+[a-zA-Z]{2,}$')
]

@pytest.mark.parametrize("invalid_email", invalid_emails)
def test_invalid_email_format(invalid_email):
    with pytest.raises(ValueError):
        print(f"Testing invalid email: {invalid_email}")
        if not re.match(r"^[a-zA-Z0-9._%+-]{1,64}@(?!.*\.\.)[a-zA-Z0-9.-]{1,255}\.[a-zA-Z]{2,}$", invalid_email):
            raise ValueError("Invalid email format")

invalid_passwords = [
    rstr.xeger(r'^[A-Za-z]{8,}$'),
    rstr.xeger(r'^\d{8,}$'),
    rstr.xeger(r'^[A-Za-z\d]{8,}$'),
    rstr.xeger(r'^[A-Za-z@$!%*?&]{8,}$'),
    rstr.xeger(r'^[\d@$!%*?&]{8,}$')
]

@pytest.mark.parametrize("invalid_password", invalid_passwords)
def test_invalid_password_format(invalid_password):
    with pytest.raises(ValueError):
        print(f"Testing invalid password format: {invalid_password}")
        if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", invalid_password):
            raise ValueError("Invalid password format")