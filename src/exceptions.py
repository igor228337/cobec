from fastapi import HTTPException


# HTTP исключения
class HTTPNotCorrectTronAddress(HTTPException):
    def __init__(self):
        super().__init__(400, "Неправильный Tron адрес")

class HTTPNotFoundTronAddress(HTTPException):
    def __init__(self):
        super().__init__(404 , "Tron адрес не найден")

class HTTPServerBad(HTTPException):
    def __init__(self):
        super().__init__(500, "Серверу плохо")

class HTTPNotVerifyDataError(HTTPException):
    def __init__(self):
        super().__init__(401, "Неверные учетные данные")