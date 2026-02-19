import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev")

    # Render suele dar DATABASE_URL en formato postgres://
    uri = os.environ.get("DATABASE_URL")
    if uri and uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_DATABASE_URI = uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    STORE_NAME = os.environ.get("STORE_NAME", "Progreso Tienda")
    STORE_RUC = os.environ.get("STORE_RUC", "9999999999")
    STORE_ADDRESS = os.environ.get("STORE_ADDRESS", "Quito, Ecuador")
    STORE_PHONE = os.environ.get("STORE_PHONE", "0999999999")
    TAX_RATE = float(os.environ.get("TAX_RATE", "0.12"))
