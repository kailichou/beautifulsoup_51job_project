# Project: Data Analyst Job Market in China based on listings at 51job

Web scrapping 51job.com with BeautifulSoup, it is a popular job hunting website in China. It would be interesting to take a look at the current job market for data analysts/data engineers since it is claimed that these are the sexiest job in 21st century and the most sought-after positions in America. Is it the case in China? After gathering data, it's time to play round with it. 


## Summary
### Dataset

| 1st Datasets               | 2nd Datasets              |
| -------------------------- | ------------------------- |
| Job_title(not null)        |
| Link_of_that_job(not null)  |
| Company_name(not null)     |
| Work_location              |
| Salary_range               |
| Date_posted                |

In total, there are 62 pages to scrape and each page has 50 job listings. Thus, the spider found 3050 job listings from 51job.com. Exclude the job posts that are not under 51job.com domain, there are 2898 job posts found. From the post dates pattern, 51job updates job listings everyday and keeps posted jobs for 2-month period among their searching results.



Note: the collected data is extremely restrictive because I targeted job titles that either related to or include 'data analyst' keywords while scraping. It is intuitive that the majority of employers scraped for this project are enterprises tend to demand of bilingual employees.

### Descriptive Statistics

|              |Job Title      |Company       |Location    |
| ------------ | ------------- | ------------ | ---------- |
| count        | 3050          | 3050         | 3050       |
| unique       | 2250          | 1528         | 81         |
| top          | 生物信息工程师   | 杭州联川生物技术股份有限公司 | 上海       |
| freqency     | 42            | 36           | 1151       |


There are 81 locations where 1528 companies are currently hiring.
Shanghai has jobs that 3.0 times more than the second ranked location.


## Reference:
[1] **Data Science and Analytics<https://www.pwc.com/us/en/library/data-science-and-analytics.html>**

