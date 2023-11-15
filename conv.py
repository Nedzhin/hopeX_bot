import PyPDF2

# Open the PDF file
for i in range(16, 17):
  
  with open('{}.pdf'.format(i+1), 'rb') as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)
    
    # Create a text file to save the contents
    with open('documents/file{}.txt'.format(i+1), 'w', encoding='utf-8') as text_file:
        for page_number in range(len(reader.pages)):
            # Extract the text from the page
            page = reader.pages[page_number]
            text = page.extract_text()
            
            # Write the text to the text file
            text_file.write(text)
        text_file.write("\n\n This is the end of the {} text \n\n".format(i+1))

print("PDF content has been written to output.txt")