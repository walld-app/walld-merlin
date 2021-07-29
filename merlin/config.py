from pydantic import BaseSettings
from kz159_utils import config, CustomLogger


class Config(BaseSettings):
    LOG_LEVEL: str


CustomLogger(config.SERVICE_NAME, Config.LOG_LEVEL)
