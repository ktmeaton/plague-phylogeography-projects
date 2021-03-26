#!/usr/bin/env python3

# Example Usage (fastq):
# ./fastq_subsample.py --r1 test_SXXX_L001_R1_001.fastq --r2 test_SXXX_L001_R2_001.fastq --depth 10 --outdir .

# Example Usage (fastq.gz):
# ./fastq_subsample.py --r1 test_SXXX_L001_R1_001.fastq.gz --r2 test_SXXX_L001_R2_001.fastq.gz --depth 10 --outdir .

import random
import argparse
import gzip
import os

# Program description
parser = argparse.ArgumentParser(description="Subsample paired-end fastq files down to a specified read depth.",
                                 add_help=True)

# Command-line argument capture
parser.add_argument('--r1',
                    help = 'Path to input fastq forward reads.',
                    action = 'store',
                    dest = 'r1File',
                    required = True)

parser.add_argument('--r2',
                    help = 'Path to input fastq forward reads.',
                    action = 'store',
                    dest = 'r2File',
                    required = True)

parser.add_argument('--outdir',
                    help = 'The output directory to write to.',
                    action = 'store',
                    dest = 'outDir',
                    required = True)

parser.add_argument('--depth',
                    help = 'Number of reads to subsample down to (ex. 1000).',
                    action = 'store',
                    dest = 'depthNum',
                    required = True)

# Retrieve user parameters
args = vars(parser.parse_args())
r1_file = args["r1File"]
r2_file = args["r2File"]
depth = int(args["depthNum"])
out_dir = args["outDir"]

# Check if the output directory exists
if not os.path.exists(out_dir):
  print("Error: The output directory does not exist.")
  exit(1)

# The output will be based on our in-house pipeline naming:
# ex. test_SXXX_L001_R1_001.fastq.gz
# Parse the input sample name
sample = r1_file.split("_")[0]
r1_out = os.path.join(out_dir, r1_file.replace(sample, sample + "-subsample" + str(depth)))
r2_out = os.path.join(out_dir, r2_file.replace(sample, sample + "-subsample" + str(depth)))

# use the default text opening function
open_func = open
if r1_file.split(".")[-1] == "gz":
  # Use the gzip opening function
  open_func = gzip.open

# Log some helpful info to output
print("Input Forward Reads:", r1_file)
print("Input Reverse Reads:", r2_file)
print("Subsample Depth:", depth)
print()

# Dictionaries to hold all r1 and r2 records
r1_dict = {} # {id: {seq: '', line3: '', qual: ''}}
r2_dict = {} # {id: [sequence, +, quality]}

# Save the current line number as a variable
# this will be used to figure out which element of a
# fastq record is being processed (header, seq, quality, etc.)

line_counter = 0

print("[1/3] Reading input files...")
# Iterate through input files and store sequences
with open_func(r1_file, "rt") as r1:
  with open_func(r2_file, "rt") as r2:
    # Read in both files, split into a list using a newline as a separator
    r1_full = r1.read().strip().split("\n")
    r2_full = r2.read().strip().split("\n")
    # Iterate through them in parallel (zip)
    for r1_line, r2_line in zip(r1_full, r2_full):

      # -----------------------------------------------
      # The first line of each record is the header
      if line_counter % 4 == 0:
        # The read ID is the characters before the first space
        r1_id = r1_line.split(" ")[0]
        r2_id = r2_line.split(" ")[0]

        # Check that the read ids match match
        if r1_id != r2_id:
          print("Error: The read IDs are mismatched.")
          print("r1 read id", r1_id, "is not the same as r2 read id", r2_id)
          exit(1)

        # Add the header to the dictionaries
        r1_dict[r1_id] = {'seq': '', 'line3': '', 'qual': ''}
        r2_dict[r2_id] = {'seq': '', 'line3': '', 'qual': ''}

      # -----------------------------------------------
      # The second line of each record is the sequence
      if line_counter % 4 == 1:
        # Add the sequences to the corresponding read id
        r1_dict[r1_id]['seq'] = r1_line
        r2_dict[r2_id]['seq'] = r2_line

      # -----------------------------------------------
      # The third line of each record is the ambiguous third line
      if line_counter % 4 == 2:
         r1_dict[r1_id]['line3'] = r1_line
         r2_dict[r1_id]['line3'] = r2_line

      # -----------------------------------------------
      # The fourth line of each record is the quality
      if line_counter % 4 == 3:
         r1_dict[r1_id]['qual'] = r1_line
         r2_dict[r1_id]['qual'] = r2_line

      line_counter += 1
print("Reading finished.")
print()

# Check if the subsampling depth is greater than the molecules in the file
if len(r1_dict) < depth:
  # If so, just assign it to all the molecules
  print("Warning: Requested depth of", depth, "is greater than the", len(r1_dict), "molecules in the file. Changing sampling depth to", len(r1_dict), ".")
  depth = len(r1_dict)

# Random sampling without replacement
print("[2/3]  Subsampling input files...")
subsample_ids = random.sample(list(r1_dict), k=depth)
print("Subsampling finished.")
print()

print("[3/3] Writing output files...")
# Write the output files
with open_func(r1_out, "wt") as r1_out_file:
  with open_func(r2_out, "wt") as r2_out_file:
    for id in subsample_ids:
      # Write the 4 components of a fasta record
      r1_out_file.write(
        id + "\n" +
        r1_dict[id]["seq"] + "\n" +
        r1_dict[id]["line3"] + "\n" +
        r1_dict[id]["qual"] + "\n",
      )

      r2_out_file.write(
        id + "\n" +
        r2_dict[id]["seq"] + "\n" +
        r2_dict[id]["line3"] + "\n" +
        r2_dict[id]["qual"] + "\n"
      )

print("Writing finished.")
print()

print("Wrote", depth, "sequences to", r1_out)
print("Wrote", depth, "sequences to", r2_out)
