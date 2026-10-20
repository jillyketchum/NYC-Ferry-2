Overview:

Team:

Research Question:

Datasets:

Timeline:

Constraints:
One of the main challenges we expect is the size and structure of the data. Each dataset covers nearly every country over many years, and once the three are combined, the result could become large and difficult to manage. The data also comes in a long format, with separate rows for each country, year, and indicator, so it will need a lot of reshaping before merging. This could make processing and analysis slow, especially if the data needs to be downloaded in multiple batches. Completeness of data is another concern as not every country reports data for every year, and the food insecurity data is particularly likely to have gaps for countries affected by conflict or with limited statistical capacity. These missing values could skew our results, since the countries with the least data are often the ones facing the most severe food insecurity. We will need to document these gaps carefully and decide whether to drop, fill, or separately analyze incomplete records.

Gaps:
There are still a few areas where we need to make decisions or would benefit from additional input. First we haven’t decided on how to handle countries with missing food insecurity data and whether to drop them, fill gaps, or limit our analysis to countries with complete data. Second, we still need to determine the best way to match annual price data to the three-year food insecurity averages. One option is to average the price data over the same three years or match each window to its middle year. Finally, we haven’t chosen which analysis methods to use, such as correlation, regression, or comparing country groups, and we expect to make a final decision once we see what the cleaned and integrated data looks like.
