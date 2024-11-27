import requests
from urllib.parse import parse_qs, urlsplit
from termcolor import colored
from devto.parser import DevToHTMLParser
from utils import format_time, display_articles
from menu import get_user_choice

def fetch_articles():
    """
    Fetches articles from the dev.to website based on user input and displays the top 5.
    """
    path = get_user_choice()
    base_url = "https://dev.to"
    url = base_url + path
    print(colored(f"\nFetching articles from: {url}\n", "cyan", attrs=["bold"]))
    try:
        response = requests.get(url,timeout=10)
        if response.status_code == 200:
            print(colored(">>> Fetch successful! Parsing articles...\n", "green", attrs=["bold"]))
            parser = DevToHTMLParser()
            parser.feed(response.text)
            parser.close()
            if  parser.articles:
                display_articles(parser.articles)
            else:
                print(colored("No articles found or content might be JavaScript-rendered.", "red"))
        else:
            print(colored(f"Failed to fetch articles. Status code: {response.status_code}", "red"))
    except requests.exceptions.RequestException as e:
        print(colored(f"An error occurred: {e}", "red"))