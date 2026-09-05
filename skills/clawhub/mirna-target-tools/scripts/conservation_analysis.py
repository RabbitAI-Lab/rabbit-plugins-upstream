#!/usr/bin/env python3
"""
miRNA 保守序列分析 (Conservation Analysis)

从 miRBase 提取目标 miRNA 在多个物种中的同源成熟序列，进行多序列比对，
计算每个位点的保守性（Shannon 信息量 bits + 同一性百分比），并输出：
  - 多序列比对 FASTA（含 gap）
  - 位点保守性统计表（TSV）
  - 汇总统计表（TSV）
  - 发表级序列 logo（信息量图，300dpi PNG + 可选 SVG）
  - 发表级多序列比对图（300dpi PNG + 可选 SVG）

用法（模式一：从 miRBase 自动提取同源序列）:
  python conservation_analysis.py --mirna miR-504-5p \
      --reference-species chi --outdir results/ --prefix miR-504

用法（模式二：用户提供多序列 FASTA）:
  python conservation_analysis.py --input-fa homologs.fa \
      --outdir results/ --prefix miR-504

依赖：
  核心（FASTA/MSA/保守性计算）为纯标准库，零第三方依赖。
  绘图需要 matplotlib（可选：缺失时跳过图，仅输出 TSV）。
"""

import argparse
import gzip
import math
import os
import sys
import urllib.request

MIRBASE_URL = "https://www.mirbase.org/download/mature.fa"
CACHE_DIR = os.path.join(os.path.expanduser("~"), ".cache", "mirna-target-tools")

# WebLogo 标准碱基配色（RNA）
BASE_COLORS = {
    'A': '#2ecc71',  # green
    'C': '#3498db',  # blue
    'G': '#f39c12',  # orange
    'U': '#e74c3c',  # red
    'T': '#e74c3c',  # red (DNA T 归并为 U)
}
VALID_BASES = set('ACGU')


# ---------------------------------------------------------------------------
# FASTA 处理
# ---------------------------------------------------------------------------

def parse_fasta(path):
    """解析 FASTA（支持 .gz）。返回 [(header, seq), ...]，header 含 '>'。"""
    seqs = []
    name = None
    seq_parts = []
    opener = gzip.open if path.endswith('.gz') else open
    with opener(path, 'rt') as fh:
        for line in fh:
            line = line.rstrip('\n')
            if line.startswith('>'):
                if name is not None:
                    seqs.append((name, ''.join(seq_parts)))
                name = line[1:].strip()
                seq_parts = []
            else:
                if line.strip():
                    seq_parts.append(line.strip().upper())
        if name is not None:
            seqs.append((name, ''.join(seq_parts)))
    return seqs


def write_fasta(path, records):
    """records: [(header_without_>, seq), ...]"""
    with open(path, 'w') as fh:
        for header, seq in records:
            fh.write(f">{header}\n")
            for i in range(0, len(seq), 80):
                fh.write(seq[i:i + 80] + "\n")


def normalize_rna(seq):
    """统一为 RNA 大写，T -> U，仅保留 ACGU（其余字符替换为 N）。"""
    seq = seq.upper().replace('T', 'U')
    return ''.join(c if c in VALID_BASES else 'N' for c in seq)


# ---------------------------------------------------------------------------
# 序列比对（Needleman-Wunsch 全局比对）
# ---------------------------------------------------------------------------

def needleman_wunsch(seq1, seq2, match=2, mismatch=-1, gap=-2):
    """端 gap 免费的全局比对（适合 miRNA：5' 种子区保守、3' 端 isomiR 变异）。

    第一行/列初始化为 0（端 gap 不惩罚），回溯从最后一行/列的全局最大得分
    处开始，保证完整保留两条序列，gap 集中于端部而非散落在序列中间。
    返回 (aligned1, aligned2)，gap 用 '-'。
    """
    m, n = len(seq1), len(seq2)
    score = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            diag = score[i - 1][j - 1] + (match if seq1[i - 1] == seq2[j - 1] else mismatch)
            up = score[i - 1][j] + gap
            left = score[i][j - 1] + gap
            score[i][j] = max(diag, up, left)

    # 回溯起点：最后一行/列的全局最大得分（端 gap 免费）
    best = -1e9
    bi, bj = m, n
    for i in range(m + 1):
        if score[i][n] > best:
            best, bi, bj = score[i][n], i, n
    for j in range(n + 1):
        if score[m][j] > best:
            best, bi, bj = score[m][j], m, j

    # 回溯到 (0, 0)
    mid1, mid2 = [], []
    i, j = bi, bj
    while i > 0 and j > 0:
        if score[i][j] == score[i - 1][j - 1] + \
                (match if seq1[i - 1] == seq2[j - 1] else mismatch):
            mid1.append(seq1[i - 1]); mid2.append(seq2[j - 1]); i -= 1; j -= 1
        elif score[i][j] == score[i - 1][j] + gap:
            mid1.append(seq1[i - 1]); mid2.append('-'); i -= 1
        else:
            mid1.append('-'); mid2.append(seq2[j - 1]); j -= 1
    # 前导端 gap（免费）
    while i > 0:
        mid1.append(seq1[i - 1]); mid2.append('-'); i -= 1
    while j > 0:
        mid1.append('-'); mid2.append(seq2[j - 1]); j -= 1
    mid1.reverse(); mid2.reverse()

    # 尾随端 gap（免费）
    tail1 = seq1[bi:]
    tail2 = seq2[bj:]
    L = max(len(tail1), len(tail2))
    tail1 = tail1 + '-' * (L - len(tail1))
    tail2 = tail2 + '-' * (L - len(tail2))
    return ''.join(mid1) + tail1, ''.join(mid2) + tail2


# ---------------------------------------------------------------------------
# 递进式多序列比对（star alignment）
#
# 模型：对齐 = 锚点（参考序列原始位置 0..L-1）+ 插入槽（槽 k = 锚点 k-1 与
# 锚点 k 之间，k=0 为开头，k=L 为结尾）。每个序列在每个锚点有一个字符（或
# gap），在每个插入槽有若干插入字符。所有序列共享同一组插入列（取各序列在
# 该槽插入字符数的最大值，不足者以 '-' 补齐，左对齐）。
# ---------------------------------------------------------------------------

def progressive_msa(seqs, names, ref_idx=0):
    """返回 dict: name -> aligned string（含 gap，长度一致）。"""
    ref = seqs[ref_idx]
    L = len(ref)
    n = len(seqs)

    # 每个序列的锚点字符（list of L chars）与插入字符（list of L+1 个槽）
    anchor = {}
    insert = {}
    anchor[names[ref_idx]] = list(ref)
    insert[names[ref_idx]] = [[] for _ in range(L + 1)]

    for i in range(n):
        if i == ref_idx:
            continue
        name = names[i]
        s = seqs[i]
        a_ref, a_s = needleman_wunsch(ref, s)

        s_anchor = ['-'] * L
        s_insert = [[] for _ in range(L + 1)]
        ref_pos = 0
        for rc, sc in zip(a_ref, a_s):
            if rc == '-':
                # ref 在此为 gap => s 在"锚点 ref_pos 之前"插入字符 sc
                # 属于插入槽 ref_pos（槽 k = 锚点 k-1 之后、锚点 k 之前）
                s_insert[ref_pos].append(sc)
            else:
                s_anchor[ref_pos] = sc
                ref_pos += 1
        anchor[name] = s_anchor
        insert[name] = s_insert

    # 合并插入槽：每个槽的列数取所有序列该槽插入字符数的最大值
    slot_len = [0] * (L + 1)
    for name in names:
        for k in range(L + 1):
            slot_len[k] = max(slot_len[k], len(insert[name][k]))

    # 渲染每个序列的最终对齐字符串（插入字符左对齐，右补 '-'）
    result = {}
    for name in names:
        chars = []
        for k in range(L + 1):
            ins = insert[name][k]
            chars.extend(ins)
            chars.extend(['-'] * (slot_len[k] - len(ins)))
            if k < L:
                chars.append(anchor[name][k])
        result[name] = ''.join(chars)
    return result


# ---------------------------------------------------------------------------
# 保守性计算
# ---------------------------------------------------------------------------

def position_conservation(column_chars):
    """给定一列字符（含 gap/N），计算保守性指标。

    返回 dict: consensus, identity(%), bits, counts, gap_count, valid_count
    - bits: Shannon 信息量 = log2(4) - H，基于非 gap/N 的 ACGU 分布
    - identity: 最常见碱基占非 gap/N 序列的比例（%）
    """
    counts = {'A': 0, 'C': 0, 'G': 0, 'U': 0}
    gap_count = 0
    for ch in column_chars:
        if ch == '-':
            gap_count += 1
        elif ch in counts:
            counts[ch] += 1
        else:
            # 'N' 或其他，视为缺失，不参与
            gap_count += 1
    valid = sum(counts.values())
    total = len(column_chars)

    total = len(column_chars)
    coverage = (valid / total * 100.0) if total > 0 else 0.0
    gap_percent = (gap_count / total * 100.0) if total > 0 else 0.0

    if valid == 0:
        return {
            'consensus': '-', 'identity': 0.0, 'bits': 0.0,
            'counts': counts, 'gap_count': gap_count, 'valid_count': 0,
            'gap_percent': gap_percent, 'coverage': coverage, 'total': total,
        }

    # 信息量（bits，基于非 gap 的 ACGU 分布）
    H = 0.0
    for b in 'ACGU':
        c = counts[b]
        if c > 0:
            p = c / valid
            H -= p * math.log2(p)
    bits = 2.0 - H  # log2(4) = 2 for RNA

    consensus = max('ACGU', key=lambda b: counts[b])
    identity = counts[consensus] / valid * 100.0

    return {
        'consensus': consensus, 'identity': identity, 'bits': bits,
        'counts': counts, 'gap_count': gap_count, 'valid_count': valid,
        'gap_percent': gap_percent, 'coverage': coverage, 'total': total,
    }


def pairwise_identity(aligned1, aligned2):
    """两序列（等长，含 gap）的成对同一性（%）。（只统计双方均非 gap 的位点）"""
    match = 0
    total = 0
    for a, b in zip(aligned1, aligned2):
        if a == '-' or b == '-':
            continue
        total += 1
        if a == b:
            match += 1
    return (match / total * 100.0) if total > 0 else 0.0


# ---------------------------------------------------------------------------
# 可视化
# ---------------------------------------------------------------------------

def draw_sequence_logo(msa, names, seed_start, seed_end, out_png, out_svg=None):
    """绘制信息量序列 logo。msa: dict name -> aligned string。"""
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        from matplotlib.patches import Rectangle
    except ImportError:
        print("Warning: matplotlib 未安装，跳过序列 logo 绘制。")
        return False

    # 转置：按列收集字符
    aligned = [msa[n] for n in names]
    width = len(aligned[0])
    cols = [[aligned[r][c] for r in range(len(aligned))] for c in range(width)]

    # 计算每列信息量与碱基高度
    stats = [position_conservation(col) for col in cols]

    fig, ax = plt.subplots(figsize=(max(6, width * 0.5), 3.2))

    for c in range(width):
        st = stats[c]
        x = c + 1
        if st['valid_count'] == 0:
            # 全 gap 位置：画灰色表示缺失
            ax.add_patch(Rectangle((x - 0.5, 0), 0.8, 2.0,
                                   facecolor='#e8e8e8', edgecolor='none', zorder=2))
            continue
        coverage = st['coverage']
        bits = st['bits']
        # 有效信息量：覆盖度 < 50% 时按覆盖度缩放，避免低覆盖位置虚高
        eff_bits = bits if coverage >= 50.0 else bits * (coverage / 100.0)
        bottom = 0.0
        # 按频率降序堆叠（更美观）
        order = sorted('ACGU', key=lambda b: st['counts'][b], reverse=True)
        for b in order:
            cnt = st['counts'][b]
            if cnt == 0:
                continue
            p = cnt / st['valid_count']
            h = p * eff_bits
            if h <= 0.001:
                continue
            ax.add_patch(Rectangle(
                (x - 0.5, bottom), 0.8, h,
                facecolor=BASE_COLORS[b], edgecolor='black', linewidth=0.3, zorder=3))
            ax.text(x, bottom + h / 2, b, ha='center', va='center',
                    fontsize=10, fontweight='bold', color='black', zorder=4)
            bottom += h
        # 低覆盖位置标注覆盖率
        if coverage < 50.0:
            ax.text(x, 2.05, f'{coverage:.0f}%', ha='center', va='bottom',
                    fontsize=6, color='#999999', zorder=5)

    # 种子区背景高亮
    if seed_start and seed_end:
        ax.axvspan(seed_start - 0.5, seed_end + 0.5, color='#fff3cd',
                   alpha=0.45, zorder=1)
        ax.text((seed_start + seed_end) / 2, 2.15, f'seed (nt {seed_start}-{seed_end})',
                ha='center', va='bottom', fontsize=8, color='#8a6d3b', style='italic')

    ax.set_xlim(0.5, width + 0.5)
    ax.set_ylim(0, 2.15)
    ax.set_xticks(range(1, width + 1))
    ax.set_xticklabels(range(1, width + 1), fontsize=8)
    ax.set_xlabel('Position (nt, 5\u2032 \u2192 3\u2032)', fontsize=10)
    ax.set_ylabel('Information content (bits)', fontsize=10)
    ax.set_title('miRNA sequence conservation', fontsize=12, fontweight='bold')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_yticks([0, 0.5, 1.0, 1.5, 2.0])

    plt.tight_layout()
    plt.savefig(out_png, dpi=300, bbox_inches='tight')
    if out_svg:
        plt.savefig(out_svg, bbox_inches='tight')
    plt.close(fig)
    return True


def draw_alignment(msa, names, seed_start, seed_end, out_png, out_svg=None):
    """绘制多序列比对图。"""
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        from matplotlib.patches import Rectangle
    except ImportError:
        print("Warning: matplotlib 未安装，跳过比对图绘制。")
        return False

    aligned = [msa[n] for n in names]
    n_rows = len(aligned)
    width = len(aligned[0])

    fig, ax = plt.subplots(figsize=(max(6, width * 0.42), max(2.5, n_rows * 0.45)))

    for r, name in enumerate(names):
        seq = aligned[r]
        y = n_rows - r  # 参考在顶部
        for c, ch in enumerate(seq):
            if ch == '-':
                color = '#d9d9d9'
            elif ch in BASE_COLORS:
                color = BASE_COLORS[ch]
            else:
                color = '#999999'
            ax.add_patch(Rectangle((c + 0.5, y - 0.4), 1.0, 0.8,
                                   facecolor=color, edgecolor='none'))
            if ch != '-':
                ax.text(c + 1.0, y, ch, ha='center', va='center',
                        fontsize=9, fontweight='bold', color='black', zorder=3)

    # 种子区背景
    if seed_start and seed_end:
        ax.axvspan(seed_start - 0.5, seed_end + 0.5, color='#fff3cd',
                   alpha=0.35, zorder=1)

    ax.set_xlim(0.5, width + 0.5)
    ax.set_ylim(0.5, n_rows + 0.5)
    ax.set_xticks(range(1, width + 1))
    ax.set_xticklabels(range(1, width + 1), fontsize=7)
    ax.set_yticks(range(1, n_rows + 1))
    ax.set_yticklabels(names, fontsize=8)
    ax.set_xlabel('Position (nt, 5\u2032 \u2192 3\u2032)', fontsize=10)
    ax.set_title('Multiple sequence alignment', fontsize=12, fontweight='bold')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='x', linestyle='-', linewidth=0.4, alpha=0.15)

    plt.tight_layout()
    plt.savefig(out_png, dpi=300, bbox_inches='tight')
    if out_svg:
        plt.savefig(out_svg, bbox_inches='tight')
    plt.close(fig)
    return True


# ---------------------------------------------------------------------------
# 主流程
# ---------------------------------------------------------------------------

def fetch_mature_fa(mature_fa=None):
    """获取 mature.fa 路径（本地文件或下载缓存）。返回路径。"""
    if mature_fa and os.path.exists(mature_fa):
        return mature_fa

    cache_path = os.path.join(CACHE_DIR, "mature.fa")
    if os.path.exists(cache_path):
        return cache_path

    os.makedirs(CACHE_DIR, exist_ok=True)
    print(f"下载 miRBase mature.fa ... ({MIRBASE_URL})")
    try:
        req = urllib.request.Request(MIRBASE_URL, headers={'User-Agent': 'mirna-target-tools/1.0'})
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = resp.read()
        with open(cache_path, 'wb') as fh:
            fh.write(data)
        print(f"已缓存到 {cache_path} ({len(data)} bytes)")
        return cache_path
    except Exception as e:
        print(f"Error: 下载 miRBase mature.fa 失败: {e}")
        print("请手动下载并指定: --mature-fa /path/to/mature.fa")
        sys.exit(1)


def extract_homologs(mature_fa, mirna_id, species_filter=None):
    """从 mature.fa 提取 mirna_id 的所有同源序列。

    mirna_id 形如 'miR-504-5p'（不含物种前缀）。
    返回 [(species_prefix, mirna_id, accession, species_name, seq), ...]
    """
    records = parse_fasta(mature_fa)
    hits = []
    for header, seq in records:
        # header: 'hsa-miR-504-5p MIMAT0002875 Homo sapiens miR-504-5p'
        fields = header.split()
        if not fields:
            continue
        name_field = fields[0]  # 'hsa-miR-504-5p'
        if '-' not in name_field:
            continue
        prefix, rest = name_field.split('-', 1)
        # 精确匹配 mirbase-id（rest == mirna_id），避免 miR-5046 误配
        if rest != mirna_id:
            continue
        accession = fields[1] if len(fields) > 1 else ''
        # 物种名 = 中间字段（去掉 name_field 和 accession 和末尾重复的 mirna-id）
        if len(fields) >= 4:
            species_name = ' '.join(fields[2:-1])
        else:
            species_name = prefix
        if species_filter and prefix not in species_filter:
            continue
        hits.append((prefix, mirna_id, accession, species_name, normalize_rna(seq)))
    return hits


def run_conservation(records, names, seed_start, seed_end, outdir, prefix,
                     ref_idx=0, make_plots=True):
    """records: [(seq, ...)] 与 names 对应，已规范化。执行比对+保守性+输出。"""
    os.makedirs(outdir, exist_ok=True)
    seqs = [r[4] for r in records]
    full_names = [f"{r[0]}-{r[1]}" for r in records]  # 'chi-miR-504-5p'

    # MSA
    msa = progressive_msa(seqs, full_names, ref_idx=ref_idx)
    # 保持输入顺序
    aligned_seqs = [msa[n] for n in full_names]

    # 1) 比对 FASTA
    fasta_path = os.path.join(outdir, f"{prefix}_aligned.fa")
    write_fasta(fasta_path, [
        (f"{r[0]}-{r[1]} {r[2]} {r[3]}", aligned_seqs[i])
        for i, r in enumerate(records)
    ])

    # 2) 位点保守性表
    width = len(aligned_seqs[0])
    cols = [[aligned_seqs[r][c] for r in range(len(aligned_seqs))] for c in range(width)]
    cons_path = os.path.join(outdir, f"{prefix}_conservation.tsv")
    with open(cons_path, 'w') as fh:
        fh.write("position\tconsensus\tidentity_percent\tbits\tA\tC\tG\tU\tgap\tvalid_count\tcoverage_percent\tis_seed\n")
        for c in range(width):
            st = position_conservation(cols[c])
            is_seed = 'yes' if (seed_start and seed_end and
                                (seed_start <= c + 1 <= seed_end)) else 'no'
            fh.write(
                f"{c + 1}\t{st['consensus']}\t{st['identity']:.2f}\t{st['bits']:.3f}\t"
                f"{st['counts']['A']}\t{st['counts']['C']}\t{st['counts']['G']}\t{st['counts']['U']}\t"
                f"{st['gap_count']}\t{st['valid_count']}\t{st['coverage']:.1f}\t{is_seed}\n"
            )

    # 3) 汇总统计
    stats = [position_conservation(col) for col in cols]
    seed_bits = []
    seed_identity = []
    all_bits = [s['bits'] for s in stats]
    all_identity = [s['identity'] for s in stats]
    for c in range(width):
        if seed_start and seed_end and (seed_start <= c + 1 <= seed_end):
            seed_bits.append(stats[c]['bits'])
            seed_identity.append(stats[c]['identity'])

    # 核心区（覆盖度 >= 50%）统计
    core_bits = [s['bits'] for s in stats if s['coverage'] >= 50.0]
    core_identity = [s['identity'] for s in stats if s['coverage'] >= 50.0]

    # 平均成对同一性
    pw = []
    for i in range(len(aligned_seqs)):
        for j in range(i + 1, len(aligned_seqs)):
            pw.append(pairwise_identity(aligned_seqs[i], aligned_seqs[j]))
    avg_pw = sum(pw) / len(pw) if pw else 0.0

    summary_path = os.path.join(outdir, f"{prefix}_summary.tsv")
    with open(summary_path, 'w') as fh:
        fh.write("metric\tvalue\n")
        fh.write(f"mirna\t{records[0][1]}\n")
        fh.write(f"num_species\t{len(records)}\n")
        fh.write(f"species_list\t{','.join(r[0] for r in records)}\n")
        fh.write(f"alignment_length\t{width}\n")
        fh.write(f"mean_bits_all\t{sum(all_bits) / width:.3f}\n")
        fh.write(f"mean_identity_all_percent\t{sum(all_identity) / width:.2f}\n")
        if seed_bits:
            fh.write(f"mean_bits_seed\t{sum(seed_bits) / len(seed_bits):.3f}\n")
            fh.write(f"mean_identity_seed_percent\t{sum(seed_identity) / len(seed_identity):.2f}\n")
        if core_bits:
            fh.write(f"core_region_length\t{len(core_bits)}\n")
            fh.write(f"mean_bits_core\t{sum(core_bits) / len(core_bits):.3f}\n")
            fh.write(f"mean_identity_core_percent\t{sum(core_identity) / len(core_identity):.2f}\n")
        fh.write(f"mean_pairwise_identity_percent\t{avg_pw:.2f}\n")
        fully_conserved = sum(1 for s in stats if s['identity'] >= 100.0 and s['valid_count'] > 0)
        fh.write(f"fully_conserved_positions\t{fully_conserved}\n")

    # 4) 图
    if make_plots:
        logo_png = os.path.join(outdir, f"{prefix}_sequence_logo.png")
        logo_svg = os.path.join(outdir, f"{prefix}_sequence_logo.svg")
        aln_png = os.path.join(outdir, f"{prefix}_alignment.png")
        aln_svg = os.path.join(outdir, f"{prefix}_alignment.svg")
        ok_logo = draw_sequence_logo(msa, full_names, seed_start, seed_end, logo_png, logo_svg)
        ok_aln = draw_alignment(msa, full_names, seed_start, seed_end, aln_png, aln_svg)
    else:
        ok_logo = ok_aln = False

    return {
        'fasta': fasta_path,
        'conservation': cons_path,
        'summary': summary_path,
        'num_species': len(records),
        'width': width,
    }


def main():
    parser = argparse.ArgumentParser(
        description='miRNA 保守序列分析（多物种同源序列比对 + 保守性可视化）')
    src = parser.add_mutually_exclusive_group(required=True)
    src.add_argument('--mirna', help='目标 miRNA（如 miR-504-5p），从 miRBase 提取同源序列')
    src.add_argument('--input-fa', help='用户提供的多序列 FASTA 文件')
    parser.add_argument('--mature-fa', help='本地 miRBase mature.fa 路径（可选）')
    parser.add_argument('--reference-species', default=None,
                        help='参考物种前缀（如 chi/hsa），用于比对锚点；默认第一个序列')
    parser.add_argument('--species', default=None,
                        help='逗号分隔的物种前缀白名单（如 hsa,chi,bta,mmu）；默认全部')
    parser.add_argument('--seed-start', type=int, default=2, help='种子区起始 nt（默认 2）')
    parser.add_argument('--seed-end', type=int, default=8, help='种子区结束 nt（默认 8）')
    parser.add_argument('--outdir', default='.', help='输出目录（默认当前）')
    parser.add_argument('--prefix', default='mirna_conservation', help='输出文件前缀')
    parser.add_argument('--no-plot', action='store_true', help='跳过绘图（仅输出 TSV）')
    args = parser.parse_args()

    if args.seed_start < 1 or args.seed_end < args.seed_start:
        print("Error: 种子区参数非法（需 1 <= seed-start <= seed-end）。")
        sys.exit(1)

    # 获取序列
    if args.mirna:
        mature_fa = fetch_mature_fa(args.mature_fa)
        species_filter = set(s.strip() for s in args.species.split(',')) \
            if args.species else None
        records = extract_homologs(mature_fa, args.mirna, species_filter)
        if not records:
            print(f"Error: 在 miRBase 中未找到 '{args.mirna}' 的同源序列。")
            print("请检查名称是否正确（如 miR-504-5p，不含物种前缀）。")
            sys.exit(1)
        print(f"找到 {len(records)} 个物种的同源序列：")
        for r in records:
            print(f"  {r[0]:>5}  {r[4]}")
    else:
        # 用户提供 FASTA
        raw = parse_fasta(args.input_fa)
        records = []
        for header, seq in raw:
            name_field = header.split()[0]
            if '-' in name_field:
                prefix, mirna_id = name_field.split('-', 1)
            else:
                prefix, mirna_id = name_field, 'unknown'
            records.append((prefix, mirna_id, '', '', normalize_rna(seq)))
        if len(records) < 2:
            print("Error: --input-fa 至少需要 2 条序列。")
            sys.exit(1)
        print(f"读取 {len(records)} 条序列。")

    # 确定参考序列
    ref_idx = 0
    if args.reference_species:
        for i, r in enumerate(records):
            if r[0] == args.reference_species:
                ref_idx = i
                break
        else:
            print(f"Warning: 未找到参考物种 '{args.reference_species}'，使用第一个序列。")

    result = run_conservation(
        records, [r[0] for r in records], args.seed_start, args.seed_end,
        args.outdir, args.prefix, ref_idx=ref_idx, make_plots=not args.no_plot)

    print()
    print("=== 输出文件 ===")
    print(f"  多序列比对 FASTA : {result['fasta']}")
    print(f"  位点保守性表     : {result['conservation']}")
    print(f"  汇总统计表       : {result['summary']}")
    if not args.no_plot:
        print(f"  序列 logo (PNG)  : {os.path.join(args.outdir, args.prefix + '_sequence_logo.png')}")
        print(f"  序列 logo (SVG)  : {os.path.join(args.outdir, args.prefix + '_sequence_logo.svg')}")
        print(f"  比对图 (PNG)     : {os.path.join(args.outdir, args.prefix + '_alignment.png')}")
        print(f"  比对图 (SVG)     : {os.path.join(args.outdir, args.prefix + '_alignment.svg')}")
    print(f"\n共 {result['num_species']} 个物种，比对长度 {result['width']} nt。")
    print("Done!")


if __name__ == '__main__':
    main()
