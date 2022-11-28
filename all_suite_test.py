import unittest

from unittest.loader import makeSuite

from test_cases.add_new_player_to_the_system import TestAddPlayer
from test_cases.dashboard_page import TestDashboardPage
from test_cases.framework import Test
from test_cases.login_to_the_system import TestLoginPage


def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(TestLoginPage))
   test_suite.addTest(makeSuite(TestDashboardPage))
   test_suite.addTest(makeSuite(TestAddPlayer))
   return test_suite


if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())