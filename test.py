import unittest
from datetime import datetime
from main import sample_measurements, MeasType, Measurement

class TestSampleMeasurements(unittest.TestCase):
    def test_sample_measurements(self):

        unsampled_measurements = [
            Measurement(datetime(2017, 1, 3, 10, 4, 45), MeasType.TEMP, 35.79),
            Measurement(datetime(2017, 1, 3, 10, 1, 18), MeasType.SPO2, 98.78),
            Measurement(datetime(2017, 1, 3, 10, 9, 7), MeasType.TEMP, 35.01),
            Measurement(datetime(2017, 1, 3, 10, 3, 34), MeasType.SPO2, 96.49),
            Measurement(datetime(2017, 1, 3, 10, 2, 1), MeasType.TEMP, 35.82),
            Measurement(datetime(2017, 1, 3, 10, 5, 0), MeasType.SPO2, 97.17),
            Measurement(datetime(2017, 1, 3, 10, 5, 1), MeasType.SPO2, 95.08),
        ]
        
        expected_output = [
            Measurement(datetime(2017, 1, 3, 10, 5, 0), MeasType.TEMP, 35.79),
            Measurement(datetime(2017, 1, 3, 10, 10, 0), MeasType.TEMP, 35.01),
            Measurement(datetime(2017, 1, 3, 10, 5, 0), MeasType.SPO2, 97.17),
            Measurement(datetime(2017, 1, 3, 10, 10, 0), MeasType.SPO2, 95.08),
        ]
        
        result = sample_measurements(datetime(2017, 1, 3, 10, 0, 0), unsampled_measurements)
        
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
