# Final project

## Introduction

In the final project, your task will be to apply the **skills** acquired in this class to *exploratory data analysis* on a real data set (or data sets).

You will work in a small group (2-3). I strongly encourage you to contact me for feedback on your ideas.

## Grading and results

The final result (what you turn in) will be a link to REPO on GitHub, where your team will post all the project files: 

- Jupyter notebook with the following sections (see table below); each section is worth a certain number of points, adding up to 16; **minimum** number of points to pass the project is 10 (see [grading scale](syllabus.md#grading-scale)).
- data (e.g., CSV files).
- additional files, aesthetically published EDA reports in Markdown format (MD, HTML, PDF, etc.) are welcome.

> After submitting the final version of the project, each project group is required to schedule a short **online meeting** with me to discuss it. The meeting is intended to confirm the self-performance of the work and allows you to ask any questions you may have about the analysis.

| Section               | Points | Description                                                                                       | Example                                                                                     |
| :-------------------: | :----: | :---------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------: |
| Introduction          |   2    | What dataset are you looking at? Where/how was it created? What questions will be asked?         | A dataset on real estate prices in Poland - prices and characteristics of the property (number of rooms, floor, city, furnishings, etc.) |
| Cleaning and organizing data |   4    | Data diagnostics; missing data - visualization, discussion, pattern, data errors and their repair, imputation of missing data, outlier observations - analysis. | Shadowmaps, heatmaps of deficiencies, discussion of the pattern, strategies for imputation of deficiencies, definition of rules for data, visualization of violations, repair, analysis of outliers with discussion. |
| Visualizations        |   4    | 4-5 charts showing specific patterns or features you want to highlight. Each visualization should be accompanied by a brief (1-2 sentence) description of what you think it shows. | Boxplot showing **prices** of properties *by city* or other characteristics - cross sections. A bar chart showing the proportion of apartments **of different finishing standards**. |
| Descriptive analysis  |   4    | 2-3 descriptive analyses, relating to the research question(s). Each analysis should be accompanied by a brief (1-3 sentences) *interpretation*. | Tables of descriptive statistics - e.g., housing price statistics by various characteristics. It would be good if they were surrounded by visualizations on the same main topic. Correlation analysis - matrix of (linear) correlations. Correlation analysis of other types (rank, qualitative) - if there are such variables. Heatmaps. |
| Conclusions           |   2    | Drawing conclusions about the dataset and the questions posed.                                   | General summary, final conclusions, limitations of the methods, suggestions for further development (modeling), etc. |

### Deadline

Please submit the final projects as link to your repository with already published EDA - team reports (as HTML, MD, PDF file) until 30/06/2025 23:59.


### Example datasets

There are two critical requirements for a data set:

1. First, it should contain the **main dependent variable** - the variable under study, under analysis. If you are not sure whether a data set qualifies, you can ask me.  
2) Second, it should contain at least **3-4 variables** (but preferably more). I would not want only one variable to be analyzed. Ideally, the relationship of multiple variables should be considered (e.g., after all, it's a **cross-sectional, exploratory** analysis). 

With that in mind, here are some ideas for **appropriate data sets**. You can use one of them (and ask the questions you find interesting), but you can also find your own; these datasets have been **verified** a bit more.

| Dataset | Domain | Description | Access |
| :------: | :----: | :----------: | :-------: |
| World Bank Open Data | Economics | Contains time series data for **many areas**, such as agricultural development, rural poverty, carbon emissions and many, many more. | [Data Bank Link](https://data.worldbank.org/); can be browsed by “indicator”; may require combining datasets for more information. |
| [World Happiness Report](https://www.kaggle.com/datasets/ajaypalsinghlo/world-happiness-report-2021) | Economics | A dataset of global happiness scores; may need to be combined with other datasets to ask useful questions. | [Kaggle](https://www.kaggle.com/datasets/ajaypalsinghlo/world-happiness-report-2021) |
| Global Energy Consumption | Energy | Contains time series data on **energy** and **electricity** consumption. | [Link on Kaggle](https://www.kaggle.com/datasets/pralabhpoudel/world-energy-consumption) |
| SCARFS (Spontaneous controlled acts of reference between friends and strangers) | Linguistics | Data on friends and strangers playing a game of **Taboo**, which clues they gave, and whether the attempt was successful. | [Link to GitHub](https://github.com/seantrott/scarfs) |
| [California Housing Prices](https://www.kaggle.com/datasets/camnugent/california-housing-prices) | Economics | Median home value information for various neighborhoods in California. | [Link on Kaggle](https://www.kaggle.com/datasets/camnugent/california-housing-prices) |
| [Student Alcohol Consumption](https://www.kaggle.com/datasets/uciml/student-alcohol-consumption?select=student-por.csv) | Public Health | Information on student behavior, including alcohol consumption and more. | [Link on Kaggle](https://www.kaggle.com/datasets/uciml/student-alcohol-consumption?select=student-por.csv) |
| [Datasets for projects with DA](https://github.com/kflisikowsky/analiza_danych_projekt_zespolowy) | Various topics | Datasets designed for team projects on Analytics. Many collections, varying in difficulty level, with descriptions. | [Link to my GitHub](https://github.com/kflisikowsky/analiza_danych_projekt_zespolowy) |

### Difficulty of the project

Note that the level of **difficulty** of the analyses involved in the project will also be taken into account, especially at the **data** stage (e.g., cleaning the data, merging multiple data sets). 

Finding and merging multiple data sets is not *necessary* - i.e., you can get full points without it - but if you successfully clean and merge multiple data sets, it can “offset” lower scores in another section (e.g., **Visualization**); i.e., you can think of it as a kind of unofficial extra credit.

Here are some examples of things that, while not necessary, would make your project more difficult, and therefore more impressive:

- The **cleaning** of the data you find to take advantage of data linkage.  
- Custom **packages and functions** used in data analysis. You can show how a given problem is solved using alternative functions from less common / more sophisticated packages.
- **Combine** description and testing with visualizations - e.g., labels of means, medians, quartiles or statistical test results against boxplots, transparent histograms, density plots, etc.

