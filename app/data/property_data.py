from typing import List
from uuid import UUID
from pydantic import BaseModel
import requests


PROPERTY_API = 'https://fa-rater-api-dev-01.azurewebsites.net/api/v1/property/'


class PropertyData(BaseModel):
    id: UUID
    tiv_building: float


def get_property_data(quote_id: UUID) -> List[PropertyData]:
    # Cache property data to avoid duplicate API calls
    proprety_data = requests.get(
        f'{PROPERTY_API}?quote_id={quote_id}&valuation_results=false&page_size=100&page_number=1&order_by=-tiv_total',
    )
    # This will error and warn us if we are missing "tiv_building"
    return [PropertyData(**property) for property in proprety_data["results"]]