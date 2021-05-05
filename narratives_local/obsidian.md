---
title: Obsidian Test
authors: 
  - Katherine Eaton
authorLinks: 'https://ktmeaton.github.io/'
affiliations: McMaster Ancient DNA Centre
date: May 2021
dataset: http://localhost:4000/plague-phylogeography-projects/main/full/all?c=continent&d=map&p=full&transmissions=show
abstract: "This narrative tests Obsidian Integration"
bibliography: library.bib
csl: apa-numeric-superscript.csl
---

# [Objectives](http://localhost:4000/plague-phylogeography-projects/main/full/all?c=continent&d=map&p=full&transmissions=show)

1. Write narratives from within [[Obsidian]].
1. Strip wiki-links and convert to standardized markdown.
1. Manage citations automatically.

\pagebreak

---

# [Pandoc](http://localhost:4000/plague-phylogeography-projects/main/full/all?c=continent&d=map&p=full&transmissions=show)

## PDF

A markdown can be converted to pdf using pandoc via:

```bash
pandoc obsidian.md -o obsidian.pdf
```

## HTML

A markdown can be converted to html using pandoc via:

```bash
pandoc obsidian.md -o obsidian.html
```

## WikiLinks

I probably want to convert the wikilinks first though:

```bash
python3 ../../pandoc/convert_wikilinks.py -i obsidian.md -o obsidian-convert.md; 
pandoc obsidian-convert.md -o obsidian-convert.pdf;
```


\pagebreak

---


# [Citations](http://localhost:4000/plague-phylogeography-projects/main/full/all?c=continent&d=map&p=full&transmissions=show)

## Pandoc 

One way of doing citations is with a bibtex key [@andradesvaltuena2017StoneAgePlague]. This will work well for processing with pandoc, but isn't going to show up in [[Auspice]].

```bash 
pandoc -s obsidian.md --filter pandoc-doi2bib --citeproc -o obsidian.pdf --bibliography ../../zotero.bib
```

## DOI

My preferred way though is to use [[DOI]] whenever possible using the [[pandoc]] filter [[doi2bib]]. [@DOI:10.21105/joss.01990]

```bash 
python3 ../../pandoc/convert_wikilinks.py -i obsidian.md -o obsidian-convert.md
pandoc -s obsidian-convert.md --filter pandoc-doi2bib --citeproc -o obsidian-convert.pdf
```

## Footnotes

Another way might be to use the [[Footnote Shortcut]] in [[Obsidian]]. Again, this works really well with [[pandoc]], but not with auspice.

```bash 
python3 ../../pandoc/convert_wikilinks.py -i obsidian.md -o obsidian-convert.md;
pandoc -s obsidian.md --filter pandoc-doi2bib --citeproc -o obsidian.pdf 
```


## [[Markdown]]

What if I convert [[Markdown]] to [[Markdown]]?

```bash 
python3 ../../pandoc/convert_wikilinks.py -i obsidian.md -o obsidian-convert.md;

pandoc -t markdown-citations -s obsidian-convert.md --filter pandoc-doi2bib --citeproc -o obsidian-convert-self.md;

grep -v ":::" obsidian-convert-self.md > obsidian-convert-self-clean.md
```


\pagebreak

---

# [Style](http://localhost:4000/plague-phylogeography-projects/main/full/all?c=continent&d=map&p=full&transmissions=show)

I like the [[MVP]] [[CSS]] a lot. Can I export [[Auspice]] markdown to this?

```bash
python3 ../../pandoc/convert_wikilinks.py -i obsidian.md -o obsidian-convert.md
pandoc \
  -s obsidian-convert.md \
  -c ../../pandoc/templates/pandoc-mvp-css/css/mvp.css \
  --template ../../pandoc/templates/pandoc-mvp-css/template.html \
  --toc \
  --toc-depth=2 \
  -o obsidian-convert_mvp.html
```

Wow, this looks gorgeous! 

\pagebreak

--- 
# [Final Workflow](http://localhost:4000/plague-phylogeography-projects/main/full/all?c=continent&d=map&p=full&transmissions=show)

The final citation workflow I've decided on is:

1. Convert [[wiki links]]:
```bash
python3 ../../pandoc/convert_wikilinks.py -i obsidian.md -o obsidian-convert.md;
```
2. Render [[Markdown]] with [[pandoc]]:
```bash
pandoc -t markdown-citations -s obsidian-convert.md --filter pandoc-doi2bib --citeproc -o obsidian-convert-self.md;
```
3. Cleanup [[Markdown]]:
```bash
grep -v ":::" obsidian-convert-self.md | \
  sed 's/\.\^/<sup>/g' | \
  sed 's/\^/<\/sup>/g' | \
  sed 's/{#references .unnumbered}//g' | \
  sed 's/authors:/author:/g' | \
  sed 's/^[#]/##/g' | \
  grep -V "\pagebreak" \
  > obsidian-convert-self-clean.md
```
4. Style with [[MVP]]:
```bash
pandoc \
  -s obsidian-convert-self-clean.md \
  -c ../../pandoc/templates/pandoc-mvp-css/css/mvp.css \
  --template ../../pandoc/templates/pandoc-mvp-css/template.html \
  --toc \
  --toc-depth=2 \
  -o obsidian-convert-self-clean.html
```
5. Convert to [[PDF]]:
```bash
pandoc -s  obsidian-convert-self-clean.md -o  obsidian-convert-self-clean.pdf
pandoc -s  obsidian-convert-self-clean.md -o  obsidian-convert-self-clean.docx
```


\pagebreak

---

# [References](http://localhost:4000/plague-phylogeography-projects/main/full/all?c=continent&d=map&p=full&transmissions=show)