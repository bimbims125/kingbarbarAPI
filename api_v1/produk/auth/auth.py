from django.http import HttpRequest
from ninja.security import HttpBasicAuth
from typing import Optional

class BasicAuth(HttpBasicAuth):
  def authenticate(self, request, username, password) -> str:
    if username == 'adminkingbarbar' and password == 'adminbarbar':
      return username