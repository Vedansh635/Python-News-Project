# Project-Description

This Python program fetches news articles from `NewsAPI.org` based on a user-input topic and displays the titles and descriptions of the articles. The user can specify the number of headlines they want to see.

# How it works
1. The program prompts the user to input a topic of interest (e.g., "technology", "sports", etc.).<br>
2. It constructs a URL to fetch news articles from `NewsAPI.org` using the input topic and a specific date (currently set to September 26, 2024).<br>
3. The program sends a GET request to the API and loads the JSON response.<br>
4. The user is then prompted to input the number of headlines they want to see.<br>
5. The program loops through the news articles and prints the title and description of each article, up to the specified number of headlines.<br>

# Features
- User-input topic and number of headlines<br>
- Fetches news articles from `NewsAPI.org`<br>
- Displays title and description of each article<br>
- Limits the number of headlines displayed based on user input<br>

# Requirements
- Python 3.x<br>
- `requests` and `json` libraries<br>
- `NewsAPI.org` API key (replace the existing key with your own)<br>

# Note
- Make sure to replace the API key with your own from `NewsAPI.org`.<br>
- If the program doesn't work, try changing the date in the API URL to the current date or obtain a new API key.
