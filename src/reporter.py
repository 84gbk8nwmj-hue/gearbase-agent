import os
from datetime import datetime
from typing import List, Dict

def format_report(data: List[Dict]) -> str:
    """収集・生成したデータをMarkdown形式にフォーマットする"""
    today = datetime.now().strftime("%Y-%m-%d")
    report = f"# GearBase日報 ({today})\n\n"
    
    current_theme = ""
    for item in data:
        if item["theme"] != current_theme:
            current_theme = item["theme"]
            report += f"## {current_theme}\n\n"
        
        report += f"### {item['title']}\n"
        report += f"- URL: {item['link']}\n\n"
        report += f"{item['ai_output']}\n\n"
        report += "---\n\n"
    
    return report

def save_report(content: str, reports_dir: str):
    """レポートをファイルに保存する"""
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)
    
    today = datetime.now().strftime("%Y-%m-%d")
    file_path = os.path.join(reports_dir, f"{today}.md")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    return file_path
