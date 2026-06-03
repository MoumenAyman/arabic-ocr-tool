import streamlit as st
from PIL import Image
import pytesseract
import os

# السطرين دول هما السحر اللي هيعرفوا السيرفر مكان أداة الـ OCR على الـ Linux
if os.path.exists("/usr/bin/tesseract"):
    pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

st.title("📝 مستخرج النصوص من الصور (Arabic OCR)")
st.write("حول أي صورة إلى نص قابل للنسخ والتعديل في ثوانٍ!")

uploaded_file = st.file_uploader("اختر صورة...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='الصورة المرفوعة')
    with st.spinner('جاري قراءة الصورة...'):
        try:
            # تحديد لغات القراءة (عربي وإنجليزي)
            extracted_text = pytesseract.image_to_string(image, lang='ara+eng')
            
            if extracted_text.strip():
                st.success("✨ تم استخراج النص بنجاح!")
                st.text_area("النص المستخرج:", value=extracted_text, height=250)
            else:
                st.warning("لم يتم العثور على نص واضح، تأكد من جودة الصورة.")
        except Exception as e:
            st.error("حدث خطأ في المعالجة الفنية على السيرفر.")

# مقال بسيط عشان جوجل أدسينس والشركات الإعلانية تقبل الموقع فوراً
st.write("---")
st.markdown("""
### 💡 ما هي أداة مستخرج النصوص من الصور؟
موقعنا يقدم خدمة **تحويل الصور إلى نصوص (OCR)** مجانية تماماً وبأعلى دقة ممكنة.
""")
