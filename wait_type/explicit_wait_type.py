from traceback import print_stack
from utilities.handy_wrappers import HandyWrappers
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class ExplicitWaitType():

	def __init__(self, driver):
		self.driver = driver
		self.hw = HandyWrappers(self.driver)
		
	def wait_for_element(self, locator, locator_type="xpath", timeout=10, poll_frequency=0.5):
		element = None
		try:
			by_type = self.hw.get_by_type(locator_type)
			print("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable")
			print("Element appeared on the web page")
			wait = WebDriverWait(self.driver, 10, poll_frequency=1, ignored_exceptions=[NoSuchElementException,
														   ElementNotVisibleException,
														   ElementNotSelectableException])
			element = wait.until(EC.element_to_be_clickable(by_type, locator))
		except:
			print("Element did not appear on the web page")
			print_stack()
		return element

