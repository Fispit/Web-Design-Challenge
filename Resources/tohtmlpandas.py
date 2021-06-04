import pandas as pd
fileloc="cities.csv"
cities_df=pd.read_csv(fileloc)
cities_df.to_html("citytable.html")