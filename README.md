## Code to reproduce the Crossref API analyses used as evidence in my Retraction Watch staff reporter application
Important to keep in mind that this code is rudimentary, was drafted quickly, and consequently is not robustly unit-tested. Prior to submission for publication the code would be updated and robustly tested. 

## Interactive link for checking bulk-upload events
You can add the following javascript as a bookmark to interactively verify the claims made in table 1 of clip 2. Keep in mind running it requires javascript and pop-ups to be allowed, and it is generally never a good idea to run javascript in your browser written by a source you don't trust. This will, however, skip over the need to use the code to verify these claims.
```   
javascript:var url = `https://api.crossref.org/journals/${prompt("insert ISSN (ANVI:1092-910X, hijacked RLJ: 2313-7851)")}/works?filter=from-deposit-date:${prompt("get records from date 1 (yyyy-mm-dd) (for RLJ, try 2023-06-17)")},until-deposit-date:${prompt("get records UNTIL date 2 (yyyy-mm-dd) (for RLJ, try 2023-06-18)")}&rows=0`;window.location.href = url;
```

## Disclaimer
If you are not a member of Retraction Watch and you have stumbled upon this code, do not take make any hasty assumptions about the author whose publications are being investigated in this codebase without reading my article, as research misconduct is a very weighty claim and accordingly requires strong and reliable evidence; this cannot be considered sufficient

## Note on csv
This is the result exporting via scopus all the citations an author has received that are indexed by scopus.  
