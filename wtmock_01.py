from unittest import mock
import pytest

m = mock.Mock()

assert isinstance(m.foo, mock.Mock)
assert isinstance(m.bar, mock.Mock)
assert isinstance(m(), mock.Mock)
assert m.foo is not m.bar is not m()

'''
Here we can create a stub, or a dummy object
with arbitrary attributes and methods.
The mock.Mock() gives us the dummy object that
we discussed, and we can attach any attribute
or method, which can be accessed as another
mock object.
Note that one mock object is different from another
so that needs to be taken care of.

'''

# # Same works for mocker, a fixture that provides plugin for 
# # using pytest facilities in mock

# m1 = mocker.Mock()
# m1.foo = 'bar'
# assert m1.foo == 'bar'
