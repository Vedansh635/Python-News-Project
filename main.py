# This program is used to fetch the news from NewsAPI.org and print the titles and the descriptions of the news
# The user can input the topic of the news they want to see and the number of headlines they want to see
import requests , json
# Get the topic of the news from the user , try to give valid news topic otherwise it will not work
newstopic = input('What type of news you want to see? ')

# Construct the url to fetch the news from the API , Note: If program not working try changing the date to current date in API Key or change the API key from `NewsAPI.org`
url = f'https://newsapi.org/v2/everything?q={newstopic}=2024-09-26&sortBy=publishedAt&apiKey=e4e94f481f19476db4224a4a633faa14'

# Send a GET request to the API and get the response
response = requests.get(url)

# Load the JSON data from the response
news = json.loads(response.text)

# Get the number of headlines the user wants to see
howmuchnews = int(input('How much headlines you want to see? '))

# Initialize a counter to count the number of headlines
count = 1

# Loop through the news and print the title and the description of each news
for article in news['articles']:
    # Break the loop if the number of headlines is more than the user wants to see
    if count>howmuchnews:
        break
    # Print the title and the description of the news
    print(f'{count}.',article['title'])
    print(article['description'] , end='\n\n')
    # Increment the counter
    count+=1
