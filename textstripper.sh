#!/bin/bash

# Remove the output file if it already exists
rm -f ./hextradocs_html.txt

# Find all HTML files in ./hextradocs/ directory recursively
find ./hextradocs/ -type f -name "*.html" | while read file; do
    # Print the filename as a separator
    echo "=== $file ===" >> ./hextradocs_html.txt
    # Extract text from HTML file using sed to remove HTML tags
    sed 's/<[^>]*>//g' "$file" | sed '/^$/d' >> ./hextradocs_html.txt
    # Add a newline for separation
    echo "" >> ./hextradocs_html.txt
done

echo "HTML text extraction complete. Output saved to ./hextradocs_html.txt"