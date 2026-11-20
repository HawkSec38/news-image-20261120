import os
import shutil

# Ensure /output directory exists
os.makedirs('/output', exist_ok=True)

# Copy the image from the repository to output
shutil.copy('entry.png', '/output/entry.png')
