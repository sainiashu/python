import unittest
import HTMLTestRunner
import os
from launchbrowser import FillForm
from alert_test import  AlertTest



# get the directory path to output report file
dir = os.getcwd()
print('current dir', dir)
# get all tests from SearchText and HomePageTest class
launchbrowser = unittest.TestLoader().loadTestsFromTestCase(FillForm)
alert_test = unittest.TestLoader().loadTestsFromTestCase(AlertTest)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([launchbrowser, alert_test])

# open the report file
outfile = open(dir + "\Report\TestSummary.html", "w")

# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,title='Test Report', description='Test Automation Report')

# run the suite using HTMLTestRunner
runner.run(test_suite)