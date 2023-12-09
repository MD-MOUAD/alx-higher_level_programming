#!/usr/bin/python3
"""Start link class to table in database 
"""
from sys import argv
from sqlalchemy import (create_engine)
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine (
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}",
        pool_pre_ping=True,
        echo=True
    )

    Base.metadata.create_all(engine)
