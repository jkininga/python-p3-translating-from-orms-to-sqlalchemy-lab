from models import Dog
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_table(base,engine):
  base.metadata.create_all(engine)

def save(session, dog):
    # dog = Dog(name = 'Kali', breed = 'German Shepard')
    session.add(dog)
    session.commit()
    
def get_all(session):
    return [dog for dog in session.query(Dog)]

def find_by_name(session, name):
    return session.query(Dog).filter_by(name = name).first()

def find_by_id(session, id):
    return session.query(Dog).filter_by(id = id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name = name, breed = breed).first()

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()
