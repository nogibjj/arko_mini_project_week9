"""
This script generates a Markdown report from a CSV file containing data on banned maps.
It uses ydata-profiling to create a profile report and converts it to Markdown format.
"""

import os
import tempfile
import shutil
import re
import requests
from requests.exceptions import RequestException
import pandas as pd
from ydata_profiling import ProfileReport
from markdownify import markdownify

# Load your data
DATA_PATH = "data/banned_maps_stats.csv"
df = pd.read_csv(DATA_PATH)

# Generate a profile report
profile = ProfileReport(df, title="Descriptive Statistics Report", explorative=True)

# Create a temporary directory for the HTML report and images
with tempfile.TemporaryDirectory() as temp_dir:
    temp_html_path = os.path.join(temp_dir, "report.html")
    # Save the HTML report
    profile.to_file(temp_html_path)

    # Read the HTML content
    with open(temp_html_path, "r", encoding="utf-8") as html_file:
        html_content = html_file.read()

    # Regex to find image tags
    img_tag_pattern = re.compile(r'<img[^>]+src="([^">]+)"', re.IGNORECASE)

    # Find all image sources
    img_sources = img_tag_pattern.findall(html_content)

    # Process each image
    for img_src in img_sources:
        img_name = os.path.basename(img_src)
        img_dst_path = os.path.join(temp_dir, img_name)

        # Download the image
        try:
            response = requests.get(img_src, stream=True, timeout=10)
            response.raise_for_status()  # Ensure we notice bad responses
            with open(img_dst_path, "wb") as out_file:
                shutil.copyfileobj(response.raw, out_file)
        except RequestException as e:
            print(f"Failed to download image {img_src}: {e}")
            continue

        # Replace the image source in the HTML content
        html_content = html_content.replace(img_src, img_name)

    # Convert HTML to Markdown
    markdown_content = markdownify(html_content)

    # Write the Markdown content to a file
    with open("report.md", "w", encoding="utf-8") as md_file:
        md_file.write(markdown_content)

    # Copy images to the current directory
    for img_src in img_sources:
        img_name = os.path.basename(img_src)
        img_dst_path = os.path.join(temp_dir, img_name)
        shutil.copy(img_dst_path, ".")

print("Markdown report and images have been generated successfully.")
