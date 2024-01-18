# Web-weaver

A Python script to discover hidden directories by brute-forcing common directory names.

## Usage

1. Edit the script to include the target URL:

   ```python
   url = "http://example.com"

# Run the script:

python directory_discover.py
The script will attempt to discover hidden directories by brute-forcing common directory names using the "common_dir.txt" wordlist.

If a directory is discovered, it will print the URL.

# Note
The script uses a common directory wordlist ("common_dir.txt") for brute-forcing directory names.
It recursively goes through each discovered path.

# Disclaimer
This tool is intended for educational and ethical use only. Ensure compliance with legal regulations and obtain proper authorization before using it in any environment.
