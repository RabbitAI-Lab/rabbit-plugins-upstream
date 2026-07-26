#!/usr/bin/env python3
"""DramaLex · fetch_subtitles.py（用户直链获取 · 法律闸门）

说明（诚实 + 风险规避）：
- 本脚本【不】内建任何受版权保护的字幕爬取/聚合获取逻辑。
- 仅【在用户明确授权下】获取用户提供的字幕直链（--url），或用户自有源端点（DRAMALEX_SUBTITLE_URL）。
- 获取前 agent 会提示字幕仅供个人非商业学习使用（见 references/SUBTITLE_LEGAL.md）。
- 想找字幕？先用 find_subtitles.py（生成合法来源检索链接），或让 agent 用 WebSearch 定位；
  定位到后由用户提供直链，再回到本脚本获取。

纯标准库（urllib）。Agent 中立。
"""
import argparse, os, sys, urllib.request, urllib.error

def download(url, out_path):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=20) as r, open(out_path, 'wb') as f:
            f.write(r.read())
        return os.path.exists(out_path) and os.path.getsize(out_path) > 0
    except Exception as e:
        print(f"获取失败: {e}", file=sys.stderr)
        return False

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--episode', help='剧集代号，如 "Friends S01E01"')
    ap.add_argument('--url', help='直接字幕文件 URL（.srt/.vtt）')
    ap.add_argument('--output', default='subtitle.auto.srt')
    args = ap.parse_args()

    url = args.url or os.environ.get('DRAMALEX_SUBTITLE_URL')
    if url:
        print(f"尝试从 URL 获取字幕: {url}")
        if download(url, args.output):
            print(f"已获取字幕 -> {args.output}")
            return
        print("获取未成功，请改用手动上传/粘贴。", file=sys.stderr)

    print("=" * 60)
    print("自动抓取不可用（未提供字幕 URL，且本技能不内建受版权保护的字幕爬取）。")
    print("合法路径（字幕仅供个人非商业学习使用）：")
    print("  0) 用 find_subtitles.py 生成合法来源检索链接 → 把直链给我；")
    print("  1) 把本集的 .srt / .vtt 文件发给我（上传）；")
    print("  2) 直接粘贴本集台词文本；")
    print("  3) 提供字幕直链 URL（--url），或设环境变量 DRAMALEX_SUBTITLE_URL。")
    print("=" * 60)
    sys.exit(2)

if __name__ == '__main__':
    main()
