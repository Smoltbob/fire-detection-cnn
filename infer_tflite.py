from model import *
import os

tflife_model = tf.lite.Interpreter(model_path="models/firenet.tflite")
tflife_model.allocate_tensors()

tflife_input_details = tflife_model.get_input_details()
tflife_output_details = tflife_model.get_output_details()


# network input sizes
rows = 224
cols = 224

frame = cv2.imread("images/chile.jpg")
# re-size image to network input size and perform prediction
small_frame = cv2.resize(frame, (rows, cols), cv2.INTER_AREA)
tflife_input_data = np.reshape(np.float32(small_frame), (1, 224, 224, 3))
tflife_model.set_tensor(tflife_input_details[0]['index'], tflife_input_data)

tflife_model.invoke()

output = tflife_model.get_tensor(tflife_output_details[0]['index'])
output = output[0][0]

if output > 0.5:
    print("au feu!", output)
else:
    print("pas de feu", output)
