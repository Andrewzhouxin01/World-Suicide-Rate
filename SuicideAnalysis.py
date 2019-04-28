# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 10:08:30 2019

@author: m48115
"""

import pandas as pd

SDF = pd.read_csv("H:\Documents\PythonProrams\Suicide Rates\master.csv")

SDF.head()

SDF.columns


SDF.rename(columns={'country':'Country',
                    'year':'Year',
                    'sex':'Gender',
                    'age':'Age',
                    'suicides_no':'SuicidesNo',
                    'population':'Population',
                    'suicides/100k pop':'Suicides100kPop',
                    'country-year':'CountryYear',
                    'HDI for year':'HDIForYear',
                    ' gdp_for_year ($) ':'GdpForYearMoney',
                    'gdp_per_capita ($)':'GdpPerCapitalMoney',
                    'generation':'Generation'}
            , inplace=True)


SDF.isnull().any()

#Most value for HDIForYear is empty, so we can delete this varable;
SDF.isnull().sum()

#How many rows and columns in this dataframe?
# (27820, 12)
SDF.shape

#Which fields have too many null values?
SDF.isnull().any()
#HDIForYear has null value
SDF.isnull().sum()
#HDIForYear has 19456 null value
NullRate=(SDF["HDIForYear"].isnull().sum())/27820
print(NullRate)
#HDIForYear 70% null value

#We can drop the fields HDIForYear and CountryYear
SDF.drop(columns=['HDIForYear','CountryYear'],inplace=True)

SDF.columns


SDF.to_csv("H:\Documents\PythonProrams\Suicide Rates\SuicideDataPhase01.csv",encoding='utf-8', index=False)




    
