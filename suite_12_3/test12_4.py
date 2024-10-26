import unittest
from suite_12_3 import runner_3 as run_3
import logging


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            hum1 = run_3.Runner('Иванов', -3)
            for i in range(10):
                hum1.walk()
            self.assertEqual(hum1.distance, 50)
            logging.info(f'"test_walk" выполнен успешно {hum1.walk}')
        except  ValueError as VE:
            logging.warning(f'Неверная скорость для Runner. ValueError: {VE}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            hum1 = run_3.Runner(9)
            for i in range(10):
                hum1.run()
            self.assertEqual(hum1.distance, 100)
            logging.info(f'"test_run" выполнен успешно {hum1.run}')
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner\n{e}")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        hum1 = run_3.Runner('Иванов')
        hum2 = run_3.Runner('Петров')
        for i in range(10):
            hum1.walk()
            hum2.run()  # тестируем на 2 разных бегунах разные методы с разными дистанциями

        self.assertNotEqual(hum1.distance, 150)


if __name__ == '__main__':
    unittest.main()

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                    encoding='utf-8', format='%(asctime)s | %(funcName)s | %(levelname)s | %(message)s')
