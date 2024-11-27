#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../modules')))

from __init__ import fetch_articles

def main():
    """
    Main entry point for the NExa application.
    Provides a CLI to fetch and display articles from dev.to.
    """
    print("Welcome to NExa - Dev.to Article Fetcher")

    try:
        fetch_articles()
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
