import pandas as pd
import matplotlib.pyplot as plt

# EDA functions
def top_artists(df):

    albums = pd.DataFrame(df['master_metadata_album_album_name'].value_counts(ascending=False).head(10))

    return albums


def top_albums(df):

    artists = pd.DataFrame(df['master_metadata_album_artist_name'].value_counts(ascending=False).head(10))

    return artists


def top_tracks(df):

    top_tracks = pd.DataFrame(df['master_metadata_track_name'].value_counts(ascending=False).head(50))
    
    return(top_tracks)


def most_skipped(df):
    
    skipped_df = df.loc[df['skipped'] == True]
    
    skipped_df = pd.DataFrame(skipped_df['master_metadata_track_name'].value_counts(ascending=False).head(50))
    
    return(skipped_df)


def col_distributions(df):
    """
    can only accept dfs with number cols
    """
    # Set up the figure and axes
    fig, axes = plt.subplots(nrows=1, ncols=len(df.columns), figsize=(100, 4))

    # Loop through each column and create a distribution plot
    for i, column in enumerate(df.columns):
        axes[i].hist(df[column], bins='auto', density=True)
        axes[i].set_title(column)

    # Adjust the spacing between subplots
    plt.tight_layout()

    # Display the figure
    plt.show()
    plt.savefig("feature_track_info_hist.png")