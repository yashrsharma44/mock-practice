from unittest import mock
import unittest

'''
This file demonstrates the fact, that mock creates a stub
to simulate a given function. However, there is a problem
with this approach, that the original function can change
its parameters, and the test still passes, as mock does not
care about the list of parameters.
Moreover, if we call the inbuilt functions on a given mock 
object, we still get no errors, as mock basically accepts new
function and returns a new instance of MagicMock for everything
    To prevent the misuse of such practices, you can ensure that
the correct method is being called, and that the functions do exist.
mock provides the tool to prevent them, called speccing.
Just pass in this parameter - autospec=True
'''

