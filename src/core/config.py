from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int

    def get_database_url(self) -> str:
        return (f"postgresql+asyncpg://"
                f"{self.DB_USER}:"
                f"{self.DB_PASSWORD}@"
                f"{self.DB_HOST}:"
                f"{self.DB_PORT}/{self.DB_NAME}")

settings = Settings()  # type: ignore