# Project-Description

This Python program fetches news articles from NewsAPI.org based on a user-input topic and displays the titles and descriptions of the articles. The user can specify the number of headlines they want to see.

# How it works
1. The program prompts the user to input a topic of interest (e.g., "technology", "sports", etc.).
2. It constructs a URL to fetch news articles from NewsAPI.org using the input topic and a specific date (currently set to September 26, 2024).
3. The program sends a GET request to the API and loads the JSON response.
4. The user is then prompted to input the number of headlines they want to see.
5. The program loops through the news articles and prints the title and description of each article, up to the specified number of headlines.

# Features
- User-input topic and number of headlines
- Fetches news articles from NewsAPI.org
- Displays title and description of each article
- Limits the number of headlines displayed based on user input

