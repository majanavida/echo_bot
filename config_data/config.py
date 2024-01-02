from dataclasses import dataclass
from dotenv import Env


@dataclass
class TgBot:
    token: str # Telegram API token 
    
    
@dataclass
class Config:
    tg_bot: TgBot
    
    
def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))