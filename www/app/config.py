import os

class Config:
    OSCAL_FEED_URL = os.getenv('OSCAL_FEED_URL', 'https://github.com/AustralianCyberSecurityCentre/ism-oscal/blob/main/ISM_catalog.json')
