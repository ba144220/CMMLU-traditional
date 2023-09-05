import argparse
from transformers import LlamaTokenizer, LlamaForCausalLM
import transformers
import torch

from mp_utils import choices, format_example, gen_prompt, softmax, run_eval
from hf_causal_model import eval

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_name_or_path", type=str, default="")
    parser.add_argument("--data_dir", type=str, default="../data")
    parser.add_argument("--save_dir", type=str, default="../results/not_specified")
    parser.add_argument("--max_length", type=int, default=2048)
    parser.add_argument("--num_few_shot", type=int, default=0)

    args = parser.parse_args()


    tokenizer = LlamaTokenizer.from_pretrained(args.model_name_or_path)
    model = LlamaForCausalLM.from_pretrained(args.model_name_or_path, torch_dtype=torch.float16, device_map="auto")

    run_eval(model, tokenizer, eval, args)
