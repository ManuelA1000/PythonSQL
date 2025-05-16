import os

from dotenv import load_dotenv
from sqlalchemy import create_engine,text

# Load environment variables
load_dotenv()
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')

# Create engine using environment variables
# engine = create_engine('mysql+pymysql://username:password@host/database_name')
engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}')

# read database creation script from schema.sql and execute to create orders table
with open('schema.sql','r') as file:
    sql_script = file.read()

# Create a connection and execute the SQL script
try:
    with engine.connect() as connection:
        connection.execute(text(sql_script))
        connection.commit()
        connection.close()

    print('Table created successfully')

except Exception as e:
    print(f'Error creating table: {e}')