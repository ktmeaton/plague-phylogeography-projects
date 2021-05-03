---
title: A Genomic History of Plague
authors: 
  - Katherine Eaton
authorLinks:
  - https://ktmeaton.github.io/
affiliations: "McMaster Ancient DNA Centre"
date: "May 2021"
dataset: "http://localhost:4000/plague-phylogeography-projects/main/full/all?c=continent&d=map&p=full&transmissions=show"
abstract: "
Plague has an impressively long and expansive history as a human pathogen. The earliest evidence of the plague bacterium *Yersinia pestis* comes from ancient DNA studies dating its emergence to at least the Neolithic. Since then, *Y. pestis* has travelled extensively due to ever-expanding global trade networks and the ability to infect a diverse array of mammalian hosts. Few regions of the ancient and modern world remain untouched by this disease, as plague has an established presence on every continent except Oceania.
"
---

<!--
To Convert This Local Narrative to Remote
local url:  http://localhost:4000/plague-phylogeography-projects/
remote url: https://nextstrain.org/community/ktmeaton/plague-phylogeography-projects@main
sed 's/http:\/\/localhost:4000\/plague-phylogeography-projects/https:\/\/nextstrain.org\/community\/ktmeaton\/plague-phylogeography-projects@main/g' plague-phylogeography-projects_main_local.md > plague-phylogeography-projects_main.md
-->


# [Lineages](http://localhost:4000/plague-phylogeography-projects/main/full/all?c=branch_number&d=tree)

### There are a wide variety of nomenclature systems to identify lineages of plague. The system shown here uses the branching pattern of the *Y. pestis* phylogeny to separate 5 major lineages. The lineage numbers have historically been assigned based on the order in which they were discovered, and how close they are to the root of the tree.

### Mousing over the legend elements will enlarge the corresponding bubbles in the phylogeny. Try to mouse over the lineage '0' legend element, and see where in the phylogeny this clade is located. Lineage 0 is the closest to the bottom (ie. the 'Root') which is why it is numbered 0.

---

# [Clades](http://localhost:4000/plague-phylogeography-projects/main/full/all?c=branch_major&d=tree)

### To provide finer resolution, the branch nomenclature system can be further divided into clades. This nomenclature combines a branch number with a 2-3 letter clade designation.

### One clade designation is 'Pestoides', shortened to PE which is part of branch 0, thus deriving the clade name '0.PE'. This clade is known for being avirulent in humans, only causing disease in wild rodent populations.

### This nomenclature system can be broken down into finer and finer units, depending on the resolution needed.

- 0
- 0.PE
- 0.PE4
- 0.PE4h

### For the purposes of this narrative, the finer designations beyond *Branch Number*.*Clade* will not be used. But if you're interested, you can view the [dataset colored by minor clades here](http://localhost:4000/plague-phylogeography-projects/main/full/all?c=branch_minor&d=tree&legend=open&p=full).

---

# [Molecular Clock](http://localhost:4000/plague-phylogeography-projects/main/full/all?branches=hide&c=branch_major&d=tree&l=scatter&regression=show&scatterY=div)

### One of the great curiosities of plague is that different lineages evolve, or accumulate mutations, at drastically different speeds. This makes modelling *Y. pestis* extremely challenging with regards to the molecular clock.

### An organism with little to no rate variation can be explained using a simple linear model, or regression. In this scenario, The sampling date (x-axis: Date) will have a strong positive correlation with the amount of mutations that have accrued (y-axis: Divergence). This will appear as samples (circles) clustering closely to the regression line and is often referred to as a "Strict Clock Model". 

### A statistical measure of this model is *R<sup>2</sup>*, where values close to 1.0 are a good fit, and values close to 0 are a poor fit.

### In contrast, samples of *Y. pestis* do not cluster around the regression line and instead are dispersed far above and below the line. The *R<sup>2</sup>* statistic is 0.09, which is very close to 0, and thus indicating a linear model is a poor fit for the data. Thus, a "Strict Clock Model" for all of *Y. pestis* is inappropriate and a more complex "Relaxed Clock Model" is often used instead.

---

# [Clade Clock](http://localhost:4000/plague-phylogeography-projects/main/full/1.PRE?branches=hide&c=branch_major&l=scatter&p=grid&regression=show&scatterY=div&tl=country&transmissions=hide)

### However, there are cases where the Strict Clock Model works exceptionally well for *Y. pestis*. Some clades have been hypothesized to show strong temporal signal, particularly clades associated with ancient epidemics.

### This graph visualizes clade *1.PRE*, which is associated with European plague in the Medieval and Early Modern Period. The *R<sup>2</sup>* statistic is 0.93, close to 1.0, indicating the model is a very good fit to the data.

### Clades that fit this model well are the:
#### - [Late Neolithic Bronze Age (LNBA)](http://localhost:4000/plague-phylogeography-projects/main/full/0.PRE?branches=hide&c=branch_major&l=scatter&p=grid&regression=show&scatterY=div&tl=country&transmissions=hide)
#### - [Roman and Justinian Plague](http://localhost:4000/plague-phylogeography-projects/main/full/0.ANT4?branches=hide&c=branch_major&l=scatter&p=grid&regression=show&scatterY=div&tl=country&transmissions=hide)
#### - [Medieval and Early Modern](http://localhost:4000/plague-phylogeography-projects/main/full/1.PRE?branches=hide&c=branch_major&l=scatter&p=grid&regression=show&scatterY=div&tl=country&transmissions=hide)

### The remaining clades of plague do not fit this model well. Some examples are the:
#### - [20th and 21st Century Pandemic](http://localhost:4000/plague-phylogeography-projects/main/full/1.ORI?branches=hide&c=branch_major&l=scatter&p=grid&regression=show&scatterY=div&tl=country&transmissions=hide)
#### - [Avirulent Pestoides Plague](http://localhost:4000/plague-phylogeography-projects/main/full/0.PE?branches=hide&c=branch_major&l=scatter&p=grid&regression=show&scatterY=div&tl=country&transmissions=hide)

### Sometimes this model even predicts that evolution can go backwards!
#### - [2.MED](http://localhost:4000/plague-phylogeography-projects/main/full/2.MED?branches=hide&c=branch_major&l=scatter&p=grid&regression=show&scatterY=div&tl=country&transmissions=hide)

---