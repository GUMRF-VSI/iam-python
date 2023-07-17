import jwt

from .schemas import TokenData


def parse_token(token) -> TokenData:
    return TokenData.model_validate(jwt.decode(token, options={"verify_signature": False}))
