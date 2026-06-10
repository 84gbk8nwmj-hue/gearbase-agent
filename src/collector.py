import feedparser
import trafilatura
from typing import List, Dict

def fetch_latest_articles(rss_url: str, limit: int = 3) -> List[Dict[str, str]]:
    """RSSフィードから最新の記事を取得する"""
    feed = feedparser.parse(rss_url)
    articles = []
    
    for entry in feed.entries[:limit]:
        articles.append({
            "title": entry.title,
            "link": entry.link
        })
    
    return articles

def extract_content(url: str) -> str:
    """URLから本文テキストを抽出する"""
    downloaded = trafilatura.fetch_url(url)
    if downloaded:
        content = trafilatura.extract(downloaded)
        return content if content else ""
    return ""

def collect_all_data(rss_feeds: Dict[str, List[str]]) -> List[Dict]:
    """全テーマのデータを収集する"""
    results = []
    for theme, urls in rss_feeds.items():
        theme_results = []
        for url in urls:
            articles = fetch_latest_articles(url)
            for article in articles:
                content = extract_content(article["link"])
                if content:
                    theme_results.append({
                        "theme": theme,
                        "title": article["title"],
                        "link": article["link"],
                        "content": content
                    })
        results.extend(theme_results)
    return results
