from unittest import mock

# We can assign attribute using three methods
# Assign directly
m = mock.Mock()
m.foo = 'bar'

assert m.foo == 'bar'

# We can use the configure_mock function
# to assign values

m.configure_mock(bar='baz')
assert m.bar == 'baz'

