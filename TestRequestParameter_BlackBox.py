import unittest
from database.src.Database import Database
from web.service.github.api.v3.RequestParameter import RequestParameter
from web.service.github.api.v3.AuthenticationsCreator import AuthenticationsCreator
from web.service.github.api.v3.authentication.Authentication import Authentication
from web.service.github.api.v3.authentication.NonAuthentication import NonAuthentication
from web.service.github.api.v3.authentication.BasicAuthentication import BasicAuthentication
from web.service.github.api.v3.authentication.TwoFactorAuthentication import TwoFactorAuthentication
from web.service.github.api.v3.authentication.OAuthAuthentication import OAuthAuthentication
from web.service.github.api.v3.authentication.OAuthTokenFromDatabaseAuthentication import OAuthTokenFromDatabaseAuthentication
from web.service.github.api.v3.authentication.OAuthTokenFromDatabaseAndCreateApiAuthentication import OAuthTokenFromDatabaseAndCreateApiAuthentication
import dataset
class TestRequestParameter_BlackBox(unittest.TestCase):
    def test_Create_OAuthAuthentication_BasicAuthentication_TokenApi(self):
        db = Database()
        db.Initialize()
        username = 'ytyaru' # 存在するユーザ名。Token登録済み。TwoFactorSecretなし。
        token = 'TestToken000'
        creator = AuthenticationsCreator(db, username)
        authentications = creator.Create() # [OAuthAuthentication, BasicAuthentication]
        self.assertEqual(list, type(authentications))
        self.assertEqual(2, len(authentications))
        self.assertEqual(OAuthAuthentication, type(authentications[0]))
        self.assertEqual(BasicAuthentication, type(authentications[1]))        
        reqp = RequestParameter(db, authentications)
        # Token認証API
        http_method = 'GET'
#        endpoint = 'https://api.github.com/user'
        endpoint = 'user'
        params = reqp.Get(http_method, endpoint)
        print(params)
        self.assertTrue('headers' in params)
        self.assertTrue('Time-Zone' in params['headers'])
        self.assertTrue('Asia/Tokyo' in params['headers']['Time-Zone'])
        self.assertTrue('User-Agent' in params['headers'])
        self.assertEqual('', params['headers']['User-Agent'])
        self.assertTrue('Accept' in params['headers'])
        self.assertEqual('application/vnd.github.v3+json', params['headers']['Accept'])
        self.assertTrue('Authorization' in params['headers'])
        self.assertEqual('token ' + token, params['headers']['Authorization'])
    def test_Create_OAuthAuthentication_BasicAuthentication_BasicApi(self):
        db = Database()
        db.Initialize()
        username = 'ytyaru' # 存在するユーザ名。Token登録済み。TwoFactorSecretなし。
        token = 'TestToken000'
        creator = AuthenticationsCreator(db, username)
        authentications = creator.Create() # [OAuthAuthentication, BasicAuthentication]
        self.assertEqual(list, type(authentications))
        self.assertEqual(2, len(authentications))
        self.assertEqual(OAuthAuthentication, type(authentications[0]))
        self.assertEqual(BasicAuthentication, type(authentications[1]))        
        reqp = RequestParameter(db, authentications)
        # Basic認証のみ使えるAPI
        http_method = 'POST'
#        endpoint = 'https://api.github.com/authorizations'
        endpoint = 'authorizations'
        params = reqp.Get(http_method, endpoint)
        print(params)
        self.assertTrue('headers' in params)
        self.assertTrue('Time-Zone' in params['headers'])
        self.assertTrue('Asia/Tokyo' in params['headers']['Time-Zone'])
        self.assertTrue('User-Agent' in params['headers'])
        self.assertEqual('', params['headers']['User-Agent'])
        self.assertTrue('Accept' in params['headers'])
        self.assertEqual('application/vnd.github.v3+json', params['headers']['Accept'])
#        self.assertTrue('Authorization' in params['headers'])
#        self.assertEqual('token ' + token, params['headers']['Authorization'])
        self.assertTrue('auth' in params)
        self.assertTrue(tuple, type(params['auth']))
        self.assertTrue(2, len(params['auth']))
        self.assertTrue(username, params['auth'][0])
        db_account = dataset.connect('sqlite:///' + './database/res/db/GitHub.Accounts.sqlite3')
        password = db_account['Accounts'].find_one(Username=username)['Password']
        self.assertTrue(username, params['auth'][0])
        self.assertTrue(password, params['auth'][1])
    def test_Create_OAuthAuthentication_TwoFactorAuthentication_TokenApi(self):
        db = Database()
        db.Initialize()
        username = 'csharpstudy0' # 存在するユーザ名。Token登録済み。TwoFactorSecretあり。
#        token = 'dummy00000000'
        creator = AuthenticationsCreator(db, username)
        authentications = creator.Create() # [OAuthAuthentication, BasicAuthentication]
        self.assertEqual(list, type(authentications))
        self.assertEqual(2, len(authentications))
        self.assertEqual(OAuthAuthentication, type(authentications[0]))
        self.assertEqual(TwoFactorAuthentication, type(authentications[1]))        
        reqp = RequestParameter(db, authentications)
        # Token認証API
        http_method = 'GET'
#        endpoint = 'https://api.github.com/user'
        endpoint = 'user'
        params = reqp.Get(http_method, endpoint)
        print(params)
        self.assertTrue('headers' in params)
        self.assertTrue('Time-Zone' in params['headers'])
        self.assertTrue('Asia/Tokyo' in params['headers']['Time-Zone'])
        self.assertTrue('User-Agent' in params['headers'])
        self.assertEqual('', params['headers']['User-Agent'])
        self.assertTrue('Accept' in params['headers'])
        self.assertEqual('application/vnd.github.v3+json', params['headers']['Accept'])
        self.assertTrue('Authorization' in params['headers'])
#        self.assertEqual('token ' + token, params['headers']['Authorization'])
    def test_Create_OAuthAuthentication_TwoFactorAuthentication_BasicApi(self):
        db = Database()
        db.Initialize()
        username = 'csharpstudy0' # 存在するユーザ名。Token登録済み。TwoFactorSecretあり。
        creator = AuthenticationsCreator(db, username)
        authentications = creator.Create() # [OAuthAuthentication, BasicAuthentication]
        self.assertEqual(list, type(authentications))
        self.assertEqual(2, len(authentications))
        self.assertEqual(OAuthAuthentication, type(authentications[0]))
        self.assertEqual(TwoFactorAuthentication, type(authentications[1]))        
        reqp = RequestParameter(db, authentications)
        # Basic認証のみ使えるAPI
        http_method = 'POST'
#        endpoint = 'https://api.github.com/authorizations'
        endpoint = 'authorizations'
        params = reqp.Get(http_method, endpoint)
        print(params)
        self.assertTrue('headers' in params)
        self.assertTrue('Time-Zone' in params['headers'])
        self.assertTrue('Asia/Tokyo' in params['headers']['Time-Zone'])
        self.assertTrue('User-Agent' in params['headers'])
        self.assertEqual('', params['headers']['User-Agent'])
        self.assertTrue('X-GitHub-OTP' in params['headers'])
        self.assertTrue('Accept' in params['headers'])
        self.assertEqual('application/vnd.github.v3+json', params['headers']['Accept'])
        self.assertTrue('auth' in params)
        self.assertTrue(tuple, type(params['auth']))
        self.assertTrue(2, len(params['auth']))
        self.assertTrue(username, params['auth'][0])
        db_account = dataset.connect('sqlite:///' + './database/res/db/GitHub.Accounts.sqlite3')
        password = db_account['Accounts'].find_one(Username=username)['Password']
        self.assertTrue(username, params['auth'][0])
        self.assertTrue(password, params['auth'][1])

