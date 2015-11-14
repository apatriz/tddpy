from selenium import webdriver
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
		self.fail('Finish the test!')

		# She is invited to enter a to-do item right away

		# She types "Buy my bf a pig" into a text box

		# When she hits enter, the page updates, and now the page lists
		# "1: Buy a pig" as an item in a to-do list

		# There is still a text box inviting her to add another item.She
		# enters "Give pig a sweater" (noone likes a cold pig)

		#The page updates again, and now shows both items on her list

		#Mini wonders whether the site will remember her list. Then she sees
		# that the site has generated a unique URL for her -- there is some
		# explanatory text to that effect

		# She visits that URL - her to-do list is still there.

		# Satisfied, she goes back to sleep

if __name__ == '__main__':
	unittest.main(warnings='ignore')
