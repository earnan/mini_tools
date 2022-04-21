
import pdfplumber

with pdfplumber.open("F:/test.pdf") as pdf:
    page = pdf.pages[2]  # 第三页
    print(page.extract_table())
    for row in page.extract_table():
        print(row)

"""
# 方法①
import tabula
import camelot

tables = camelot.read_pdf("F:/test.pdf")
print(tables)
tables.export("F:/extracted.csv", f="csv", compress=True)

# 方法②, 需要安装Java8

tabula.read_pdf("tables.pdf", pages="all")
tabula.convert_into("table.pdf", "output.csv",
                    output_format="csv", pages="all")
"""
