import requests
from PIL import Image
from transformers import BlipProcessor, BlipForQuestionAnswering

# Load the BLIP processor and model
processor = BlipProcessor.from_pretrained("Salesforce/blip-vqa-base")
model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base")

# Load the image from file
image_url = 'https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg' 
raw_image = Image.open(requests.get(image_url, stream=True).raw).convert('RGB')

# Ask a question about the image
question = "what is the background in picture?"
inputs = processor(raw_image, question, return_tensors="pt")

# Generate the answer using the model
output = model.generate(**inputs, max_new_tokens=50)

# Decode and print the answer
answer = processor.decode(output[0], skip_special_tokens=True)
print("Answer:", answer)