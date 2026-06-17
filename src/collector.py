import feedparser
import trafilatura
from typing import List, Dict

def fetch_latest_articles(rss_url: str, limit: int = 1) -> List[Dict[str, str]]:
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

def collect_all_data(rss_feeds: Dict[str, List[str]], total_limit: int = 5) -> List[Dict]:
    """全テーマのデータを収集する（全体の件数を制限）"""
    results = []
    all_candidates = []
    
    for theme, urls in rss_feeds.items():
        for url in urls:
            articles = fetch_latest_articles(url, limit=1)
            for article in articles:
                all_candidates.append({
                    "theme": theme,
                    "title": article["title"],
                    "link": article["link"]
                })
    
    # 候補の中から上限数だけ抽出して本文を取得
    for item in all_candidates[:total_limit]:
        content = extract_content(item["link"])
        if content:
            results.append({
                "theme": item["theme"],
                "title": item["title"],
                "link": item["link"],
                "content": content
            })
    return results
