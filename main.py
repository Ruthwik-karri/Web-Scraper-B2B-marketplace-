from selenium import webdriver
from bs4 import BeautifulSoup
import time
import json
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def scrape_products(keyword):

    url = f"https://dir.indiamart.com/search.mp?ss={keyword}"

    driver = webdriver.Chrome()
    driver.get(url)

    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, "html.parser")

    products = []

    items = soup.find_all("div", class_="cardbody")

    for item in items[:10]:   # for first 10 products

        name = item.find("a")

        if name:
            products.append({
                "product_name": name.text.strip(),
                "category": keyword
            })

    driver.quit()

    return products

categories = ["machinery", "electronics", "textiles"]

all_products = []

for cat in categories:
    print(f"\nCollecting: {cat}")

    data = scrape_products(cat)

    print(f"Products found: {len(data)}")

    all_products.extend(data)


print("\nTotal products collected:", len(all_products))


os.makedirs("output", exist_ok=True)  # creating a Folder if not exists 


# Save JSON type 
with open("output/products.json", "w") as f:
    json.dump(all_products, f, indent=4)  # convert it into file type 


# Save CSV
df = pd.DataFrame(all_products)
csv_file = "output/products.csv"
df.to_csv(csv_file, index=False)

print("\nData saved in output folder as JSON and CSV")

print("\nData saved in output folder")



def perform_eda(csv_file):
    df = pd.read_csv(csv_file)

    print(df.head())

    print("Summary Statistics")
    print(df.describe(include='all'))

    print(" Products per Category")
    print(df['category'].value_counts())

    # Top 10 products
    top_products = df['product_name'].value_counts().head(10)
    print("\nTop 10 Products")
    print(top_products)

    plt.figure(figsize=(10,6))
    sns.barplot(x=top_products.values, y=top_products.index, palette="viridis")
    plt.title("Top 10 Products by Count")
    plt.xlabel("Count")
    plt.ylabel("Product Name")
    plt.tight_layout()
    plt.show()

    # Check missing data
    print("\n Missing Values")
    print(df.isnull().sum())

perform_eda(csv_file)