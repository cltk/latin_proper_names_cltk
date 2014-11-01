# About
The file `proper_names.txt` contains a newline-delimited file which contains all of the words in the PHI5 which are likely proper names (persons, places, etc.). The value of this list is that, since everything is a noun, it may be used as a default POS tagger for these unusual words. The IPython notebook `build_proper_names_list.ipynb` illustrates how this file was made. As output, `proper_names.txt` contains 40,683 unique, alphabetized words.

Important note: This list contains some words that are not proper nouns. Its needs to be edited by a human to remove accidental inclusions.


# License
Copyright (c) 2014 Kyle P. Johnson, under the MIT License. See 'LICENSE' for details.