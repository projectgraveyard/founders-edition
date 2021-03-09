from os import name, system
from time import sleep
from datetime import datetime
from json import loads, dumps
from urllib3 import PoolManager
from webbrowser import open_new
http = PoolManager()

shop = "https://shop.nvidia.com/en-gb/geforce/store/"
basepath = "https://api.nvidia.partners/edge/product/search"
parameters = {
    "page": "1", "limit": "9", "locale": "en-gb", "manufacturer": "NVIDIA", 
    "manufacturer_filter": "NVIDIA~5,3XS%20SYSTEMS~1,ACER~6,AORUS~3,ASUS~37,EVGA~7,GIGABYTE~26,HP~6,LENOVO~4,MSI~16,PALIT~14,PNY~5,RAZER~8,ZOTAC~12"
}

def alert():
    for _ in range(20):
        print("\007", end="", flush=True)
        sleep(0.5)

def open_browswer(url: str):
    open_new(url)


while True:
    now = datetime.now()
    print(now.strftime("%d %b: %H:%M:%S"))

    r = http.request("GET", basepath, fields=parameters)

    as_json = loads(r.data)
    products = as_json["searchedProducts"]
    listings = products["productDetails"] + [products["featuredProduct"]]
    
    for listing in listings:
        name = listing["displayName"]
        availability = listing["prdStatus"]
        print("%s: %s" % (name, availability))

        if availability != "out_of_stock":
            open_browswer(shop)
            alert()

    sleep(20)
    system('cls' if name == 'nt' else 'clear')