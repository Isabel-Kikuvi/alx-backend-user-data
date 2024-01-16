#!/usr/bin/env python3
"""
Module for authentication
"""

from typing import List, TypeVar
from flask import request


class Auth:
    """a class to manage the API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """public method to check if auth is required
        """
        return False


    def authorization_header(self, request=None) -> str:
        """public method that gets auth header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """public method to return flask object
        """
        return None
