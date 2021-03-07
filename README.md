# Tandem Repeat Identifier

## Purpose
This is a small program for detecting perfect, tandem sequence repeats in a FASTA file containing one or more sequences. It will detect only repeats with motifs of a user-specified length and will not return repeats with longer motifs, or which can be decomposed into repeats with a shorter motif. The program cannot detect imperfect or interrupted repeats.

## Installation
You may download and execute the program in an environment containing python3.

## Running the Script
To execute the script you can invoke python directly providing a single FASTA file as input:
```
python3 TRI_v_1_0.py NC_045512.2.fasta
```
or modify the permissions and run:
```
chmod 755 TRI_v_1_0.py  # you need only do this once
./TRI_v_1_0.py NC_045512.2.fasta
```
You may then answer the questions as prompted to determine:

* the motif size detected (e.g., if you enter 7 then septanucleotide repeats will be detected)
* the minimum number of repeats (e.g., if you enter 4, tandem repeats with 3 or fewer repeats will be ignored),
* the output file name (esp. if you want to use an alternative name).

In each case a default is indicated and will be used if the user presses enter with no other input.

The input file may contain one or more DNA sequences and must have a `.fasta`, `.fna` or `.fa` extension. Amino acid sequences are not analyzed by this program.

## Output
The output is a tab separated file with a comment line indicating run parameters and a header showing column contents.

## Acknowledgements
The Wuhan SARS-CoV-2 sequence (Wu et al., 2020) used in this repository was obtained from NCBI (2021) Nucleotide database.

Detection of repetitive strings took advantage of the solution [cited here](https://stackoverflow.com/a/29489919) and was used to exclude motifs that are themselves repetitive.

>National Center for Biotechnology Information (NCBI)[Internet]. Bethesda (MD): National Library of Medicine (US), National Center for Biotechnology Information; [1988] – [cited 2021 Mar 07]. Available from: https://www.ncbi.nlm.nih.gov/

>Wu F, Zhao S, Yu B, Chen YM, Wang W, Song ZG, Hu Y, Tao ZW, Tian JH, Pei YY, Yuan ML, Zhang YL, Dai FH, Liu Y, Wang QM, Zheng JJ, Xu L, Holmes EC, Zhang YZ. A new coronavirus associated with human respiratory disease in China. Nature. 2020 Mar;579(7798):265-269. doi: [10.1038/s41586-020-2008-3](https://dx.doi.org/10.1038/s41586-020-2008-3). Epub 2020 Feb 3. Erratum in: Nature. 2020 Apr;580(7803):E7. PMID: 32015508; PMCID: PMC7094943.

>Zhang D. [2015 Apr 07]. StackOverflow Response. Permalink: https://stackoverflow.com/a/29489919

## Licence
Please see licence file in this repository.

## Sample Output from SARS-CoV-2 Wuhan Sequence

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
