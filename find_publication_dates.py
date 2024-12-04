""" A naive script to analyze the publicate date distribution from all works published by a given member in 
Crossref. Allows one to analyze if there are heavy "dumps" of hundreds of articles on a single day, or unusual changes in 
publishing rate. Heavily relies on starter code written by habanero package's author Scott Campbell here: https://github.com/sckott/habanero/tree/main.
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

#CROSSREF_ISSN: str = "2313-7851" ## To check RLJ
CROSSREF_ISSN: str ="1092-910X" ## TODO set to the ISSN of the journal you are checking. 1092-910X is ANVI

def return_dates(res):
    print(sum([ len(z['message']['items']) for z in res ]))  # Confirming the # of documents published by member in Crossref's system
    items = [ z["message"]['items'] for z in res1] # Extracting only the document informaiton
    titles = [item["title"][0] for sublist in items for item in sublist] # Extracting titles informaiton
    issued_dates = [item["issued"]["date-parts"][0] for sublist in items for item in sublist ] # Extracting issued dates informaiton
    dates = [ item["deposited"]["date-parts"][0] for sublist in items for item in sublist ] # Extracting deposited dates informaiton
    day_months = [ str(item[1])+"/"+str(item[2])+"/"+str(item[0]) for item in dates]  # Sorry, American
    day_months_issued = [ str(item[1])+"/"+str(item[2])+"/"+str(item[0]) for item in issued_dates]  # Sorry, American
    dict_dates = {} # Init
    dict_dates_issued = {} # Init
    ct_empty = 0; # Init
    for date in day_months:
            if date != None:
                dict_dates[date] = dict_dates.get(date,0) + 1  # Increment count of works deposited on this date
            else:
                ct_empty +=1;
    for date in day_months_issued:
            if date != None:
                dict_dates_issued[date] = dict_dates_issued.get(date,0) + 1 # Increment count of works with "issued" date set to this date
            else:
                ct_empty +=1;
    ct_yr = {}
    for date in dict_dates_issued.keys():
        year = date[len(date)-4:];  # Last 4 digits=year
        ct_yr[year] = ct_yr.get(year,0) + dict_dates_issued[date]; 
    return set(day_months), set(day_months_issued), dict_dates, dict_dates_issued, ct_yr, ct_empty

res1 = cr.journals(CROSSREF_ISSN, works=True, order='desc', cursor="*", progress_bar = True )

unique_dates_deposited, unique_dates_issued, dates_deposited_dict, dates_issued_dict, ct_yr, ct_empty = return_dates(res1);
print(unique_dates_deposited);
print(unique_dates_issued)
print(dates_deposited_dict)
print(dates_issued_dict)
print(ct_yr)
print(ct_empty)
breakpoint()


