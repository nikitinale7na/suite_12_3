import unittest
import test12_2, test12_1

runtest_ = unittest.TestSuite()
loader = unittest.TestLoader()
runtest_.addTest(loader.loadTestsFromTestCase(test12_2.TournamentTest))
runtest_.addTest(loader.loadTestsFromTestCase(test12_1.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runtest_)
