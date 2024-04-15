from google_images_download import google_images_download  # Install using pip install google_images_download

# Define your search query
search_query = "Big Dogs"

# Set the download directory and number of images
download_directory = "images"
num_images = 100

# Create the downloader object
downloader = google_images_download.googleimagesdownload() 

# Build the arguments for downloading
arguments = {
    "keywords": search_query,
    "limit": num_images,
    "output_directory": download_directory,
    "user_agent": "your_user_agent (optional)"  # Optional user agent string
}

# Download the images
try:
    downloader.download(arguments)
    print(f"Downloaded {num_images} images for '{search_query}' to '{download_directory}'.")
except Exception as e:
    print(f"Error downloading images: {e}")