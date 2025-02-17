##importing libraries needed
import pandas as pd

##all sources from https://www.data.gov.uk/dataset/cb7ae6f0-4be6-4935-9277-47e5ce24a11f/road-safety-data

##identifying sources
##accidents
dfcollisions = pd.read_csv("https://data.dft.gov.uk/road-accidents-safety-data/dft-road-casualty-statistics-collision-2023.csv", low_memory=False, error_bad_lines=False)
dfcollisions2019 = pd.read_csv("https://data.dft.gov.uk/road-accidents-safety-data/dft-road-casualty-statistics-collision-2019.csv", low_memory=False, error_bad_lines=False)
dfcollisions2020 = pd.read_csv("https://data.dft.gov.uk/road-accidents-safety-data/dft-road-casualty-statistics-collision-2020.csv", low_memory=False, error_bad_lines=False)
dfcollisions2021 = pd.read_csv("https://data.dft.gov.uk/road-accidents-safety-data/dft-road-casualty-statistics-collision-2021.csv", low_memory=False, error_bad_lines=False)
dfcollisions2022 = pd.read_csv("https://data.dft.gov.uk/road-accidents-safety-data/dft-road-casualty-statistics-collision-2022.csv", low_memory=False, error_bad_lines=False)
##vehicles
dfvehicles = pd.read_csv("https://data.dft.gov.uk/road-accidents-safety-data/dft-road-casualty-statistics-vehicle-2023.csv", low_memory=False, error_bad_lines=False)
dfvehicles2019 = pd.read_csv("https://data.dft.gov.uk/road-accidents-safety-data/dft-road-casualty-statistics-vehicle-2019.csv", low_memory=False, error_bad_lines=False)
dfvehicles2020 = pd.read_csv("https://data.dft.gov.uk/road-accidents-safety-data/dft-road-casualty-statistics-vehicle-2020.csv", low_memory=False, error_bad_lines=False)
dfvehicles2021 = pd.read_csv("https://data.dft.gov.uk/road-accidents-safety-data/dft-road-casualty-statistics-vehicle-2021.csv", low_memory=False, error_bad_lines=False)
dfvehicles2022 = pd.read_csv("https://data.dft.gov.uk/road-accidents-safety-data/dft-road-casualty-statistics-vehicle-2022.csv", low_memory=False, error_bad_lines=False)

##casualties
dfcasualties= pd.read_csv("https://data.dft.gov.uk/road-accidents-safety-data/dft-road-casualty-statistics-casualty-2023.csv", low_memory=False, error_bad_lines=False)
dfcasualties2019= pd.read_csv("https://data.dft.gov.uk/road-accidents-safety-data/dft-road-casualty-statistics-casualty-2019.csv", low_memory=False, error_bad_lines=False)
dfcasualties2020= pd.read_csv("https://data.dft.gov.uk/road-accidents-safety-data/dft-road-casualty-statistics-casualty-2020.csv", low_memory=False, error_bad_lines=False)
dfcasualties2021= pd.read_csv("https://data.dft.gov.uk/road-accidents-safety-data/dft-road-casualty-statistics-casualty-2021.csv", low_memory=False, error_bad_lines=False)
dfcasualties2022= pd.read_csv("https://data.dft.gov.uk/road-accidents-safety-data/dft-road-casualty-statistics-casualty-2022.csv", low_memory=False, error_bad_lines=False)



##mergecolumns
merge1= pd.merge(dfcollisions, dfvehicles, how='outer')
merge2= pd.merge(merge1, dfcasualties, how='outer')

merge3= pd.merge(dfcollisions2019, dfvehicles2019, how='outer')
merge4= pd.merge(merge3, dfcasualties2019, how='outer')

merge6= pd.merge(dfcollisions2020, dfvehicles2020, how='outer')
merge7= pd.merge(merge6, dfcasualties2020, how='outer')

merge9= pd.merge(dfcollisions2021, dfvehicles2021, how='outer')
merge10= pd.merge(merge9, dfcasualties2021, how='outer')

merge12= pd.merge(dfcollisions2022, dfvehicles2022, how='outer')
merge13= pd.merge(merge12, dfcasualties2022, how='outer')


merge4.to_csv(r'code/A96_roadtrafficdata2019.csv')
merge7.to_csv(r'code/A96_roadtrafficdata2020.csv')
merge10.to_csv(r'code/A96_roadtrafficdata2021.csv')
merge13.to_csv(r'code/A96_roadtrafficdata2022.csv')
merge2.to_csv(r'code/A96_roadtrafficdata2023.csv')
