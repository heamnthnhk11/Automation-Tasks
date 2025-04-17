from selenium.webdriver.common.by import By
from time import sleep

resume_keywords = [
    'ansible', 'aws', 'ci/cd', 'cloud', 'cloudformation', 'devops', 'docker', 'dynatrace', 'ec2',
    'eks', 'elb', 'git', 'groovy', 'helm', 'iam', 'infrastructure', 'jenkins', 'kubernetes', 'lambda',
    'linux', 'maven', 'monitoring', 'python', 'rds', 'route 53', 's3', 'shell', 'splunk', 'sre',
    'terraform', 'vpc'
]

def calculate_match_score(text):
    text = text.lower()
    matched = [kw for kw in resume_keywords if kw in text]
    return int((len(matched) / len(resume_keywords)) * 100)

def search_jobs_and_match(driver, keyword="DevOps Engineer", location="bangalore", min_exp=6, max_exp=8):
    search_query = keyword.lower().replace(" ", "-")
    location_query = "-jobs-in-" + location.lower()
    url = f"https://www.naukri.com/{search_query}{location_query}?experience={min_exp}-{max_exp}"

    driver.get(url)
    sleep(5)

    matched_jobs = []
    listings = driver.find_elements(By.CLASS_NAME, "jobTuple")[:10]

    for job in listings:
        try:
            title_elem = job.find_element(By.CLASS_NAME, "title")
            title = title_elem.text
            company = job.find_element(By.CLASS_NAME, "companyName").text
            link = title_elem.get_attribute("href")

            match_score = calculate_match_score(title + " " + company)
            if match_score >= 60:
                matched_jobs.append({
                    "title": title,
                    "company": company,
                    "link": link,
                    "match_score": match_score
                })
        except Exception:
            continue

    return matched_jobs
