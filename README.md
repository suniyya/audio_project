# hackathon-destroke
A repo to hold a small app that compares speech patterns from the same person, reading sentences used in the NIH Stroke Scale.

`main.py` contains the barebones UI
One can write two filenames to compare their speech content and speed, and play the two files. 

Based on whether there is a permissible level of variation (in our case, only variations in pauses are tolerated - word mismatches, words out of order are not), the test file is given a score that very roughly represents the likelihood of the sample coming from a patient undergoing a stroke.
