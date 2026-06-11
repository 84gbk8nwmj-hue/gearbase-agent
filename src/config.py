import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# 収集対象のテーマとRSSフィードURL
RSS_FEEDS = {
    "AI": [
        "https://openai.com/news/rss.xml",
        "https://deepmind.google/blog/rss.xml"
    ],
    "Gemini": [
        "https://blog.google/products/gemini/rss/"
    ],
    "Flutter": [
        "https://medium.com/feed/flutter",
        "https://flutterdev.com/rss/"
    ],
    "個人開発": [
        "https://zenn.dev/topics/%E5%80%8B%E4%BA%BA%E9%96%8B%E7%99%BA/feed"
    ],
    "キャンプ": [
        "https://camphack.nap-camp.com/feed"
    ]
}

# レポート保存設定
REPORTS_DIR = "reports"

# Gemini設定
GEMINI_MODEL_NAME = "gemini-3-flash-preview"
