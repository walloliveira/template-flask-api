import unittest

from app.exceptions import BadRequestException, UnauthorizedException, ConflictException, UnprocessableException, \
    NotFoundException


class TestExceptions(unittest.TestCase):
    def test_not_found_exception_should_be_code_404_and_msg_is_default_value(self):
        ex = NotFoundException()
        self.assertEqual(ex.code, 404)
        self.assertEqual(ex.description, 'Not Found Exception')

    def test_bad_request_exception_should_be_code_400_and_msg_is_default_value(self):
        ex = BadRequestException()
        self.assertEqual(ex.code, 400)
        self.assertEqual(ex.description, 'Bad Request Exception')

    def test_unauthorized_exception_should_be_code_401_and_msg_is_default_value(self):
        ex = UnauthorizedException()
        self.assertEqual(ex.code, 401)
        self.assertEqual(ex.description, 'Unauthorized Exception')

    def test_conflict_exception_should_be_code_404_and_msg_is_default_value(self):
        ex = ConflictException()
        self.assertEqual(ex.code, 409)
        self.assertEqual(ex.description, 'Conflict Exception')

    def test_unprocessable_exception_should_be_code_404_and_msg_is_default_value(self):
        ex = UnprocessableException()
        self.assertEqual(ex.code, 422)
        self.assertEqual(ex.description, 'Unprocessable Exception')
