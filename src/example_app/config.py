from pydantic import BaseSettings

# https://python.plainenglish.io/how-to-read-env-variables-without-using-the-os-module-in-python-4ab23f5429cf

class Settings(BaseSettings):

    DB_NAME: str = 'local'
    DB_USER: str = 'localuser'
    DB_HOST: str = "mysql.localhost.com"
    DB_PASSWORD: str
    API_ENDPOINT: str

    class Config:
        env_file = ".env"



settings = Settings()
print(settings.API_ENDPOINT)
print(settings.DB_HOST)
print(settings.DB_NAME)
