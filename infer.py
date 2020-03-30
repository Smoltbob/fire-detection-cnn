from model import *
import os

model = firenet (224, 224, training=False)
model.load(os.path.join("models/FireNet", "firenet"),weights_only=True)

# network input sizes
rows = 224
cols = 224

frame = cv2.imread("images/protest.jpg")
# re-size image to network input size and perform prediction
small_frame = cv2.resize(frame, (rows, cols), cv2.INTER_AREA)
output = model.predict([small_frame])[0][0]

if output > 0.5:
    print("au feu!", output)
else:
    print("pas de feu", output)
