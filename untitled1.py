# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 15:16:10 2023

@author: Hp
"""

import requests 
import pandas as pd
r = requests.get("https://storelocator.space48apps.com/store-locator/dng8lm8hez/1/")
r = r.json()

df = pd.DataFrame(r["data"]["locations"])
df.sort_values(by="postcode", ignore_index=True)
df.to_csv("Malouf.csv")