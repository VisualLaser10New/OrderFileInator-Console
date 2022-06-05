# OrderFileInator-Console
Handles and sorts files by extension

## Description
This script, written in python, can manages files in a folder and sort them by extension.
The program operates by copying and pasting files in properly folders.

## Args
- -r: Recursive mode, foreach folder enter and manage that files too.
- -d: Delete files after copy.
- -c: Force to create folder where copy the files. If they already exist, it replaces them.
- -s: Replaces files that already exist in destination folders.
- -f: The path of folder from which to retrieve the files.
- -b: Next you must insert a number in byte. This excludes files bigger than the number.

## Usage
An example is: <br>
``OrderFileInator.py -c -b 1000000 -f ..\``
