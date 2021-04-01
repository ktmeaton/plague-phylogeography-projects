#!/usr/bin/env python3

import random
import click

@click.command()
@click.help_option("--help", "-h")
@click.option(
    "--r1",
    help="Path to input fastq forward reads.",
    type=click.Path(exists=True, dir_okay=False, allow_dash=True),
)
@click.option(
    "--r2",
    help="Path to input fastq reverse reads.",
    type=click.Path(exists=True, dir_okay=False, allow_dash=True),
)
@click.option(
    "-d",
    "--depth",
    help="Subsampling down to read depth.",
    type=int,
)

def main(
    r1: str,
    r2: str,
    depth: int,
):
  """Subsample paired-end fastq files down to a specified read depth."""

  print("Forward Reads:", r1)
  print("Reverse Reads:", r2)
  print("Depth:", depth)

if __name__ == "__main__":
    main()
