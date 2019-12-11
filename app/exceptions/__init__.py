from werkzeug.exceptions import HTTPException


class BadRequestException(HTTPException):
    def __init__(self, msg: str = 'Bad Request Exception'):
        super().__init__(description=msg)
        self.code = 400


class UnauthorizedException(HTTPException):
    def __init__(self, msg: str = 'Unauthorized Exception'):
        super().__init__(description=msg)
        self.code = 401


class NotFoundException(HTTPException):
    def __init__(self, msg: str = 'Not Found Exception'):
        super().__init__(description=msg)
        self.code = 404


class ConflictException(HTTPException):
    def __init__(self, msg: str = 'Conflict Exception'):
        super().__init__(description=msg)
        self.code = 409


class UnprocessableException(HTTPException):
    def __init__(self, msg: str = 'Unprocessable Exception'):
        super().__init__(description=msg)
        self.code = 422
