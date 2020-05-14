# Project: Data Analyst Job Market in China 
## Scraped data from a Chinese recruitment website

### Objective

A question popped into my head while looking for job opportunities. What is the current job market for data analyst/data engineers? Instead of getting information from a report, it is even more straightforward to look at the first-hand data from the market.

Hence, I prepared to make a research. It's intriguing to take a look at the sexiest job in 21st century. Is it the case in China? After gathering data, it's time to play round with it. 


## Summary
### Dataset

|             |             |                     |              |               |              |                    |
| ------------| ------------|---------------------|--------------|---------------|--------------|--------------------|
| 1st Datasets| Date_posted | Job_title(not null) | Company_name | Work_location | Minimum  | new_max                   |
| 2nd Datasets| Job_title   | Company_name        | Entity       | Staff_number  | Industry     | Job_responsibility |
 


In total, there are 3050 job listings over 2 month period in whole China. Exclude the job posts that are not under 51job.com domain, there are 2898 job posts found. Based on the post dates pattern, 51job updates job listings everyday and keeps posted jobs for 2-month period among their searching results.





### Descriptive Statistics

|              |Job Title      |Company       |Location    |
| ------------ | ------------- | ------------ | ---------- |
| count        | 3050          | 3050         | 3050       |
| unique       | 2250          | 1528         | 81         |
| top          | 生物信息工程师   | 杭州联川生物技术股份有限公司 | 上海       |
| freqency     | 42            | 36           | 1151       |

There are 81 locations where 1528 companies are currently hiring.
Shanghai has 3.47 times more jobs than the second ranked location.






## BI | Interactive Data Visualisation

**[Tableau Link](https://public.tableau.com/profile/kaili8237#!/vizhome/DataAnalystsAnalystsJobMarketinChina/DataAnalystsJobMarketinChina?publish=yes)**

Note: the collected data is extremely restrictive because I targeted job titles that either related to or include 'data analyst' keywords while scraping. It is intuitive that the majority of employers scraped for this project are enterprises tend to demand of bilingual employees.
