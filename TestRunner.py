import unittest

import HtmlTestRunner

from tests import FarmRiseTests

# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(FarmRiseTests))

# initialize a runner, pass it your suite and run it
runner = HtmlTestRunner.HTMLTestRunner(output='reports/test-reports', verbosity=2)
runner.run(suite)
