from fastapi import Request, HTTPException
import os
import requests
import pprint

class AuthVerifier:
  def __init__(self, request: Request):
    self.request = request
    self.client_id = os.getenv('OKTA_CLIENT_ID')
    self.introspect_endpoint = f"{os.getenv('OKTA_DOMAIN')}/oauth2/v1/introspect"
    self.authorized = False
  
  def get_token(self):
    return self.request.headers.get('authorization').split("Bearer ")[1]

  def get_payload(self):
    return {
      'token': self.get_token(),
      'token_type_hint': 'access_token'
    }
  
  def get_params(self):
    return {
      'client_id': self.client_id
    }
  
  def check_authorization_status(self):
    response = requests.post(self.introspect_endpoint, params=self.get_params(), data=self.get_payload())
    if response.json()['active']:
      self.authorized = True

  def is_authorized(self):
    self.check_authorization_status()
    if not self.authorized:
      raise HTTPException(status_code=401, detail="User is unauthorized.")
    else:
      return self.authorized
    
