import PyPDF2

# The below read_file helps to read the input file either in pdf or text format for generating the MCQs by LLM model
def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
        except Exception as e:
            raise Exception("Error reading the PDF file")
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    else:
        raise Exception("Unsupported file format. Only PDF and text files are supported")
