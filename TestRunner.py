import unittest

import HtmlTestRunner

from tests import FarmRiseTests


loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(FarmRiseTests))

runner = HtmlTestRunner.HTMLTestRunner(output='test-report', verbosity=2)
runner.run(suite)
