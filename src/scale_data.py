""" scale_data.py

This File is where information from our 
GoogleSheets Database is pre-processed for analysis

    SCALE PROJECT -- KRONFORST LABORATORY AT THE UNIVERSITY OF CHICAGO 
                  -- ALL RIGHTS RESERVED 
        
        Lukas Elsrode - Undergraduate Researcher at the Kronforst Laboratory wrote and tested this code 
        (10/21/2021)
"""
# %%
import pandas as pd  # We use Pandas.DataFrame Object Classes to hold our data
import json          # We keep our database access limited
import os

# The Numeric Ranges of Our Measurements in the GoogleSheets Spreadsheet
DEFAULT_WT_RANGE = (8, 15)
DEFAULT_MUTANT_RANGE = (14, 21)
DEFAULT_SAMPLES_RANGE = (12, 19)

# Associate Inputs to get a certain DataFrame to work with
sheet_input_range = {
    'wt_table': DEFAULT_WT_RANGE,
    'mutant_table': DEFAULT_MUTANT_RANGE,
    'samples_info': DEFAULT_SAMPLES_RANGE
}


def get_secret():
    os.chdir('../')
    file = open('secret.json',)
    return json.load(file)['sheet_id']

# We write a function to get and write into a Pandas.DataFrame from a URL


def get_df(sheet_name='wt_table'):
    """Returns DataFrame of Relevant DataSheet Associated with our DataBase 
        Inputs:
            (string)- sheet_name : Name of the sheet i.e 'wt_table','mutant_table','samples_info'
        Outputs:
            ('Pandas.DataFrame' Class Object) - df_raw : Raw Data of our study formated
    """
    # get secret #
    secret = get_secret()
    # get data
    url = f"https://docs.google.com/spreadsheets/d/{secret}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    df = pd.read_csv(url)
    rv = []
    # manual cleaning of columns
    for c in df.columns:
        if c[0:3] == 'Unn':
            pass
        else:
            rv.append(c)
    df = df[rv]

    # get the numeric range of measurement entries
    q1, q2 = sheet_input_range[sheet_name]
    # define the columns which are numbers not strings
    quant_vars = [i for i in df.columns[q1:q2]]
    qual_vars = [i for i in df.columns if i not in quant_vars]
    # Force strings into floats
    for numeric_var in quant_vars:
        df[numeric_var] = pd.to_numeric(
            df[numeric_var], errors='coerce')

    for qual_var in qual_vars:
        # Format some strings to be uniform
        df[qual_var] = [str(i).lower().replace(" ", "")
                        for i in df[qual_var].values]

    return df


# Something to split up the Phylogenetic portion of the data
def segment_df_by_field(df, group_by='f'):
    """ Segments Pandas.DataFrame of Data by Group of total entries within the set of Group_By
        i.e 'scale_color'

            Inputs: 
                (string) - group_by: Single letter to represent what to segment the dataset by
                    ________________
                    'f': by family -- DEFAULT VALUE
                    's': by species
                    'g': by genotype
                    'sf': by subfamily
                    't': by tribe
                    'ge': by genus
                    'c': by scale color

            Outputs:
                (list of 'Pandas.DataFrame' Object Classes) - l : A list of datasets 
                    segmented by all values in the group_by set.
    """
    # initilize list to return
    l = []

    # set of all_possible results
    all_species, all_families, all_colors, all_genotypes, all_subfams, all_tribes, all_genuses = set(df.species), set(
        df.family), set(df.scale_color), set(df.genotype), set(df.subfamily), set(df.tribe), set(df.genus)

    # initilize relavant dictionary
    d = {'f': ('family', all_families),
         's': ('species', all_species),
         'c': ('scale_color', all_colors),
         'g': ('genotype', all_genotypes),
         'sf': ('subfamily', all_subfams),
         't': ('tribe', all_tribes),
         'ge': ('genus', all_genuses)}

    # set the variables needed
    # breaking up the data-frame

    for m in d[group_by][1]:
        df_member = df[df[d[group_by][0]] == m]
        l.append(df_member)

    return l


# THE THREE MAIN DATAFRAMES COMPRISING OUR STUDY
WT_DATA, SAMPLES_DATA, MUTANT_DATA = get_df(), get_df(
    'samples_info'), get_df('mutant_table')

print(WT_DATA)

# %%
