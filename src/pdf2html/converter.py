import PyPDF2
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def pdf_to_html(pdf_path):
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            num_pages = pdf_reader.numPages

            html_content = '<html><body>'
            for page_num in range(num_pages):
                page = pdf_reader.getPage(page_num)
                text = page.extract_text()
                html_content += f'<div>Page {page_num + 1}</div>'
                html_content += f'<div>{text}</div>'
            html_content += '</body></html>'

        return html_content
    except Exception as e:
        logging.error(f"Error occurred while converting PDF to HTML: {e}")
        return ""
