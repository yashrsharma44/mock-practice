from unittest import TestCase, mock
import unittest

import wtmock_04_builtins as wk
from wtmock_04_builtins import work_on

class TestBuiltin(TestCase):

    def test_patch_dict(self):

        with mock.patch('wtmock_04_builtins.print') as mock_print:
            with mock.patch('wtmock_04_builtins.os.getcwd', return_value='/home/'):
                with mock.patch('wtmock_04_builtins.os.environ', {'MY_VAR':'testing'}):
                    self.assertEqual(work_on(), '/home/testing')
                    mock_print.assert_called_once_with('Working on /home/testing')
if __name__ == "__main__":
    unittest.main()