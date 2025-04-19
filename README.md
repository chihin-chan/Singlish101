# Singlish-UKEnglish 101: Siao ah, you alright?!

![alt text](Cover/Figures/cover.png)

A repository for documenting translations between common phrases spoken in the Singlish and UK English language.

This document is integrated with [Google forms](https://docs.google.com/forms/d/1xC0B0aKq7cU7MXO0mhMt-IBiMesHfgXJaLT6TNtVGuc/edit), in which a GitHub CI checks for new entries and adds them into `Chaptermate/gsheets.tex`.

The GitHub CI has been instructed to check for new entries every 10 minutes, however, it seems to be entirely random at times - any feedback is greatly appreciated.

## Overview

The repository is organised as follows,

- **Cover Page** - `Cover/cover.tex`
- **Cover Figures** - `Cover/Figures/`
- **Main Document with chapters** - `main.tex`
- **Chaptermate** - `Chaptermate/gsheets.tex` (Contains phrases fetched from Google sheets)

## Compiling the Document

To compile the document into a PDF, use the following command:

```bash
latexmk -pdf main.tex
```

Tested with latexmk version 4.67.
