
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


###############################################
import inspect
import logging
import os
import sys
import pytest
from logging.handlers import RotatingFileHandler


@pytest.mark.usefixtures('setup')
class BaseClass:
    _logger_configured = False  # Class-level flag to track logger configuration

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        if not self._logger_configured:
            try:
                # Create logs directory in project root if it doesn't exist
                log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
                os.makedirs(log_dir, exist_ok=True)

                log_file = os.path.join(log_dir, 'automation.log')

                # Clear existing handlers to avoid duplicates
                logger.handlers = []

                # Set up file handler
                file_handler = RotatingFileHandler(
                    log_file,
                    maxBytes=1024 * 1024,  # 1MB
                    backupCount=5,
                    encoding='utf-8'
                )
                formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
                file_handler.setFormatter(formatter)

                # Set up console handler
                console_handler = logging.StreamHandler(sys.stdout)
                console_handler.setFormatter(formatter)

                logger.addHandler(file_handler)
                logger.addHandler(console_handler)
                logger.setLevel(logging.DEBUG)

                # Add a filter to ensure proper handling of Unicode characters
                class UnicodeFilter(logging.Filter):
                    def filter(self, record):
                        if isinstance(record.msg, str):
                            record.msg = record.msg.encode('utf-8', 'replace').decode('utf-8')
                        return True

                logger.addFilter(UnicodeFilter())

                self._logger_configured = True

            except Exception as e:
                print(f"\nLogger initialization error: {str(e)}", file=sys.stderr)
                # Fallback to basic config if setup fails
                logging.basicConfig(
                    level=logging.INFO,
                    format="%(asctime)s : %(levelname)s : %(name)s : %(message)s",
                    stream=sys.stdout
                )

        return logger