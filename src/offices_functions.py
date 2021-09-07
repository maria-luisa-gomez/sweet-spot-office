
def getFromDictColumn(column, dict_keys, dataset):
    """
    This fuction splits keys values into another columns from a selected column dictionary type from a dataset
    Input: 
    - column: column which values are dictioraries (key values)
    - dict_keys: the list of the keys you want to split into new columns
    - dataset: dataset you want to select the dict column from and add the new columns

    Out: dataset with the keys values selected converted to new columns
    """
    for key in dict_keys:
        dataset[key] = dataset[column].apply(lambda o : o.get(key))
    return dataset.head()