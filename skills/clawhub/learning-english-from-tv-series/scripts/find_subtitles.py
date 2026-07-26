#!/usr/bin/env python3
"""DramaLex · find_subtitles.py — 合法字幕「检索入口」（不爬、不托管、不下载）

设计原则（规避法律风险）：
- 本脚本【不】内建任何受版权保护的字幕爬取逻辑，只生成「公开来源」的检索链接。
- 真正获取字幕走来源直链（fetch_subtitles.py --url），由 agent 自主检索到位。
- Agent 也可直接用自身的 WebSearch 能力去定位字幕，但同样遵循下方「使用提示」。

合法来源优先级（公开渠道，个人非商业学习）：
  1) 官方平台：用户已订阅/购买的流媒体（Netflix/Disney+/Apple TV 等），用其官方字幕导出方式；
  2) OpenSubtitles：用户自建账号、遵守其 ToS（很多字幕由用户贡献，限个人使用）；
  3) 公有领域影片：archive.org 等可自由再分发的字幕；
  4) 用户自有光盘/媒体提取的字幕。

⚠️ 使用提示（agent 会说明）：在把任何链接交给用户之前，agent 会说明字幕来源于互联网公开渠道、仅供个人非商业学习使用，
纯标准库。
"""
import argparse, json, urllib.parse, sys

LEGAL_GATE = (
    "⚖️ 使用提示：字幕来源于互联网公开渠道，仅供个人非商业学习使用。\n"
    "   请通过合法渠道观看正片，以获得原速听力（弱读、连读、语调）。"
)


def build_links(title, year=None, lang='eng'):
    q = title
    if year:
        q += f" {year}"
    enc = urllib.parse.quote_plus(q)
    links = {
        "OpenSubtitles（自建账号·遵守 ToS）":
            f"https://www.opensubtitles.org/en/search2/sublanguageid-{lang}/moviename-{enc}",
        "Subscene（社区字幕）":
            f"https://subscene.com/subtitles/link?query={enc}",
        "archive.org（优先找公有领域影片字幕）":
            f"https://archive.org/search?query={enc}+subtitles",
        "通用检索（请自行甄别来源合法性）":
            f"https://www.google.com/search?q={enc}+subtitles",
    }
    return links


def main():
    ap = argparse.ArgumentParser(description="生成合法字幕来源检索链接（不下载）")
    ap.add_argument('--title', required=True, help='影片/剧集名，如 "The Pursuit of Happyness"')
    ap.add_argument('--year', default=None, help='年份，可选')
    ap.add_argument('--lang', default='eng', help='字幕语言代码，默认 eng')
    ap.add_argument('--json', action='store_true', help='输出 JSON')
    args = ap.parse_args()

    links = build_links(args.title, args.year, args.lang)
    if args.json:
        print(json.dumps({"title": args.title, "links": links}, ensure_ascii=False, indent=2))
    else:
        print(f"🔎 《{args.title}》合法字幕检索入口：")
        for name, url in links.items():
            print(f"  · {name}\n    {url}")
        print()
    print(LEGAL_GATE.format(title=args.title))
    print("下一步：agent 用 fetch_subtitles.py --url <直链> 自主检索获取。")


if __name__ == '__main__':
    main()
