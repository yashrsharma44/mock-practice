from unittest import TestCase, mock
import unittest
from wtmock_01_work import work_on

class TestWorkMockingModule(TestCase):
    '''
    Using mock's patch method, we can simulate dummy imports
    of a module. Note that we patch those modules, whose test
    we are carrying on.
    Each of the Python module has its own set of imported modules
    For eg, we can have a module A, which import os, scrapy and json
    So if we want to patch os, so that we can simulate a dummy
    object/event for os getting used, we would patch A.os and 
    not os itself. We know that os is a global module, and patching 
    it would effect other tests.
    We can directly patch A.os, so we would simulate a os module
    in the function itself. Then the function can perform the requisite
    method calls with the module, and then we can check if the module
    is getting called, or if provided a return value, what it is returning.
    '''

    def test_using_context_manager(self):
        with mock.patch('wtmock_01_work.os') as mocked_os:
            work_on()
            mocked_os.getcwd.assert_called_once()

    @mock.patch('wtmock_01_work.os')
    def test_using_decorator(self, mocked_os):
        '''
        we can use mock.patch as a decorator 
        to pass the patched object.
        Note that we need to pass in a parameter
        space to provide, the mocked object
        '''

        work_on()
        mocked_os.getcwd.assert_called_once()

    def test_using_return_value(self):
        '''
        with mock, you can mock internal objects
        that can return a pre-defined value.
        Using them, you can perform operations
        which is normally possible if you execute 
        them for real, but for mock, you can literally
        mock  out the internal objects
        '''

        with mock.patch('wtmock_01_work.os.getcwd', return_value='testing'):
            assert work_on() == 'testing'

if __name__ == "__main__":
    unittest.main()