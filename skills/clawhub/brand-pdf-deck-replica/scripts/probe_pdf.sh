#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────────────────
# probe_pdf.sh — 品牌 PDF 复刻前置探针：4 条命令判定「能不能反解数据」
#
# 用法： bash probe_pdf.sh <src.pdf> [页码]
#
# 输出四段：
#   1. 页数 / 页面尺寸 → 决定 deck 的 @page 尺寸
#   2. 文本可读性      → 中文是否缺 ToUnicode 映射（乱码则文字须重建）
#   3. 内嵌位图分布    → 哪些页是着色蒙版位图（不可矢量还原）
#   4. 单页矢量构成    → 该页 path/rect/颜色，确认图表是否为矢量
# ─────────────────────────────────────────────────────────────────────────────
set -uo pipefail

SRC="${1:-}"
PG="${2:-6}"
[ -n "$SRC" ] && [ -f "$SRC" ] || { sed -n '2,14p' "$0"; exit 2; }

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

echo "════════ 1. 页数 / 页面尺寸 ════════"
pdfinfo "$SRC" 2>/dev/null | grep -E '^(Pages|Page size|Producer|Creator)'

echo
echo "════════ 2. 文本可读性（中文是否乱码）════════"
pdftotext -f "$PG" -l "$PG" -layout "$SRC" - 2>/dev/null | sed '/^\s*$/d' | head -8
echo "--- 拉丁/数字抽样（这些应当正常）---"
pdftotext -f "$PG" -l "$PG" "$SRC" - 2>/dev/null \
  | grep -oE '[A-Za-z][A-Za-z0-9.%-]{3,}' | sort -u | head -8

echo
echo "════════ 3. 内嵌位图分布（每页 image 数）════════"
pdfimages -list "$SRC" 2>/dev/null \
  | awk 'NR>2{c[$1]++} END{for(p in c) printf "  p%-3s %d 张\n", p, c[p]}' \
  | sort -t p -k2 -n
echo "  ↑ 某页 image 数达数百且颜色极少 = 该页图形是着色蒙版位图，无法矢量还原"

echo
echo "════════ 4. 单页矢量构成（p$PG）════════"
pdftocairo -svg -f "$PG" -l "$PG" "$SRC" "$TMP/pg.svg" 2>/dev/null || true
if [ -s "$TMP/pg.svg" ]; then
  printf '  path 数      : %s\n' "$(grep -o '<path' "$TMP/pg.svg" | wc -l | tr -d ' ')"
  printf '  rect 数      : %s\n' "$(grep -o '<rect' "$TMP/pg.svg" | wc -l | tr -d ' ')"
  printf '  image 数     : %s\n' "$(grep -o '<image' "$TMP/pg.svg" | wc -l | tr -d ' ')"
  printf '  clipPath 数  : %s\n' "$(grep -o 'clipPath' "$TMP/pg.svg" | wc -l | tr -d ' ')"
  echo "  --- 文件内出现的颜色（前 12）---"
  grep -oE 'fill="[^"]+"' "$TMP/pg.svg" | sort | uniq -c | sort -rn | head -12 | sed 's/^/    /'
  echo "  --- 无 <image> 且有多种 fill → 图表为矢量，可反解 ---"
else
  echo "  [!] 该页未导出矢量内容"
fi
