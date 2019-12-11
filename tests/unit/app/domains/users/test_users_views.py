from tests.unit import AbstractViewUnitTest
from unittest.mock import patch, MagicMock, Mock


class TestUsersViews(AbstractViewUnitTest):

    @patch('app.domains.users.views.get_users')
    def test_get_users_should_be_1(self, get_user_mock):
        # Arrange
        obj = Mock()
        obj.serialize = MagicMock(return_value={})
        get_user_mock.return_value = [obj]

        # Action
        response = self._client.get('/users')
        data = response.get_json()

        # Assertions
        self.assertEqual(len(data), 1)
        self.assertTrue(get_user_mock.called)

    @patch('app.domains.users.views.get_user_by_id')
    def test_get_user_by_id_should_be_1(self, get_user_by_id_mock):
        # Arrange
        obj = Mock()
        obj.serialize = MagicMock(return_value={})
        get_user_by_id_mock.return_value = obj
        id = '1'

        # Action
        response = self._client.get('/users/{}'.format(id))

        # Assertions
        self.assertEqual(response.status_code, 200)
        get_user_by_id_mock.assert_called_once_with(id)

    @patch('app.domains.users.views.create_user')
    def test_post_user_should_be_created(self, create_user_mock):
        # Arrange
        payload = {
            'name': 'AAAA',
            'email': 'asdfdasfasdff',
        }
        obj = Mock()
        obj.serialize = MagicMock(return_value={})
        create_user_mock.return_value = obj
        # Action
        response = self._client.post('/users', json=payload)

        # Assertions
        self.assertEqual(response.status_code, 201)
        create_user_mock.assert_called_once_with({
            'name': 'AAAA',
            'email': 'asdfdasfasdff',
        })

    @patch('app.domains.users.views.update_user')
    def test_put_user_should_be_updated(self, update_user_mock):
        # Arrange
        _id = '1'
        obj = Mock()
        obj.serialize = MagicMock(return_value={'name': 'AAA'})
        update_user_mock.return_value = obj

        # Action
        response = self._client.put('/users/{}'.format(_id), json={
            'name': 'BBBB',
        })

        # Assertions
        self.assertEqual(response.status_code, 200)
        update_user_mock.assert_called_once_with('1', {
            'name': 'BBBB',
        })
