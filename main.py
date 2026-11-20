import os
import shutil

# Create output directory
os.makedirs('/output', exist_ok=True)

# Copy the image from the repository to output
shutil.copy('entry.png', '/output/entry.png')
