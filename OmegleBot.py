from selenium import webdriver
from selenium.webdriver.common.keys import Keys

intr = None
msg = None

#Taking Inputs
while(intr == None):
	intr = input("Enter Your interests (Seprated by a comma ',' (Use Space for empty)) :")
	
while(msg == None):
	msg = input("Enter the message you want to send : ")
	
dd = False
driver=webdriver.Firefox()
driver.get("https://omegle.com")

#For Adding Interests
msgbox=driver.find_element_by_class_name('newtopicinput')
msgbox.send_keys(intr)
msgbox.send_keys(Keys.ENTER)

start=driver.find_element_by_id('textbtn')
start.click()

while(dd == False):
	try:
		driver.find_element_by_xpath('//textarea[@rows="3"]').clear()
		send = driver.find_element_by_xpath('//button[@class="sendbtn"]')
		message = driver.find_element_by_xpath('//textarea[@rows="3"]')
		disconnect = driver.find_element_by_xpath('//button[@class="disconnectbtn"]')
		message.send_keys(msg)
		send.click()
		disconnect.click()
		disconnect.click()
		disconnect.click()
	except:
		a=1