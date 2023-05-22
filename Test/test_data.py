import requests
import numpy as np
import pickle
import base64


def send_data(img):
    data = {}
    data['image'] = base64.b64encode(pickle.dumps(img)).decode('utf-8')
    data['essay'] = "test_0_topic"
    data['topic'] = "test_0_topic"
    data['Content'] = [50, "good"]
    data['Statement'] = [50, "good"]
    data['Organization'] = [50, "good"]
    data['Readability'] = [50, "good"]
    data['Grammar'] = [50, "good"]
    data['Overall'] = "good"
    res = requests.post('http://localhost:8088/api/img_upload', data=data)
    print(res)


if __name__ == "__main__":
    img = np.ones((100, 100, 3), dtype=np.uint8) * 255
    send_data(img)
