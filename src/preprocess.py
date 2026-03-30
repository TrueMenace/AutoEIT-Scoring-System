import re

def extract_syllable_count(text):
    if not isinstance(text, str):
        return None
    
    match = re.search(r'\((\d+)\)', text)
    if match:
        return int(match.group(1))
    return None


def clean_text(text):
    if not isinstance(text, str):
        return ""
    
    # Remove (number) pattern
    text = re.sub(r'\(\d+\)', '', text)
    
    # Lowercase
    text = text.lower()
    
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text