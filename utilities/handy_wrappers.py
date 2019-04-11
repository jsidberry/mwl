from selenium.webdriver.common.by import By


class HandyWrappers():

	def __init__(self, driver):
		self.driver = driver
		
		
	def get_by_type(self, locator_type):
		locator_type = locator_type.lower()
		if locator_type == "id":
			return By.ID
		elif locator_type == "name":
			return By.NAME
		elif locator_type == "xpath":
			return By.XPATH
		elif locator_type == "css":
			return By.CSS_SELECTOR
		elif locator_type == "classname":
			return By.CLASS_NAME
		elif locator_type == "linktext":
			return By.LINK_TEXT
		else:
			print("Locator type " + locator_type + " not correct/supported")
		return False

