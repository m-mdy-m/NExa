import requests
from urllib.parse import parse_qs, urlsplit
from termcolor import colored
from devto.parser import DevToHTMLParser
from utils import format_time,display_articles
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
        response=''
        search_query = path.split("?")[-1]
        print('search_query:', search_query)
        print('base_url',base_url)
        print('url',url)
        query_params = {}
        if search_query.startswith("q=") or search_query.startswith("utf8"):
            for param in search_query.split("&"):
                key, value = param.split("=")
                query_params[key] = value
            query_params.setdefault("sort_by", "published_at")
            query_params.setdefault("sort_direction", "desc")
            
            print('Query Parameters:', query_params)
            # Fetch articles with properly constructed query parameters
            response = requests.get(f"{base_url}/search", timeout=10, params=query_params)
        else:
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

if __name__ == "__main__":
    fetch_articles()