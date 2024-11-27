from termcolor import colored
from devto.search import construct_search_url
def get_user_choice():
    """
    Displays an interactive menu to guide the user in selecting a category or tag.
    Provides clear instructions and formal presentation.
    
    Returns:
        (str): The URL path corresponding to the user's choice.
    """
    print(colored("""
===========================================================
             WELCOME TO THE DEV.TO ARTICLE FETCHER
===========================================================
    Stay informed with the latest, trending, and curated 
    articles from Dev.to. Select your preferred category 
    or tag to get started!
-----------------------------------------------------------
""", "blue", attrs=["bold"]))

    print(colored("HOW TO USE THIS MENU:", "magenta", attrs=["bold"]))
    print("""
1. Simply type the number or keyword corresponding to your choice.
2. For "Articles by Tag", enter the tag starting with # (e.g., #webdev).
3. For Top Articles, you will be prompted to choose a time frame.
-----------------------------------------------------------
""")

    print(colored("MAIN MENU:", "cyan", attrs=["bold"]))
    print("""
    1. Latest Articles - Get the most recent articles.
    2. Discover Articles - Explore curated selections.
    3. Top Articles - Access the most popular posts by time frame.
    4. Articles by Tag - Focus on topics of interest (e.g., #webdev).
""")

    user_choice = input(colored("Enter your choice (1/2/3/4/5): ", "yellow")).strip().lower()

    if user_choice == "1" or user_choice == "latest":
        print(colored("\n--- You've chosen: Latest Articles ---\n", "green", attrs=["bold"]))
        return "/latest"

    elif user_choice == "2" or user_choice == "discover":
        print(colored("\n--- You've chosen: Discover Articles ---\n", "green", attrs=["bold"]))
        return "/discover"

    elif user_choice == "3" or user_choice == "top":
        print(colored("""
--- Top Articles ---
Select a time frame for top articles:
    a. Week - See what's trending this week.
    b. Month - Check out the most popular posts this month.
    c. Year - Explore highlights from the past year.
    d. All Time - Access the best of all time.
""", "cyan"))
        time_frame = input(colored("Enter your choice (a/b/c/d): ", "yellow")).strip().lower()
        time_frames = {"a": "week", "b": "month", "c": "year", "d": "infinity"}
        choice = time_frames.get(time_frame, "week")
        print(colored(f"\n--- You've chosen: Top Articles ({choice.capitalize()}) ---\n", "green", attrs=["bold"]))
        return f"/top/{choice}"

    elif user_choice.startswith("#"):
        tag = user_choice.lstrip("#")
        print(colored(f"""
--- Articles for Tag: #{tag} ---
Choose a filter to refine your selection:
    1. Top of All Time - Discover timeless posts.
    2. Top of the Week - Focus on this week's highlights.
    3. Top of the Month - See the most discussed topics this month.
    4. Top of the Year - Reflect on the year's top content.
    5. Latest - Get the most recent articles for this tag.
""", "cyan"))
        tag_filter_choice = input(colored("Enter your choice (1/2/3/4/5): ", "yellow")).strip()
        filters = {
            "1": "top/infinity",
            "2": "top/week",
            "3": "top/month",
            "4": "top/year",
            "5": "latest"
        }
        tag_filter = filters.get(tag_filter_choice, "top/infinity")
        print(colored(f"\n--- You've chosen: #{tag} ({tag_filter.split('/')[-1].capitalize()}) ---\n", "green", attrs=["bold"]))
        return f"/t/{tag}/{tag_filter}"
    else:
        print(colored("\nInvalid input. Defaulting to: Latest Articles\n", "red", attrs=["bold"]))
        return "/latest"
