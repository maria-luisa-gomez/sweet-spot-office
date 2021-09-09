import requests 
import json
import os
import pandas as pd
from dotenv import load_dotenv

from functools import reduce
import operator
import geopandas as gdp
import shapely

from pymongo import MongoClient
    

def getCoordinates(direcciones):

    '''
    What this function does is: given a list of addresses/name of locations it gives you back a dictionary with the latitute and longitude of each of them
    Input: list of addresses/location names
    Output: a dictionary with their correspodant coordinates
    '''
    dict_ = {}
    try: 
        for direccion in direcciones:
            locations = requests.get(f'https://geocode.xyz/{direccion}?json=1')
            locations = locations.json()
            dict_[direccion] = locations
    except:
        return "Error"
        
    return dict_


def actualCoordinates(dictionary):
    '''
    What this function does is: given a dictionary locations with its coordenates, 
    gives back same location as a key which values are latitude and longitud type
    
    '''
    dict_2 = {}
    for k, v in dictionary.items():
        coor = [float(v["longt"]),float(v["latt"])]
        dict_2[k] = coor
    return dict_2
    


def foursquareQueries(latitude, longitude, url, *args):
    '''
    What this function does is: given a list of querys, it makes a call to the foursquare API for each query and gives back 
    name and location information that will store in a dict.

    '''  
    dict2_ = {}
    token1 =  'xxxxxxxx'
    token2 = 'xxxxxxxxx'
    # client_id= os.getenv("token1")
    # client_secret = os.getenv("token2")
    
    for i in args: 
        params = {"client_id" : token1,
                  "client_secret" : token2,
                  "v": "20180323",
                  "ll": f"{latitude},{longitude}", 
                  "query":i,
                  "limit": 50,
                  "radius": 5000}  

        resp = requests.get(url= url, params=params)
        data = json.loads(resp.text)        
        dict2_[i] = data
        
    return dict2_




def responseGroups(result):
    '''
    What this function does is: given a dictionary with the previous foursquare api queries information, returns a dictionary per query

    '''


    for key, values in result.items():
        
        if key == "Nursery" or key == "Preschool":
            school = result.get(key)
            response = school.get('response')
            decoded = response.get('groups')[0]
            school_decoded = decoded.get('items')

 
            
            
        elif key == "Pub" or key == "Club":
            hangout = result.get(key)
            response = hangout.get('response')
            decoded = response.get('groups')[0]
            hangout_decoded = decoded.get('items')
            
        elif key == "Airport" or key == "Train Station":
            travel = result.get(key)
            response = travel.get('response')
            decoded = response.get('groups')[0]
            travel_decoded = decoded.get('items')
        
        elif key == "Vet" or key == "Pet Grooming":
            petgrooming = result.get(key)
            response = petgrooming.get('response')
            decoded = response.get('groups')[0]
            petgrooming_decoded = decoded.get('items')    
         
        else:
            vegan = result.get(key)
            response = vegan.get('response')
            decoded = response.get('groups')[0]
            vegan_decoded = decoded.get('items')
            
    results = [school_decoded, hangout_decoded, travel_decoded, petgrooming_decoded, vegan_decoded]
            
    return results

def getFromDict(diccionario,mapa):
    return reduce (operator.getitem,mapa,diccionario)

# def type_point(lista):
#     return {"type": "Point", 
#             "coordinates": lista }

def toDataframe(*args):
    '''
    What this function does is: given list of dictionaries containing information structured API format, 
    transforms each of the dictionaries into a readable dataframe
    '''
    mapa_nombre = ["venue","name"]
    m_latitud = ["venue","location","lat"]
    m_longitud = ["venue","location","lng"]
    m_category = ["venue", "categories"]
    
    results = []

    for i in args:
        for dic in i:            
            paralista = {}
            paralista["name"] = getFromDict(dic,mapa_nombre)
            paralista["latitud"] = getFromDict(dic,m_latitud)
            paralista["longitud"] = getFromDict(dic,m_longitud)
            paralista["category"] = getFromDict(dic,m_category)
            # paralista["location"]=  type_point([paralista["latitud"],paralista["longitud"]])
            results.append(paralista)
    df = pd.DataFrame(results)

    return df