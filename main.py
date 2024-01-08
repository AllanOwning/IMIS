import os
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image
from flask import Flask, render_template, request
from torchvision import models

app = Flask(__name__)
model = models.vgg16()
#segmodelhemo =
#segmodelische =
clsmodel = './model/Adam_best_model.pth'
torch.save(model.state_dict(), clsmodel)
model.load_state_dict(torch.load(clsmodel))
num_features = model.classifier[6].in_features
model.classifier[6] = nn.Linear(num_features, 3)
model.eval()

@app.route('/', methods=['GET'])
def website():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def predict():
    classes = {0: 'Hemorrhagic', 1: 'Ischemic', 2: 'Normal'}

    imageinput = request.files['imageinput']
    image_path = "./Storage/" + imageinput.filename
    imageinput.save(image_path)

    image = Image.open(image_path)
    image = image.convert("RGB")
    image = image.resize((256, 256))
    image = transforms.ToTensor()(image)
    image = image.unsqueeze(0)


    output = model(image)
    probabilities = torch.nn.functional.softmax(output, dim=1)

    _, predicted = torch.max(output, 1)
    confidenceScore = round(probabilities[0, predicted.item()].item() * 100, 2)

    predictionResult = classes[predicted.item()]
    print(f"Predicted: {predicted}")
    print(f"Classes length: {len(classes)}")

    return render_template('result.html', prediction=predictionResult, confidence=confidenceScore)

if __name__ == "__main__":
    app.run()

