import unittest
from app import app


class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_predict_endpoint_valid_input(self):
        # Sample data matching the Iris dataset format
        sample_data = {
            'sepal_length': 5.1,
            'sepal_width': 3.5,
            'petal_length': 1.4,
            'petal_width': 0.2
        }
        response = self.app.post('/predict', json=sample_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('prediction', response.json)

    def test_predict_endpoint_error_handling(self):
        # Incorrect data format to test error handling
        incorrect_data = {}
        response = self.app.post('/predict', json=incorrect_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('error', response.json)


if __name__ == '__main__':
    unittest.main()
