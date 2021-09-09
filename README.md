# Sweet Spot Office

![portada](https://i.pinimg.com/originals/90/ec/8a/90ec8a1f2408f9046e0976b88acdbddc.jpg)

### Objective

Our goal is to place the new company offices in the best place for the company to grow. 

Like any other company, what we are trying to avoid is high turnover. We want to have as many happy employees as possible. 

We got a list of our employees requirements.


It's impossible to cover all requirements, so we have to prioritize.


This new company in the GAMING industry. The company have the following scheme:

TEAM

- Designers: 20
- UI/UX Engineers: 5
- Frontend Developers: 10
- Data Engineers: 15 
- Backend Developers: 5
- Account Managers: 20
- Maintenance guy that loves basketball: 1
- Executives: 10
- CEO/President: 1
- Dog: 1

TOTAL EMPLOYEES = 87 + 1 dog


Apart form the CEO that is invaluable for the company we need to stablish a priority criteria and we choose to start with needs that affect more number of employees in descending order.


Also everyones cares about the dog wellbeing so it will count as it affects all employees motivation.


That being said that is how our priority requirements list would look like:


- NEED 1: The CEO is vegan = 1 --> vegan restaurants

- NEED 2: The office dog—"Dobby" needs a hairdresser every month. Ensure there's one not too far away = 87 --> vet or pet hairdresser

- NEED 3: Everyone in the company is between 25 and 40, give them some place to go party = 87  --> pubs and clubs

- NEED 4: 30% of the company staff have at least 1 child = 26 --> nurseries or schools

- NEED 5: Designers like to go to design talks and share knowledge. There must be some nearby companies that also do design. = 20 --> gaming related companies around

- NEED 6: Account managers need to travel a lot = 20 --> airports or train stations

- NEED 7: Developers like to be near successful tech startups that have raised at least 1 Million dollars = 15 (Front and Back) --> succesfull tech companies around

- NEED 8: Executives like Starbucks A LOT. Ensure there's a starbucks not too far = 10 --> Starbucks cafe

- NEED 9: If you want to make the maintenance guy happy, a basketball stadium must be around 10 Km = 1 --> backetball stadium

We are going to try to meet the first 6 and maybe 7 needs



### METHODS

Mongo queries

Foursquare API

GeoMongo

Folium


### STEPS

1 - Meet NEED 5 and 7 (Mongo) **(1 - MongoQueries_CompaniesCollection_find_city.ipynb)**: We've already got a companies database from which we can filter companies by company industry. Since the company is in the GAMING industry we will filter out companies by this category. Also, to meet NEED 7 we also have available in this database information about the money raised by these companies. We can filter out companies that have raised at least 1 Million.
From these queries will choose top2 cities around the globe and we will pick randomly two offices addresses, one per city. The best suitable city office location we'll be taken for the company 


2 - Meet NEED 1, 2, 3, 4 and 6(Foursquare API) **2 - Foursquare API.ipynb**: We will make API calls/queries related with our different requirements ("Nursery", "Preschool", "Train Station", "Airport", "Pub", "Club", "Vet", "Pet Grooming", "vegan restaurant") for each of our selected location in our two cities. We will store the information into dataframes formatted accodingly and export them into separate csv files.


3 - Geoqueries - **3 - Near Geoqueries.ipynb**: data coming from previous step need to be transformed in order to be stored in a mongo database, specifically coordenates information (to point type). Once data is with the adecuate format, we create two collections in Mongo Compass (2dsphere indexed), one per city. We will store there the geoqueries which will give us back venues not far form the maximum distance w stablished from our offices addreses. These geoqueries will also have a new parameter called distance, where the distance between our offices addreses and each venue will be calculated.


4 - Compare results of each city and calculate city ranking - **4 - Compare cities.ipynb**: In order to find out which of the two cities is more convenient for our requirements we need to stablish a ranking method. This will be min-max scaling normalization for the distance column and weights of importance will be asigned by venue type based on our priority requirements explanined before. 


5 - San Francisco venues display - **5 - San Francisco Map.ipynb**- San Francisco came up to be the most suitable city to stablish the company's headquarters. We used folium to represent the final venues display around the new office.

## Libraries

[sys](https://docs.python.org/3/library/sys.html)

[requests](https://pypi.org/project/requests/2.7.0/)

[pandas](https://pandas.pydata.org/)

[dotenv](https://pypi.org/project/python-dotenv/)

[pymongo](https://www.mongodb.com/2)

[json](https://docs.python.org/3/library/json.html)

[os](https://docs.python.org/3/library/os.html)

[geopandas](https://geopandas.org/)

[shapely](https://pypi.org/project/Shapely/)

[reduce](https://docs.python.org/3/library/functools.html)

[operator](https://docs.python.org/3/library/operator.html)

[import dumps](https://pymongo.readthedocs.io/en/stable/api/bson/json_util.html)

[re](https://docs.python.org/3/library/re.html)

[folium](https://python-visualization.github.io/folium/)
