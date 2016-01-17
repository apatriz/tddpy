from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Mini is always forgetting things. She heard about this cool
        # online to-do app. She checks it out...
        self.browser.get(self.server_url)

        # She notices the title and header of the page mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item right away
        inputbox = self.get_item_input_box()
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "Buy my bf a pig" into a text box
        inputbox.send_keys('Buy my bf a pig')

        # When she hits enter, she is taken to a new URL,
        # and now the page lists "1: Buy my bf a pig" as an item
        # in a to-do list table
        inputbox.send_keys(Keys.ENTER)
        mini_list_url = self.browser.current_url
        self.assertRegex(mini_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy my bf a pig')

        # There is still a text box inviting her to add another item.She
        # enters "Give pig a sweater" (noone likes a cold pig)
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Give pig a sweater')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('1: Buy my bf a pig')
        self.check_for_row_in_list_table('2: Give pig a sweater')

        # Now a new user, Francis, comes along to the site.

        # We use a new browser session to make sure that no information
        # of Mini's is coming through from cookies etc.
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis visits the home page. There is no sign of Mini's
        # list
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy my bf a pig', page_text)
        self.assertNotIn('Give pig a sweater', page_text)

        # Francis starts a new list by entering a new item. He
        # is less interesting than Mini...
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, mini_list_url)

        # Again, there is no trace of Mini's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy my bf a pig', page_text)
        self.assertIn('Buy milk', page_text)

        # Satisfied, she goes back to sleep
