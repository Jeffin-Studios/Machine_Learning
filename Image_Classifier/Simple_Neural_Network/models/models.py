import json

data = {}  

data["mnist_model"] = {
    "input_height": 28,
    "input_width": 28,
    "script": "mnist_cnn",
    "model_file": "mnist_model/frozen_model.pb",
    "checkpoint_file": "mnist_model/model.ckpt-20000.meta",
    "label_file": "mnist_model/labels.txt",
    "input_node": "Reshape",
    "output_node": "softmax_tensor"
}  


# mobilenet_v1_1.0_224

with open("models.json", "w") as outfile:  
    json.dump(data, outfile)