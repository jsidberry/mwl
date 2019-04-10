from __future__ import print_function
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from wait_type.explicit_wait_type import ExplicitWaitType
import time
import csv
# from lxml import html


class Wireplan:	
	
	def __init__(self):
		self.driver = driver = webdriver.Firefox()
		self.signin_url = "http://mdms-settings.charter.com:8300/operators/sign_in"
		self.base_url = "http://mdms-settings.charter.com:8300/"
		self.regions_url = "http://mdms-settings.charter.com:8300/qrm/regions"
		self.stevens_pt_pumps_url = "http://mdms-settings.charter.com:8300/prm/regions/sldcmo-ndc2/headends/stevens-pt-fsm/pumps"
		self.stevens_pt_qam_groups_url = "http://mdms-settings.charter.com:8300/qrm/regions/sldcmo-ndc2/headends/stevens-pt-fsm/qam_groups"
		self.stevens_pt_service_groups_url = "http://mdms-settings.charter.com:8300/qrm/regions/sldcmo-ndc2/headends/stevens-pt-fsm/service_groups"
		self.user_email_address = "c-juan.sidberry@charter.com"
		self.user_password = "24652mdms"
		
		
	def login_process(self):
		print("Opening browser and logging in...")
		driver = self.driver
		user_email_address = self.user_email_address
		user_password = self.user_password
		self.driver.get(self.signin_url)
		wait = WebDriverWait(self.driver, 10, poll_frequency=1, ignored_exceptions=[NoSuchElementException,
														   ElementNotVisibleException,
														   ElementNotSelectableException])
		# element = wait.until(EC.element_to_be_clickable(By.XPATH , locator))
		driver.find_element(By.XPATH, "//header/section/article/ul/li/a").click()
		driver.find_element(By.XPATH, "//form[@id='new_operator']//input[@id='operator_email']").send_keys(user_email_address)
		# driver.find_element(By.ID, "operator_password").send_keys(user_password)
		element = wait.until(EC.presence_of_element_located((By.ID, "operator_password")))
		element.send_keys(user_password)
		driver.find_element(By.XPATH, "//form[@id='new_operator']//input[@name='commit']").click()
		
		
		
	def goto_qam_pumps(self):
		driver = self.driver
		stevens_pt_pumps_url = self.stevens_pt_pumps_url
		driver.get(stevens_pt_pumps_url)
		time.sleep(7)
		driver.quit()
		
	
	def goto_gam_group(self):
		driver = self.driver
		stevens_pt_pumps_qam_groups_url = self.stevens_pt_pumps_qam_groups_url
		driver.get(stevens_pt_pumps_qam_groups_url)
		time.sleep(7)
		driver.quit()
	
	
	def streaming_resource_management(self):
		signin_url = "http://mdms-settings.charter.com:8300/operators/sign_in"
		base_url = "http://mdms-settings.charter.com:8300/"
		regions_url = "http://mdms-settings.charter.com:8300/qrm/regions"
		stevens_pt_pumps_url = "http://mdms-settings.charter.com:8300/prm/regions/sldcmo-ndc2/headends/stevens-pt-fsm/pumps"
		stevens_pt_pumps_qam_groups_url = "http://mdms-settings.charter.com:8300/qrm/regions/sldcmo-ndc2/headends/stevens-pt-fsm/qam_groups"
		user_email_address = "c-juan.sidberry@charter.com"
		user_password = "24652mdms"
		
		# Instantiate webdriver
		driver = webdriver.Firefox()
		# driver.maximize_window()
		
		#Open MDMS UI to login page
		print("Opening the page..")
		driver.get(stevens_pt_pumps_url)
		
		# Check is already Logged In
		print("Loggin in...")
		driver.find_element(By.XPATH, "//header/section/article/ul/li/a").click()
		driver.find_element(By.XPATH, "//form[@id='new_operator']//input[@id='operator_email']").send_keys(user_email_address)
		driver.find_element(By.ID, "operator_password").send_keys(user_password)
		driver.find_element(By.XPATH, "//form[@id='new_operator']//input[@name='commit']").click()
		# driver.find_element(By.XPATH, "//header/section/article/ul/li/a")
		
		time.sleep(3)
		driver.quit()
	
	
	def get_csv_data(filename):
		# create an empty list to store rows
		rows = []
		
		# open the CSV file
		data_file = open(filename, "r")
		
		# create a CSV reader from CSV file
		csv_reader = csv.reader(data_file)
		
		# skip the header
		next(reader)
		
		# add rows from reader to list
		for row in csv_reader:
			rows.append(row)
			
		return rows
	
	
	def test(self):
		driver = self.driver
		# driver.maximize_window()
				
		print("Stevens-Point QAM Group URL...")
		print("")
		stevens_pt_pumps_qam_groups_url = self.stevens_pt_pumps_qam_groups_url
		driver.get(stevens_pt_pumps_qam_groups_url)
		
		wait = WebDriverWait(self.driver, 10, poll_frequency=1, ignored_exceptions=[NoSuchElementException,
														   ElementNotVisibleException,
														   ElementNotSelectableException])
		# element = wait.until(EC.element_to_be_clickable(by_type, locator))
		
		print("Search Options...")
		print("")
		element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='page-search']//form[@class='page-search']//div[@class='page-search-box']//p[@class='search']/a")))
		element.click()
		# /html/body/div/section/section/div[2]/div/div/div[6]/form/div[1]/div[2]/div/div[3]/p[2]/a
		# //div[@id='content']//div[@class='box']//div[@id='headends_qam_groups']//div[@class='page-search']//p[@class='search']/a
		# //div[@class='page-search']//form[@class='page-search']//div[@class='page-search-box']//p[@class='search']/a
		
		print("Enter search value...")
		print("")
		search_value = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='search_name']")))
		search_value.send_keys("*172.17.81.161*") # this value will come fro a CSV file. TODO: load data from CSV into list/dict/tuple
		stevens_pt_current_url = driver.current_url
		
		print("Clicking Search button...")
		print("")
		blue_search_button = driver.find_element(By.XPATH, "//div[@id='headends_qam_groups']//form[@action='/qrm/regions/sldcmo-ndc2/headends/stevens-pt-fsm/qam_groups']/div[2]/div/div/div[2]/a[1]")
		blue_search_button.click()
		driver.implicitly_wait(5)
		
		print("Click 1st link on resulting list...")
		print("")
		first_link_in_table = driver.find_element(By.XPATH, "//table[@id='qam_groups']//a[1]")
		first_link_in_table.click()
		driver.implicitly_wait(5)
		
		print("Search Options...")
		print("")
		driver.find_element(By.XPATH, "//p[@class='search']/a[@href='#']").click()
		driver.implicitly_wait(5)
		
		print("Enter search value...")
		print("")
		search_value = driver.find_element(By.XPATH, "//input[@id='search_name']")
		search_value.send_keys("*46005Q1*") # this value will come fro a CSV file. TODO: load data from CSV into list/dict/tuple
		driver.implicitly_wait(5)
		
		print("Clicking BLUE Search button...")
		print("")
		blue_search_button = driver.find_element(By.XPATH, "/html/body/div/section/section[2]/article/dl/dd[4]/div/div/div[6]/div/form/div[2]/div/div/div[2]/a[1]")
		blue_search_button.click()
		driver.implicitly_wait(5)
		
		time.sleep(7)
		driver.quit()
		
		
	def read_qam_groups_from_mdms(self,csv_file="some.csv"):
		driver = self.driver
		print("Reading Service Groups from MDMS for Stevens Point headend...")
		print("")
		
		service_groups = []
		
		stevens_pt_qam_groups_url = self.stevens_pt_qam_groups_url
		driver.get(stevens_pt_qam_groups_url)
		
		qam_group_table = driver.find_element_by_xpath("//table[@id='qam_groups']")
		x = 1

		element = driver.find_element_by_xpath("//div[@class='counts']/p[2]")
		# //*[@id="headends_qam_groups"]/div[6]/form/div[1]/div[1]/div/div[3]/p[2]
		num_of_pages_text = element.text
		a,current_page_number,b,last_page_num = num_of_pages_text.split(" ")
		# print(last_page_num)
		qam_group_data_dict = {}
		for page in range(0,int(last_page_num)):
			
			if page != int(last_page_num):
				# element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='counts']/p[2]")))	
				element = driver.find_element(By.XPATH, "//div[@class='counts']/p[2]")
				num_of_pages_text = element.text
				# print(num_of_pages_text)
				temp_a,temp_current_page_number,temp_b,temp_last_page_num = num_of_pages_text.split(" ")
				
				for row in qam_group_table.find_elements_by_xpath(".//tr"):
					qam_group_name = driver.find_elements_by_xpath(".//td/a")
					header_text = "Name Streaming IP Address QAM Streams"
					
					if row.text != header_text:
						row_text = row.text
						qam_group_name,qam_group_streaming_ip_address,qam_group_streams = row_text.split(" ")
						print(qam_group_name,qam_group_streaming_ip_address)
						qam_group_data_dict.update({qam_group_name:qam_group_streaming_ip_address})
				
				next_page_link = driver.find_element(By.XPATH, "//*[@id='headends_qam_groups']/div[6]/form/div[1]/div[1]/div/div[4]/a")
				next_page_link.click()
				time.sleep(5)
		
		print("")
		print("Creating the CSV file...")
		with open(csv_file, 'a') as csvfile:
			for key, value in qam_group_data_dict.iteritems():
				csvfile.write(key + "," + qam_group_data_dict[key] + "\n")


	def read_service_group_data_from_qam_group(self):
		driver = self.driver
		print("Reading Service Groups Data from QAM Group for Stevens Point headend...")
		print("")
		
		service_groups = []
		
		stevens_pt_service_groups_url = self.stevens_pt_service_groups_url
		driver.get(stevens_pt_service_groups_url)
		
		qam_table = driver.find_element_by_xpath("//table[@id='qams']")
		
		element = driver.find_element_by_xpath("//div[@class='counts']/p[2]")
		num_of_pages_text = element.text
		a,current_page_number,b,last_page_num = num_of_pages_text.split(" ")
		# print(last_page_num)
		qam_data_dict = {}
		
		# for page in range(0,int(last_page_num)):
			
			# if page != int(last_page_num):
				# element = driver.find_element(By.XPATH, "//div[@class='counts']/p[2]")
				# num_of_pages_text = element.text
				# print(num_of_pages_text)
				# temp_a,temp_current_page_number,temp_b,temp_last_page_num = num_of_pages_text.split(" ")
				
				# for row in qam_table.find_elements_by_xpath(".//tr"):
					# qam_group_name = driver.find_elements_by_xpath(".//td/a")
					# header_text = "Name TSID Frequency Streams QAM Usage QAM Group Server Group Status"
					
					# if row.text != header_text:
						# row_text = row.text
						# qam_name,qam_streaming_ip_address,qam_streams = row_text.split(" ")
						# print(qam_name,qam_streaming_ip_address)
						# qam_group_data_dict.update({qam_name:qam_streaming_ip_address})
				
				# next_page_link = driver.find_element(By.XPATH, "//*[@id='headends_qam_groups']/div[6]/form/div[1]/div[1]/div/div[4]/a")
				# next_page_link.click()
				# time.sleep(5)
		
		# print("")
		# print("Creating the CSV file...")
		# with open('some.csv', 'a') as csvfile:
			# for key, value in qam_group_data_dict.iteritems():
				# csvfile.write(key + "," + qam_group_data_dict[key] + "\n")

# //*[@id="qams"]/tbody/tr[1]/td[1]/a
		
		# driver.quit()

		
ff = Wireplan()
ff.login_process()   # User login to MDMS UI
# ff.goto_qam_pumps()  # 
# ff.goto_gam_group()  # goto QAM Group tab
csv_qam_data_file = "qam_data_file.csv"
ff.read_qam_groups_from_mdms(csv_qam_data_file)
# ff.read_service_group_data_from_qam_group(csv_qam_data_file)
# ff.test()
