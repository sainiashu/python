import unittest

from class_method import HomePageTest
from search_text import SearchText

#get all tests from the SearchText and class_method
search_text = unittest.TestLoader().loadTestsFromTestCase(SearchText)
home_page = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

#create a test suite combining search text and home page
test_suite = unittest.TestSuite([search_text, home_page])

#run the test suite
unittest.TextTestRunner(verbosity=2).run(test_suite)