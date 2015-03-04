# About
The file `proper_names.txt` contains a newline-delimited file which contains all of the words in the PHI5 which are likely proper names (persons, places, etc.). The value of this list is that, since everything is a noun, it may be used as a default POS tagger for these unusual words. The IPython notebook `build_proper_names_list.ipynb` illustrates how this file was made (`build_proper_names_list.py` works too). As output, `proper_names.txt` contains 40,683 unique, alphabetized words.

# Important notes:

* This list contains some words that are not proper nouns, and is currently being hand-checked to remove these.  It is currently hand-checked to line 5000.
* Some processing artifacts remain in the text, esp forms w/ a trailing _ (underscore) character. These will be removed later via automatic processing.
* Similarly, there are a number of doublets as a result of a lexeme + underscore + additional lexeme; e.g., 'Alexandro' vs 'Alexandro_erat'.
* A certain number of forms with attached clitics (e.g., -que, -ve) are present in the corpus; the host lexemes of these clitics are often doublets of non-cliticized lexemes.
* A number of apparent abbreviations have been left intact; e.g., 'Achil'.
* There is a certain amount of orthographic doubling as the result of u/v or i/j spellings; e.g., 'Achivis' vs. 'Achiuis', or '-que' vs '-qve'.  Similarly, in Greek words there are a number of doublets from variant y/u spellings; e.g., 'Amphitruone' vs. 'Amphitryone'.


# License
Copyright (c) 2014 Kyle P. Johnson, under the MIT License. See 'LICENSE' for details.
