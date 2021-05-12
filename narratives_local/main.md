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

1. [Introduction](http://localhost:4000/narratives/plague-phylogeography-projects/main/local?n=1)

2. [Molecular Clock](http://localhost:4000/narratives/plague-phylogeography-projects/main/local?n=3)

3. [Geographic Dispersal](http://localhost:4000/narratives/plague-phylogeography-projects/main/local?n=6)

"

---

<!--
To Convert This Local Narrative to Remote
Dataset local url:  http://localhost:4000/plague-phylogeography-projects/
Dataset remote url: https://nextstrain.org/community/ktmeaton/plague-phylogeography-projects@main

Narrative Local url: http://localhost:4000/narratives/plague-phylogeography-projects/main/local
Narrative remote url: https://nextstrain.org/community/narratives/ktmeaton/plague-phylogeography-projects@main/main

cat plague-phylogeography-projects_main_local.md | \
  sed 's/http:\/\/localhost:4000\/plague-phylogeography-projects/https:\/\/nextstrain.org\/community\/ktmeaton\/plague-phylogeography-projects@main/g' | \
  sed 's/http:\/\/localhost:4000\/narratives\/plague-phylogeography-projects\/main\/local/https:\/\/nextstrain.org\/community\/narratives\/ktmeaton\/plague-phylogeography-projects@main\/main/g' \
  > plague-phylogeography-projects_main.md

-->

# [The Field of Plague Genomics](http://localhost:4000/plague-phylogeography-projects/main/full/all?c=continent&d=map&p=full&transmissions=show)

The field of plague genomics has changed considerably over the last decade, from [17 bacterial genomes](https://doi.org/10.1038/ng.705)to [over 1300](https://doi.org/10.1101/gr.251678.119) In 2011, *Y. pestis* became the first pathogen to be [fully sequenced from ancient DNA](https://doi.org/10.1038/nature10549) and since then, over 100 genomes have been isolated from skeletal remains. To date, *Y. pestis* is the most intensively sequenced historical pathogen.

---

### Methods
 
1693 *Y. pestis* genome sequencing projects were identified from the NCBI databases using [NCBImeta](https://doi.org/10.21105/joss.01990).  Collection date and geographic location were curated by cross-referencing the original publications. Geocoding was performed using [GeoPy]() and the [Nominatim API]() for [OpenStreetMap](). Latitude and longitude for each sample were standardized at the levels of country and state. 

Genomes were removed if no associated date or location could be identified or if laboratory manipulation was documented. After curation, 600 genomes remained, comprised of 539 modern (90%) and 61 ancient (10%).  

To root the phylogentic tree, two genomes from the outgroup *Yersinia pseudotuberculosis* were downloaded ([NCTC10275](https://www.ncbi.nlm.nih.gov/nuccore/LR134373.1), [IP32953](https://www.ncbi.nlm.nih.gov/nuccore/NZ_CP009712.1)). 

---

# [Introducing Phylogenetics](http://localhost:4000/plague-phylogeography-projects/main/full/all?c=branch_major&d=tree&m=div)

The ability to differentiate strains of *Y. pestis* is at the core of genomics research. Numerous taxonomic systems have developed to identify unique lineages of plague using biochemical and molecular characteristics.
### Branch Taxonomy

The system shown here uses the phylogenetic branching patterns to separate 5 major groups, numbered **0** through **4**. These branch numbers have historically been assigned based on the order in which they were discovered and their relative proximity to the root of the tree.

### Clades

The branch nomenclature system can be further divided into clades. This nomenclature combines a branch number with a 2-3 letter clade designation. This approach is widely adopted in plague genomics research, and is suitable for broad-scale comparisons.

One example is the 'Pestoides' clade, shortened to **PE** which is part of branch **0**, thus deriving the clade name **0.PE**. This clade is known for being avirulent in humans, and only causes disease in wild rodent populations.

### Sub-Clades
This nomenclature system can be broken down into finer and finer units, depending on the resolution needed.

- *0*
- *0.PE*
- *0.PE4*
- *0.PE4h*

For the purposes of this narrative, the sub-clade nomenclature will not be used. But if you're interested, you can view the [dataset colored by sub-clades here](http://localhost:4000/plague-phylogeography-projects/main/full/all?c=branch_minor&d=tree&legend=open&m=div&p=full).

---

### Methods

Sequencing projects that were only available from the Sequence Read Archive (SRA) underwent pre-processing using the [nf-core/eager pipeline](https://doi.org/10.7717/peerj.10947). Reads were trimmed for synthetic sequences, merged across paired end libraries and lanes, and aligned to the [*Y. pestis* reference genome](https://www.ncbi.nlm.nih.gov/assembly/GCA_000009065.1). Ancient DNA (aDNA) projects were required to obtain 70% coverage of the reference genome at a minimum depth of 3X. For modern projects, a minimum depth of 10X was enforced.

The [snippy pipeline](https://github.com/tseemann/snippy) was used to perform variant calling and multiple alignment on post-processed SRA datasets and pre-assembled genomes. The output multiple alignment was filtered to only include chromosomal regions, and sites with no more than 5% missing data. 

Model selection was performed using [Modelfinder](https://doi.org/10.1038/nmeth.4285) and a maximum likelihood tree was estimated across 10 independent runs of [IQTREE](https://doi.org/10.1093/molbev/msaa015) using the K3Pu+F+I model. Branch support was evaluated using 1000 iterations of the [ultrafast bootstrap approximation (UFboot)](https://doi.org/10.1093/molbev/msx281) and considered to have strong support if UFboot >= 95.

---

# [Molecular Clock](http://localhost:4000/plague-phylogeography-projects/main/full/all?branches=hide&c=branch_major&d=tree&l=scatter&regression=show&scatterY=div)

One of the great curiosities of *Y. pestis* is that different lineages evolve, or accumulate mutations, at drastically different speeds. This makes modelling *Y. pestis* extremely challenging with regards to the molecular clock.

An organism with little to no rate variation can be explained using a simple linear model, or regression. In this scenario, The sampling date (x-axis: Date) will have a strong positive correlation with the amount of mutations that have accrued (y-axis: Divergence). This will appear as samples clustering closely to the regression line and is often referred to as a **Strict Clock Model**. 

A statistical measure of this model is *R<sup>2</sup>*, where values close to 1.0 are a good fit, and values close to 0 are a poor fit.

In contrast, samples of *Y. pestis* do not cluster around the regression line and instead are dispersed far above and below the line. The *R<sup>2</sup>* statistic is 0.09, which is very close to 0, indicating a simple linear model is a poor fit for the data. Thus, a **Strict Clock Model** is inappropriate to apply to all *Y. pestis*.

---

# [Clade Clock](http://localhost:4000/plague-phylogeography-projects/main/full/1.PRE?branches=hide&c=branch_major&l=scatter&p=grid&regression=show&scatterY=div&tl=blank)

There are cases where the **Strict Clock Model** works exceptionally well for *Y. pestis*. Some clades have been hypothesized to show strong temporal signal, particularly those associated with ancient epidemics.

This graph visualizes clade **1.PRE**, which is associated with European plague in the Medieval and Early Modern Period. The *R<sup>2</sup>* statistic is 0.93, close to 1.0, indicating the model is a very good fit to the data.

Clades that fit this model well are the:
- [Late Neolithic Bronze Age (LNBA)](http://localhost:4000/plague-phylogeography-projects/main/full/0.PRE?branches=hide&c=branch_major&l=scatter&p=grid&regression=show&scatterY=div&tl=blank)
- [Roman and Justinian Plague](http://localhost:4000/plague-phylogeography-projects/main/full/0.ANT4?branches=hide&c=branch_major&l=scatter&p=grid&regression=show&scatterY=div&tl=blank)
- [Medieval and Early Modern Period](http://localhost:4000/plague-phylogeography-projects/main/full/1.PRE?branches=hide&c=branch_major&l=scatter&p=grid&regression=show&scatterY=div&tl=blank)

The remaining clades of plague do not fit this model well. Some examples are the:
- [20th and 21st Century Pandemic](http://localhost:4000/plague-phylogeography-projects/main/full/1.ORI?branches=hide&c=branch_major&l=scatter&p=grid&regression=show&scatterY=div&tl=blank)
- [Avirulent Pestoides Plague](http://localhost:4000/plague-phylogeography-projects/main/full/0.PE?branches=hide&c=branch_major&l=scatter&p=grid&regression=show&scatterY=div&tl=blank)

Sometimes this model even predicts that evolution can go backwards!
- [2.MED](http://localhost:4000/plague-phylogeography-projects/main/full/2.MED?branches=hide&c=branch_major&l=scatter&p=grid&regression=show&scatterY=div&tl=blank)

---

# [Model Testing](http://localhost:4000/plague-phylogeography-projects/main/full/all?branches=hide&c=branch_major&d=tree&l=scatter&regression=show&scatterY=div)

A placeholder slide for Bayesian testing of **Relaxed Clock Models**.

---

# [Geographic Origins](http://localhost:4000/plague-phylogeography-projects/main/full/0.PRE?branchLabel=Province%20Confidence&c=province_conf_category&f_branch_major=0.PRE&p=grid&tl=province&ci&legend=closed)

Another great curiosity of plague is its geographic history with regards to origins and migration events.

The oldest, or most basal, clade of *Y. pestis* is **0.PE** which is associated with the Late Neolithic and Bronze Age. This clade has been isolated from skeletal remains from all across Eurasia.

In this analysis, the geographic location of ancestral nodes in the tree has been estimated to the level of state. Locations that are estimated with high confidence (>=0.95) are indicated by the color purple, while low confidence is indicated by a white/grey color.

The majority of ancestral locations cannot be confidently estimated given the sparseness of the data with regards to the geographic breadth.

One event has high confidence, and that is a migration from Germany (Bavaria) to Russia (Altai Krai). However, this is likely an artifact of sampling bias, given that 50% of samples in this clade derive from Russia, and 25% are from Germany. Given the data, there is an X% probability of observing this result simply by chance.

# [Plague of Justinian](http://localhost:4000/plague-phylogeography-projects/main/full/0.ANT4?branchLabel=Country%20Confidence&c=country_conf_category&ci&tl=country&legend=closed)

Similar to the Late Neolithic Bronze Age (LNBA) plague, the spread of plague during the Roman period and the Plague of Justinian are highly uncertain. The only migration event that is confidently estimated is between Germany and France. However, given that ~40% of this clade's samples derive from Germany, it is highly possible that this is an artifact of sampling bias as well.

# [Medieval and Early Modern Plague](http://localhost:4000/plague-phylogeography-projects/main/full/1.PRE?branchLabel=Branch%20Support&c=clade_rtt_dist&legend=closed&m=div&p=grid&tl=country_date_strain&transmissions=hide)

Within this clade, plague can be grouped into 3 clusters. This phylogeny is colored by distance to the clade root and branches are labelled with their UFboot support value.

---
## 14th Century (Blue)

At the clade root is a multifurcation or polytomy where numerous strains diverge simultaneously. Samples from this event have been isolated from all across Europe, from Russia to England. Despite having such a broad geographic range, they derive from a relatively narrow time window of the 14th century.

---

## 15th-17th Century (Turquoise, Green)

This clade has a more localized distribution around the Alps and the Baltic Sea and is observed from the 15th-17th century.

---

## 17th-18th Century (Yellow, Orange, Red)

The last identified clade of the Early Modern period again has a broad geographic distribution from Russia to England, and dates from the 17th-18 centuries.


