import unittest
from datetime import datetime
from data_types import Measurement, MeasurementType
from main import sample_measurements

class TestSampleMeasurements(unittest.TestCase):
    
    def test_example_input(self):
        unsampled_measurements = [
            Measurement(datetime(2017, 1, 3, 10, 4, 45), MeasurementType.TEMP, 35.79),
            Measurement(datetime(2017, 1, 3, 10, 1, 18), MeasurementType.SPO2, 98.78),
            Measurement(datetime(2017, 1, 3, 10, 9, 7), MeasurementType.TEMP, 35.01),
            Measurement(datetime(2017, 1, 3, 10, 3, 34), MeasurementType.SPO2, 96.49),
            Measurement(datetime(2017, 1, 3, 10, 2, 1), MeasurementType.TEMP, 35.82),
            Measurement(datetime(2017, 1, 3, 10, 5, 0), MeasurementType.SPO2, 97.17),
            Measurement(datetime(2017, 1, 3, 10, 5, 1), MeasurementType.SPO2, 95.08),
        ]
        
        expected_output = [
            Measurement(datetime(2017, 1, 3, 10, 5, 0), MeasurementType.TEMP, 35.79),
            Measurement(datetime(2017, 1, 3, 10, 10, 0), MeasurementType.TEMP, 35.01),
            Measurement(datetime(2017, 1, 3, 10, 5, 0), MeasurementType.SPO2, 97.17),
            Measurement(datetime(2017, 1, 3, 10, 10, 0), MeasurementType.SPO2, 95.08),
        ]
        
        result = sample_measurements(unsampled_measurements)
        
        self.assertEqual(result, expected_output)

    def test_measurements_on_5_min_intervals(self):
        unsampled_measurements = [
            Measurement(datetime(2023, 6, 10, 10, 0, 0), MeasurementType.HR, 70),
            Measurement(datetime(2023, 6, 10, 10, 5, 0), MeasurementType.HR, 72),
            Measurement(datetime(2023, 6, 10, 10, 10, 0), MeasurementType.HR, 74),
        ]
        
        expected_output = [
            Measurement(datetime(2023, 6, 10, 10, 0, 0), MeasurementType.HR, 70),
            Measurement(datetime(2023, 6, 10, 10, 5, 0), MeasurementType.HR, 72),
            Measurement(datetime(2023, 6, 10, 10, 10, 0), MeasurementType.HR, 74),
        ]
        
        result = sample_measurements(unsampled_measurements)
        
        self.assertEqual(result, expected_output)

    def test_measurements_in_same_minute(self):
        unsampled_measurements = [
            Measurement(datetime(2023, 6, 10, 10, 3, 15), MeasurementType.HR, 65),
            Measurement(datetime(2023, 6, 10, 10, 3, 45), MeasurementType.HR, 67),
        ]
        
        expected_output = [
            Measurement(datetime(2023, 6, 10, 10, 5, 0), MeasurementType.HR, 67),
        ]
        
        result = sample_measurements(unsampled_measurements)
        
        self.assertEqual(result, expected_output)

    def test_different_measurement_types(self):
        unsampled_measurements = [
            Measurement(datetime(2023, 6, 10, 10, 4, 30), MeasurementType.SPO2, 98.5),
            Measurement(datetime(2023, 6, 10, 10, 6, 0), MeasurementType.HR, 70),
            Measurement(datetime(2023, 6, 10, 10, 8, 0), MeasurementType.TEMP, 36.6),
            Measurement(datetime(2023, 6, 10, 10, 5, 30), MeasurementType.HR, 72),
        ]
        
        expected_output = [
            Measurement(datetime(2023, 6, 10, 10, 10, 0), MeasurementType.TEMP, 36.6),
            Measurement(datetime(2023, 6, 10, 10, 10, 0), MeasurementType.HR, 70),
            Measurement(datetime(2023, 6, 10, 10, 5, 0), MeasurementType.SPO2, 98.5),
        ]
        
        result = sample_measurements(unsampled_measurements)
        
        self.assertEqual(result, expected_output)

    def test_single_measurement_type(self):
        unsampled_measurements = [
            Measurement(datetime(2023, 6, 10, 10, 2, 30), MeasurementType.SPO2, 96.5),
            Measurement(datetime(2023, 6, 10, 10, 7, 30), MeasurementType.SPO2, 97.0),
        ]
        
        expected_output = [
            Measurement(datetime(2023, 6, 10, 10, 5, 0), MeasurementType.SPO2, 96.5),
            Measurement(datetime(2023, 6, 10, 10, 10, 0), MeasurementType.SPO2, 97.0),
        ]
        
        result = sample_measurements(unsampled_measurements)
        
        self.assertEqual(result, expected_output)

    def test_no_measurements(self):
        unsampled_measurements = []
        
        expected_output = []
        
        result = sample_measurements(unsampled_measurements)
        
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
