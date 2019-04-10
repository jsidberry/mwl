from selenium import webdriver


class BrowserInteractions:

	def test(self):
		base_url = "https://letskodeit.teachable.com/pages/practice"
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
		base_url = "http://mdms-settings.charter.com:8300/operators/sign_in"
		driver = webdriver.Firefox()
		user_email_address = "c-juan.sidberry@charter.com"
		user_password = "24652mdms"
		
		#Open MDMS UI to login page
		driver.get(base_url)
		
		email_element_id = driver.find_element_by_id("operator_email")
		if email_element_id is not None:
			print("Found email on login form.")
		
		
ff = BrowserInteractions()
ff.login()
		