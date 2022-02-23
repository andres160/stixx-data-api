## Introduction

API built as a middleware application to handle STIX-formatted data.

Framework used: FASTAPI

https://fastapi.tiangolo.com/

Dataset used to test: Poison Ivy Threat Intelligence Data
More information: https://www.mandiant.com/resources/poison-ivy-assessing-damage-and-extracting-intelligence


## Background:

The dataset was obtained from STIX's documentation page as an example STIX object in JSON format:
https://oasis-open.github.io/cti-documentation/stix/examples

STIX is an open standard used in the security domain for the interoperablity of structured CTI (Cyber Threat Intelligence) data.


## Start the app

To test the API, install the required dependencies within requirements.txt on a virtual environment and run the following command on the terminal at the main app location:

uvicorn main:app --reload

Browse to the docs endpoint to test the API using an openAPI UI (built-in within FASTAPI)

http://127.0.0.1:8000/docs#/



