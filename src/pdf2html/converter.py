import PyPDF2


def pdf_to_html(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        num_pages = pdf_reader.numPages

        html_content = '<html><body>'
        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            text = page.extractText()
            html_content += f'<div>Page {page_num + 1}</div>'
            html_content += f'<div>{text}</div>'
        html_content += '</body></html>'

    return html_content


# Example usage
pdf_path = 'example.pdf'
html_output = pdf_to_html(pdf_path)

# Save HTML output to a file
with open('output.html', 'w') as output_file:
    output_file.write(html_output)
