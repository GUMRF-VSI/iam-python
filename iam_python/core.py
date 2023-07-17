from .schemas import UserResponse

from .client import Client


class IAMService:
    def __init__(self, host: str,  access_token: str, base_url: str = '/api/v1/internal/'):
        self.__host = host
        self.__base_url = base_url
        self.__access_token = access_token

    @property
    def client(self):
        return Client(host=self.__host, base_url=self.__base_url, token=self.__access_token)

    def verify_token(self, token: str):
        response = self.client.validate_token(token)
        return response.is_valid

    def get_user(self, token: str) -> UserResponse:
        return self.client.get_user(token)
