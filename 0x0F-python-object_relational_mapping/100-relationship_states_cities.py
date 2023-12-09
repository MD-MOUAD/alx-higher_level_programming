#!/usr/bin/python3
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State

if __name__ == "__main__":
    db_url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    engine = create_engine(db_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="California")
    # add new city using cities relationship
    new_state.cities.append(City(name="San Francisco"))
    session.add(new_state)
    session.commit()
    session.close()
