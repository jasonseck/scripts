import pandas as pd

# A text file with one tweet per line

DATA_FILE = "./bitcoin.json"

# Build a JSON array

data = "[{0}]".format(",".join([l for l in open(DATA_FILE).readlines()]))

# Create a pandas DataFrame (think: 2-dimensional table) to get a 
# spreadsheet-like interface into the data

df = pd.read_json(data, orient='records')

print "Successfully imported", len(df), "tweets"



print df
