from indeed import extract_indeed_pages, extract_indeed_jobs

last_page = extract_indeed_pages()

indeed_jobs = extract_indeed_jobs(last_page)


for i in indeed_jobs :
#   print(i["location"])
  print (f"{i}\n")


