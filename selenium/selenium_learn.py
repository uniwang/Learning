from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class test_webdriver(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_search_python(self):
		driver = self.driver
		driver.get('http://www.baidu.com/')
		print driver.title
		elem = driver.find_element_by_name('wd')
		print elem
		print driver.get_cookies()
		elem.send_keys("python")
		elem.send_keys(Keys.RETURN)

	def tearDown(self):
		pass
		#self.driver.close()


if __name__ == '__main__':
	unittest.main()