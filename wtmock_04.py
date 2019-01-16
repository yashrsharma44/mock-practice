from unittest import mock

m = mock.Mock()

# m.assert_called()

try:
    m.assert_called_once()
except AssertionError:
    # print('Hey')
    assert True
else:
    assert False