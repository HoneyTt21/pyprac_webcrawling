import requests 
from bs4 import BeautifulSoup

LIMIT = 50
URL = "https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&limit=50"

def extract_indeed_pages():
  

  result = requests.get(URL)

  soup = BeautifulSoup(result.text, "html.parser")

  pagination = soup.find("div", {"class" : "pagination"})

  links = pagination.find_all("a")
  pages = []

  for link in links[:-1]:
    pages.append(int(link.find("span").string))
  max_page = pages[-1]

  return max_page

def extract_jobs(html):
  # title
  title = html.find("h2", {"class":"title"}).find("a").get("title")
  
  # company
  company = html.find("span", {"class":"company"})
  company_anchor = company.find("a")
  if company_anchor is not None :
    company = (company_anchor.string)
  else:
    company = (company.string)
  company = company.strip()
  
  # location
  location = html.find("span", {"class":"location accessible-contrast-color-location"}).string

  # data_id
  data_id = html.find("div", {"class":"recJobLoc"}).get("id").strip("recJobLoc_")

  return ({"title" : title, "company" : company, "location" : location, "data-id" : data_id})

def extract_indeed_jobs(last_page):
  jobs = []
  # for page in range(last_page):
  result = requests.get(f"{URL}&start={0 * LIMIT}")
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})
  for res in results:
    job = extract_jobs(res)
    jobs.append(job)
  return jobs