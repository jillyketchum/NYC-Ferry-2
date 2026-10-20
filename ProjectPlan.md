Overview:
The goal of our project is to analyze whether global food prices relate to food insecurity rates. To do this, we will use three datasets from the World Bank’s Data360 site: food price inflation, the food consumer price index, and the number of people who are moderately or severely food insecure. Together, these datasets allow us to understand whether countries with sharper or more sustained food price increases saw larger rises in food insecurity. Our approach follows the data curation workflow discussed in class. We will first collect each dataset through the Data360 API using separate Python Scripts. Next, we will assess the quality of each dataset across accuracy, completeness, timeliness, and consistency, all of which will help to clean the datasets. This also includes standardizing data and handling missing data. Then, we will merge the cleaned datasets by country and year, fulfilling the assignment requirement that the datasets must be joined. After verifying everything is ready for analysis, we can analyze how food price trends relate to changes in food insecurity. All of the discussed content will be written in a final report. 

Team:

Christine W: 
- Collect metadata for each dataset for reproducibility and provenance
- Exploratory analysis into datasets. Assessment of accuracy, completeness, timeliness, and consistency. (with Jillian)
- Cleaning the joined dataset (with Ella)
- Finalize the written report (with the entire group)

Jillian K: 
- Identify legal constraints for the use and analysis of each dataset
- Download/collect the datasets (with Christine)
- Exploratory analysis into datasets (with Christine)
- Provide a workflow (with Shubhayon)
- Finalize the written report (with the entire group)

Shubhayon M:
- Evaluate data lifecycle for each dataset
- Join the datasets (with Ella)
- Evaluate accuracy, completeness, timeliness, consistency for joined dataset (with Ella)
- Provide workflow (with Jillian)
- Finalize the written report (with the entire group)

Ella N:
- Collect data on the organization behind the creation of each dataset
- Join the datasets (with Shubhayon)
- Assess accuracy, completeness, timeliness, and consistency for the joined dataset (with Shubhayon)
- Clean the joined dataset (with Christine)
- Create a ReadMe file
- Finalize the written report (with the entire group)


Research Question:

Datasets:

Timeline:

Constraints:
One of the main challenges we expect is the size and structure of the data. Each dataset covers nearly every country over many years, and once the three are combined, the result could become large and difficult to manage. The data also comes in a long format, with separate rows for each country, year, and indicator, so it will need a lot of reshaping before merging. This could make processing and analysis slow, especially if the data needs to be downloaded in multiple batches. Completeness of data is another concern as not every country reports data for every year, and the food insecurity data is particularly likely to have gaps for countries affected by conflict or with limited statistical capacity. These missing values could skew our results, since the countries with the least data are often the ones facing the most severe food insecurity. We will need to document these gaps carefully and decide whether to drop, fill, or separately analyze incomplete records.

Gaps:
There are still a few areas where we need to make decisions or would benefit from additional input. First we haven’t decided on how to handle countries with missing food insecurity data and whether to drop them, fill gaps, or limit our analysis to countries with complete data. Second, we still need to determine the best way to match annual price data to the three-year food insecurity averages. One option is to average the price data over the same three years or match each window to its middle year. Finally, we haven’t chosen which analysis methods to use, such as correlation, regression, or comparing country groups, and we expect to make a final decision once we see what the cleaned and integrated data looks like.
