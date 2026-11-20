<h2>Task Progress and Updated Timeline</h2>
Looking at our feedback from Milestone 2, we did not make any changes to the content of our plan based on that since there were no critiques. However, since there are more factors to consider for joining the datasets, we will continue to revise that section to help best answer our project question.

1. Check data lifecycle of each dataset: We will relate our project to one or more of the lifecycle models discussed in class.
  - Completed by Shubhayon

2. Collect metadata for each dataset: 
  - Completed by Christine

3. Collect data on the organization behind the creation of each dataset: 
  - Completed by Ella

4. Identify legal constraints for the use and analysis of each dataset: This includes issues related to copyright, licenses, and terms for all of our datasets. This information will be added to the written report as well.
  - Completed by Jillian

5. Download/collect the datasets: Once datasets are found, a paragraph for the written report will be made with all four quality dimensions used in grading: accuracy, completeness, timeliness, and consistency
  - Completed by Christine, Jillian

6. Exploratory analysis into datasets. Assessment of accuracy, completeness, timeliness, and consistency. Check if it is feasible to join the datasets and if they are able to answer the research question
  - Completed by Jillian, Christine

7. Joining datasets: The datasets each contribute different information related to food insecurity needed to address our question, and they will be joined into one dataset
  - In progress by Shubhayon, Ella

8. Assessment of accuracy, completeness, timeliness, and consistency for the joined dataset
  - In progress by Shubhayon, Ella

9. Cleaning datasets: The datasets will be cleaned, missing values will be taken care of, as well as columns that we do not need for our analysis will be dropped. We will add to the written report the data cleaning methods applied (e.g., missing values, outliers, syntactic or semantic cleaning)
  - Date to be completed: Nov 25, 2026
  - Completed by who: Christine, Ella

10. Provide a workflow composed of separate, single-purpose scripts tied together by an orchestrator
  - Date to be completed: Dec 1st, 2026
  - Completed by who: Shubhayon, Jillian

11. Create a ReadMe file: A written description that introduces the project and how to use it.
  - Date to be completed: Dec 6th, 2026
  - Completed by who: Ella

12. Finalize written report: Many components of the report will be worked on as the above steps are completed, so our final step is to make sure the report includes all necessary components.
  - Date completed: Dec 8th, 2026
  - Completed by who: Christine, Ella, Shubhayon, Jillian

<h2>Changes to Project Plan</h2>
Looking at our feedback from Milestone 2, we did not make any changes to the content of our plan based on that since there were no critiques. However, since there are more factors to consider for joining the datasets, we will continue to revise that section to help best answer our project question. 
<br>

<h2>Challenges</h2>
We ran into a few challenges so far. First, the food insecurity data reports the number of people rather than a rate, so large countries dominate the results. We plan to add population data to convert the counts into rates. Second, food price inflation is calculated directly from the food CPI, so we will use inflation as our main price measure and the CPI only as a check. Third, the price data is monthly, while food insecurity is a three-year average. We resolved this by averaging inflation into matching three-year windows, and we will account for the overlapping windows when we choose our analysis methods. Several major countries, like India and China, are also missing food insecurity data, so we will make clear that our results only apply to the countries FAO reports on. We will keep the extreme hyperinflation values but reduce their effect with a log transformation. Finally, we originally downloaded the data by hand, which isn't reproducible, so we wrote collect_data.py to pull all three datasets from the API.
<br>

<h2>Individual Contributions</h2>
<b>Shubhayon:</b> I was responsible for understanding and applying a data lifecycle framework to our datasets and project as a whole. I chose to apply them to the USGS data lifecycle because that is the one I am the most familiar with, having learned about it and applied it in another course. I then looked at the requirements of the project, what we have done so far, and what we have agreed to do in the coming weeks and wrote a more detailed description for each stage of the framework. Finally, I pushed it to our GitHub repository under the name “Data_Lifecycle.md”. Along with exploring methods to join the datasets with Ella, I also began looking at the dimensions of data quality for the merged dataset, which once again are accuracy, timeliness, completeness, and consistency. So far, I have only looked at timeliness, but I will evaluate the others in the coming days This is available under the name "Merged_Data_Quality_Dimensions.md".<br> 
<br>
<b>Ella:</b> My first task was to collect data on the organization behind the creation of each dataset. We found our datasets on the World Bank’s Data360 platform, but the original data is from the Food and Agriculture Organization of the United Nations (FAO). I started by exploring the FAO website, specifically their “About” page, to learn more about the organization. Once I gathered information from that page, I looked into each individual dataset and the information relevant to how FAO relates to the creation of the dataset and how they categorize food insecurity levels. The information is pushed to our GitHub repository under “Org_Data.md”. I also explored methods of joining the datasets for another step in our timeline that I am completing with Shubhayon. Initially, I merged the datasets using vertical concatenation because the three datasets shared column names, and I wanted to preserve as much information as possible since the cleaning step comes later. However, I realized that this is not the best method for answering our project question because the datasets use different measurements of time (temporal granularity mismatch of months versus years), so the observed value would not be an accurate representation. Finally, I merged the datasets by first grouping all the years together to produce 3-year statistics. This is uploaded to our GitHub repository as a file titled “join_datasets.ipynb”. Shubhayon and I are also evaluating the dimensions of data quality for the merged dataset, and so far, I have looked at the completeness of the dataset.
<br>
<b>Christine:</b> My first task in this process was collecting metadata about the 3 datasets that we used: Food price inflation, Moderately or severely food insecure people (million) (3-year average), and Consumer Prices, Food Indices (2015 = 100). When reviewing the webpages about each dataset on the World Bank Group website, I was able to locate metadata documents for each dataset. In the DatasetMetadata.md that I created to record the information, I included details on document names, versions, tagging, authors, and more. While Jillian decided to access the datasets through APIs, I decided to explore the data just my downloading through the button the each of the webpages. Out of all the download formats, I chose the SDMX CSV, which I learned is just a CSV but with stricter limitations. The next steps I took in the Jupiter Notebook named ACTC_Report.ipynb looks into accuracy, completeness, timeliness, and consistency. I first did an initial exploratory analysis, so I looked at the datatypes, null/non-null counts, and structure. Then I honed in to access each factor separately. For accuracy, I tried to check for extremities and making sure that the data values felt feasible. For completeness, I checked for missing timestamps for each included area in the dataset. I also checked whether or not the same areas were mentioned between the three datasets. Timeliness can be accessed using the metadata on the webpage about the update schedules, which in this case, are annual or monthly. 
