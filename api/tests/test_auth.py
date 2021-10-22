from lib.auth import AuthVerifier
from . mocks.mock_request import request

auth = AuthVerifier(request)

def test_active_token():
  # Tests that an active token returns a boolean
  # from the class
  assert True == False

def test_unauthenticated_token():
  # Tests that an incorrect token raises a 401 error
  assert True == False