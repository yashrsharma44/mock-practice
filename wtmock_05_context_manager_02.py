from io import StringIO
from unittest import TestCase, mock
import unittest
from wtmock_05_context_manager_01 import size_of

class TestContextManager(TestCase):

    def test_context_manager(self):
        with mock.patch('wtmock_05_context_manager_01.open') as mock_open:
            mock_open.return_value.__enter__.return_value = StringIO('testing')
            self.assertEqual(size_of(),7)

if __name__ == "__main__":
    unittest.main()
