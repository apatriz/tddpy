from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Mini is always forgetting things. She heard about this cool
		# online to-do app. She checks it out...
		self.browser.get('http://localhost:8000')


		#She notices the title and header of the page mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# She is invited to enter a to-do item right away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
				inputbox.get_attribute('placeholder'),
				'Enter a to-do item'
		)

		# She types "Buy my bf a pig" into a text box
		inputbox.send_keys('Buy my bf a pig')
		# When she hits enter, the page updates, and now the page lists
		# "1: Buy my bf a pig" as an item in a to-do list
		inputbox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Buy my bf a pig', [row.text for row in rows])

		# There is still a text box inviting her to add another item.She
		# enters "Give pig a sweater" (noone likes a cold pig)
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Give pig a sweater')
		inputbox.send_keys(Keys.ENTER)

		#The page updates again, and now shows both items on her list
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Buy my bf a pig', [row.text for row in rows])
		self.assertIn(
			'2: Give pig a sweater' ,
			[row.text for row in rows]
		)

		#Mini wonders whether the site will remember her list. Then she sees
		# that the site has generated a unique URL for her -- there is some
		# explanatory text to that effect
		self.fail('Finish the test!')

		# She visits that URL - her to-do list is still there.

		# Satisfied, she goes back to sleep

if __name__ == '__main__':
	unittest.main(warnings='ignore')
