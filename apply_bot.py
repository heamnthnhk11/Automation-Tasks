from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def apply_to_job(driver, job, tab_index):
    # Open job link in a new tab
    driver.execute_script("window.open(arguments[0], '_blank');", job["link"])
    sleep(4)

    # Switch to the newly opened tab
    driver.switch_to.window(driver.window_handles[tab_index])

    try:
        # Wait until the apply button is visible and clickable
        apply_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Apply") or contains(text(), "apply now")]'))
        )
        apply_button.click()
        sleep(2)
        print(f"✅ Applied to: {job['title']} at {job['company']}")
        return "Applied"
    except Exception as e:
        print(f"⚠️ Could not apply to: {job['title']} at {job['company']} - {str(e)}")
        return "Skipped"
    finally:
        # Close the current tab after applying
        driver.close()

    # Switch back to the original tab
    driver.switch_to.window(driver.window_handles[0])
