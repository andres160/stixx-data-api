from pydantic import BaseModel
from typing import List, Optional


class ItemBase(BaseModel):
    spec_version: Optional[str]
    created: Optional[str]
    modified: Optional[str]
    name: Optional[str]
    description: Optional[str]

    class Config:
        orm_mode = True


class MalwareRecord(ItemBase):
    malware_id: str
    is_family: Optional[str]


class AttackPattern(ItemBase):
    attack_pattern_id: str


class Campaign(ItemBase):
    campaign_id: str
    first_seen: str


class CourseOfAction(ItemBase):
    course_of_action_id: str
    created_by_ref: str


class Identity(ItemBase):
    identity_id: str
    identity_class: Optional[str]


class Indicator(ItemBase):
    indicator_id: str
    pattern_type: str
    valid_from: str


class Relationship(BaseModel):
    relationship_id: str
    relationship_type: str
    source_ref: str
    target_ref: str
    spec_version: str
    created: str
    modified: str

    class Config:
        orm_mode = True


class Report(ItemBase):
    report_id: str
    published: str
