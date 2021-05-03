---
title: A Genomic History of Plague
authors: 
  - Katherine Eaton
authorLinks:
  - https://ktmeaton.github.io/
affiliations: "McMaster Ancient DNA Centre"
date: "May 2021"
dataset: "https://nextstrain.org/community/ktmeaton/plague-phylogeography-projects@main/main/full/all?c=continent&d=map&p=full&transmissions=show"
abstract: "
Plague has an impressively long and expansive history as a human pathogen. The earliest evidence of the plague bacterium *Yersinia pestis* comes from ancient DNA studies dating its emergence to at least the Neolithic. Since then, *Y. pestis* has travelled extensively due to ever-expanding global trade networks and the ability to infect a diverse array of mammalian hosts. Few regions of the ancient and modern world remain untouched by this disease, as plague has an established presence on every continent except Oceania.
"
---

<!--
To Convert This Local Narrative to Remote
local url:  https://nextstrain.org/community/ktmeaton/plague-phylogeography-projects@main/
remote url: https://nextstrain.org/community/ktmeaton/plague-phylogeography-projects@main
sed 's/http:\/\/localhost:4000\/plague-phylogeography-projects/https:\/\/nextstrain.org\/community\/ktmeaton\/plague-phylogeography-projects@main/g' plague-phylogeography-projects_main_local.md > plague-phylogeography-projects_main.md
-->


# [Introducing the Tree](https://nextstrain.org/community/ktmeaton/plague-phylogeography-projects@main/main/full/all?c=branch_number&d=tree)

There are a wide variety of nomenclature systems to identify lineages of plague. The system shown here uses the branching pattern of the *Y. pestis* phylogeny to separate 5 major lineages. The lineage numbers have historically been assigned based on the order in which they were discovered, and how close they are to the root of the tree.

Mousing over the legend elements will enlarge the corresponding bubbles in the phylogeny. Try to mouse over the lineage '0' legend element, and see where in the phylogeny this clade is located. Lineage 0 is the closest to the bottom (ie. the 'Root') which is why it is numbered 0.

---

# [The Sub Clades](https://nextstrain.org/community/ktmeaton/plague-phylogeography-projects@main/main/full/all?c=branch_major&d=tree)

To provide finer resolution, the branch nomenclature system can be further divided into clades. This nomenclature combines a branch number with a 2-3 letter clade designation.

One clade designation is 'Pestoides', shortened to PE which is part of branch 0, thus deriving the clade name '0.PE'. This clade is known for being avirulent in humans, only causing disease in wild rodent populations.

This nomenclature system can be broken down into finer and finer units, depending on the resolution needed.

- 0
- 0.PE
- 0.PE4
- 0.PE4h

For the purposes of this narrative, the finer designations beyond *Branch Number*.*Clade* will not be used. But if you're interested, you can view the [dataset colored by minor clades here](https://nextstrain.org/community/ktmeaton/plague-phylogeography-projects@main/main/full/all?c=branch_minor&d=tree&legend=open&p=full).

---

# [Rates and Dates](https://nextstrain.org/community/ktmeaton/plague-phylogeography-projects@main/main/full/all?branches=hide&c=branch_major&d=tree&l=scatter&regression=show&scatterY=div)

One of the great curiosities of plague is that different lineages evolve, or accumulate mutations, at drastically different speeds. This makes modelling *Y. pestis* extremely challenging with regards to the molecular clock.

An organism with little to no rate variation can be explained using a simple linear model, or regression. In this scenario, The sampling date (x-axis: Date) will have a strong positive correlation with the amount of mutations that have accrued (y-axis: Divergence). This will appear as samples (circles) clustering closely to the regression line and is often referred to as a "Strict Clock Model". 

A statistical measure of this model is *R<sup>2</sup>*, where values close to 1.0 are a good fit, and values close to 0 are a poor fit.

In contrast, samples of *Y. pestis* do not cluster around the regression line and instead are dispersed far above and below the line. The *R<sup>2</sup>* statistic is 0.09, which is very close to 0, and thus indicating a linear model is a poor fit for the data. Thus, a "Strict Clock Model" for all of *Y. pestis* is inappropriate and a more complex "Relaxed Clock Model" is often used instead.

---

# [Clade Clock](https://nextstrain.org/community/ktmeaton/plague-phylogeography-projects@main/main/full/1.PRE?branches=hide&c=branch_major&l=scatter&p=grid&regression=show&scatterY=div&tl=country&transmissions=hide)

However, there are cases where the Strict Clock Model works exceptionally well for *Y. pestis*. Some clades have been hypothesized to show strong temporal signal, particularly clades associated with ancient epidemics.

This graph visualizes clade *1.PRE*, which is associated with European plague in the Medieval and Early Modern Period. The *R<sup>2</sup>* statistic is 0.93, close to 1.0, indicating the model is a very good fit to the data.

Clades that fit this model well are the:
- [Late Neolithic Bronze Age (LNBA)](https://nextstrain.org/community/ktmeaton/plague-phylogeography-projects@main/main/full/0.PRE?branches=hide&c=branch_major&l=scatter&p=grid&regression=show&scatterY=div&tl=country&transmissions=hide)
- [Roman and Justinian Plague](https://nextstrain.org/community/ktmeaton/plague-phylogeography-projects@main/main/full/0.ANT4?branches=hide&c=branch_major&l=scatter&p=grid&regression=show&scatterY=div&tl=country&transmissions=hide)
- [Medieval and Early Modern](https://nextstrain.org/community/ktmeaton/plague-phylogeography-projects@main/main/full/1.PRE?branches=hide&c=branch_major&l=scatter&p=grid&regression=show&scatterY=div&tl=country&transmissions=hide)

The remaining clades of plague do not fit this model well. Some examples are the:
- [20th and 21st Century Pandemic](https://nextstrain.org/community/ktmeaton/plague-phylogeography-projects@main/main/full/1.ORI?branches=hide&c=branch_major&l=scatter&p=grid&regression=show&scatterY=div&tl=country&transmissions=hide)
- [Avirulent Pestoides Plague](https://nextstrain.org/community/ktmeaton/plague-phylogeography-projects@main/main/full/0.PE?branches=hide&c=branch_major&l=scatter&p=grid&regression=show&scatterY=div&tl=country&transmissions=hide)

Sometimes this model even predicts that evolution can go backwards!
- [2.MED](https://nextstrain.org/community/ktmeaton/plague-phylogeography-projects@main/main/full/2.MED?branches=hide&c=branch_major&l=scatter&p=grid&regression=show&scatterY=div&tl=country&transmissions=hide)

---

# [Geographic History](https://nextstrain.org/community/ktmeaton/plague-phylogeography-projects@main/main/full/all?branches=hide&d=map&l=scatter&p=full&regression=show&scatterY=div&tl=country&transmissions=hide)

Another curiosity of plague is its complex geographic history.

The Americas have only ever been colonized by one clade of plague: 1.ORI.

# [Geographic Origins](https://nextstrain.org/community/ktmeaton/plague-phylogeography-projects@main/main/full/0.PRE?branchLabel=Province%20Confidence&c=province_conf_category&f_branch_major=0.PRE&p=grid&tl=province&ci&legend=closed)

The oldest, or most basal, clade of *Y. pestis* is **0.PE** which is associated with the Late Neolithic and Bronze Age Period. This clade has been isolated from skeletal remains from all across Eurasia.

In this analysis, the geographic location of ancestral nodes in the tree has been estimate to the province/state level. Locations that are estimated with high confidence (>=0.95) are indicated by the color purple, while low confidence is indicated by a white/grey color.

The majority of ancestral locations cannot be confidently estimated given the sparseness of the data both in quantity (N=8), and geographic breadth.

One migration event has high confidence, and that is migration from Germany (Bavaria) to Russia (Altai Krai). However, this result has almost no intepretative value due to sampling biases present in the data. For example, if ancestral location is [estimated at the country level](https://nextstrain.org/community/ktmeaton/plague-phylogeography-projects@main/main/full/0.PRE?branchLabel=Country&c=country_conf_category&f_branch_major=0.PRE&p=grid&tl=country), the pattern changes substantially.

# [Plague of Justinian](https://nextstrain.org/community/ktmeaton/plague-phylogeography-projects@main/main/full/0.ANT4?branchLabel=Country%20Confidence&c=country_conf_category&ci&tl=country&legend=closed)

Similar to the Late Neolithic Bronze Age (LNBA) plague, the spread of plague during the Roman period and the Plague of Justinian are highly uncertain. The only migration event that is confidently estimate across multiple geographic resolutions is between Germany and France. However, given that ~40% of this clade's samples derive from Germany, it is highly possible that this is an artifact of sampling bias as well.

# [Medieval and Early Modern Plague](https://nextstrain.org/community/ktmeaton/plague-phylogeography-projects@main/main/full/1.PRE?branchLabel=Province%20Confidence&c=clade_rtt_dist&ci&legend=closed&p=grid&tl=country&transmissions=hide)

Within this clade, plague can be grouped into 3 clusters. 

## 14th Century (Blue)

At the clade root is a multifurcation or polytomy where numerous strains diverge simultaneously. Samples from this event have been isolated from all across Europe, from Russia to England. Despite having such a broad geographic range, they derive from a relatively narrow time window of the 14th century.

## 15th-17th Century (Turquoise, Green)

This clade has a more localized distribution around the Alps and the Baltic Sea and is observed from the 15th-17th century.

## 17th-18th Century (Yellow, Orange, Red)

The last identified clade of the Early Modern period again has a broad geographic distribution from Russia to England, and dates from the 17th-18 centuries.


