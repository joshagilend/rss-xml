import xml.etree.ElementTree as ET
import requests

# Example RSS feed URL
RSS_FEED_URL = "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"

def fetch_rss_feed(url):
    """
    Fetch RSS feed data from a URL.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to fetch RSS feed.")
        return None

def parse_rss_feed(feed_data):
    """
    Parse the RSS feed XML and extract item titles and links.
    """
    items = []
    try:
        root = ET.fromstring(feed_data)
        for item in root.findall(".//item"):
            title = item.find("title").text
            link = item.find("link").text
            items.append((title, link))
    except ET.ParseError as e:
        print("Failed to parse RSS feed:", e)
    return items

def display_feed_items(items):
    """
    Display the RSS feed items in a readable format.
    """
    for idx, (title, link) in enumerate(items, start=1):
        print(f"{idx}. {title}\n   {link}\n")

def main():
    """
    Main function to fetch, parse, and display RSS feed items.
    """
    print("Fetching RSS feed...")
    feed_data = fetch_rss_feed(RSS_FEED_URL)
    if not feed_data:
        return
    
    print("Parsing RSS feed...")
    items = parse_rss_feed(feed_data)
    
    if items:
        print("\nFeed Items:\n")
        display_feed_items(items)
    else:
        print("No items found in the feed.")

if __name__ == "__main__":
    main()
