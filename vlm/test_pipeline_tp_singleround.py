import os
from lmdeploy import pipeline, PytorchEngineConfig
from lmdeploy.vl import load_image

os.environ['CUDA_VISIBLE_DEVICES'] = '3,4'

# configurations
tp = 1
backend_config = PytorchEngineConfig(
    tp=tp,
)

# init pipeline
model_path = "models--Qwen--Qwen2.5-VL-7B-Instruct"
pipe = pipeline(
    model_path,
    backend_config=backend_config,
    log_level='INFO'
)

# inference
prompt = 'describe this image'
image = load_image('https://raw.githubusercontent.com/open-mmlab/mmdeploy/main/tests/data/tiger.jpeg')
response = pipe((prompt, image))
print(response)
