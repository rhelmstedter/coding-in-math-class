#!/usr/bin/env python3

import requests
import json
from bs4 import BeautifulSoup
import csv
from pprint import pprint as pp


URL = "https://www.autotrader.com/cars-for-sale/ventura-ca?newSearch=false&numRecords=100&zip=93001"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
cars = soup.find_all("div", class_="col-xs-12 display-flex col-sm-4")
with open("used_cars.csv", mode="w") as used_car_db:
    fieldnames = [
        "brand",
        "model",
        "color",
        "mpg",
        "fuel_type",
        "full_name",
        "price",
        "mileage",
        "year",
    ]
    car_writer = csv.DictWriter(used_car_db, fieldnames=fieldnames)
    for car in cars[:3]:
        try:
            car_data = json.loads(car.find("script").text)
            pp(car_data)
            fields = [
                car_data["brand"]["name"]["name"],  # brand
                car_data["model"]["name"],  # model
                car_data["color"],  # color
                car_data["fuelEfficiency"],  # mpg
                car_data["fuelType"]["name"],  # fuel_type
                car_data["name"],  # full_name
                car_data["offers"]["price"],  # price
                car_data["mileageFromOdometer"]["value"],  # mileage
                car_data["productionDate"],  # year
            ]
        except AttributeError:
            pass
        # car_writer.writerow({fn: f for fn, f in zip(fieldnames, fields)})
