
###Original File
# import inspect
# import logging
# import pytest
#
#
#
#
# @pytest.mark.usefixtures('setup')
# class BaseClass:
#
#
#     def getLogger(self):
#         loggerName = inspect.stack()[1][3]
#         logger = logging.getLogger(loggerName)
#
#         fileHandlar = logging.FileHandler('../CustomerLogin/logfile.log')
#         formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s :%(message)s")
#         fileHandlar.setFormatter(formatter)
#
#         logger.addHandler(fileHandlar)  # file handle object
#         logger.setLevel(logging.DEBUG)
#         return logger

#







####For testing
# import inspect
# import logging
# import os
# import pytest
#
#
# @pytest.mark.usefixtures('setup')
# class BaseClass:
#     def getLogger(self):
#         try:
#             loggerName = inspect.stack()[1][3]
#             logger = logging.getLogger(loggerName)
#
#             # Create logs directory in project root if it doesn't exist
#             log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
#             os.makedirs(log_dir, exist_ok=True)
#
#             log_file = os.path.join(log_dir, 'automation.log')
#             fileHandler = logging.FileHandler(log_file)
#             formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
#             fileHandler.setFormatter(formatter)
#
#             logger.addHandler(fileHandler)
#             logger.setLevel(logging.DEBUG)
#             return logger
#         except Exception as e:
#             print("\ncode fat gaya hai - Logger initialization failed!")
#             print(f"Error: {str(e)}")
#             # Fallback to basic console logging
#             logging.basicConfig(level=logging.INFO)
#             return logging.getLogger("console_fallback")























####USe For screenshots
import inspect
import logging
import os
import pytest


@pytest.mark.usefixtures('setup')
class BaseClass:
    def getLogger(self):
        try:
            loggerName = inspect.stack()[1][3]
            logger = logging.getLogger(loggerName)

            # Create logs directory in project root if it doesn't exist
            log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
            os.makedirs(log_dir, exist_ok=True)

            log_file = os.path.join(log_dir, 'automation.log')
            fileHandler = logging.FileHandler(log_file)
            formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
            fileHandler.setFormatter(formatter)

            logger.addHandler(fileHandler)
            logger.setLevel(logging.DEBUG)
            return logger
        except Exception as e:
            print("\ncode fat gaya hai - Logger initialization failed!")
            print(f"Error: {str(e)}")
            # Fallback to basic console logging
            logging.basicConfig(level=logging.INFO)
            return logging.getLogger("console_fallback")
