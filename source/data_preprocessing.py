import pandas as pd
import numpy as np
from datetime import datetime
from numpy.linalg import norm


# Dropping irrelevant columns... (subject to change)

def pre_processing(spotify_df):
    """
    docstring
    """

    # drop irrelevant columns
    spotify_df = spotify_df.drop(columns=['username', 'platform', 'ip_addr_decrypted', 
                                            'user_agent_decrypted', 'incognito_mode',
                                            'episode_name', 'episode_show_name', 'spotify_episode_uri'])
    
    # removing null rows + podcast data
    spotify_df = spotify_df[spotify_df['spotify_track_uri'].notna()]

    # replace null values with string in skipped column
    spotify_df['skipped'].fillna('no_value', inplace = True)

    # create seconds and mins played column
    spotify_df['secs_played'] = spotify_df['ms_played']/1000
    spotify_df['mins_played'] = spotify_df['secs_played']/60

    # turn timestamp col to datetime object
    spotify_df['ts'] = pd.to_datetime(spotify_df['ts'], format='%Y-%m-%dT%H:%M:%SZ')

    return spotify_df


def track_info_process(spotify_df, track_info_df):
    """
    docstring
    """
    # rename track col 
    track_info_df = track_info_df.rename(columns={'uri': 'spotify_track_uri'})

    # merge with other df
    spotify_df = spotify_df.merge(track_info_df, on = 'spotify_track_uri', how = 'left')

    # print df missing values
    missing_values = spotify_df.isnull().sum()
    columns_with_missing = missing_values[missing_values > 0]

    if columns_with_missing.empty:
        print("No missing values in the DataFrame.")
    else:
        print("Columns with missing values and their counts:")
        for column, count in columns_with_missing.items():
            print(f"{column}: {count}")

    return spotify_df


def features_to_arrays(spotify_df):
    """
    docstring
    """
    features_df = spotify_df
    
    features_arrays = np.array(features_df)
    
    return features_arrays


def cosine_similarity(array1, array2):
    """
    docstring
    """
    cosine = np.dot(array1,array2)/(norm(array1)*norm(array2))
    print("Cosine Similarity:", cosine)

    return cosine

def implicit_ratings_distance(array1, array2):
    """
    docstring
    """
    if array1.shape != array2.shape:
        raise ValueError("Input arrays must have the same shape")

    return np.sum(np.abs(array1 - array2))
