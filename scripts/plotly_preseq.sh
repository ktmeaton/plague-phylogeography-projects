#!/bin/bash

# 1. Extract Individual Samples from multiqc preseq data.

INFILE=$1
FILTER=L001

# Make a list of samples
SAMPLES=(`cut -f 1 $INFILE |
	sed '/^$/d' |
	awk -F "-" '{print $1}' |
	sed 's/ /_/g' |
	uniq |
	tr '\n' ' '`)

for sample in ${SAMPLES[@]}
do
	echo $sample;
	grep "$sample.*$FILTER" $INFILE -B 1 |
  	awk -F "\t" -v sample=$sample '{
		  x="";
			y="";
			for (i=2;i<=NF;i++)
			{
		    x=x"\t"$i;
			  y=y"\t"$i;
			}
			if (NR == 1)
			{
			  print sample"_X"x;
			}
			if (NR == 2)
			{
			print sample"_Y"y;
			}
		}' > preseq_$sample.tsv;

	# Transpose the file
	awk '{
    for (i=1; i<=NF; i++)
	  {
      a[NR,i] = $i;
	  }
    if (NF>p)
	  {
			p = NF;
		}
  }
  END {
    for(j=1; j<=p; j++)
		{
      str=a[1,j]
      for(i=2; i<=NR; i++)
			{
        str=str"\t"a[i,j];
      }
    print str
    }
  }' preseq_${sample}.tsv > preseq_${sample}_tranpose.tsv

done
