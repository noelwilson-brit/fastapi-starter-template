import requests
import pandas as pd


def basic_rater(rate: float):
    return rate * 2


def get_property_data(quote_id) -> dict:
    # Get data from an API (This is missing auth and will not work this is just for example)
    proprety_data = requests.get(
        f'https://fa-rater-api-dev-01.azurewebsites.net/api/v1/property/?quote_id={quote_id}&valuation_results=false&page_size=100&page_number=1&order_by=-tiv_total',
    )
    return proprety_data["results"]


def calculate_tiv_sum(property_data: dict) -> float:
    # Parse the data into dataframe
    df = pd.DataFrame(property_data)

    # Do the maths
    return df["tiv_building"].sum()


def save_file(output_data, file_name="output.txt"):
    with open(file_name, "wb") as fp: 
        fp.write(output_data)


def get_tiv_sum(quote_id):
    proprety_data = get_property_data(quote_id=quote_id)

    tiv_sum = calculate_tiv_sum(property_data=proprety_data)

    save_file(tiv_sum)

    return tiv_sum


if __name__ == "__main__":
    print(get_tiv_sum("666322de-abfa-4902-a2dd-6c7e9b2d5eea"))