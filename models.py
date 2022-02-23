from sqlalchemy import Column, Integer, String
from database.database import Base


class MalwareRecord(Base):
    __tablename__ = "malware"

    malware_id = Column(String, primary_key=True)
    spec_version = Column(String)
    created = Column(String)
    modified = Column(String)
    name = Column(String)
    description = Column(String)
    is_family = Column(Integer)


class AttackPattern(Base):
    __tablename__ = "attack_pattern"

    attack_pattern_id = Column(String, primary_key=True, index=True)
    spec_version = Column(String)
    created = Column(String)
    modified = Column(String)
    name = Column(String)
    description = Column(String)


class Campaign(Base):
    __tablename__ = "campaign"

    campaign_id = Column(String, primary_key=True, index=True)
    spec_version = Column(String)
    created = Column(String)
    modified = Column(String)
    first_seen = Column(String)
    name = Column(String)
    description = Column(String)


class CourseOfAction(Base):
    __tablename__ = "course_of_action"

    course_of_action_id = Column(String, primary_key=True, index=True)
    spec_version = Column(String)
    created = Column(String)
    modified = Column(String)
    created_by_ref = Column(String)
    name = Column(String)
    description = Column(String)


class Identity(Base):
    __tablename__ = "identity"

    identity_id = Column(String, primary_key=True, index=True)
    spec_version = Column(String)
    created = Column(String)
    modified = Column(String)
    identity_class = Column(String)
    name = Column(String)


class Relationship(Base):
    __tablename__ = "relationship"

    relationship_id = Column(String, primary_key=True, index=True)
    spec_version = Column(String)
    created = Column(String)
    modified = Column(String)
    relationship_type = Column(String)
    source_ref = Column(String)
    target_ref = Column(String)


class Report(Base):
    __tablename__ = "report"

    report_id = Column(String, primary_key=True, index=True)
    spec_version = Column(String)
    created = Column(String)
    modified = Column(String)
    name = Column(String)
    description = Column(String)
    published = Column(String)
