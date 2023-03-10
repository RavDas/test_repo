# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 00:49:30 2023

@author: RaveenD
"""
import glassdoor_scrapper as gs
import pandas as pd

path = "C:/Users/RaveenD/Documents/ds_salary_proj/chromedriver"
df = gs.get_jobs("data scientists", 15, False, path, 15)
df.to_csv('glassdoor_jobs.csv', index=False)