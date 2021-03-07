# Tandem Repeat Identifier

## Purpose
This repository contains two small programs for detecting perfect, tandem sequence repeats in a FASTA file containing one or more sequences. These programs will detect only repeats with motifs of a **user-specified length**.

The program will look only for repeats of the length specified at run time. Repeats of longer motifs, or repeats of motifs that can themselves be decomposed into shorter motifs, will not be identified. However, identified repeats may overlap with one another (e.g., `ATA.ATA.ATA.A` can be read as `A.TAA.TAA.TAA`). Neither program can detect imperfect or interrupted repeats.

## Sample Use Case
You could run this script multiple times to detect the presence of repeats with different motif lengths in a large number of viral genomes. If you need to detect multiple different types of repeat in a single run (including more complex types such as interspersed repeats in a eukaryotic genome) consider a tool such as [RepeatMasker](http://www.repeatmasker.org).

## Input File
The input file must be a DNA [FASTA file](https://en.wikipedia.org/wiki/FASTA_format) containing one or more DNA sequences. Amino acid sequences are not analyzed by this program. The file must have a `.fasta`, `.fna` or `.fa` extension.

## Output Files
The TRIMAN program returns a human-readable tab-separated values (TSV) output file. A comment line at the top of the file shows the parameters chosen and a header row is included. The TSV file is 1-based throughout (meaning that a repeat with start=623 begins at the 623rd nucleotide in the FASTA entry).

The TRIBED program generates a BED6 file (a BED file with 6 columns; see specifications [linked here](https://bedtools.readthedocs.io/en/latest/content/general-usage.html#bed-format)). BED files have 0-based start and 1-based end coordinates.

Output files are not sorted by coordinates. Use a tool such as [bedtools sort](https://bedtools.readthedocs.io/en/latest/content/tools/sort.html) to do this.

## Installation
You may download and execute the program in an environment containing python3. Biopython is not required.

## Execution
To run the script you can invoke python directly. Provide the FASTA input file as the sole argument:
```
python3 TRI_v_1_0.py NC_045512.2.fasta
```

An alternative method of execution is possible if you first modify the permissions:
```
chmod 755 TRI_v_1_0.py  # you need only do this once
```
and then you can execute from bash/zsh:
```
./TRI_v_1_0.py NC_045512.2.fasta
```

## Options
No options are set when the script is invoked. However, you will be prompted and have to answer three questions to determine:

* the motif size in identified repeats (e.g., if you enter 7 then septanucleotide repeats will be detected)
* the minimum number of repeats (e.g., if you enter 4, tandem repeats with 3 or fewer repeats will be ignored),
* the output file name (esp. if you want to use an alternative name).

In each case a default is indicated and will be used if the user presses _Enter_ with no other input.

# Acknowledgements
The Wuhan SARS-CoV-2 sequence (Wu et al., 2020) used in this repository was obtained from NCBI (2021) Nucleotide database. Detection of repetitive strings took advantage of a solution found on Stack Overflow (Zhang, 2015) and was used to exclude motifs that are themselves repetitive. Yes I know this is a somewhat typical pattern while coding!

>National Center for Biotechnology Information (NCBI)[Internet]. Bethesda (MD): National Library of Medicine (US), National Center for Biotechnology Information; [1988] – [cited 2021 Mar 07]. Available from: https://www.ncbi.nlm.nih.gov/

>Wu F, Zhao S, Yu B, Chen YM, Wang W, Song ZG, Hu Y, Tao ZW, Tian JH, Pei YY, Yuan ML, Zhang YL, Dai FH, Liu Y, Wang QM, Zheng JJ, Xu L, Holmes EC, Zhang YZ. A new coronavirus associated with human respiratory disease in China. Nature. 2020 Mar;579(7798):265-269. doi: [10.1038/s41586-020-2008-3](https://dx.doi.org/10.1038/s41586-020-2008-3). Epub 2020 Feb 3. Erratum in: Nature. 2020 Apr;580(7803):E7. PMID: 32015508; PMCID: PMC7094943.

>Zhang D. [2015 Apr 07]. StackOverflow Response. Permalink: https://stackoverflow.com/a/29489919

## Licence
Please see the file called LICENSE in this repository for details.

## Sample TSV Output from SARS-CoV-2 Wuhan Sequence
For ease of reading this is formatted into a table. See sample outputs directly in this repository.

`#TandemRepeatIdentifier v.1.0.0. Settings: motif_length: 3, min_reps: 3.`
| genome                                                                                            | motif   | genomesize   | start   | end     | sequence       | strand   |
|---------------------------------------------------------------------------------------------------|---------|--------------|---------|---------|----------------|----------|
| NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome   | AAC     | 29903        | 28989   | 28997   | AACAACAAC      | +        |
| NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome   | AAG     | 29903        | 3057    | 3065    | AAGAAGAAG      | +        |
| NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome   | AAG     | 29903        | 3075    | 3083    | AAGAAGAAG      | +        |
| NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome   | AAG     | 29903        | 3189    | 3197    | AAGAAGAAG      | +        |
| NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome   | AAG     | 29903        | 29390   | 29398   | AAGAAGAAG      | +        |
| NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome   | AAT     | 29903        | 25758   | 25766   | AATAATAAT      | +        |
| NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome   | ACA     | 29903        | 28990   | 28998   | ACAACAACA      | +        |
| NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome   | AGA     | 29903        | 3076    | 3084    | AGAAGAAGA      | +        |
| NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome   | AGA     | 29903        | 3190    | 3198    | AGAAGAAGA      | +        |
| NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome   | AGT     | 29903        | 23089   | 23097   | AGTAGTAGT      | +        |
| NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome   | ATC     | 29903        | 11911   | 11919   | ATCATCATC      | +        |
| NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome   | ATG     | 29903        | 11367   | 11375   | ATGATGATG      | +        |
| NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome   | CAA     | 29903        | 28988   | 28999   | CAACAACAACAA   | +        |
| NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome   | CGA     | 29903        | 26192   | 26200   | CGACGACGA      | +        |
| NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome   | CTG     | 29903        | 29022   | 29030   | CTGCTGCTG      | +        |
| NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome   | CTT     | 29903        | 4737    | 4745    | CTTCTTCTT      | +        |
| NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome   | CTT     | 29903        | 14757   | 14765   | CTTCTTCTT      | +        |
| NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome   | GAA     | 29903        | 3056    | 3064    | GAAGAAGAA      | +        |
| NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome   | GAA     | 29903        | 3074    | 3082    | GAAGAAGAA      | +        |
| NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome   | GAC     | 29903        | 26193   | 26201   | GACGACGAC      | +        |
| NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome   | GAT     | 29903        | 3206    | 3214    | GATGATGAT      | +        |
| NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome   | GAT     | 29903        | 13897   | 13905   | GATGATGAT      | +        |
| NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome   | GCT     | 29903        | 28936   | 28944   | GCTGCTGCT      | +        |
| NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome   | GTA     | 29903        | 23090   | 23098   | GTAGTAGTA      | +        |
| NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome   | GTG     | 29903        | 28557   | 28565   | GTGGTGGTG      | +        |
| NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome   | GTT     | 29903        | 25644   | 25652   | GTTGTTGTT      | +        |
| NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome   | TCT     | 29903        | 4739    | 4747    | TCTTCTTCT      | +        |
| NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome   | TGA     | 29903        | 13896   | 13904   | TGATGATGA      | +        |
| NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome   | TGC     | 29903        | 28935   | 28943   | TGCTGCTGC      | +        |
| NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome   | TGT     | 29903        | 25643   | 25651   | TGTTGTTGT      | +        |
| NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome   | TTC     | 29903        | 627     | 635     | TTCTTCTTC      | +        |
| NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome   | TTC     | 29903        | 4738    | 4746    | TTCTTCTTC      | +        |
| NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome   | TTC     | 29903        | 22321   | 22329   | TTCTTCTTC      | +        |
