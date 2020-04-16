

*Load the JSON 'a_movie.json' into the variable json_data within the context provided by the with statement. To do so, use the function json.load() within the context manager.
*Use a for loop to print all key-value pairs in the dictionary json_data. Recall that you can access a value in a dictionary using the syntax: dictionary[key].



# Load JSON: json_data
with open("a_movie.json") as json_file:
    json_data = json.load(json_file)

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])


API Requests:
    

#Import the requests package.
#Assign to the variable url the URL of interest in order to query 'http://www.omdbapi.com' for the data corresponding to the movie The Social Network.
#The query string should have two arguments: apikey=72bc447a and t=the+social+network. You can combine them as follows: apikey=72bc447a&t=the+social+network.
#Print the text of the response object r by using its text attribute and passing the result to the print() function.

# Import requests package
import requests

# Assign URL to variable: url
url= 'http://www.omdbapi.com/?apikey=72bc447a&t=the+social+network'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Print the text of the response
print(r.text)



JSON from web to python:
    

Pass the variable url to the requests.get() function in order to send the relevant request and catch the response, assigning the resultant response message to the variable r.
Apply the json() method to the response object r and store the resulting dictionary in the variable json_data.
Hit Submit Answer to print the key-value pairs of the dictionary json_data to the shell.

# Import package
import requests

# Assign URL to variable: url
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=social+network'

# Package the request, send the request and catch the response: r
r=requests.get(url)

# Decode the JSON data into a dictionary: json_data

json_data= r.json()
# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])



Checking out the Wikipedia API:
    

#Assign the relevant URL to the variable url.
#Apply the json() method to the response object r and store the resulting dictionary in the variable json_data.
#The variable pizza_extract holds the HTML of an extract from Wikipedia's Pizza page as a string; use the function print() to print this string to the shell.

# Import package
import requests

# Assign URL to variable: url
url= "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza"

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data= r.json()

# Print the Wikipedia page extract
pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)






























