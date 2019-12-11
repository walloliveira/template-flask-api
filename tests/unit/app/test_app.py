from werkzeug.exceptions import InternalServerError

from app.exceptions import NotFoundException
import unittest

from app import create_app

_app = create_app()


@_app.route('/test-not-found-exception')
def route_not_found_exception():
    raise NotFoundException()


@_app.route('/test-internal-server-error-exception')
def route_internal_server_error_exception():
    raise InternalServerError()


class TestApp(unittest.TestCase):

    def test_app_should_be_raises_not_found_exception_and_code_404(self):
        client = _app.test_client()
        response = client.get('/test-not-found-exception')
        data = response.get_json()
        self.assertEqual(data.get('code'), 404)
        self.assertEqual(data.get('message'), 'Not Found Exception')

    def test_app_should_be_raises_internal_server_error_exception_and_code_500(self):
        client = _app.test_client()
        response = client.get('/test-internal-server-error-exception')
        data = response.get_json()
        self.assertEqual(data.get('code'), 500)
        self.assertEqual(data.get('message'), 'Sorry, we cant process request. Try again.')
