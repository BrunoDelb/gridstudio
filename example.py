# Read all data
df = pd.read_csv("https://opendata.ecdc.europa.eu/covid19/casedistribution/csv").dropna()
print(df.head())
# Convert date to integer (because of Grid Studio limitation)
df.dateRep = pd.to_datetime(df.dateRep, format='%d/%m/%Y').dt.strftime('%Y%m%d').astype(int)
# Filtrer
# Get Australia data
df_oz = df[df.countriesAndTerritories == 'Australia']
# select only the dateRep, cases and deaths columns.
df_oz = df_oz[['dateRep', 'cases', 'deaths']]
# calculate the cumulative cases and deaths.
df_oz = df_oz.sort_values('dateRep')
df_oz['cumCases'] = df_oz.cases.cumsum()
df_oz['cumDeaths'] = df_oz.deaths.cumsum()
# Show in sheet
sheet("A1", df_oz)
# Pandas / Plot
data = sheet("B1:B40")
data.plot(title='Daily New Cases')
show()
