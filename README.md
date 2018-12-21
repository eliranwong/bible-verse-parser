# bible-verse-parser
A python parser to parse bible verse references from a text.

This was originally created to tag resources for building <a href="https://marvel.bible">https://marvel.bible</a>.<br>
The script is now modified for general use.

# Feature:
1. Search for verse references from text file(s)
2. Add taggings on verse references
3. Support books of bible canon and apocrypha
4. Support tagging on chains of refernces, e.g. Rom 1:2, 3, 5, 8; 9:2, 10
5. Support books of one chapter only, like Obadiah 2, Jude 3, 3John 4, etc.
6. Support chapter references [references without verse number specified], e.g. Gen 1, 3-4; 8, 9-10.
7. Support standardisation of book abbreviations and verse reference format.

# Main file: 
<a href="https://github.com/eliranwong/bible-verse-parser/blob/master/bible-verse-parser.py">bible-verse-parser.py</a>

# Usage:

Command line: python bible-verse-parser.py

Prompting question (1) "Enter filename here: "<br>
Enter the filename of the file you want to parse.

Prompting question (2) "Do you want to standardise all verse references [YES/NO]? "<br>
Enter YES if you want to standardise all verse references with SBL-style-abbreviations and common format like Gen 2:4; Deut 6:4, etc.<br>
Any answers other than "YES" skip the standarisation.

# A practical example:

Copy files "bible-verse-parser.py" and "dictionary-for-testing.txt" and put in the same folder<br>
(Remarks: "dictionary-for-testing.txt" is the Mounce Concise Greek-English Dictionary in plain text format)<br>
(bible-verse-parser.py is used here to add taggings for bible verse references.)<br>

Enter command in terminal: python bible-verse-parser.py<br>
"Enter filename here: " dictionary-for-testing.txt<br>
"Do you want to standardise all verse references [YES/NO]? " YES<br>
You can find the output file in the same folder named as "output_dictionary-for-testing.txt"<br>

# Credits of file "dictionary-for-testing.txt"

Source: <a href="https://github.com/billmounce/dictionary/blob/master/dictionary.txt">https://github.com/billmounce/dictionary/blob/master/dictionary.txt</a>

Attribution:<br>
Mounce Concise Greek-English Dictionary<br>
Copyright 1993 All Rights Reserved<br>
www.teknia.com/greek-dictionary
