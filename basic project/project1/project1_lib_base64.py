import os

# 현재 스크립트 파일의 디렉토리 경로
script_dir = os.path.dirname(__file__)
print(script_dir)

import base64

file_name = "0005303739_001_20220828154501895.jpg"
path = os.path.join(script_dir, "img", file_name)
# 바이너리 파일 읽기
with open(path, 'rb') as img:
    image = img.read()

# base64 인코딩
with open(path, 'rb') as img:
    data = img.read()
    encoded = base64.b64encode(data)

# base64 디코딩
decoded = base64.decodebytes(encoded)

file_path = os.path.join(script_dir, "result", "decode.png")

with open(file_path, 'wb') as image_file:
    image_file.write(decoded)
