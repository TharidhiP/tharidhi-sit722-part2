import os

class Settings:
    DATABASE_URL: str = os.getenv("postgresql://sit722_week6_user:DVVbPrxfI3ta80cpVAq5xdFnoBeevrPj@dpg-cr2ae22j1k6c73ekigig-a.oregon-postgres.render.com/sit722_week6")

settings = Settings()
