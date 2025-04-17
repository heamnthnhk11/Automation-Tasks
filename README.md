To run the script on Windows, you'll need a few essential tools and libraries. Here's a breakdown of everything required and how to set it up:

✅ Tools and Requirements
**1. Python (3.8+)**
Make sure Python is installed.

Download from: https://www.python.org/downloads/windows/

During installation, select “Add Python to PATH”.

To verify: python --version

**2. Google Chrome**
This script uses Chrome WebDriver, so make sure Google Chrome is installed.

Download: https://www.google.com/chrome/

**3. ChromeDriver**
ChromeDriver version must match your installed Chrome version.

Download: https://sites.google.com/chromium.org/driver/

📌 Extract and place chromedriver.exe in a known folder, and add that folder to your system PATH, or provide the path explicitly in your login_to_naukri function.

To check version compatibility:

Go to chrome://settings/help to see your Chrome version.

Match it exactly with the correct ChromeDriver version.

**4. Python Packages**
Install required packages with pip:

pip install selenium pandas

Optional (for safety):
pip install webdriver-manager

If using webdriver-manager, you can avoid downloading ChromeDriver manually.

**5. Selenium**
Used for browser automation.

To verify:

python
import selenium
print(selenium.__version__)

**6. Custom Module: naukri_bot**
You have:

python
from naukri_bot import login_to_naukri

This is your custom script/module. Ensure that:

naukri_bot.py exists in the same folder as your main script.

It contains the login_to_naukri(driver) function that:

Initializes the driver.

Logs into your Naukri account using credentials.

Returns a valid driver object.



✅ Summary Checklist

Requirement	Description
✅ Python	Installed and added to PATH
✅ Chrome Browser	Installed
✅ ChromeDriver	Matching your Chrome version
✅ selenium, pandas	Installed via pip
✅ naukri_bot module	Available and contains login_to_naukri()

Run main.py and provide credentials in .env file
