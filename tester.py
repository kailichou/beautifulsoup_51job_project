from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import pandas as pd



        
   



def spider(self):
    count = 0
    #insert p values in link
    jobs = []
    
    urls = [self.format(p) for p in range(1,62)]
    for url in urls:
        webpage = uReq(url).read().decode('gbk').encode('utf-8') 
        html = soup(webpage, "html.parser", from_encoding="utf-8") #parse webpages
        
        for containers in html.find_all(class_='t1'):
            
            job_title = containers.find('a')
            
            link = containers.find('a')
          
            company = containers.parent.find(class_='t2').text

            location = containers.parent.find(class_='t3').text
            salary = containers.parent.find(class_='t4').text
            date = containers.parent.find(class_='t5').text
        
            #job dictionaries map job_title to value scrapped 
            
            
            if job_title is not None:  
                j = job_title.text.strip()
                l = link.get('href')
                
            
                job= {"job_title":j, "link":l, "company": company, "location": location, "salary": salary, "date": date}
                jobs.append(job) #add collected job data to list jobs
                #a job just added
                count += 1
            print("so far it has crawled ", count," jobs." + '\n')


  
    spiderjob = pd.DataFrame(jobs)
    return spiderjob.head()
   
link = ("https://search.51job.com/list/000000,000000,0000,00,9,99,data%2520analyst,2,{}.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=")    
print(spider(link))

  


    

    
  
