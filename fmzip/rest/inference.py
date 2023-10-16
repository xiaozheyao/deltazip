import torch
import transformers
from typing import List, Tuple
from fmzip.pipelines.hf_pipeline import HuggingFacePipeline
from fmzip.pipelines.fmzip_pipeline import FMZipPipeline


class InferenceService:
    def __init__(
        self,
        base_model: str,
        backend: str,
        mapping: dict,
        backend_args,
        gen_configs: str,
    ) -> None:
        self.backend = backend
        self.base_model = base_model
        self.backend_args = backend_args
        self.model_mapping = mapping
        if backend == "hf":
            self.pipeline = HuggingFacePipeline(base_model, **backend_args)
        elif backend == "fmzip":
            self.pipeline = FMZipPipeline(base_model=base_model, **backend_args)
        self.gen_configs = gen_configs

    def generate(self, queries: List[Tuple]):
        if self.backend == "hf":
            reformatted_queries = [(x["prompt"], x["model"]) for x in queries]
        elif self.backend == "fmzip":
            reformatted_queries = [
                (
                    x["prompt"],
                    self.model_mappingmapping[
                        x["model"]
                        if not self.backend_args["lossless_only"]
                        else x["model"] + "-lossless"
                    ],
                )
                for x in queries
            ]
        results = self.pipeline.generate(reformatted_queries)
        return results

    @property
    def batch_size(self):
        return self.backend_args['batch_size']
