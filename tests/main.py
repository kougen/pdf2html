import os
import sys
from pathlib import Path
from src.converter import pdf_to_html

def main(pdf_path, output_path):
    html_output = pdf_to_html(pdf_path)

    # Save HTML output to a file
    with open(output_path, 'w') as output_file:
        output_file.write(html_output)
    print(f"HTML content has been written to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <pdf_path> <output_path>")
    else:
        pdf_path = sys.argv[1]
        output_path = sys.argv[2]
        main(pdf_path, output_path)
        
