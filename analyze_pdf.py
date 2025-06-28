import fitz  # PyMuPDF
import os

input_dir = "input_pdfs"
output_dir = "output"

# التأكد من وجود مجلد الإخراج
os.makedirs(output_dir, exist_ok=True)

# قراءة جميع ملفات PDF داخل المجلد
for filename in os.listdir(input_dir):
    if filename.endswith(".pdf"):
        file_path = os.path.join(input_dir, filename)
        doc = fitz.open(file_path)

        # استخراج النص من جميع الصفحات
        text = ""
        for page in doc:
            text += page.get_text()

        doc.close()

        # كتابة النص إلى ملف جديد في مجلد الإخراج
        output_filename = filename.replace(".pdf", "_output.txt")
        output_path = os.path.join(output_dir, output_filename)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"تم استخراج النص من {filename} بنجاح.")


