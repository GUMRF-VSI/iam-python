from typing import Optional, List, Dict

from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserResponse(BaseModel):
    id: int

    email: EmailStr
    last_name: Optional[str]
    first_name: Optional[str]
    middle_name: Optional[str]

    is_staff: bool
    is_active: bool

    last_login: Optional[bool]

    created_at: datetime
    updated_at: Optional[bool]


class TokenRequest(BaseModel):
    access_token: str


class VerifyTokenResponse(BaseModel):
    is_valid: bool


class TokenData(BaseModel):
    iat: int
    exp: int
    auth_time: int
    sub: str
    sid: str
    typ: str = 'Bearer'
    roles: List[Dict]
