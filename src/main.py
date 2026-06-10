import os
from .config import RSS_FEEDS, REPORTS_DIR
from .collector import collect_all_data
from .summarizer import summarize_content
from .reporter import format_report, save_report

def main():
    print("GearBase Agent 起動中...")
    
    # 1. プロンプトの読み込み
    prompt_path = os.path.join("prompts", "daily_prompt.md")
    with open(prompt_path, "r", encoding="utf-8") as f:
        prompt_template = f.read()
    
    # 2. データ収集 (RSS + 本文抽出)
    print("情報収集を開始します...")
    raw_data = collect_all_data(RSS_FEEDS)
    
    # 3. AIによる要約・生成
    print(f"{len(raw_data)} 件の記事が見つかりました。要約を生成中...")
    processed_data = []
    for item in raw_data:
        print(f"処理中: {item['title']}")
        ai_output = summarize_content(item["content"], prompt_template)
        item["ai_output"] = ai_output
        processed_data.append(item)
    
    # 4. レポート生成・保存
    print("レポートを作成しています...")
    report_content = format_report(processed_data)
    file_path = save_report(report_content, REPORTS_DIR)
    
    print(f"完了! レポートが保存されました: {file_path}")

if __name__ == "__main__":
    main()
