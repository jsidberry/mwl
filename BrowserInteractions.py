from selenium import webdriver
import os


class BrowserInteractions:

	def test(self):
		base_url = "https://www.zillow.com"
		driver = webdriver.Firefox()
		
		#Maximize browser
		driver.maximize_window()
		
		#Open URL
		driver.get(base_url)
		
		# Get title of the page
		title = driver.title
		print(title)
		
		# Close the browser
		driver.quit()
		
		
	def login(self):
		base_url = "https://www.zillow.com"
		driver = webdriver.Firefox()
		# user_email_address = "c-juan.sidberry@charter.com"
		user_email_address = os.environ['TEST_USERNAME']
		user_password = os.environ['TEST_PSSWD']
		# user_password = "24652mdms"
		
		#Open MDMS UI to login page
		driver.get(base_url)
		signin_link = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/header/nav/div[2]/ul[3]/li[1]/a").click()
		# driver.signin_link.click()
		email_element_id = driver.find_element_by_id("inputs-newEmail")
		if email_element_id is not None:
			print("Found email on login form.")
		
		# Close the browser
		driver.quit()
		

ff = BrowserInteractions()
# ff.test()
ff.login()
