import os
from dotenv import load_dotenv

load_dotenv()

ENV_VARIABLES = {
    'DATABASE_NAME': os.getenv('DATABASE_NAME'),
    'DATABASE_USER': os.getenv('DATABASE_USER'),
    'DATABASE_PASSWORD': os.getenv('DATABASE_PASSWORD'),
    'DATABASE_HOST': os.getenv('DATABASE_HOST'),
    'DATABASE_PORT': os.getenv('DATABASE_PORT')
}
