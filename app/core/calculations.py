import requests
import pandas as pd


def basic_rater(rate: float):
    return rate * 2


def get_tiv_sum(quote_id):
    # Get data from an API (This is missing auth and will not work this is just for example)
    proprety_data = requests.get(
        f'https://fa-rater-api-dev-01.azurewebsites.net/api/v1/property/?quote_id={quote_id}&valuation_results=false&page_size=100&page_number=1&order_by=-tiv_total',
    )

    # Parse the data into dataframe
    df = pd.DataFrame(proprety_data.json()["results"])

    # Do the maths
    tiv_sum = df["tiv_building"].sum()

    # Save the results
    with open("output.txt", "wb") as fp: 
        fp.write(tiv_sum)

    # Return the results
    return tiv_sum


if __name__ == "__main__":
    print(get_tiv_sum("666322de-abfa-4902-a2dd-6c7e9b2d5eea"))