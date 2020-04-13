from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from mainapp.database import Base

class AccountHero(Base):
    ''' Base class for Account Hero data '''
    __tablename__ = 'account_heroes'
    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey('accounts.id'), index=True)

    def __repr__(self):
        return str.format('<Account {} - {}>', self.name, self.id)

class Account(Base):
    ''' Base class for Account data '''
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    arena_bonus = Column(Integer)
    heroes = relationship('AccountHero', backref='owner', lazy='dynamic')
    equipment = relationship('Artifact', backref='owner', lazy='dynamic')

    def __repr__(self):
        return str.format('<Account {} - {}>', self.name, self.id)
