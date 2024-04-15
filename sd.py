import requests
from bs4 import BeautifulSoup
import os

def download_image(url, output_dir):
  """
  Downloads an image from the given URL and saves it to the output directory.

  Args:
    url: The URL of the image.
    output_dir: The directory where the image should be saved.
  """
  try:
    response = requests.get(url, stream=True)
    response.raise_for_status()

    # Get the filename from the URL (if possible)
    filename = os.path.basename(url)
    if not filename:
      # If filename unavailable, generate a unique filename
      filename = f"image_{hash(url)}.jpg"

    filepath = os.path.join(output_dir, filename)
    with open(filepath, "wb") as f:
      for chunk in response.iter_content(1024):
        f.write(chunk)

    print(f"Image downloaded: {filename}")
  except requests.exceptions.RequestException as e:
    print(f"Error downloading image from {url}: {e}")


def scrape_images_by_topic(topic, max_images=100, output_dir="downloaded_images"):
  """
  Scrapes images for a specific topic using Google image search and downloads
  them to the output directory, with a limit on the number of downloaded images.

  Args:
    topic: The topic to search for images.
    max_images (optional): The maximum number of images to download (default: 100).
    output_dir (optional): The directory where the images should be saved (default: "downloaded_images").
  """
  # Construct Google image search URL with the topic
  search_url = f"https://www.google.com/search?q={Dogs}&tbm=isch"

  response = requests.get(search_url)
  soup = BeautifulSoup(response.content, "html.parser")

  # Find all image results
  image_results = soup.find_all("img", class_="Q4LuWd")

  # Extract image URLs and download them, limited to max_images
  downloaded_count = 0
  for image_result in image_results:
    image_url = image_result.get("src")
    if image_url and downloaded_count < max_images:  # Check for valid URL and limit
      download_image(image_url, output_dir)
      downloaded_count += 1

  print(f"Scraped {downloaded_count} images for '{topic}' from Google Search")


# Example usage
topic = "Dogs"  # Replace with your desired topic
max_images = 100  # Adjust the maximum images to download

scrape_images_by_topic(topic, max_images)