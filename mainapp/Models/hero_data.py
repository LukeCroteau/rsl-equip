from sqlalchemy import Column, Integer, String
from mainapp.database import Base

class Hero(Base):
    ''' Base class for Hero data '''
    __tablename__ = 'heroes'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    hero_type = Column(String)
    hp = Column(Integer)
    attack = Column(Integer)
    defense = Column(Integer)
    speed = Column(Integer)
    crit_rate = Column(Integer)
    crit_damage = Column(Integer)
    resistance = Column(Integer)
    accuracy = Column(Integer)

    def __repr__(self):
        return str.format('<Hero {} - {}>', self.id, self.name)
