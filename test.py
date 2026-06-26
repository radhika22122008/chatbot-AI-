
import google.generativeai as genai

genai.configure(api_key="AQ.Ab8RN6Js_Jb6qJyS_7eLYjiSZA8GVNXqiz0du7rTt0MKMYJ-lw")

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"✅ {m.name}")
