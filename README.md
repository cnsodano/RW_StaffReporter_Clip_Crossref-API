## Code to reproduce the Crossref API analyses used as evidence in my Retraction Watch staff reporter application
Important to keep in mind that this code is rudimentary, was drafted quickly, and consequently is not robustly unit-tested. Prior to submission for publication the code would be updated and robustly tested. 

## Interactive link for checking bulk-upload events
You can drag this [link](javascript%3Avar%20url%20%3D%20%60https%3A%2F%2Fapi.crossref.org%2Fjournals%2F%24%7Bprompt(%22insert%20ISSN%20(ANVI%3A1092-910X%2C%20hijacked%20RLJ%3A2313-7851)%22)%7D%2Fworks%3Ffilter%3Dfrom-deposit-date%3A%24%7Bprompt(%22get%20records%20from%20date%201%20(yyyy-mm-dd)%22)%7D%2Cuntil-deposit-date%3A%24%7Bprompt(%22get%20records%20UNTIL%20date%202%20(yyyy-mm-dd)%22)%7D%26rows%3D0%60%3Bwindow.location.href%20%3D%20url%3B) to your bookmarks bar. Keep in mind it requires javascript and pop-ups to be allowed, and it is generally never a good idea to run javascript in your browser written by a source you don't trust. This will, however, skip over the need to use the code to verify the claims made in table 1 of clip 2. 

## Disclaimer
If you are not a member of Retraction Watch and you have stumbled upon this code, do not take make any hasty assumptions about the author whose publications are being investigated in this codebase without reading my article, as research misconduct is a very weighty claim and accordingly requires strong and reliable evidence; this cannot be considered sufficient
