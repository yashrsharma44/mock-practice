from unittest import TestCase, mock
import unittest

from wtmock_01_worker import Worker, Helper

class TestWorkerModule(TestCase):

    def test_patching_class(self):
        with mock.patch('wtmock_01_worker.Helper', autospec=True) as MockHelper:
            MockHelper.return_value.get_path.return_value = 'testing'
            worker = Worker()
            MockHelper.assert_called_once_with('db')
            self.assertEqual(worker.work(),'testing')


if __name__ == "__main__":
    unittest.main()