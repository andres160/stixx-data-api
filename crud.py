from os import name
from sre_constants import SUCCESS
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from typing import List, Optional, Generic, TypeVar, Type
from pydantic import BaseModel

import models

# malware
def get_all_malware(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MalwareRecord).offset(skip).limit(limit).all()


def get_malware_record(db: Session, malware_id):
    malware_record = db.query(models.MalwareRecord).filter(
        models.MalwareRecord.malware_id == malware_id).first()
    if malware_record:
        return malware_record
    return None


# attack_pattern
def get_all_attack_patterns(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.AttackPattern).offset(skip).limit(limit).all()


def get_attack_pattern(db: Session, attack_pattern_id):
    attack_pattern = db.query(models.AttackPattern).filter(
        models.AttackPattern.attack_pattern_id == attack_pattern_id).first()
    if attack_pattern:
        return attack_pattern
    return None


# campaign
def get_all_campaigns(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Campaign).offset(skip).limit(limit).all()


def get_campaign(db: Session, campaign_id):
    campaign = db.query(models.Campaign).filter(
        models.Campaign.campaign_id == campaign_id).first()
    if campaign:
        return campaign
    return None


# course of action
def get_all_courses_of_action(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CourseOfAction).offset(skip).limit(limit).all()


# identity
def get_identity(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Identity).offset(skip).limit(limit).all()


# indicator
def get_all_indicators(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Indicator).offset(skip).limit(limit).all()


def get_indicator(db: Session, indicator_id):
    indicator = db.query(models.Indicator).filter(
        models.Indicator.indicator_id == indicator_id).first()
    if indicator:
        return indicator
    return None


# relationship
def get_all_relationships(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Relationship).offset(skip).limit(limit).all()


def get_relationship(db: Session, relationship_id):
    relationship = db.query(models.Relationship).filter(
        models.Relationship.relationship_id == relationship_id).first()
    if relationship:
        return relationship
    return None


# report
def get_report(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Report).offset(skip).limit(limit).all()
