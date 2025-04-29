### original graph
sns.histplot(data = df_gapminder[df_gapminder['year']==2007], x = 'population', stat = 'probability');


### The plot is extremely **right-skewed**. We could transform it using a log-transform.
df_gapminder['pop_log'] = df_gapminder['population'].apply(lambda x: np.log10(x))
sns.histplot(data = df_gapminder, x = 'pop_log', stat = 'probability');
plt.xlabel("Population (Log 10)")

### Rather than transforming the data directly, we can do this using `sns.histplot`.

sns.histplot(data = df_gapminder, x = 'pop_log', stat = 'probability', log_scale = True);