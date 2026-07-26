#!/usr/bin/env python3
"""DramaLex · retrieve_subtitles.py — agent 检索字幕来源后的一键解析 + 校验（在你合法授权范围内使用）

字幕来源与法律边界（务必读 references/SUBTITLE_LEGAL.md）：
  - 本脚本**不**内建任何字幕爬虫；它只负责把 **agent 已用 WebSearch 自主检索、
    并核对过准确性**的字幕来源（.srt/.vtt，或常见的 .zip/.gz 归档）**检索到位**，
    解析成 subtitle.json，并做基本校验。
  - 现实字幕多为 .zip/.gz 归档，agent 会**自动解压**取其中第一个字幕文件，
    全程不需要你手动解压或粘贴直链——agent 自己检索、自己核对、自己把字幕获取到位、自己解压。
  - 运行时会**自动打印一份法律免责声明**（说明本工具仅协助你检索定位字幕，
    字幕仅供个人非商业学习使用），属说明式提示，不拦截、不阻塞。

用法（由 agent 直接调用，你无需参与找直链）：
  # 直链（含归档自动解压）：
  python retrieve_subtitles.py --url "https://tvsubs.net/files/House.of.Cards.S01E01.WEBRip.NTb.en.zip" \
      --title "House of Cards" --year 2013 --episode "S01E01" \
      --known-lines known.txt --output subtitle.srt --parse-out subtitle.json
  # 也可直接吃本地已检索到的文件（--file）：
  python retrieve_subtitles.py --file "House.of.Cards.S01E01.WEBRip.NTb.en.srt" \
      --title "House of Cards" --year 2013 --episode "S01E01" --parse-out subtitle.json
  # 校验：会统计行数，并尝试在字幕中匹配 known-lines（逐行子串），给出命中率，确认没找错版本。
"""
import argparse, json, os, re, sys, shutil, zipfile, gzip

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import parse_subtitles as ps

_SUB_EXTS = ('.srt', '.vtt', '.ass', '.ssa', '.sub')

def _is_archive(path):
    p = path.lower()
    return p.endswith('.zip') or p.endswith('.gz') or p.endswith('.tgz')

def _extract_archive(archive_path, out_dir):
    """解压 .zip/.gz，返回内部第一个字幕文件路径；非归档则原样返回。"""
    low = archive_path.lower()
    if low.endswith('.zip'):
        with zipfile.ZipFile(archive_path) as z:
            names = [n for n in z.namelist() if n.lower().endswith(_SUB_EXTS) and not n.endswith('/')]
            if not names:
                raise RuntimeError("zip 内未找到字幕文件")
            # 优先英文/无 HI 标识的 .srt
            names.sort(key=lambda n: (0 if n.lower().endswith('.srt') else 1,
                                      1 if re.search(r'\.hi\.|\.hi_|hearing', n, re.I) else 0))
            target = names[0]
            dest = os.path.join(out_dir, os.path.basename(target))
            with z.open(target) as src, open(dest, 'wb') as f:
                shutil.copyfileobj(src, f)
            return dest
    if low.endswith('.gz') or low.endswith('.tgz'):
        dest = os.path.join(out_dir, os.path.basename(archive_path)[:-3])
        if dest.lower().endswith('.tgz'):
            dest = dest[:-4] + '.srt'
        with gzip.open(archive_path, 'rb') as src, open(dest, 'wb') as f:
            shutil.copyfileobj(src, f)
        return dest
    return archive_path

def fetch_subtitle(url_or_path, out_dir):
    """把直链或本地文件归一化为一个 .srt/.vtt 路径，自动获取+解压。
    返回最终字幕文件路径；失败抛异常。"""
    os.makedirs(out_dir, exist_ok=True)
    # 本地文件（绝对/相对路径或 file://）
    if url_or_path.startswith('file://'):
        url_or_path = url_or_path[len('file://'):]
    is_remote = url_or_path.lower().startswith(('http://', 'https://'))
    if not is_remote:
        if not os.path.exists(url_or_path):
            raise FileNotFoundError(f"本地字幕不存在: {url_or_path}")
        archive = url_or_path
    else:
        import urllib.request
        # 远程：下载到 out_dir，保留原名
        fname = os.path.basename(url_or_path.split('?')[0]) or 'subtitle.bin'
        archive = os.path.join(out_dir, fname)
        req = urllib.request.Request(url_or_path, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=60) as r, open(archive, 'wb') as f:
            shutil.copyfileobj(r, f)
        if os.path.getsize(archive) == 0:
            raise RuntimeError("下载到 0 字节，直链可能失效或被拦截")
    # 解压（若是归档）
    if _is_archive(archive):
        sub = _extract_archive(archive, out_dir)
    else:
        sub = archive
    if not os.path.exists(sub) or os.path.getsize(sub) == 0:
        raise RuntimeError("未得到有效字幕文件")
    return sub

# 兼容旧调用：直接获取（不带解压），保留以便脚本被单独使用
def download(url, out_path):
    import urllib.request
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=30) as r, open(out_path, 'wb') as f:
            f.write(r.read())
        return os.path.exists(out_path) and os.path.getsize(out_path) > 0
    except Exception as e:
        print(f"下载失败: {e}", file=sys.stderr)
        return False

def parse_to_json(srt_path, json_path):
    """用 parse_subtitles 的解析器把 .srt/.vtt 转成 subtitle.json。"""
    raw = open(srt_path, encoding='utf-8', errors='ignore').read()
    ext = os.path.splitext(srt_path)[1].lower()
    if ext == '.srt':
        lines = ps.parse_srt(raw)
    elif ext == '.vtt':
        lines = ps.parse_vtt(raw)
    else:
        lines = [{"time": "", "text": ps.clean_text(l)} for l in raw.split('\n') if l.strip()]
    for ln in lines:
        sp, tx = ps.detect_speaker(ln['text'])
        ln['speaker'], ln['text'] = sp, tx
    out = {"episode": os.path.splitext(os.path.basename(srt_path))[0], "lines": lines}
    json.dump(out, open(json_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    return lines

def verify(segs, title=None, year=None, known_lines=None):
    """基本校验：行数 + 已知台词命中率。"""
    n = len(segs)
    rep = {"lines": n, "title": title, "year": year, "known_hit": None, "known_total": 0}
    if known_lines:
        hits = 0
        total = 0
        norm = lambda s: re.sub(r"[^a-z0-9 ]", "", (s or '').lower()).strip()
        blob = " \n ".join(norm(s.get('text', '')) for s in segs)
        for kl in known_lines:
            kl = kl.strip()
            if not kl:
                continue
            total += 1
            if norm(kl)[:40] in blob:   # 取前 40 字符做宽松匹配
                hits += 1
        rep["known_total"] = total
        rep["known_hit"] = hits
        if total and hits == 0:
            rep["warn"] = "⚠️ 已知台词 0 命中：可能是错误版本/语言/季数，请核对后再用。"
        elif total:
            rep["ok"] = f"✅ 已知台词命中 {hits}/{total}，版本大概率正确。"
    return rep

def main():
    ap = argparse.ArgumentParser(description="DramaLex 字幕检索 + 解析 + 校验（agent 协助检索到位）")
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument('--url', default=None, help='字幕来源直链（.srt/.vtt/.zip/.gz），由 agent 自主检索并核对准确性后传入')
    src.add_argument('--file', default=None, help='本地字幕路径（.srt/.vtt/.zip/.gz），agent 已检索到本地时直接用')
    ap.add_argument('--title', default=None, help='片名（用于校验报告）')
    ap.add_argument('--year', default=None, help='年份')
    ap.add_argument('--episode', default=None, help='集数，如 S01E01')
    ap.add_argument('--known-lines', default=None, help='已知台词文件（每行一句），用于核对版本正确')
    ap.add_argument('--output', default='subtitle.srt', help='最终输出的 .srt 路径（解压后归一成此名）')
    ap.add_argument('--parse-out', default='subtitle.json', help='解析后的 subtitle.json 路径')
    args = ap.parse_args()

    print("⚖️ 法律免责声明：本工具仅协助你从互联网公开渠道**检索并定位**字幕资源；"
          "字幕来源于公开渠道，仅供个人非商业学习使用。"
          "DramaLex 不存储、不托管、不外传字幕，亦不对来源站点内容主张任何权利。")

    src_arg = args.url or args.file
    print(f"来源：{src_arg}")
    work_tmp = os.path.join(os.path.dirname(os.path.abspath(args.output)) or '.', '.retrieve_tmp')
    try:
        srt_path = fetch_subtitle(src_arg, work_tmp)
    except Exception as e:
        print(f"获取字幕失败: {e}", file=sys.stderr)
        return 2
    # 归一成 --output 名（方便后续 prepare 引用）
    if os.path.abspath(srt_path) != os.path.abspath(args.output):
        shutil.copyfile(srt_path, args.output)
    else:
        args.output = srt_path
    print(f"已就绪 -> {args.output}")
    # 解析
    try:
        segs = parse_to_json(args.output, args.parse_out)
    except Exception as e:
        print(f"解析失败: {e}", file=sys.stderr); return 3
    # 校验
    known = None
    if args.known_lines and os.path.exists(args.known_lines):
        known = open(args.known_lines, encoding='utf-8').read().splitlines()
    rep = verify(segs or [], args.title, args.year, known)
    print("\n📋 校验报告：")
    print(f"  行数：{rep['lines']}")
    if rep.get('known_total'):
        print(f"  已知台词命中：{rep['known_hit']}/{rep['known_total']}")
    if rep.get('ok'):
        print(" ", rep['ok'])
    if rep.get('warn'):
        print(" ", rep['warn'])
    print(f"\n下一步：python scripts/run_episode.py prepare --subtitle {args.parse_out} --work-dir .")
    return 0

if __name__ == '__main__':
    sys.exit(main())
