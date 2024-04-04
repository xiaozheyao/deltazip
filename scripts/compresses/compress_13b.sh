python cli/compress.py --base-model meta-llama/Llama-2-70b-hf --target-model meta-llama/Llama-2-70b-chat-hf --outdir .local/compressed_models/meta-llama.Llama-2-70b-chat-hf.2b50s128g --dataset .local/datasets/meta.jsonl --n-samples 256 --bits 2 --sparsity 0.5 --lossless gdeflate --delta subtract  --shuffle-dataset --fast-tokenizer --perc-damp 0.01 --block-size 128