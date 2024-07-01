import unittest
from lamrand.lamrand import LamRand
from openpyxl import Workbook, load_workbook
from openpyxl.chart import LineChart, Reference
import os
import statistics

class TestLamRand(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.excel_file = 'test_results.xlsx'
        if not os.path.exists(cls.excel_file):
            wb = Workbook()
            ws = wb.active
            ws.title = "TestResults"
            ws.append(["Test Name", "Result", "Details"])
            wb.save(cls.excel_file)

    def setUp(self):
        self.randomizer = LamRand()

    def save_to_excel(self, test_name, result, details=""):
        wb = load_workbook(self.excel_file)
        ws = wb.active
        ws.append([test_name, result, details])
        wb.save(self.excel_file)

    def test_next(self):
        values = [self.randomizer.next() for _ in range(1000)]
        self.assertEqual(len(values), len(set(values)), "Values are not unique")
        self.save_to_excel("test_next", "passed")
        print("✔ test_next passed")

    def test_next_float(self):
        values = [self.randomizer.next_float() for _ in range(100000)]
        mean = statistics.mean(values)
        self.assertTrue(0 <= min(values) < max(values) <= 1, "Values are out of range")
        self.assertAlmostEqual(mean, 0.5, delta=0.01, msg="Mean is not approximately 0.5")
        self.save_to_excel("test_next_float", "passed", f"Mean: {mean}")
        print("✔ test_next_float passed")

    def test_next_int(self):
        values = [self.randomizer.next_int(1, 10) for _ in range(100000)]
        counts = [values.count(i) for i in range(1, 11)]
        self.assertTrue(all(9000 <= count <= 11000 for count in counts), "Values are not evenly distributed")
        self.save_to_excel("test_next_int", "passed", f"Counts: {counts}")
        print("✔ test_next_int passed")

    def test_next_gaussian(self):
        values = [self.randomizer.next_gaussian() for _ in range(100000)]
        mean = statistics.mean(values)
        stdev = statistics.stdev(values)
        self.assertAlmostEqual(mean, 0, delta=0.1, msg="Mean is not approximately 0")
        self.assertAlmostEqual(stdev, 1, delta=0.1, msg="Standard deviation is not approximately 1")
        self.save_to_excel("test_next_gaussian", "passed", f"Mean: {mean}, Stdev: {stdev}")
        print("✔ test_next_gaussian passed")

    def test_next_bool(self):
        values = [self.randomizer.next_bool() for _ in range(100000)]
        true_count = values.count(True)
        false_count = values.count(False)
        self.assertTrue(49000 <= true_count <= 51000, "True values are not evenly distributed")
        self.assertTrue(49000 <= false_count <= 51000, "False values are not evenly distributed")
        self.save_to_excel("test_next_bool", "passed", f"True: {true_count}, False: {false_count}")
        print("✔ test_next_bool passed")

    def test_shuffle(self):
        data = [i for i in range(10)]
        shuffled_data = self.randomizer.shuffle(data[:])
        self.assertNotEqual(data, shuffled_data, "Data is not shuffled")
        self.assertCountEqual(data, shuffled_data, "Shuffled data does not have the same elements")
        self.save_to_excel("test_shuffle", "passed")
        print("✔ test_shuffle passed")

    def test_next_string(self):
        value = self.randomizer.next_string(10)
        self.assertIsInstance(value, str)
        self.assertEqual(len(value), 10)
        self.save_to_excel("test_next_string", "passed")
        print("✔ test_next_string passed")

    @classmethod
    def tearDownClass(cls):
        cls.create_charts()

    @classmethod
    def create_charts(cls):
        wb = load_workbook(cls.excel_file)
        ws = wb.active

        chart = LineChart()
        chart.title = "Test Results Over Time"
        chart.y_axis.title = "Result"
        chart.x_axis.title = "Test Case"

        data = Reference(ws, min_col=2, min_row=1, max_row=ws.max_row, max_col=2)
        categories = Reference(ws, min_col=1, min_row=2, max_row=ws.max_row)
        chart.add_data(data, titles_from_data=True)
        chart.set_categories(categories)
        chart.height = 10
        chart.width = 20

        ws.add_chart(chart, "D1")
        wb.save(cls.excel_file)

if __name__ == '__main__':
    unittest.main()