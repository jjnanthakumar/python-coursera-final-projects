import requests_with_caching
def get_movies_from_tastedive(moviename):
    baseurl = "https://tastedive.com/api/similar"
    movie_resp = requests_with_caching.get(baseurl, params ={"q":moviename,"type":"movies","limit":5})
    return movie_resp.json()
def extract_movie_titles(somedict):   
    return [d['Name'] for d in somedict['Similar']['Results']]
def get_related_titles(movie_list):
    li = []
    for movie in movie_list:
        li.extend(extract_movie_titles(get_movies_from_tastedive(movie)))
    return list(set(li))
    
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
print(get_related_titles(["Black Panther", "Captain Marvel"]))
# get_related_titles([])

