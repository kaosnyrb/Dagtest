from dask import delayed as delay
import dask.dataframe as dd
import numpy as np
from datetime import datetime, timedelta
import time
from distributed import Client

c = Client()
c
br = dd.read_csv('s3://bryntestbucket/mockdi/Brand.csv')
br.to_csv('s3://bryntestbucket/scores/ASL.*.csv')
