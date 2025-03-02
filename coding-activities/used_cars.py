#!/usr/bin/env python3

import csv
import install_playwright

from bs4 import BeautifulSoup
import time

from playwright.sync_api import sync_playwright

URL = "https://www.autotrader.com/cars-for-sale/ventura-ca?newSearch=false&numRecords=100&zip=93001"
FIELDNAMES = [
    "make",
    "model",
    "year",
    "price",
    "mileage",
]


def load_html() -> str:
    """Load the HTML content of the page."""
    try:
        with open("used_cars.html", "r") as f:
            html_content = f.read()

    except FileNotFoundError:
        with sync_playwright() as p:
            install_playwright.install(p.chromium)
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto(URL)
            # Scroll to the bottom of the page
            for chunk in range(20):
                page.mouse.wheel(0, 2000)
                time.sleep(.1)
            time.sleep(10)

            # Get the HTML content of the page
            html_content = page.content()

            with open("used_cars.html", "w") as f:
                f.write(html_content)
            # Close the browser
            browser.close()
    return html_content


def extract_cars(html_content: str) -> list:
    soup = BeautifulSoup(html_content, "html.parser")
    cars = soup.find_all("div", class_="col-xs-12 col-sm-4 display-flex")
    return cars


def write_to_csv(cars: list):
    with open("used_cars.csv", mode="w", encoding="utf-8") as used_car_db:
        car_writer = csv.DictWriter(used_car_db, fieldnames=FIELDNAMES)
        car_writer.writeheader()
        seen = set()
        for car in cars:
            try:
                car_data = car.find("div", class_="inventory-listing-body padding-3")
                car = car_data.find("h2").text
                mileage = car_data.find("div", class_="text-bold text-subdued-lighter margin-top-3").text
                price = car_data.find("div", class_="text-size-500 text-ultra-bold first-price").text
                _, year, make, *model = car.split()

                fields = [
                    make,
                    " ".join(model),
                    year,
                    int(mileage.split()[0].replace(",", "")),
                    float(price.replace(",", "")),
                ]
                row = {fn: f for fn, f in zip(FIELDNAMES, fields)}
                static_row = tuple(row.items())
                if static_row not in seen:
                    car_writer.writerow(row)
                seen.add(static_row)
            except AttributeError:
                pass


if __name__ == "__main__":
    html_content = load_html()
    cars = extract_cars(html_content)
    write_to_csv(cars)
