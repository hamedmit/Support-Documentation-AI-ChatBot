from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import json
import os
import random

# Browser settings
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
user_agent = os.getenv("USER_AGENT", "Your_Real_User_Agent_String")
options.add_argument(f"user-agent={user_agent}")

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Get depth level from the user
max_depth = int(input("🔢 Enter depth level (e.g., 0, 1, 2, 3, ...): "))

# Website URL
base_url = "https://support.payever.org/"
driver.get(base_url)

try:
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.footer"))
    )
    print("✅ Main page loaded successfully!")
except Exception as e:
    print(f"⚠️ Error loading the main page: {e}")

# Function to extract all links from a page


def get_all_links(soup):
    links = set()
    for a_tag in soup.find_all('a', href=True):
        link = a_tag['href']
        if link.startswith('/'):
            link = base_url + link[1:]
        if link.startswith(base_url):
            links.add(link)
    return list(links)

# Function to crawl links recursively up to the specified depth


def crawl_links(starting_links, depth):
    visited_links = set()
    all_links = set(starting_links)
    current_level_links = set(starting_links)

    for level in range(1, depth + 1):
        print(f"\n🔍 Crawling depth level {level}/{depth} ...")
        next_level_links = set()

        for idx, link in enumerate(current_level_links, start=1):
            if link in visited_links:
                continue
            print(f"➡️ Checking link {idx}/{len(current_level_links)}: {link}")
            try:
                driver.get(link)
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                soup = BeautifulSoup(driver.page_source, "html.parser")
                new_links = get_all_links(soup)
                next_level_links.update(new_links)
                all_links.update(new_links)
                visited_links.add(link)
                time.sleep(random.uniform(3, 7))  # Random delay to avoid getting blocked
            except Exception as e:
                print(f"⚠️ Error processing {link}: {e}")

        current_level_links = next_level_links
        if not current_level_links:
            print("🚫 No more links to crawl.")
            break

    return all_links


# Step 1: Extract links from the main page
print("🔍 Extracting links from the main page...")
main_soup = BeautifulSoup(driver.page_source, "html.parser")
first_level_links = get_all_links(main_soup)
print(f"📌 Number of links found on the main page: {len(first_level_links)}")

# Execute crawling based on the specified depth level
all_links = crawl_links(first_level_links, max_depth)
print(f"✅ Total final links for processing: {len(all_links)}")

# Extract content from the crawled links
all_content = []
visited_links = set()

for idx, link in enumerate(all_links, start=1):
    if link not in visited_links:
        print(f"📄 Extracting content from link {idx}/{len(all_links)}: {link}")
        try:
            driver.get(link)
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            soup = BeautifulSoup(driver.page_source, "html.parser")

            content = {
                "url": link,
                "title": soup.title.string if soup.title else "No Title",
                "paragraphs": [p.get_text(strip=True) for p in soup.find_all("p")],
                "headers": [h.get_text(strip=True) for h in soup.find_all(["h1", "h2"])],
            }
            all_content.append(content)
            visited_links.add(link)
            time.sleep(random.uniform(3, 7))  # Random delay to avoid getting blocked
        except Exception as e:
            print(f"⚠️ Error extracting content from {link}: {e}")

# Save extracted data to a JSON file
output_file = "data/extracted_content.json"
output_dir = os.path.dirname(output_file)

# If there is no directory, make it!!
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save file
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(all_content, file, indent=2, ensure_ascii=False)

# Close the browser
driver.quit()
print(f"✅ Content extraction completed! Data saved in '{output_file}'.")
