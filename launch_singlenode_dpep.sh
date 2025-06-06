lmdeploy serve proxy --server-port 8000 --server-name 172.16.4.52



LMDEPLOY_DP_MASTER_ADDR=172.16.4.52 \
LMDEPLOY_DP_MASTER_PORT=29555 \
lmdeploy serve api_server \
    Qwen/Qwen3-235B-A22B-FP8 \
    --backend pytorch \
    --tp 1 \
    --dp 8 \
    --ep 8 \
    --proxy-url http://172.16.4.52:8000 \
    --nnodes 1 \
    --node-rank 0 --log-level INFO 2>&1 | tee benchmark/api_serve_node0.log
