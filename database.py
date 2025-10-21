# from sqlalchemy import create_engine, text
# from sqlalchemy.orm import sessionmaker
# from dotenv import load_dotenv
# import os

# load_dotenv()

# # db_url=dialect+driver://dbuser;dbpassword;dbhost;dbport;dbname
# db_url=f'mysql+pymysql://{os.getenv("dbuser")};{os.getenv("dbpassword")};{os.getenv("dhost")};{os.getenv("dbport")};{os.getenv("dbname")}'

# engine = create_engine(db_url)

# session = sessionmaker(bind=engine)

# db = session()

# query = text("select * from user")

# users = db.execute(query).fetchall()

# print(users)




from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import url
from dotenv import load_dotenv
import os
import sys

load_dotenv()


# db_url = dialect+driver://dbuser;dbpassword;dbhost;dbport;dbname

dbuser = os.getenv("dbuser")
dbpassword = os.getenv("dbpassword")
dbhost = os.getenv("dbhost")
dbport = os.getenv("dbport")
dbname = os.getenv("dbname")

if not all([dbuser, dbpassword, dbhost, dbport, dbname]):
    raise ValueError("Missing one or more database environment variables: dbuser, dbpassword, dbhost, dbport, dbname")

# correct URL format: dialect+driver://user:password@host:port/dbname
# db_url = url.make_url(f"mysql+pymysql://{dbuser}:{dbpassword}@{dbhost}:{dbport}/{dbname}")
db_url = f"mysql+pymysql://{os.getenv('dbuser')}:{os.getenv('dbpassword')}@{os.getenv('dbhost')}:{os.getenv('dbport')}/{os.getenv('dbname')}"


engine = create_engine(db_url)

session = sessionmaker(bind=engine)

db = session()

query = text("select * from user")

result = db.execute(query)
users = result.fetchall()

print(users)



