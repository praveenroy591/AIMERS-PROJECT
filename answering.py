import requests
from PIL import Image
from transformers import BlipProcessor, BlipForQuestionAnswering

# Load the BLIP processor and model
processor = BlipProcessor.from_pretrained("Salesforce/blip-vqa-base")
model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base")

# Load the image from file
image_path = 'captured_image.png'  # Specify the path to your image file
raw_image = Image.open(image_path).convert('RGB')

# Ask a question about the image
question = "shirt color in picture?"
inputs = processor(raw_image, question, return_tensors="pt")

# Generate the answer using the model
output = model.generate(**inputs, max_new_tokens=50)

# Decode and print the answer
answer = processor.decode(output[0], skip_special_tokens=True)
print("Answer:", answer)