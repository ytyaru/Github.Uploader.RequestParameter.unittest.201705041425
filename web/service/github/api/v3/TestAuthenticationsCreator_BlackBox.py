import unittest
import database
from AuthenticationsCreator import AuthenticationsCreator
class TestAuthenticationsCreator_BlackBox(unittest.TestCase):
    def test_Create_UnregisteredException_ConstractorParameter(self):
        db = database.src.Database.Database()
        db.Initialize()
        username = 'NoneExistUsername' # 存在しないユーザ名
        creator = AuthenticationsCreator(db, username)
        with self.assertRaises(Exception) as e:
            creator.Create()
            self.assertEqual(e.msg, '指定したユーザ {0} はDBに未登録です。登録してから実行してください。'.format(username))
    def test_Create_UnregisteredException_MethodParameter(self):
        db = database.src.Database.Database()
        db.Initialize()
        username = 'ytyaru' # 存在するユーザ名
        creator = AuthenticationsCreator(db, username) # 
        with self.assertRaises(Exception) as e:
            username = 'NoneExistUsername' # 存在しないユーザ名
            creator.Create(username=username)
            self.assertEqual(e.msg, '指定したユーザ {0} はDBに未登録です。登録してから実行してください。'.format(username))
            
