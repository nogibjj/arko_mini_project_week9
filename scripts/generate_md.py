"""
This script generates a Markdown report from a CSV file containing data on banned maps.
It uses ydata-profiling to create a profile report and converts it to Markdown format.
"""

import os
import tempfile

import pandas as pd
from ydata_profiling import ProfileReport
from markdownify import markdownify

# Load your data
DATA_PATH = 'data/banned_maps_stats.csv'
df = pd.read_csv(DATA_PATH)

# Generate a profile report
profile = ProfileReport(df, title="Descriptive Statistics Report", explorative=True)

# Create a temporary file for the HTML report
with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as temp_html_file:
    temp_html_path = temp_html_file.name
    profile.to_file(temp_html_path)
    # Convert the HTML report to Markdown
    with open(temp_html_path, "r", encoding='utf-8') as html_file:
        html_content = html_file.read()

    markdown_content = markdownify(html_content)

# Write the Markdown content to a file
with open("report.md", "w", encoding='utf-8') as md_file:
    md_file.write(markdown_content)

# Clean up the temporary HTML file
os.remove(temp_html_path)
