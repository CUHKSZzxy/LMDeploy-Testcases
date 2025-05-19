import os
from lmdeploy import pipeline, PytorchEngineConfig, GenerationConfig

os.environ['CUDA_VISIBLE_DEVICES'] = '3,4'

# configurations
tp = 1
backend_config = PytorchEngineConfig(
    tp=tp,
)
gen_config = GenerationConfig(
    max_new_tokens=5,
)

# init pipeline
model_path = "models--Qwen--Qwen2.5-7B-Instruct"
pipe = pipeline(
    model_path,
    backend_config=backend_config,
    log_level='INFO'
)

# inference
prompt = 'Who are you?'
response = pipe([prompt])  # Batch input
print(response)
