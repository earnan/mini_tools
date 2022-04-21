# 方法①
import tabula
import camelot

tables = camelot.read_pdf("F:/test.pdf")
print(tables)
tables.export("F:/extracted.csv", f="csv", compress=True)
"""
# 方法②, 需要安装Java8

tabula.read_pdf("tables.pdf", pages="all")
tabula.convert_into("table.pdf", "output.csv",
                    output_format="csv", pages="all")
"""
