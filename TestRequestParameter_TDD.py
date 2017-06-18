import unittest
#from AuthenticationsCreator import AuthenticationsCreator
from web.service.github.api.v3.AuthenticationsCreator import AuthenticationsCreator
from web.service.github.api.v3.RequestParameter import RequestParameter
class TestRequestParameter_TDD(unittest.TestCase):
    def test_HasAttribute(self):
        self.assertTrue(hasattr(RequestParameter, 'Get'))
        
