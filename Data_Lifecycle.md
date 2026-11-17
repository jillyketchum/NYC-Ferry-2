Using a data lifecycle framework in a project is essential to making sure that data is managed, handled, and secured properly throughout its lifetime. Our project is no different, and we will be referring to the USGS data lifecycle to ensure that we can meet these goals. Our application of this framework is as follows:

Plan: The main goal of our project is to understand the dynamic relationship between food insecurity and inflation rates worldwide. These datasets give us the components necessary to do that. The Consumer Prices, Food Indices dataset tracks the changes in food prices, using 2015 as a reference point. Next, the Moderately or Severely Food Insecure dataset shows a three year rolling average of how many people are either moderately or severely food insecure in every country. Lastly, the Food Price Inflation dataset also tracks the changes in food prices, using percent change. 

Acquire: All three datasets come from the same source, and can either be downloaded as a CSV or accessed through an API. We will be downloading each as a CSV.

Process: In order to gain proper insights, the datasets need to be integrated and cleaned. Given each dataset contains information about countries around the world, they will be joined on their names. Then, the merged dataset needs to be cleaned. This includes correcting any formatting differences, making sure dates are valid, dropping irrelevant columns, and dealing with missing values. All of this will be done using both Python and Open Refine. 

Analyze: Using the integrated and cleaned dataset, we will be using tools such as Python and Microsoft Excel to look at patterns and trends using descriptive statistics and visualizations. 

Preserve: In order to preserve the work we did, we will keep copies at all of the steps the dataset(s) went through. There will be the three separated, original datasets, the merged and unclean dataset, and finally the merged and cleaned dataset.  

Publish: All of our progress, final work, analysis, and other findings will be pushed to GitHub in accordance with the requirements for this project. 
