import os
import time

from .config import RSS_FEEDS, REPORTS_DIR
from .collector import collect_all_data
from .summarizer import summarize_content
from .reporter import format_report, output_report


def main():
    print("GearBase Agent 起動中...")

    # 1. プロンプトの読み込み
    prompt_path = os.path.join("prompts", "daily_prompt.md")
    with open(prompt_path, "r", encoding="utf-8") as f:
        prompt_template = f.read()

    # 2. データ収集（RSS + 本文抽出）
    print("情報収集を開始します...")
    raw_data = collect_all_data(RSS_FEEDS, total_limit=5)

    if not raw_data:
        print("記事が見つかりませんでした。")
        return

    # 3. AIによる要約・投稿文生成
    print(f"{len(raw_data)} 件の記事が見つかりました。要約を生成中...")

    processed_data = []

    for item in raw_data:
        print(f"処理中: {item['title']}")

        ai_output = summarize_content(
            item["content"],
            prompt_template
        )

        item["ai_output"] = ai_output
        processed_data.append(item)

        # Gemini Free API (5 RPM) 対策
        time.sleep(13)

    # 4. レポート生成
    print("レポートを生成しています...")
    report_content = format_report(processed_data)

    # 5. 出力
    # GitHub Actions → Actions Summary
    # ローカル実行 → reports/YYYY-MM-DD.md
    output_report(report_content, REPORTS_DIR)

    print("完了！")


if __name__ == "__main__":
    main()
