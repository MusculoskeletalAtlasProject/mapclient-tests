'''
MAP Client, a program to generate detailed musculoskeletal models for OpenSim.
    Copyright (C) 2012  University of Auckland
    
This file is part of MAP Client. (http://launchpad.net/mapclient)

    MAP Client is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    MAP Client is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with MAP Client.  If not, see <http://www.gnu.org/licenses/>..
'''

import unittest

def suite():
    tests = unittest.TestSuite()

    from tests.widgets.test_mainwindow import MainWindowTestCase
    tests.addTests(unittest.TestLoader().loadTestsFromTestCase(MainWindowTestCase))

    from tests.widgets.utils import UtilsTestCase
    tests.addTests(unittest.TestLoader().loadTestsFromTestCase(UtilsTestCase))

    return tests

def load_tests(loader, tests, pattern):
    return suite()

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
