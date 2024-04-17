import re

def transform_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove special characters except hyphens and whitespace
    text = re.sub(r'[^a-zA-Z0-9\s-]', '', text)
    # Replace whitespace with hyphens
    text = re.sub(r'\s+', '-', text)
    return text


input_text = "A meta systematic review of artificial intelligence in higher education: a call for increased ethics, collaboration, and rigour"
output_text = transform_text(input_text)
print(output_text)