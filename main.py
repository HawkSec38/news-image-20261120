import os
import shutil

# Ensure output directory exists and is writable
output_dir = '/output'
if not os.path.exists(output_dir):
    try:
        os.makedirs(output_dir, exist_ok=True)
    except PermissionError:
        # /output should already exist in the grader
        pass

# Copy the image from the repository to output
try:
    shutil.copy('entry.png', os.path.join(output_dir, 'entry.png'))
except Exception as e:
    # Try to write directly
    import sys
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
