#!/bin/bash

cd ../src


python taide_llama.py \
    --model_name_or_path /home/u5061819/llama-task-vector/taide-task-vector/models/llama2-13b_stage2-h-s23063_ft-b.2-e3 \
    --save_dir ../results/llama2-13b_stage2-h-s23063_ft-b.2-e3 \
    --num_few_shot 0

python taide_llama.py \
    --model_name_or_path /home/u5061819/llama-task-vector/taide-task-vector/models/llama2-13b_stage2-h-s23063_ft-b.2-e3 \
    --save_dir ../results/llama2-13b_stage2-h-s23063_ft-b.2-e3 \
    --num_few_shot 5
