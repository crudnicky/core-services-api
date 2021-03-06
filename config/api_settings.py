from pydantic import BaseSettings

class Settings(BaseSettings):
  app_name: str = "Core Services API"

  class Config:
    env_file = '.env.dev'