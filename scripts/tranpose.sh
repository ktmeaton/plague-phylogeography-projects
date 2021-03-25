#!/bin/bash

# @ghostdog74
# https://stackoverflow.com/questions/1729824/an-efficient-way-to-transpose-a-file-in-bash

INFILE=$1

awk '{
  for (i=1; i<=NF; i++)
	{
    a[NR,i] = $i;
	}
if (NF>p)
	{ p = NF}
}
END {
for(j=1; j<=p; j++) {
  str=a[1,j]
  for(i=2; i<=NR; i++){
     str=str"\t"a[i,j];
  }
  print str
  }
}' $INFILE
