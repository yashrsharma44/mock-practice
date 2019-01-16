'''
Suppose, if we want to patch a class object,
we can use patch.object function
Here, we pass the class object to be patched,
and the name of the attribute/method that we want to
patch

'''

from unittest import TestCase, mock
import unittest

from wtmock_01_worker import Worker, Helper
from wtmock_06_class_attributes_01 import Pricer

class TestWorker(TestCase):

    def test_patching_class(self):

        with mock.patch.object(Helper, 'get_path', return_value='testing'):
            worker = Worker()
            self.assertEqual(worker.helper.path, 'db')
            self.assertEqual(worker.work(),'testing')


class TestClassAttributes(TestCase):
    '''
    This class demonstrates the different ways to test
    out the class attributes. We will give a docstring 
    what method we will demonstrate, and progress 
    accordingly
    '''
    
    def test_patch_instance_attribute(self):
        '''
        In this method, we are creating an object
        and setting the class attributes, and then
        asserting it.
        Note that this is a safe method, as it is not infecting
        the value of class attribute when used by other
        tests.
        '''

        pricer = Pricer()
        pricer.DISCOUNT = 0.5
        self.assertAlmostEqual(pricer.get_discounted_price(100), 50.0)

    def test_set_class_attribute(self):
        '''
        In this method, we set the class attribute
        and then test out by assertion. Note that,
        the class attribute gets infected, and cannot be used
        by other methods. One has to reset the class
        attributes
        
        '''
        Pricer.DISCOUNT = 0.5
        pricer = Pricer()
        self.assertAlmostEqual(pricer.get_discounted_price(100),50.0)

    @unittest.expectedFailure
    def test_patch_incorrect_class_attribute(self):
        '''
        This method patches out the class attribute, however
        it patches out the incorrect class attribute.
        This demonstrates a certain fact, that in previous test
        we are hardcoding the class attribute. If somehow, the
        class attributes' name changes, the test as expected,
        would fail, however the message would not be clear.
        So in order, to provide clear message, we can patch 
        out the class' attribute, and if the main function changes
        the class attribute, then it would raise error that the 
        class attributes don't match
        
        ########################################
        Difference between mock.patch and mock.patch.object
        For mock.patch, we have to pass in the full module
        which it is coming,
        while with mock.patch.object, we are mocking the class itself
        '''
        with mock.patch.object(Pricer,'PERCENTAGE',1):
            pricer = Pricer()
            self.assertAlmostEqual(pricer.get_discounted_price(100),100)

    def test_patch_class_attribute(self):
        with mock.patch.object(Pricer,'DISCOUNT',1):
            pricer = Pricer()
            self.assertAlmostEqual(pricer.get_discounted_price(100),100)
if __name__ == "__main__":
    unittest.main()