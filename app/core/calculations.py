from ast import List
from uuid import UUID
import pandas as pd
from ..data.property_data import get_property_data, PropertyData


def basic_rater(rate: float):
    return rate * 2


class CalculateTiv():

    def __init__(self):
        self.property_data = None

    def get_property_data(self, quote_id: UUID) -> List[PropertyData]:
        # Cache property data to avoid duplicate API calls
        if self.property_data is None:
            self.proprety_data = get_property_data(quote_id=quote_id)
        # This will error and warn us if we are missing "tiv_building"
        return self.property_data

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