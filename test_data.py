# import the libraries
import pandas as pd
import pytest
from datetime import datetime

# read the HINDALCO_1D.xlsx file data
dataframe = pd.read_excel('HINDALCO_1D.xlsx', engine='openpyxl')
dataframe.head(5)

# check input data are decimal
def column_values_are_decimal(number):
    assert isinstance(number, float)

# testing values in close, high, low, open column are decimal
@pytest.mark.unit
def test_column_values_are_decimal():
    dataframe.apply(lambda row: column_values_are_decimal(row["close"]) , axis=1)
    dataframe.apply(lambda row: column_values_are_decimal(row["high"]) , axis=1)
    dataframe.apply(lambda row: column_values_are_decimal(row["low"]) , axis=1)
    dataframe.apply(lambda row: column_values_are_decimal(row["open"]) , axis=1)

# check input data are integers
def column_values_are_integer(number):
    assert isinstance(number, int)

# testing values in volume column are integer
@pytest.mark.unit
def test_volume_is_integer():
    dataframe.apply(lambda row: column_values_are_integer(row["volume"]) , axis=1)

# check input data are string
def column_values_are_string(text):
    assert isinstance(text, str)

# testing values in instrument column are string
@pytest.mark.unit
def test_instrument_is_string():
    dataframe.apply(lambda row: column_values_are_string(row["instrument"]) , axis=1)

# check input data are datetime
def column_values_are_datetime(date_time):
    assert isinstance(date_time, datetime)

# testing values in datetime column are datetime
@pytest.mark.unit
def test_datetime_column_is_datetime():
    dataframe.apply(lambda row: column_values_are_datetime(row["datetime"]) , axis=1)
