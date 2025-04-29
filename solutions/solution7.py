sns.lineplot(data = df_melted, x = 'Year', y = 'Days Missed', hue = "Reason")

# To jest w porządku, ale nie do końca to, czego chcemy. To jest grupowanie według `Year`. Ale my chcemy grupować zarówno według `Year`, jak i `Month`.

# Wykorzystajmy `datetime`

# Stwórzmy nową kolumnę o nazwie `date`, która łączy `Month` i `Year`.
# Następnie możemy użyć `pd.to_datetime`, aby przekształcić ją w niestandardową reprezentację `pandas`.

# Najpierw połączmy każdy miesiąc i rok w jeden ciąg znaków

df_melted['date'] = df_melted.apply(lambda row: str(row['Month']) + '-' + str(row['Year']), axis = 1)
df_melted.head(2)

# Ponownie wykres:

sns.lineplot(data = df_melted, x = "datetime", y = "Days Missed", hue = "Reason");

# Duzo lepiej!


