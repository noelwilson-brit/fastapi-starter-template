from ast import List
from uuid import UUID
import requests
import pandas as pd
from  pydantic import BaseModel


def basic_rater(rate: float):
    return rate * 2


PROPERTY_API = 'https://fa-rater-api-dev-01.azurewebsites.net/api/v1/property/'


class PropertyData(BaseModel):
    id: UUID
    tiv_building: float


class CalculateTiv():

    def __init__(self):
        self.property_data = None

    def get_property_data(self, quote_id: UUID) -> List[PropertyData]:
        # Cache property data to avoid duplicate API calls
        if self.property_data is None:
            self.proprety_data = requests.get(
                f'{PROPERTY_API}?quote_id={quote_id}&valuation_results=false&page_size=100&page_number=1&order_by=-tiv_total',
            )
        # This will error and warn us if we are missing "tiv_building"
        return [PropertyData(**property) for property in self.proprety_data["results"]]

    def calculate_tiv_sum(self, property_data: List[PropertyData]) -> float:
        # Parse the data into dataframe
        df = pd.DataFrame(property_data)

        # Do the maths
        return df["tiv_building"].sum()

    def save_file(self, output_data, file_name="output.txt"):
        with open(file_name, "wb") as fp: 
            fp.write(output_data)


    def get_tiv_sum(self, quote_id):
        proprety_data = self.get_property_data(quote_id=quote_id)

        tiv_sum = self.calculate_tiv_sum(property_data=proprety_data)

        self.save_file(tiv_sum)

        return tiv_sum


if __name__ == "__main__":
    calc_instance = CalculateTiv()
    print(calc_instance.get_tiv_sum("666322de-abfa-4902-a2dd-6c7e9b2d5eea"))