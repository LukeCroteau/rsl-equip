from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from mainapp.database import Base

class StatTypes(Base):
    ''' Base class for Stat Type Constants data '''
    __tablename__ = 'stat_types'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    flat = Column(Boolean)

    def __repr__(self):
        return str.format('<StatType {} - {}>', self.id, self.name)

class ArtifactTypes(Base):
    ''' Base class for Artifact Type Constants data '''
    __tablename__ = 'artifact_types'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    def __repr__(self):
        return str.format('<ArtifactType {} - {}>', self.id, self.name)

class ArtifactSets(Base):
    ''' Base class for Artifact Set Constants data '''
    __tablename__ = 'artifact_sets'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    count_for_bonus = Column(Integer)
    bonus_stat_1 = Column(Integer, ForeignKey('stat_types.id'))
    bonus_value_1 = Column(Integer)
    bonus_flat_1 = Column(Boolean)
    bonus_stat_2 = Column(Integer, ForeignKey('stat_types.id'))
    bonus_value_2 = Column(Integer)
    bonus_flat_2 = Column(Boolean)

    def __repr__(self):
        return str.format('<ArtifactSet {} - {}>', self.id, self.name)

class Artifact(Base):
    ''' Base class for Artifact data '''
    __tablename__ = 'artifacts'
    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey('accounts.id'), index=True)
    set = Column(Integer, ForeignKey('artifact_sets.id'), index=True)
    type = Column(Integer, ForeignKey('artifact_types.id'), index=True)
    stars = Column(Integer, index=True)
    level = Column(Integer, index=True)
    equipped_to = Column(Integer, index=True)
    main_stat = Column(Integer, ForeignKey('stat_types.id'), index=True)
    main_stat_value = Column(Integer)
    sub_stat_1 = Column(Integer, ForeignKey('stat_types.id'), index=True)
    sub_stat_1_value = Column(Integer)
    sub_stat_1_upgrades = Column(Integer)
    sub_stat_1_rune_value = Column(Integer)
    sub_stat_2 = Column(Integer, ForeignKey('stat_types.id'), index=True)
    sub_stat_2_value = Column(Integer)
    sub_stat_2_upgrades = Column(Integer)
    sub_stat_2_rune_value = Column(Integer)
    sub_stat_3 = Column(Integer, ForeignKey('stat_types.id'), index=True)
    sub_stat_3_value = Column(Integer)
    sub_stat_3_upgrades = Column(Integer)
    sub_stat_3_rune_value = Column(Integer)
    sub_stat_4 = Column(Integer, ForeignKey('stat_types.id'), index=True)
    sub_stat_4_value = Column(Integer)
    sub_stat_4_upgrades = Column(Integer)
    sub_stat_4_rune_value = Column(Integer)

    def __repr__(self):
        return str.format('<Artifact {} - Set {} - Level {}>', self.id, self.set, self.level)
