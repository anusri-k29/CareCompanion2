import cv2
import pytesseract
import re
import json
import os
import glob

# --- Enhanced Medical Regex Patterns ---
MEDICAL_PATTERNS = {
    'patient': {
        'age_gender_pattern1': r'PATIENT\s*\(\s*(?P<gender1>M|F|Male|Female)\s*\)\s*/\s*(?P<age1>\d{1,3})(?=Y\b)',
        'age_gender_pattern2': r',\s*(?P<age2>\d{1,3})\s*/\s*(?P<gender2>M|F|Male|Female)\b'
    },
    'clinical': {
        'diagnosis': r'(?i)Diagnosis[:\s-]+([\s\S]+?)(?=\n\s*\n|Medicine Name)',
        'vitals': {
            'bp': r'(?i)(?:BP|Blood\s*Pressure)[\s:]*(\d{2,3}\s*/\s*\d{2,3})\s*(?:mmHg)?',
            'pulse': r'(?i)(?:Pulse|Heart\s*Rate)[\s:]*(\d{2,3})\s*(?:bpm)?',
        }
    },
    'medications': {
        'pattern': r'(?m)^\s*\d+\)\s*((?:(?!^\s*\d+\)).)+)'
    }
}

class OCRProcessor:
    @staticmethod
    def extract_text(img_path):
        img = cv2.imread(img_path)
        if img is None:
            raise ValueError(f"Could not read image at {img_path}")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray)
        return text

class MedicalDataExtractor:
    @staticmethod
    def extract_medical_data(text):
        text = re.sub(r'[ \t]+', ' ', text)
        text = re.sub(r'\n\s*\n', '\n\n', text)

        result = {"patient": {}, "vitals": {}, "diagnosis": [], "medications": []}
        
        age_gender = re.search(MEDICAL_PATTERNS['patient']['age_gender_pattern1'], text)
        if age_gender:
            result["patient"].update({"age": age_gender.group('age1').strip(), "gender": age_gender.group('gender1').strip()})
        
        for vital, pattern in MEDICAL_PATTERNS['clinical']['vitals'].items():
            match = re.search(pattern, text)
            if match:
                result["vitals"][vital] = match.group(1).strip()
        
        diagnosis = re.search(MEDICAL_PATTERNS['clinical']['diagnosis'], text)
        if diagnosis:
            result["diagnosis"] = [line.strip() for line in diagnosis.group(1).split('\n') if line.strip()]
        
        meds = re.findall(MEDICAL_PATTERNS['medications']['pattern'], text, re.DOTALL | re.MULTILINE)
        if meds:
            result["medications"].extend([re.sub(r'\s+', ' ', m).strip() for m in meds if m.strip()])
        
        return result

class MedicalOCRApp:
    def __init__(self):
        self.processor = OCRProcessor()
        self.extractor = MedicalDataExtractor()
    
    def process_image(self, img_path):
        extracted_text = self.processor.extract_text(img_path)
        structured_data = self.extractor.extract_medical_data(extracted_text)
        return structured_data

# Function to integrate into Streamlit UI
def run_medical_ocr(image_path):
    app = MedicalOCRApp()
    return app.process_image(image_path)
