#-*- coding: utf-8 -*-
from typing import AbstractSet, Any, Mapping, Optional, Union
from pydantic import BaseModel

from utils.exceptions import ResponseError   

RESPONSE_INVALID_PARAMS = ResponseError(code="000001", message="wrong param")
RESPONSE_INVALID_SIGNATURE = ResponseError(code="000001", message="wrong signature")
RESPONSE_NOT_LOGIN = ResponseError(code="000003", message="login first")
RESPONSE_PERMISSION_DENIED = ResponseError(code="000004", message="not enough permission")
RESPONSE_INTERNAL_SERVER_ERROR = ResponseError(code="000004", message="internal server error")

RESPONSE_USER_NOT_EXISTS_OR_INVALID_PASSWORD = ResponseError(code="001001", message="wrong user or incorrect password")
RESPONSE_USER_NOT_EXISTS = ResponseError(code="001002", message="user not exist")

RESPONSE_CATEGORY_NOT_EXISTS = ResponseError(code="002001", message="category not exist")
RESPONSE_DUPLICATED_CATEGORY_NAME = ResponseError(code="002002", message="duplicate category")

RESPONSE_ARTICLE_NOT_EXISTS = ResponseError(code="003001", message="article not exist")

class Response(BaseModel):
    code: str = "000000"
    message: str = "success"
    data: Any = None
    
    def dict(
        self,
        *,
        include: Optional[
            Union[AbstractSet[Union[int, str]], Mapping[Union[int, str], Any]]
        ] = None,
        exclude: Optional[
            Union[AbstractSet[Union[int, str]], Mapping[Union[int, str], Any]]
        ] = None,
        by_alias: bool = False,
        skip_defaults: Optional[bool] = None,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
    ):
         return super().dict(
            include=include,
            exclude=exclude,
            by_alias=by_alias,
            skip_defaults=skip_defaults,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=True,
         )
    