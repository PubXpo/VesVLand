<h1>Vessel vs Landings</h1>

This project investigates the average landing of fish stocks, into the UK, in comparison to the average vessel sizes at each port. It uses two datasets to accomplish this. 

One dataset of UK fishing vessels, to get details such as length sizes and administrative ports. The other of fish landings, to get details such as species type, port of landing and landed weight, in tonnes.

The two datasets will consider two questions. First: Does the month impact the species caught throughout the year? Then: Do administrative ports with similar vessels land similar species groups? 

## Features

- Cleans dirty data (e.g. duplicates, null values)
- Merges datasets
- Imports to MongoDB collections
- Runs pipeline queries
- Displays charts and graphs
- Displays a visual map 

## Python Library Imports

### Standard Imports:
    import pandas as pd
    import chardet
    import re
    import os
    import glob
    import matplotlib.pyplot as plt
    import seaborn as sns
### Mapping Imports:
    import geopy
    import folium
### Database Imports:
    from pymongo import MongoClient
### Machine Learning Imports:
    from sklearn.metrics import silhouette_samples
    from sklearn import cluster
    from sklearn.cluster import KMeans

## Requirements:

- **Python** 3.0+
- **MongoDB**

A MongoDB container can be setup with Docker a if portable DB is preferred.

## Findings

For the question: Does the month impact the species caught throughout the year? The findings suggest that it does for the pelagic landings. The investigation looked at data for individual years and combinations. 

    The result showed that Shellfish and Demersal remained within similar monthly ebbs and flow. 
    This suggest that month does not impact the landings greatly for these. 

    However the Pelagic landings seems to depend on the month. May, June and December had the 
    lowest landings, recommending that these are the worst time to fish.  


For the question: Do administrative ports with similar vessels land similar species groups? The findings suggest that it does. The investigation analysed and visualised clusters and produced a descriptive map.

    It showed close grouping in cluster 0. It confirmed and presented on a map that vessels a 
    little over 10m were likely to produce the same average quantity of landings at each port. 

NOTE: A descriptive written report is available for review on request.

## License

The datasets in the /Analysis_data folder is from GOV.UK and is assured under the Open Government Licence version 3. According to National Archives (n.d.) information from the public-sector can be “copied, adapted and combined with other information as long as the source is acknowledged”. The investigation uses this clause to proceed with merging and adapting the data files.

The National Archives (n.d.) ‘The Open Government Licence’, [Online].
Available at: https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/ 
