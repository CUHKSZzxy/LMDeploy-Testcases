curl http://127.0.0.1:23333/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "models--deepseek-ai--DeepSeek-V3",
    "messages": [{"role": "user", "content": "Hello! How are you?"}]
  }'
