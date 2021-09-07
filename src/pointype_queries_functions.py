import pandas as pd
from bson.json_util import dumps
import shapely
import geopandas as gdp
# import json
from pymongo import MongoClient
from pymongo import GEOSPHERE


def typePoint(dataframe):
    '''
    What this function does is: given a dataframe gets its coordinates columns
    and turns them into a single column type point
    '''
    
    #Geopoints
    gdf = gdp.GeoDataFrame(dataframe, geometry= gdp.points_from_xy(dataframe.longitud, dataframe.latitud ))
    gdf.columns=['name', 'lat', 'long', 'category', 'geometry']
    
    gdf['geometry']= gdf['geometry'].apply(lambda x:shapely.geometry.mapping(x))
   
    return gdf


def nearQueries(gdf, mongo_database, collection_name, lon, lat, max_distance):
    ''' 
    What this function does is: given a geodataframe with coordinates point type of each of the venues in the dataframe, 
    the longitud and latitud of our reference location and the max distance we wish the geoquery to look for venues,
    creates a new collection in your selected mongo database and stores the results in it. It also returns a list of venues found with
    the desire query and creates a new column named "distance" that calculates the distance between our selected location and the venue. 
    '''
    #creates collection (if it already exists, delete)
    client = MongoClient(f"mongodb://localhost/{mongo_database}")
    db = client.get_database()
    col = db[f"{collection_name}"]

    if col.drop():
        print('Collection already exists -> Collection Deleted')
    else:
        print('This collection is new -> Collection Created')

    collection = db.create_collection(name = f"{collection_name}")
    collection.create_index([("geometry", GEOSPHERE)])

    data = gdf.to_dict(orient='records')
    collection.insert_many(data)

    #Queries for closest venues
    query = [{
    "$geoNear": {'near': [lon, lat],
                 'distanceField': 'distance',
                 'maxDistance': max_distance,
                 'distanceMultiplier': 6371, 
                 'spherical'  : True}}]
    geoloc = collection.aggregate(query)
    # response_json = json.loads(dumps(geoloc))
    
    return list(geoloc)

    
def countQueryDocs(collection_name, mongo_database):
    ''' 
    What this function does is: given a mongo database name and a collection name it counts
    how many documents has in it
    '''
    client = MongoClient(f"mongodb://localhost/{mongo_database}")
    db = client.get_database()
    collection = db.get_collection(f"{collection_name}")
    count_collection = len(list(collection.find()))
    

    return print(f"{count_collection} results in {collection_name}")