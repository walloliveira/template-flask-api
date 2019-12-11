import unittest
from unittest.mock import patch, MagicMock, Mock
from app.domains.users.actions import get_by_id, update, create, get
from app.domains.users.models import User


class TestUsersActions(unittest.TestCase):
    @patch('app.domains.users.actions.save')
    def test_action_create_should_be_created_new_user(self, save_mock):
        create({'name': 'a', 'email': 'a@a.com.br'})

        self.assertTrue(save_mock.called)
        calls = save_mock.call_args
        args = calls[0]
        user = args[0]
        self.assertIsInstance(user, User)
        self.assertEqual(user.name, 'a')
        self.assertEqual(user.email, 'a@a.com.br')

    @patch('app.domains.users.actions.User')
    def test_action_get_by_id_should_be_return_user(self, user_mock):
        # Arrange
        user_saved = User()
        user_saved.name = 'Name'
        user_saved.email = 'test@test.com.br'
        query = Mock()
        query.get = MagicMock(return_value=user_saved)
        user_mock.query = query

        # Action
        user = get_by_id('id')

        # Assertions
        user_mock.query.get.assert_called_once_with('id')
        self.assertEqual(user_saved, user)

    @patch('app.domains.users.actions.User')
    def test_action_get_should_be_return_users(self, user_mock):
        # Arrange
        user_saved = User()
        user_saved.name = 'Name'
        user_saved.email = 'test@test.com.br'
        query = Mock()
        query.all = MagicMock(return_value=[user_saved])
        user_mock.query = query

        # Action
        users = get()

        # Assertions
        self.assertTrue(user_mock.query.all.called)
        self.assertEqual(len(users), 1)

    @patch('app.domains.users.actions.get_by_id')
    @patch('app.domains.users.actions.commit')
    def test_action_update_should_be_updated_user(self, commit_mock, get_by_id_mock):
        # Arrange
        user_saved = User()
        user_saved.name = 'Name'
        user_saved.email = 'test@test.com.br'
        get_by_id_mock.return_value = user_saved

        # Action
        user = update('id', {'name': 'NotName'})

        # Assertions
        get_by_id_mock.assert_called_once_with('id')
        self.assertTrue(commit_mock.called)
        self.assertEqual(user.name, 'NotName')
