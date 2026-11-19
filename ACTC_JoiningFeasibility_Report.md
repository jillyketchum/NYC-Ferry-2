# Accuracy, Completeness, Timeliness, Consistency and Feasibility of Joining Analysis Report


### Accuracy: 

All missing data in price data is from Nicaragua. Each missing value is labelled “Missing value,” and there is no estimation/ imputation flags in these data. The food price inflation data (23014) can be perfectly recreated using the food CPI data (23013). Calculating year-on-year change from the index values in 61,048 corresponding data points gave agreement to within 0.1%. However, extreme values do occur due to hyper-inflation. In Venezuela, the index reaches ~2.9tn. Monthly inflation rates reach ~371,000% in early 2019. Hyper-inflation greater than 100% occurs in many countries too: Zimbabwe, Lebanon, Argentina, Sudan, South Sudan, Syria, Türkiye, Haiti and more. While these values seem plausible, they will have an overriding affect on the correlation. Some negative values are unusual. The West Bank and Gaza region show a value of ~-42% in late 2025. This is worth double-checking. Food insecurity data does not contain any flags, however since they are modelled estimates from surveys, uncertainty is present within the data.



### Completeness: 

Price data contains data for 204 regions, and is almost complete with only 12 missing data points in Syria, and 2 in Madagascar. Only 4 data sets end early: DR Congo, Venezuela (Oct 2024), Yemen, and British Virgin Islands. The food insecurity data is very incomplete. It contains data for 136 countries, but is very unbalanced. Only 93 countries had values in the first time window (2014-16), increasing to approximately 132 in 2022/23. Due to many missing data points, several countries with the highest food insecurity are completely missing (India, China, Sudan, Somalia, Syria, Iraq, Venezuela). Therefore any correlation found only applies to the countries that the FAO are reporting on, not globally. Within this data, 3 entries exist for each country and window: total, male and female. Therefore, 2/3 of data is redundant, and only total data (SEX = _T) should be taken.



### Timeliness:

The price data is recent. 199/204 regions in price data go up to March 2026. The food insecurity data however ends in 2023/25. Since it is an average over 3 years, this means that we effectively only have 10 time windows. This is limiting in our analysis. As the windows overlap, consecutive values for a given country will have 2 out of 3 years in common. Therefore, the data points are not independent. Much of the monthly price data is not used in this analysis. In 2026, there is no corresponding food insecurity data.



### Consistency: 

Since one variable can be derived from the other, only one of the price data sets should be used in an analysis. If both were used, we would be double-counting the same data. The units do not match between the two. Price inflation is given as a monthly (year-on-year) % value, whereas food insecurity is an average over 3 years (given by the end year of the time window). The units do not match either. Food insecurity is given in terms of the number of people (millions), not a proportion. No population data or proportions are included. Therefore, correlating with count data mainly reflects population size. The 3 countries with the highest food insecurity in 2022/24 are Nigeria (170 million people), Ethiopia (79 million people) and Pakistan (56 million people) purely due to them having large populations. ISO3 codes are consistent across data sets, and keys match well. The only country missing from the price data is Guyana.



### Feasibility of joining:

It is feasible to merge our three datasets. All three use the same ISO3 country codes, so we can join them based on country code and year. Of the 136 countries in the food insecurity dataset, 135 also appear in both price datasets. The only one missing is Guyana, which does not have food price data. 
Before merging, we need to make a few adjustments. First, the food insecurity data has three rows for each country and year (Total, Male, and Female), so we will keep only the Total rows to avoid triple counting. Second, the time periods don’t line up. The price data is monthly, while the food insecurity data is a three-year average labeled by its last year. To match them, we will average the monthly inflation data into yearly values, then into the same three-year windows as the food insecurity data. For the few countries with missing months, such as Madagascar, we will calculate the yearly averages from the months that are available. When we tested this, the merge produced 1,148 matched observations across 134 countries. However, because the three-year windows overlap, neighboring observations for the same country share two of their three years, so they are not fully independent. We will need to keep this in mind when choosing our analysis methods and interpreting our results. 
The merged data can answer our research question, with two changes. Our question is about food insecurity rates, but the dataset reports the number of people in millions, so we will need to add population data or look at changes within each country. Otherwise, large countries like Nigeria would dominate the results just because of their size. Also, since food price inflation is calculated directly from the food CPI, we will use only inflation as our main price measure, so we don’t count the same information twice.
