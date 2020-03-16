import mammoth
input_file = "C:\\doc\\FINAL Nitron Group - NEW FORM SALES CONTRACT  GTCs Edited 3.13.2020.docx"
output_file = "output.html"

style_map = """
p[style-name='Section Title'] => h1:fresh
p[style-name='Subsection Title'] => h2:fresh
p.ListParagraph => ul > li:fresh
"""

with open(input_file,'rb') as doc:
    results = mammoth.convert_to_html(doc, style_map=style_map)

print(results.value)
print(results.messages)

with open(output_file,"w", encoding="utf-8") as out:
    out.write(results.value)
