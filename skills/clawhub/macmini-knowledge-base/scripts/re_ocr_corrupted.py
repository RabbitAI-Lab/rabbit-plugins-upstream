#!/usr/bin/env python3
"""
重新 OCR 已识别的乱码 PDF，覆盖 summaries/ 和 archives/

用法：
  python3 re_ocr_corrupted.py [--dry-run] [--max N]

行为：
1. 接收 PDF 路径列表（按乱码字符数排序的前 N 个）
2. 对每份跑 extract_pdf_text（自动 CMap 自检 + 强制 OCR）
3. 生成新 summary 写入 summaries/（新时间戳）
4. 把 archives/ 里所有对应 basename 的乱码版本覆盖
5. 报告每份结果（含路径、字数、是否成功）
"""
import os, sys, glob, re, time, json, shutil
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import extract_pdf_text, is_cmap_broken, PDFExtractError

KNOWLEDGE = os.path.expanduser('~/.openclaw/workspace/knowledge')
SUMMARIES = os.path.join(KNOWLEDGE, '.analysis/summaries')
ARCHIVES = os.path.join(KNOWLEDGE, '.analysis/summaries/archives')
TIMESTAMP = datetime.now().strftime('%Y%m%d_%H%M%S')


def find_corrupted_summaries():
    """扫描 archives/ 找出所有乱码 summary（已在 Step 1 用过的逻辑）"""
    files = glob.glob(f'{ARCHIVES}/*.summary.txt')
    bad = []
    for f in files:
        with open(f, encoding='utf-8', errors='replace') as fh:
            text = fh.read()
        pua = sum(1 for c in text if 0xE000 <= ord(c) <= 0xF8FF)
        cjk_ext = sum(1 for c in text if 0x20000 <= ord(c) <= 0x2EBEF)
        cjk_compat = sum(1 for c in text if 0xF900 <= ord(c) <= 0xFAFF)
        cid = text.count('(cid:')
        bad_count = pua + cjk_ext + cjk_compat + cid
        if bad_count > 0:
            bad.append({'path': f, 'bad_count': bad_count, 'text_len': len(text)})
    return sorted(bad, key=lambda x: -x['bad_count'])


def summary_to_pdf_basename(s_fname):
    """从 summary 文件名提取原 PDF 的 basename（不含扩展名）"""
    base = os.path.basename(s_fname)
    base = re.sub(r'^\d{8}_\d{6}_', '', base)
    base = re.sub(r'\.summary\.txt$', '', base)
    # 去掉扩展名（.pdf / .pptx 等），让 find_pdf_by_basename 自己加
    base = re.sub(r'\.(pdf|pptx|docx|doc|ppt)$', '', base, flags=re.IGNORECASE)
    return base


def find_pdf_by_basename(target_bn):
    """在 knowledge/ 下找对应 basename 的 PDF/PPTX/DOCX"""
    for ext in ['.pdf', '.pptx', '.docx', '.doc', '.ppt']:
        candidates = glob.glob(f'{KNOWLEDGE}/**/{target_bn}{ext}', recursive=True)
        if candidates:
            return candidates[0]
    return None


def re_ocr_one(pdf_path, dry_run=False):
    """对一份 PDF 重新 OCR，返回结果"""
    bn = os.path.basename(pdf_path)
    result = {
        'pdf_path': pdf_path,
        'basename': bn,
        'success': False,
        'new_text_len': 0,
        'summaries_updated': 0,
        'archives_updated': 0,
        'error': None,
        'elapsed': 0,
    }
    
    t0 = time.time()
    try:
        text = extract_pdf_text(pdf_path)
        result['new_text_len'] = len(text)
        result['success'] = True
        result['text_still_broken'] = is_cmap_broken(text)
    except PDFExtractError as e:
        result['error'] = f"PDFExtractError: {e.reason}"
        result['elapsed'] = time.time() - t0
        return result
    except Exception as e:
        result['error'] = f"{type(e).__name__}: {e}"
        result['elapsed'] = time.time() - t0
        return result
    
    result['elapsed'] = time.time() - t0
    
    if dry_run:
        return result
    
    # 1. 写入新的 summary 到 summaries/
    new_summary_path = f'{SUMMARIES}/{TIMESTAMP}_{bn}.summary.txt'
    with open(new_summary_path, 'w', encoding='utf-8') as f:
        f.write(text)
    result['summaries_updated'] = 1
    result['new_summary_path'] = new_summary_path
    
    # 2. 覆盖 archives/ 里所有对应 basename 的乱码版本
    archives_matched = glob.glob(f'{ARCHIVES}/*_{bn}.summary.txt')
    for arch_path in archives_matched:
        with open(arch_path, 'w', encoding='utf-8') as f:
            f.write(text)
        result['archives_updated'] += 1
    
    return result


def main():
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('--dry-run', action='store_true')
    p.add_argument('--max', type=int, default=5, help='最多处理前 N 个乱码 summary')
    p.add_argument('--pdf-list', help='指定 PDF 路径列表（逗号分隔），跳过自动扫描')
    args = p.parse_args()
    
    print(f"🔍 扫描 archives/ 中的乱码 summary...")
    corrupted = find_corrupted_summaries()
    print(f"📊 发现 {len(corrupted)} 个乱码 summary")
    
    if args.pdf_list:
        pdf_list = args.pdf_list.split(',')
    else:
        # 找到每份乱码对应的 PDF，去重
        seen_pdfs = set()
        pdf_list = []
        for c in corrupted:
            bn = summary_to_pdf_basename(c['path'])
            pdf = find_pdf_by_basename(bn)
            if pdf and pdf not in seen_pdfs:
                seen_pdfs.add(pdf)
                pdf_list.append(pdf)
            if len(pdf_list) >= args.max:
                break
    
    print(f"\n📋 将处理 {len(pdf_list)} 份 PDF:")
    for p in pdf_list:
        rel = p.replace(KNOWLEDGE + '/', '')
        if len(rel) > 60: rel = '...' + rel[-57:]
        print(f"  - {rel}")
    
    print(f"\n{'='*80}")
    print(f"🚀 开始{'DRY-RUN' if args.dry_run else '实际执行'}")
    print(f"{'='*80}")
    
    results = []
    for i, pdf_path in enumerate(pdf_list, 1):
        print(f"\n[{i}/{len(pdf_list)}] {os.path.basename(pdf_path)[:60]}")
        r = re_ocr_one(pdf_path, dry_run=args.dry_run)
        results.append(r)
        
        if r['success']:
            status = "✅"
            warn = " ⚠️ 文本仍异常" if r.get('text_still_broken') else ""
            print(f"   {status} {r['elapsed']:.1f}s, 文本 {r['new_text_len']:,} 字{warn}")
            if not args.dry_run:
                print(f"   📝 summaries/: +1")
                print(f"   📝 archives/: {r['archives_updated']} 个被覆盖")
        else:
            print(f"   ❌ 失败: {r['error']}")
    
    print(f"\n{'='*80}")
    print(f"📊 最终报告")
    print(f"{'='*80}")
    success_count = sum(1 for r in results if r['success'])
    fail_count = len(results) - success_count
    
    print(f"\n总处理: {len(results)} 个 PDF")
    print(f"  ✅ 成功: {success_count}")
    print(f"  ❌ 失败: {fail_count}")
    
    if fail_count > 0:
        print(f"\n❌ 失败的文件（需要人工处理）：")
        for r in results:
            if not r['success']:
                print(f"  - {r['pdf_path']}")
                print(f"    原因: {r['error']}")
    
    total_summaries = sum(r['summaries_updated'] for r in results)
    total_archives = sum(r['archives_updated'] for r in results)
    print(f"\n📝 文件更新：")
    print(f"  summaries/ 新增: {total_summaries}")
    print(f"  archives/ 覆盖: {total_archives}")
    
    # 输出 JSON 报告
    report_path = f'{KNOWLEDGE}/.analysis/re_ocr_report_{TIMESTAMP}.json'
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n📄 详细报告: {report_path}")
    
    return 0 if fail_count == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
