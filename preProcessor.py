
import pandas as pd


# Function to change "Not Available" to 0
def cleanNotAvailable(var):
    if str(var) == 'Not Available':
        return 0.0
    else:
        return float(var)

# Function to code Principal activity
def coding(col, codeDict):
  colCoded = pd.Series(col, copy=True)
  for key, value in codeDict.items():
    colCoded.replace(key, value, inplace=True)
  return colCoded


def preProcessTrain(x):
    df = pd.read_csv(x)

    dfnew = pd.DataFrame(
        columns=["Year Built", "Number of Buildings - Self-reported", "Occupancy", "Site EUI (kBtu/ft²)", 
                "Natural Gas Use (kBtu)", "Weather Normalized Site Natural Gas Use (therms)", 
                "Weather Normalized Site Electricity (kWh)", "Total GHG Emissions (Metric Tons CO2e)", 
                "Direct GHG Emissions (Metric Tons CO2e)", "Indirect GHG Emissions (Metric Tons CO2e)",
                "Property GFA - Self-Reported (ft²)", "Water Use (All Water Sources) (kgal)", 
                "Water Intensity (All Water Sources) (gal/ft²)", "Source EUI (kBtu/ft²)",
                "Primary Property Type - Self Selected", 

                "Largest Property Use Type (ft²)", "2nd Largest Property Use (ft²)",
                "3rd Largest Property Use Type (ft²)", "Total area (ft²)", "Site Gas (kBtu/ft²)",
                "Electricity Use Grid Purchase (kBtu)",
                "ENERGY STAR Score", "Property Id"])


    dfnew["Property Id"] = df["Property Id"]
    dfnew["ENERGY STAR Score"] = df["ENERGY STAR Score"]
    dfnew["Year Built"] = df["Year Built"]
    dfnew["Number of Buildings - Self-reported"] = df["Number of Buildings - Self-reported"]
    dfnew["Occupancy"] = df["Occupancy"]
    dfnew["Site EUI (kBtu/ft²)"] = df["Site EUI (kBtu/ft²)"]
    dfnew["Primary Property Type - Self Selected"] = df["Primary Property Type - Self Selected"]


        # Tratando o Not Available 
    dfnew["Natural Gas Use (kBtu)"] = df["Natural Gas Use (kBtu)"].apply(cleanNotAvailable)
    dfnew["Weather Normalized Site Natural Gas Use (therms)"] = df["Weather Normalized Site Natural Gas Use (therms)"].apply(cleanNotAvailable)
    dfnew["Electricity Use - Grid Purchase (kBtu)"] = df["Electricity Use - Grid Purchase (kBtu)"].apply(cleanNotAvailable)
    dfnew["Weather Normalized Site Electricity (kWh)"] = df["Weather Normalized Site Electricity (kWh)"].apply(cleanNotAvailable)
    dfnew["Total GHG Emissions (Metric Tons CO2e)"] = df["Total GHG Emissions (Metric Tons CO2e)"].apply(cleanNotAvailable)
    dfnew["Direct GHG Emissions (Metric Tons CO2e)"] = df["Direct GHG Emissions (Metric Tons CO2e)"].apply(cleanNotAvailable)
    dfnew["Indirect GHG Emissions (Metric Tons CO2e)"] = df["Indirect GHG Emissions (Metric Tons CO2e)"].apply(cleanNotAvailable)
    dfnew["Property GFA - Self-Reported (ft²)"] = df["Property GFA - Self-Reported (ft²)"].apply(cleanNotAvailable)
    dfnew["Water Use (All Water Sources) (kgal)"] = df["Water Use (All Water Sources) (kgal)"].apply(cleanNotAvailable)
    dfnew["Water Intensity (All Water Sources) (gal/ft²)"] = df["Water Intensity (All Water Sources) (gal/ft²)"].apply(cleanNotAvailable)
    dfnew["Source EUI (kBtu/ft²)"] = df["Source EUI (kBtu/ft²)"].apply(cleanNotAvailable)
    dfnew["Largest Property Use Type (ft²)"] = df["Largest Property Use Type - Gross Floor Area (ft²)"].apply(cleanNotAvailable)
    dfnew["2nd Largest Property Use (ft²)"] = df["2nd Largest Property Use - Gross Floor Area (ft²)"].apply(cleanNotAvailable)
    dfnew["3rd Largest Property Use Type (ft²)"] = df["3rd Largest Property Use Type - Gross Floor Area (ft²)"].apply(cleanNotAvailable)
    dfnew["Electricity Use Grid Purchase (kBtu)"] = df["Electricity Use - Grid Purchase (kBtu)"].apply(cleanNotAvailable)
    dfnew["Total GHG Emissions (Metric Tons CO2e)"] = df["Total GHG Emissions (Metric Tons CO2e)"].apply(cleanNotAvailable)
    dfnew["Water Use (All Water Sources) (kgal)"] = df["Water Use (All Water Sources) (kgal)"].apply(cleanNotAvailable)

    dfnew["Total area (ft²)"] = dfnew["Largest Property Use Type (ft²)"] + dfnew["2nd Largest Property Use (ft²)"] + dfnew["3rd Largest Property Use Type (ft²)"]
    dfnew["Site Gas (kBtu/ft²)"] = dfnew["Natural Gas Use (kBtu)"] / dfnew["Total area (ft²)"]
    dfnew["Electricity Use Area (kBtu/ft²)"] = dfnew["Electricity Use Grid Purchase (kBtu)"] / dfnew["Total area (ft²)"]
    dfnew["GHG Emissions Area (Metric Tons CO2e/ft²)"] = dfnew["Total GHG Emissions (Metric Tons CO2e)"] / dfnew["Total area (ft²)"]
    dfnew["Water use Area (kgal/ft²)"] = dfnew["Water Use (All Water Sources) (kgal)"] / dfnew["Total area (ft²)"]

    dfnew["Code Property Type"] = coding(df["Primary Property Type - Self Selected"], 
            { 'Multifamily Housing':0,
            'Office':1,
            'Hotel':2,
            'Non-Refrigerated Warehouse':3,
            'Residence Hall/Dormitory':4,
            'K-12 School':5,
            'Senior Care Community':6,
            'Distribution Center':7,
            'Retail Store':8,
            'Other':9,
            'Medical Office': 10,
            'College/University': 11,
            'Hospital (General Medical & Surgical)': 12,
            'Financial Office': 13,
            'Worship Facility':14,
            'Mixed Use Property': 15,
            'Supermarket/Grocery Store': 16,
            'Refrigerated Warehouse': 17,
            'Wholesale Club/Supercenter': 18,
            'Self-Storage Facility': 19,
            'Courthouse': 20,
            'Residential Care Facility': 21,
            'Bank Branch': 22,
            'Manufacturing/Industrial Plant': 23,
            'Fitness Center/Health Club/Gym':24})

    return dfnew

def preProcessTest(x):
    df = pd.read_csv(x)

    dfnew = pd.DataFrame(
        columns=["Year Built", "Number of Buildings - Self-reported", "Occupancy", "Site EUI (kBtu/ft²)", 
                "Natural Gas Use (kBtu)", "Weather Normalized Site Natural Gas Use (therms)", 
                "Weather Normalized Site Electricity (kWh)", "Total GHG Emissions (Metric Tons CO2e)", 
                "Direct GHG Emissions (Metric Tons CO2e)", "Indirect GHG Emissions (Metric Tons CO2e)",
                "Property GFA - Self-Reported (ft²)", "Water Use (All Water Sources) (kgal)", 
                "Water Intensity (All Water Sources) (gal/ft²)", "Source EUI (kBtu/ft²)", 
                "Largest Property Use Type (ft²)", "2nd Largest Property Use (ft²)",
                "3rd Largest Property Use Type (ft²)", "Total area (ft²)", "Site Gas (kBtu/ft²)",
                "Electricity Use Grid Purchase (kBtu)", 
                "Property Id"])


    dfnew["Property Id"] = df["Property Id"]
    dfnew["Year Built"] = df["Year Built"]
    dfnew["Number of Buildings - Self-reported"] = df["Number of Buildings - Self-reported"]
    dfnew["Occupancy"] = df["Occupancy"]
    dfnew["Site EUI (kBtu/ft²)"] = df["Site EUI (kBtu/ft²)"]


        # Tratando o Not Available 
    dfnew["Natural Gas Use (kBtu)"] = df["Natural Gas Use (kBtu)"].apply(cleanNotAvailable)
    dfnew["Weather Normalized Site Natural Gas Use (therms)"] = df["Weather Normalized Site Natural Gas Use (therms)"].apply(cleanNotAvailable)
    dfnew["Electricity Use - Grid Purchase (kBtu)"] = df["Electricity Use - Grid Purchase (kBtu)"].apply(cleanNotAvailable)
    dfnew["Weather Normalized Site Electricity (kWh)"] = df["Weather Normalized Site Electricity (kWh)"].apply(cleanNotAvailable)
    dfnew["Total GHG Emissions (Metric Tons CO2e)"] = df["Total GHG Emissions (Metric Tons CO2e)"].apply(cleanNotAvailable)
    dfnew["Direct GHG Emissions (Metric Tons CO2e)"] = df["Direct GHG Emissions (Metric Tons CO2e)"].apply(cleanNotAvailable)
    dfnew["Indirect GHG Emissions (Metric Tons CO2e)"] = df["Indirect GHG Emissions (Metric Tons CO2e)"].apply(cleanNotAvailable)
    dfnew["Property GFA - Self-Reported (ft²)"] = df["Property GFA - Self-Reported (ft²)"].apply(cleanNotAvailable)
    dfnew["Water Use (All Water Sources) (kgal)"] = df["Water Use (All Water Sources) (kgal)"].apply(cleanNotAvailable)
    dfnew["Water Intensity (All Water Sources) (gal/ft²)"] = df["Water Intensity (All Water Sources) (gal/ft²)"].apply(cleanNotAvailable)
    dfnew["Source EUI (kBtu/ft²)"] = df["Source EUI (kBtu/ft²)"].apply(cleanNotAvailable)
    dfnew["Largest Property Use Type (ft²)"] = df["Largest Property Use Type - Gross Floor Area (ft²)"].apply(cleanNotAvailable)
    dfnew["2nd Largest Property Use (ft²)"] = df["2nd Largest Property Use - Gross Floor Area (ft²)"].apply(cleanNotAvailable)
    dfnew["3rd Largest Property Use Type (ft²)"] = df["3rd Largest Property Use Type - Gross Floor Area (ft²)"].apply(cleanNotAvailable)
    dfnew["Electricity Use Grid Purchase (kBtu)"] = df["Electricity Use - Grid Purchase (kBtu)"].apply(cleanNotAvailable)
    dfnew["Total GHG Emissions (Metric Tons CO2e)"] = df["Total GHG Emissions (Metric Tons CO2e)"].apply(cleanNotAvailable)
    dfnew["Water Use (All Water Sources) (kgal)"] = df["Water Use (All Water Sources) (kgal)"].apply(cleanNotAvailable)

    dfnew["Total area (ft²)"] = dfnew["Largest Property Use Type (ft²)"] + dfnew["2nd Largest Property Use (ft²)"] + dfnew["3rd Largest Property Use Type (ft²)"]
    dfnew["Site Gas (kBtu/ft²)"] = dfnew["Natural Gas Use (kBtu)"] / dfnew["Total area (ft²)"]
    dfnew["Electricity Use Area (kBtu/ft²)"] = dfnew["Electricity Use Grid Purchase (kBtu)"] / dfnew["Total area (ft²)"]
    dfnew["GHG Emissions Area (Metric Tons CO2e/ft²)"] = dfnew["Total GHG Emissions (Metric Tons CO2e)"] / dfnew["Total area (ft²)"]
    dfnew["Water use Area (kgal/ft²)"] = dfnew["Water Use (All Water Sources) (kgal)"] / dfnew["Total area (ft²)"]

    dfnew["Code Property Type"] = coding(df["Primary Property Type - Self Selected"], 
            { 'Multifamily Housing':0,
            'Office':1,
            'Hotel':2,
            'Non-Refrigerated Warehouse':3,
            'Residence Hall/Dormitory':4,
            'K-12 School':5,
            'Senior Care Community':6,
            'Distribution Center':7,
            'Retail Store':8,
            'Other':9,
            'Medical Office': 10,
            'College/University': 11,
            'Hospital (General Medical & Surgical)': 12,
            'Financial Office': 13,
            'Worship Facility':14,
            'Mixed Use Property': 15,
            'Supermarket/Grocery Store': 16,
            'Refrigerated Warehouse': 17,
            'Wholesale Club/Supercenter': 18,
            'Self-Storage Facility': 19,
            'Courthouse': 20,
            'Residential Care Facility': 21,
            'Bank Branch': 22,
            'Manufacturing/Industrial Plant': 23,
            'Fitness Center/Health Club/Gym':24})

    return dfnew

