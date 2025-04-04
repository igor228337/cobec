from fastapi import Request
from sqladmin.authentication import AuthenticationBackend
import secrets

from src.exceptions import HTTPNotVerifyDataError
from src.enviroment import enviroment


class BasicAuthBackend(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username = form.get("username")
        password = form.get("password")

        # Проверка логина и пароля
        correct_username = secrets.compare_digest(username, enviroment.LOGIN_ADMIN)
        correct_password = secrets.compare_digest(password, enviroment.PASSWORD_ADMIN)

        if not (correct_username and correct_password):
            raise HTTPNotVerifyDataError()

        # Сохраняем пользователя в сессии
        request.session.update({"username": username})
        return True

    async def logout(self, request: Request) -> bool:
        # Очищаем сессию
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        # Проверяем, авторизован ли пользователь
        username = request.session.get("username")
        return username == enviroment.LOGIN_ADMIN
