from fastapi import APIRouter

from app.core.logger import logger
from app.core.calculations import basic_rater

router = APIRouter()


@router.get('/')
def read_root():
    logger.info('This is an example of logging')
    return {'hello': 'world'}

@router.post('/calculate')
def calculate(premium):
    result = basic_rater(float(premium))
    logger.info(f'Calulated rate of {result}')
    return result
