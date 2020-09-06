import pandas as pd

try:
    data = pd.read_csv('IOT-temp.csv')
except:
    print("The file is not found")
