from unittest import mock

# To override the calls to the mock, i.e. you want to
# access the methods return value, you can use return_value
# Note that, the mock object that you created itself would 
# have a return statement and not a method, using which you 
# would get the return value. 

m = mock.Mock()

# Set the return value of the mock object
m.return_value = 42
assert m() == 42

# You can also use side_effect to set a return value.
# However it acts as a proxy, so you can provide a 
# function say A, so that it can pass through the given
# function A, to preprocess the value, and return
# the data to the callee
m.side_effect = ['yash','piyush','kritika']

assert m() == 'yash'
assert m() == 'piyush'
assert m() == 'kritika'

m.side_effect = RuntimeError('Boom!')

try:
    m()
except RuntimeError:
    assert True
else:
    assert False