import pandas as pd
import geopandas as gdp
import folium
from folium import Choropleth, Circle, Marker, Icon, Map
from folium.plugins import HeatMap, MarkerCluster
import re


# This function aggregates categories within a column given a list of categories

def categoryAggr(dataset, ref_column):
    """
    What this function does is: given a dataset and a column from this dataset, finds and replaces its values
    based on the above regex statements
    """
    dataset[ref_column] = dataset[ref_column].str.replace(".*?Airport.*\w?", "Transportation")
    dataset[ref_column] = dataset[ref_column].str.replace(".*?Car.*\w?", "Transportation")
    dataset[ref_column] = dataset[ref_column].str.replace(".*?Taxi.*\w?", "Transportation")
    dataset[ref_column] = dataset[ref_column].str.replace(".*?Train.*\w?", "Transportation")
    dataset[ref_column] = dataset[ref_column].str.replace(".*?Bus.*\w?", "Transportation")
    dataset[ref_column] = dataset[ref_column].str.replace(".*?Boat.*\w?", "Transportation")
    dataset[ref_column] = dataset[ref_column].str.replace(".*?Plane.*\w?", "Transportation")
    dataset[ref_column] = dataset[ref_column].str.replace(".*?Ferry.*\w?", "Transportation")
    dataset[ref_column] = dataset[ref_column].str.replace(".*?Transportation.*\w?", "Transportation")
    dataset[ref_column] = dataset[ref_column].str.replace(".*?Travel.*\w?", "Transportation")
    dataset[ref_column] = dataset[ref_column].str.replace(".*?Pet.*\w?", "Pet Services")
    dataset[ref_column] = dataset[ref_column].str.replace(".*?Bar.*\w?", "Going Out")
    dataset[ref_column] = dataset[ref_column].str.replace(".*?[C|c]lub.*\w?", "Going Out")
    dataset[ref_column] = dataset[ref_column].str.replace(".*?Pub.*\w?", "Going Out")
    dataset[ref_column] = dataset[ref_column].str.replace(".*?Café.*\w?", "Going Out")
    dataset[ref_column] = dataset[ref_column].str.replace(".*?Restaurant.*\w?", "Vegan Restaurant")
    dataset[ref_column] = dataset[ref_column].str.replace("Daycare", "Preschool")
    dataset[ref_column] = dataset[ref_column].str.replace(".*?School.*\w?", "Preschool")
    dataset[ref_column] = dataset[ref_column].str.replace(".*?Pet.*\w?", "Pet Services")

    

        # dataset[new_column] = dataset[ref_column].str.replace(".*?Airport.*\w?", "Transportation")
        # dataset[new_column] = dataset[ref_column].str.replace(".*?Car.*\w?", "Transportation")
        # dataset[new_column] = dataset[ref_column].str.replace(".*?Taxi.*\w?", "Transportation")
        # dataset[new_column] = dataset[ref_column].str.replace(".*?Train.*\w?", "Transportation")
        # dataset[new_column] = dataset[ref_column].str.replace(".*?Bus.*\w?", "Transportation")
        # dataset[new_column] = dataset[ref_column].str.replace(".*?Boat.*\w?", "Transportation")
        # dataset[new_column] = dataset[ref_column].str.replace(".*?Plane.*\w?", "Transportation")
        # dataset[new_column] = dataset[ref_column].str.replace(".*?Ferry.*\w?", "Transportation")
        # dataset[new_column] = dataset[ref_column].str.replace(".*?Transportation.*\w?", "Transportation")
        # dataset[new_column] = dataset[ref_column].str.replace(".*?Travel.*\w?", "Transportation")
        # dataset[new_column] = dataset[ref_column].str.replace(".*?Pet.*\w?", "Pet Services")
        # dataset[new_column] = dataset[ref_column].str.replace(".*?Bar.*\w?", "Going Out")
        # dataset[new_column] = dataset[ref_column].str.replace(".*?[C|c]lub.*\w?", "Going Out")
        # dataset[new_column] = dataset[ref_column].str.replace(".*?Pub.*\w?", "Going Out")
        # dataset[new_column] = dataset[ref_column].str.replace(".*?Café.*\w?", "Going Out")
        # dataset[new_column] = dataset[ref_column].str.replace(".*?Restaurant.*\w?", "Vengan Restaurant")
        # dataset[new_column] = dataset[ref_column].str.replace("Daycare", "Preschool")
        # dataset[new_column] = dataset[ref_column].str.replace(".*?School.*\w?", "Preschool")
        # dataset[new_column] = dataset[ref_column].str.replace(".*?Pet.*\w?", "Pet Services")



def min_max_scaling(df, column):
    '''
    What this function does is: applies The min-max feature scaling to a
    column selected from a dataframe.
    The min-max approach (often called normalization) rescales the feature to a fixed range of [0,1] 
    by subtracting the minimum value of the feature and then dividing by the range
    '''

    # df[column] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())  
    df[column]=(df[column]-df[column].min())/(df[column].max()-df[column].min())   
  
    df = df.reset_index(drop = False)
    return df



def importance(dataset, ref_column):
    '''
    What this function does is: given a dataset and a column from this dataset, finds and replaces its values
    based on the above regex statements
    '''
    dataset[ref_column] = dataset[ref_column].str.replace("Vegan Restaurant", "0.25")
    dataset[ref_column] = dataset[ref_column].str.replace("Pet Services", "0.25")
    dataset[ref_column] = dataset[ref_column].str.replace("Going Out", "0.2")
    dataset[ref_column] = dataset[ref_column].str.replace("Preschool", "0.15")
    dataset[ref_column] = dataset[ref_column].str.replace("Transportation", "0.15")

    dataset[ref_column] = dataset[ref_column].astype("float")