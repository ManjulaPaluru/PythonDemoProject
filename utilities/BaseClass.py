import pytest
import inspect
from selenium.webdriver.support.select import Select
import logging

@pytest.mark.usefixtures("setup")
class BaseClass:

        def getlogger(self):
                loggername = inspect.stack()[1][3]
                logger = logging.getLogger(loggername)
                fileHandler = logging.FileHandler('Logfile.log')
                formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s:%(message)s")
                fileHandler.setFormatter(formatter)
                logger.addHandler(fileHandler)
                logger.setLevel(logging.DEBUG)
                logger.debug("debug log")
                logger.info("information")
                logger.warning("warning")
                logger.error("error")
                logger.critical("critical")
                return logger



        def selectOptionByText(self,locator,text):
                sel =Select(locator)
                sel.select_by_visible_text(text)
