from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Check out homepage
        self.browser.get('http://localhost:8000')

        # To-Do in title and header
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test')

        # Invited to enter a to-do item straight away

        # Type 'note' in a textbox

        # If enter is hit the page lists:
        # '1: note' as an item on the list

        # Text box for extra items is still available

        # Another item is entered

        # Page updates
        # Both items are on the list

        # A URL is generated to find the list later


if __name__ == '__main__':
    unittest.main()
