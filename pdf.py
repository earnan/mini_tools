# PDF加密
import pikepdf

pdf = pikepdf.open("F:/test.pdf")
pdf.save('F:/encrypt.pdf', encryption=pikepdf.Encryption(
    owner="0000", user="0000", R=4))
pdf.close()
# PDF解密

pdf = pikepdf.open("F:/encrypt.pdf",  password='0000')
pdf.save("F:/decrypt.pdf")
pdf.close()
