from bs4 import BeautifulSoup
import requests
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5",
}

url = "https://thegita.net/chapter-16/"

try:
    req = requests.get(url, headers=headers)

    # Check if request was successful
    if req.status_code == 200:
        print("Request was successful.")
        soup = BeautifulSoup(req.content, 'html.parser')

        # Find all images in the page
        images = soup.find_all('img')

        if images:
            # Iterate over the images and print the source URL
            for image in images:
                if 'src' in image.attrs:
                    print("Image source URL:", image['src'])
                elif 'data-src' in image.attrs:  # Some sites use data-src for lazy loading
                    print("Image source URL:", image['data-src'])
                else:
                    print("Image source URL not found.")

        else:
            print("No images found on the page.")
    else:
        print("Request failed with status code:", req.status_code)

except requests.RequestException as e:
    print("An error occurred:", e)

# Introduce a delay before making another request
time.sleep(5)  # Wait for 5 seconds before making the next request
