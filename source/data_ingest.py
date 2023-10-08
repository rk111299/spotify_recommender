import pandas as pd
import json


# Ingesting the data from JSON files into pandas dataframes
def og_data_ingest():
    numbers = [0,1,2,3,4,5]

    dfs = []

    for val in numbers:
        with open(f"../original_download/StreamingHistory{val}.json") as f:
            file_data = json.load(f)
            df = pd.DataFrame(file_data)
            dfs.append(df)

    og_spotify_df = pd.concat(dfs, ignore_index=True)

    return og_spotify_df

def ext_data_ingest():
    values = ['2022_31', '2022_32', '2022-2023_33', '2023_34', '2023_35']

    dfs = []

    for val in values:
        with open(f"../ext_streaming//Streaming_History_Audio_{val}.json") as f:
            file_data = json.load(f)
            df = pd.DataFrame(file_data)
            dfs.append(df)

    ext_spotify_df = pd.concat(dfs, ignore_index=True)

    return ext_spotify_df