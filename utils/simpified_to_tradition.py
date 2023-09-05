import argparse
import os

import opencc
converter = opencc.OpenCC('s2t.json')


def main():
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir", type=str, default="")
    parser.add_argument("--output_dir", type=str, default="")
    args = parser.parse_args()

    # Read all csv files in input_dir
    for filename in os.listdir(args.input_dir):
        # Read only csv files
        if not filename.endswith(".csv"):
            continue
        
        # Read file
        with open(os.path.join(args.input_dir, filename), "r") as f:
            lines = f.readlines()
        
        # Convert simplified Chinese to traditional
        for i in range(len(lines)):
            lines[i] = converter.convert(lines[i])
        
        # Write to output_dir
        with open(os.path.join(args.output_dir, filename), "w") as f:
            f.writelines(lines)

main()