import imp
from os import name
from pyexpat import model
from fastapi import Depends, FastAPI
from fastapi_pagination import Page, add_pagination, paginate
from fastapi.encoders import jsonable_encoder
# from prometheus_client import Enum
from enum import Enum
from sqlalchemy.orm import Session

import crud, models, schemas
from database.database import get_db


app = FastAPI(
    title="Malware API",
    description="A REST API using python and sql lite",
    version="0.0.1",
)

class Tags(Enum):
    malware = 'Malware'
    attack_pattern = 'Attack Patterns'
    campaign = 'Campaigns'
    course_of_action = 'Course of Action'
    identity = 'Identity'
    indicator = 'Indicators'
    relationship = 'Relationships'
    report = "Reports"


#malware_endpoints
@app.get("/malware/", response_model=Page[schemas.MalwareRecord], tags=[Tags.malware], summary="Get all malware records")
async def get_malware_records(db: get_db = Depends()):
    results = crud.get_all_malware(db)
    return paginate(results)

@app.get("/malware/{malware_id}", response_model=schemas.MalwareRecord, tags=[Tags.malware], summary="Get malware record by malware_id")
async def get_malware_records_by_id(malware_id: str, db: get_db = Depends()):
    result = crud.get_malware_record(db, malware_id)
    return result

@app.patch("/malware/{malware_id}", response_model=schemas.MalwareRecord, tags=[Tags.malware], summary="Modidy a malware record")
async def update_malware(*, malware_id: str, updated_malware: schemas.MalwareRecord, db: get_db = Depends()):
    malware_model = db.query(models.MalwareRecord).filter(models.MalwareRecord.malware_id == malware_id).first()
    malware_data = updated_malware.dict(skip_defaults=True, exclude_unset=True)
    for key, value in malware_data.items():
        setattr(malware_model, key, value)
    db.add(malware_model)
    db.commit()
    db.refresh(malware_model)
    return malware_model


#attack_pattern_endpoints
@app.get("/attack_pattern/", response_model=Page[schemas.AttackPattern], tags=[Tags.attack_pattern], summary="Get all attack patterns")
async def get_attack_patterns(db: get_db = Depends()):
    results = crud.get_all_attack_patterns(db)
    return paginate(results)

@app.get("/attack_pattern/{attack_pattern_id}", response_model=schemas.AttackPattern, tags=[Tags.attack_pattern], summary="Get attack pattern by attack_pattern_id")
async def get_attack_pattern_by_id(attack_pattern_id: str, db: get_db = Depends()):
    result = crud.get_attack_pattern(db, attack_pattern_id)
    return result


#campaign_endpoints
@app.get("/campaign/", response_model=Page[schemas.Campaign], tags=[Tags.campaign], summary="Get all campaigns")
async def get_campaigns(db: get_db = Depends()):
    results = crud.get_all_campaigns(db)
    return paginate(results)

@app.get("/campaign/{campaign_id}", response_model=schemas.Campaign, tags=[Tags.campaign], summary="Get campaign by campaign_id")
async def get_campaign_by_id(campaign_id: str, db: get_db = Depends()):
    result = crud.get_campaign(db, campaign_id)
    return result


#course of action endpoint
@app.get("/course_of_action/", response_model=Page[schemas.CourseOfAction], tags=[Tags.course_of_action], summary="Get course of action")
async def get_courses_of_action(db: get_db = Depends()):
    results = crud.get_all_courses_of_action(db)
    return paginate(results)


#identiy endpoint
@app.get("/identity/", response_model=Page[schemas.Identity], tags=[Tags.identity], summary="Get identity")
async def get_identity_main(db: get_db = Depends()):
    results = crud.get_identity(db)
    return paginate(results)


#indicator_endpoints
@app.get("/indicator/", response_model=Page[schemas.Indicator], tags=[Tags.indicator], summary="Get all indicators")
async def get_indicators(db: get_db = Depends()):
    results = crud.get_all_indicators(db)
    return paginate(results)

@app.get("/indicator/{indicator_id}", response_model=schemas.Indicator, tags=[Tags.indicator], summary="Get indicator by indicator_id")
async def get_indicator_by_id(indicator_id: str, db: get_db = Depends()):
    result = crud.get_indicator(db, indicator_id)
    return result


#relationship_endpoints
@app.get("/relationship/", response_model=Page[schemas.Relationship], tags=[Tags.relationship], summary="Get all relationships")
async def get_relationships(db: get_db = Depends()):
    results = crud.get_all_relationships(db)
    return paginate(results)

@app.get("/relationship/{relationship_id}", response_model=schemas.Relationship, tags=[Tags.relationship], summary="Get relationship by relationship_id")
async def get_relatinship_by_id(relationship_id: str, db: get_db = Depends()):
    result = crud.get_relationship(db, relationship_id)
    return result


#report endpoint
@app.get("/report/", response_model=Page[schemas.Report], tags=[Tags.report], summary="Get report")
async def get_report_main(db: get_db = Depends()):
    results = crud.get_report(db)
    return paginate(results)


add_pagination(app)