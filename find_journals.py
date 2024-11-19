""" A naive script to pull each unique container-title (journal title) from all works published by a given member in 
Crossref. Heavily relies on starter code written by habanero package's author Scott Campbell here: https://github.com/sckott/habanero/tree/main.
Scott Campbell's website: https://scottchamberlain.info/


Script written by Christian Sodano on 11/19/2024 with python version 3.11.0 and habanero version 1.2.6. All links accessed at this date. 

For help, visit the habanero docs here:https://habanero.readthedocs.io/en/stable/modules/crossref.html or contact me at cnsodano@gmail.com"""



from habanero import Crossref


cr = Crossref()  # Instantiate the Crossref() object, see https://habanero.readthedocs.io/en/stable/modules/crossref.html docs for the class definition
                 # Or, https://github.com/sckott/habanero/blob/main/habanero/crossref/crossref.py line 13
Crossref(base_url = "https://api.crossref.org/")  # Set base URL for API calls to be Crossref's

## If you own one, set an api key 
# Crossref(api_key = "123456")

## Set a mailto address to get into the "polite pool", more details @ https://github.com/CrossRef/rest-api-doc#good-manners--more-reliable-service under "Etiquette" header
Crossref(mailto = "csodano@unc.edu")  # Replace with your email address

## Set an additional user-agent string, more details @ https://github.com/CrossRef/rest-api-doc#good-manners--more-reliable-service under "Etiquette" header
# Crossref(ua_string = "foo bar")  # Replace "foo bar"


CROSSREF_MEMBER_ID: int = 34126;  # Set this to be the member ID you are investigating. 
PREFIX: str = None;  # If you don't know the member ID, replace None with the prefix (wrappde in "") and uncomment the next 
                     # five lines to print out the member ID
# member_ID = cr.prefixes(ids="10.18137")["message"]["member"]
# member_ID = member_ID.split("http://id.crossref.org/member/")[1]
# print(member_ID)
# breakpoint()
## TODO set CROSSREF_MEMBER_ID above to the member_ID value printed out 



def return_results(res):
    print(sum([ len(z['message']['items']) for z in res ]))  # Confirming the # of documents published by member in Crossref's system
    items = [ z['message']['items'] for z in res ]  # Extracting only the document informaiton
    items = [ item for sublist in items for item in sublist ]  # Extracting only the document information
    dict_containers  = {};  # Initializing dictionary to carry unique journal titles
    ct_empty = 0;  # Initializing count of failed attempts to retrieve journal title of work
    for item in items:
        """For each work, check the container-title, if it's accessible and not already seen, add it to the dictionary,
        if it's accessible and already seen, increment the count in the dictionary, and if it's not accessible then increment
        the count of nonaccessible works."""
        if 'container-title' in item:
            dict_containers[item["container-title"][0]] = dict_containers.get(item["container-title"][0],0) + 1;
        else:
            ct_empty +=1;
            #breakpoint()  # Optional to look at each empty work to try to understand why empty
    return dict_containers, ct_empty


res = cr.members(ids=CROSSREF_MEMBER_ID, works=True, select="container-title", cursor ="*", progress_bar = True)
journals, ct_empty = return_results(res)

# Pretty printing results with help from: https://www.geeksforgeeks.org/python-program-to-print-the-dictionary-in-table-format/
# Print the names of the columns
print("{:<10} {:<10} {:<10}".format('JOURNAL NAME',"||", 'NUM OF WORKS FOUND '))
# Print each data item
for key in journals:
    print("{:<10} {:<10}".format(key, journals[key]))
print("Number of failed journal-lookups:" + str(ct_empty))
breakpoint()