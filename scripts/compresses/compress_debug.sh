python cli/compress.py --target-model /home/xzyao/Documents/cache/experiments/fmzip/finetuned_raw/task112_asset_simple_sentence_identification/global_step180 --base-model EleutherAI/pythia-2.8b-deduped --dataset /home/xzyao/Documents/cache/datasets/qi/ar/task112_asset_simple_sentence_identification.train.jsonl --bits 4 --sparsity 0.6 --lossless gdeflate --delta subtract --outdir .cache/compressed_models/p2.8b_gsd_133 --group-size -1 --n-samples 1024 --perc-damp 0.02