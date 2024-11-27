from html.parser import HTMLParser
class DevToHTMLParser(HTMLParser):
    """
    A custom HTML parser for extracting article data from the dev.to discover page.

    This class parses HTML content to extract the following details for each article:
      - Title
      - Link
      - Author
      - Post date and time
      - Tags (topics)

    Usage:
    - Feed the HTML content of the dev.to discover page to an instance of this class.
    - After parsing, the `articles` attribute will contain a list of dictionaries, 
      each representing an article with its associated data.
    """
    def __init__(self):
        super().__init__()
        self.articles = []
        self.current_article = {}
        self.current_tag = ''
        self.inside_tags = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'a' and 'class' in attrs and 'crayons-story__hidden-navigation-link' in attrs['class']:
            if self.current_article:
                self.articles.append(self.current_article)
            self.current_article = {'tags': []}
            self.current_article['link'] = attrs.get('href', '')
            self.current_tag = 'title'

      
        elif tag == 'a' and 'class' in attrs and 'crayons-story__secondary' in attrs['class']:
            self.current_tag = 'author'

      
        elif tag == 'a' and 'class' in attrs and 'crayons-tag' in attrs['class']:
            self.current_tag = 'tag'
            self.inside_tags = True

      
        elif tag == 'time' and 'datetime' in attrs:
            self.current_article['posted_at'] = attrs['datetime']

    def handle_endtag(self, tag):
        if tag == 'a':
            self.current_tag = ''
            self.inside_tags = False

    def handle_data(self, data):
        if self.current_tag == 'title':
          
            self.current_article['title'] = data.strip()
            self.current_tag = ''

        elif self.current_tag == 'author':
          
            self.current_article['author'] = data.strip()
            self.current_tag = ''

        elif self.current_tag == 'tag' and self.inside_tags:
          
            tag = data.strip()
            if tag and tag != "#":
                self.current_article['tags'].append(tag)
    def handle_entityref(self, name):
      
        self.handle_data(f"&{name};")
    def handle_charref(self, name):
      
        self.handle_data(chr(int(name)))
    def close(self):
      
        if self.current_article:
            self.articles.append(self.current_article)
        super().close()

