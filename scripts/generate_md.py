import pandas as pd
from ydata_profiling import ProfileReport
from markdownify import markdownify
import tempfile
import os

# Load your data
data_path = 'data/banned_maps_stats.csv'
df = pd.read_csv(data_path)

# Generate a profile report
profile = ProfileReport(df, title="Descriptive Statistics Report", explorative=True)

# Create a temporary file for the HTML report
with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as temp_html_file:
    temp_html_path = temp_html_file.name
    profile.to_file(temp_html_path)
    
    # Convert the HTML report to Markdown
    with open(temp_html_path, "r") as html_file:
        html_content = html_file.read()

    markdown_content = markdownify(html_content)

# Write the Markdown content to a file
with open("report.md", "w") as md_file:
    md_file.write(markdown_content)

# Clean up the temporary HTML file
os.remove(temp_html_path)
