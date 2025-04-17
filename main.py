from naukri_bot import login_to_naukri
import pandas as pd
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set keywords to skip
SKIP_KEYWORDS = ['tcs', 'appstix', 'accenture', 'cognizent', 'capgemini']

# Apply job function
def apply_to_job(driver, job_url):
    try:
        driver.execute_script("window.open(arguments[0], '_blank');", job_url)
        driver.switch_to.window(driver.window_handles[-1])

        # Wait for Apply button and click
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Apply")]'))
        ).click()

        print(f"✅ Applied: {job_url}")
        time.sleep(2)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        return "Applied"

    except Exception as e:
        print(f"⚠️ Error applying to job: {job_url} — {str(e)}")
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        return "Failed"

if __name__ == "__main__":
    driver = login_to_naukri()

    job_titles = ["DevOps Engineer", "Site Reliability Engineer"]
    locations = ["remote"]
    all_applied_jobs = []

    for title in job_titles:
        for location in locations:
            print(f"\n🔍 Searching: {title} in {location}")
            driver.get(f"https://www.naukri.com/{title.replace(' ', '-')}-jobs-in-{location}?experience=3-8")

            try:
                # Wait for job cards to appear
                WebDriverWait(driver, 20).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.title'))
                )

                job_cards = driver.find_elements(By.CSS_SELECTOR, 'a.title')

                if not job_cards:
                    print("⚠️ No job cards found.")
                    continue

                for i, job in enumerate(job_cards[:20]):
                    job_title = job.get_attribute('title')
                    job_link = job.get_attribute('href')

                    if not job_title or not job_link:
                        continue

                    # Skip blocked companies
                    if any(skip in job_title.lower() for skip in SKIP_KEYWORDS):
                        print(f"❌ Skipping (blocked): {job_title}")
                        continue

                    print(f"➡️ {i + 1}. {job_title} — {job_link}")
                    status = apply_to_job(driver, job_link)

                    all_applied_jobs.append({
                        'title': job_title,
                        'link': job_link,
                        'status': status,
                        'date': datetime.now().strftime('%Y-%m-%d')
                    })

            except Exception as e:
                print(f"⚠️ Error loading job list: {str(e)}")

    # Save results
    if all_applied_jobs:
        df = pd.DataFrame(all_applied_jobs)
        df.to_csv("matched_jobs.csv", index=False)
        print("\n✅ All done. Results saved to matched_jobs.csv")
    else:
        print("⚠️ No applications submitted.")
