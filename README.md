# Project: Analysis of Data Analyst Job Positions listed at 51job

Web scrapping 51job.com with BeautifulSoup, it is a popular job hunting website in China. It would be interesting to take a look at the job market for data analysts/data engineers since data scientists are the sexiest job in 21st century and the most sought-after positions in America. Is it the case in China? After gathering data, it's time to play round with it. 


## Summary
### Dataset
- Job_title(not null)
- Link_to_the_job(not null)
- Company_name(not null)
- Work_location
- Salary_range
- Date_posted


Note: the collected data is extremely selective because I targeted job titles that related to or include 'data analyst'. In total, there is 62 pages and each page has 50 job listings. In total, the spider found 3050 job listings. 51job.com updates job listings everyday and keeps posted jobs for 2-month period among their searching results.


### Descriptive Statistics

|              |Job Title      |Company       |Location    |
| ------------ | ------------- | ------------ | ---------- |
| count        | 3050          | 3050         | 3050       |
| unique       | 2250          | 1528         | 81         |
| top          | 生物信息工程师   | 杭州联川生物技术股份有限公司 | 上海       |
| freqency     | 42            | 36           | 1151       |


There are 81 locations where 1528 companies are currently hiring.
Shanghai has jobs that 3.0 times more than the second ranked location.
