import streamlit as st
import streamlit.components.v1 as components  
from PIL import Image
import pytesseract

st.title(" مستخرج النصوص من الصور (Arabic OCR)")
st.write("حول أي صورة أو وثيقة مكتوبة إلى نص قابل للنسخ والتعديل في ثوانٍ!")

st.markdown("""
    <style>
    * { direction: rtl; text-align: right; }
    textarea { text-align: right; direction: rtl; }
    </style>
""", unsafe_allow_html=True)

st.write("قم برفع الصورة هنا (يدعم صيغ PNG, JPG, JPEG):")
uploaded_file = st.file_uploader("اختر صورة من جهازك...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='الصورة المرفوعة')

    st.write("---")

    with st.spinner('جاري قراءة الصورة واستخراج النص... انتظر قليلاً'):
        try:
            extracted_text = pytesseract.image_to_string(image, lang='ara+eng')

            if extracted_text.strip():
                st.success(" تم استخراج النص بنجاح!")
                st.text_area("النص المستخرج:", value=extracted_text, height=250)
            else:
                st.warning("لم نتمكن من العثور على نص واضح في الصورة. تأكد من جودة الإضاءة ووضوح الخط.")
        except Exception as e:
            st.error("عذراً، حدث خطأ أثناء المعالجة الفنية على الخادم.")

            st.write("---")
ad_html = """
<div style="text-align: center; margin-top: 20px;">
    <script type="text/javascript">
	atOptions = {
		'key' : 'كود_المفتاح_بتاعك_هنا',
		'format' : 'iframe',
		'height' : 90,
		'width' : 728,
		'params' : {}
	};
    </script>
    <script type="text/javascript" src="//www.highperformanceformat.com/كود_المفتاح_بتاعك/invoke.js"></script>
</div>
"""
components.html(ad_html, height=120, scrolling=False)
            st.write("اضغط على الزر بالأسفل للحصول على كورسات مجانية وأدوات ذكاء اصطناعي مدفوعة مجاناً اليوم:")

            ad_url = "https://www.effectivecpmnetwork.com/iqgj1jtvww?key=f7e706f2b0edf09001cb50d0c9f6488c"

            st.markdown(f'''
            <a href="{ad_url}" target="_blank" style="text-decoration: none;">
                <div style="background-color: #25D366; color: white; text-align: center; padding: 15px; border-radius: 10px; font-size: 20px; font-weight: bold; box-shadow: 2px 2px 5px rgba(0,0,0,0.2);">
                 اضغط هنا لتفعيل الميزات المتقدمة وسحب الهدايا مجانا
                </div>
            </a>
            ''', unsafe_allow_html=True)
            st.write("---")

st.write("---")
st.markdown("""
###  ما هي أداة مستخرج النصوص من الصور؟
موقعنا يقدم خدمة **تحويل الصور إلى نصوص (OCR)** مجانية تماماً وبأعلى دقة ممكنة. تتيح لك هذه الأداة الرقمية المتطورة رفع أي وثيقة مصورة، صفحات الكتب، الأبحاث الدراسية، أو لقطات الشاشة (Screenshots) وتحويل الكلمات والعبارات الموجودة داخل الصورة إلى نص رقمي مكتوب بالكامل.

###  مميزات الخدمة الذكية:
* **دعم كامل ومتطور للغة العربية:** الأداة مدربة على فهم الخطوط العربية المتنوعة واستخراجها بدقة عالية.
* **دعم ثنائي اللغة (عربي + إنجليزي):** يمكنك رفع صور تحتوي على نصوص باللغتين العربية والإنجليزية معاً في نفس الوقت.
* **سرعة فائقة في المعالجة:** يتم معالجة الصورة وفحص الكلمات واستخراجها في أقل من 3 ثوانٍ لتوفير وقتك ومجهودك.
""")
