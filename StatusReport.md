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
<h2>Challenges</h2>
<h2>Individual Contributions</h2>
<b>Shubhayon:</b> I was responsible for understanding and applying a data lifecycle framework to our datasets and project as a whole. I chose to apply them to the USGS data lifecycle because that is the one I am the most familiar with, having learned about it and applied it in another course. I then looked at the requirements of the project, what we have done so far, and what we have agreed to do in the coming weeks and wrote a more detailed description for each stage of the framework. Finally, I pushed it to our GitHub repository under the name “Data_Lifecycle.md”. Along with exploring methods to join the datasets with Ella, I also began looking at the dimensions of data quality for the merged dataset, which once again are accuracy, timeliness, completeness, and consistency. So far, I have only looked at timeliness, but I will evaluate the others in the coming days This is available under the name "Merged_Data_Quality_Dimensions.md".<br> 
<br>
<b>Ella:</b> My first task was to collect data on the organization behind the creation of each dataset. We found our datasets on the World Bank’s Data360 platform, but the original data is from the Food and Agriculture Organization of the United Nations (FAO). I started by exploring the FAO website, specifically their “About” page, to learn more about the organization. Once I gathered information from that page, I looked into each individual dataset and the information relevant to how FAO relates to the creation of the dataset and how they categorize food insecurity levels. The information is pushed to our GitHub repository under “Org_Data.md”. I also explored methods of joining the datasets for another step in our timeline that I am completing with Shubhayon. Initially, I merged the datasets using vertical concatenation because the three datasets shared column names, and I wanted to preserve as much information as possible since the cleaning step comes later. However, I realized that this is not the best method for answering our project question because the datasets use different measurements of time (temporal granularity mismatch of months versus years), so the observed value would not be an accurate representation. Finally, I merged the datasets by first grouping all the years together to produce 3-year statistics. This is uploaded to our GitHub repository as a file titled “join_datasets.ipynb”. Shubhayon and I are also evaluating the dimensions of data quality for the merged dataset, and so far, I have looked at the completeness of the dataset.
