import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from datetime import datetime

import data_ingest
import data_preprocessing

# Data ingestion
og_spotify_df = data_ingest.og_data_ingest()

ext_spotify_df = data_ingest.ext_data_ingest()

# Data pre-processing
ext_spotify_df = data_preprocessing.pre_processing(ext_spotify_df)

# EDA


# Accessing the spotify api


