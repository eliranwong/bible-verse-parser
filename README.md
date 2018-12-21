# bible-verse-parser
A python parser to parse bible verse references from a text.

Feature:
1. Search for verse references from a text and add taggings programatically
2. Support books of canon and apocrypha
3. Support taggings of chains of refernces, e.g. Rom 1:2, 3, 5, 8; 9:2, 10
4. Support books of one chapter only, like Obadiah, Philemon, 2John, 3John, Jude, etc.
5. Support standardisation of book abbreviations and verse reference format.

Main file: bible-verse-parser.py

Usage: python bible-verse-parser.py

Prompting question (1) "Enter filename here: "
Enter the filename of the file you want to parse.

Prompting question (2) "Do you want to standardise all references [YES/NO]? "
Enter YES if you want to standardise all verse references with SBL-style-abbreviations and common format like Gen 2:4; Deut 6:4, etc.
Any answers other than "YES" skip the standarisation.

For example:
