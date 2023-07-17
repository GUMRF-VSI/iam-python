import requests

from .schemas import UserResponse, TokenRequest, VerifyTokenResponse
from .utils import parse_token
from .exceptions import UserNotFound


class Client:
    def __init__(self, host: str, base_url: str, token: str):
        self._host = host
        self._base_url = base_url
        self._token = token
        self.session = requests.Session()

    @property
    def api_url(self):
        end_slash = '/' if not self._base_url.endswith('/') else ''
        start_slash = '/' if not self._base_url.startswith('/') else ''
        return f'{self._host}{start_slash}{self._base_url}{end_slash}'

    def url(self, path):
        end_slash = '/' if not path.endswith('/') else ''
        start_slash = '/' if not path.startswith('/') else ''
        return f'{self.api_url}/{start_slash}{path}{end_slash}'

    def get_user(self, token) -> UserResponse:
        token_data = parse_token(token)
        response = self.session.get(url=self.url(f'/user/{token_data.sub}'))
        if response.status_code == '404':
            raise UserNotFound(f'User with sub {token_data.sub} not found!')
        return UserResponse.model_validate_json(response.text)

    def validate_token(self, token):
        payload = TokenRequest(access_token=token)
        response = self.session.post(url=self.url('/token/verify'), json=payload.model_dump_json())
        return VerifyTokenResponse.model_validate_json(response.text)
