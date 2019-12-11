import unittest

from app.domains.users.models import User
from uuid import uuid4


class TestUsersModels(unittest.TestCase):
    def test_user_model_should_be_serialized(self):
        id = str(uuid4())
        user = User(id=id, name='Teste', email='test@test.com')
        json = user.serialize()
        self.assertEqual(json['id'], id)
        self.assertEqual(json['name'], 'Teste')
