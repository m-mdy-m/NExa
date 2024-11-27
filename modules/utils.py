from datetime import datetime
from termcolor import colored
def format_time(posted_at):
    """
    Formats the ISO datetime string to a more user-friendly format.
    Args:
        posted_at (str): The ISO datetime string.
    Returns:
        str: Formatted datetime string.
    """
    try:
        dt = datetime.fromisoformat(posted_at.replace("Z", "+00:00"))
        return dt.strftime("%Y-%m-%d %H:%M:%S (UTC)")
    except ValueError:
        return "Invalid date"


def display_articles(articles):
    """
    Displays the top 5 articles from the provided list.
    """
    if articles:
        print(colored(f"--- Total Articles Found: {len(articles)} ---\n", "cyan", attrs=["bold"]))
         # Sort articles by posting time (most recent first)
        sorted_articles = sorted(
                articles,
                key=lambda x: x.get('posted_at', '1970-01-01T00:00:00Z'),
                reverse=True
        )
        top_5_articles = articles[:5]
        print(colored(">>> Here are the Top 5 Articles:\n", "magenta", attrs=["bold"]))
        for i, article in enumerate(top_5_articles, start=1):
            print(colored(f"== ARTICLE {i} ==", "yellow", attrs=["bold"]))
            print(f"{colored('Title:', 'cyan')} {article.get('title', 'No Title')}")
            print(f"{colored('Link:', 'cyan')} https://dev.to{article.get('link', 'No Link')}")
            print(f"{colored('Author:', 'cyan')} {article.get('author', 'Unknown')}")
            print(f"{colored('Posted At:', 'cyan')} {format_time(article.get('posted_at', 'Unknown'))}")
            tags = ', '.join(article.get('tags', []))
            print(f"{colored('Tags:', 'cyan')} {tags if tags else 'No Tags'}")
            print(colored("-" * 50, "green"))
    else:
        print(colored("No articles found. The HTML structure might have changed.", "red"))
