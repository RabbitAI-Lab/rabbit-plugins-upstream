#!/usr/bin/env bash
# render_draw.sh — 零依赖 SVG 图表渲染器 (纯 awk 生成矢量图)
# 子命令:
#   render_draw.sh line --title T --subtitle S --ylabel U \
#       --series "名称1:文件1" ["名称2:文件2" ...] [--who 数值] [--who-label 文本] \
#       [--theme light|dark] [--width W] [--height H] --out out.svg
#   render_draw.sh bar --title T --subtitle S --ylabel U \
#       --items "名称1:数值1" ["名称2:数值2" ...] [--who 数值] [--who-label 文本] \
#       [--theme light|dark] [--width W] [--height H] --out out.svg
set -euo pipefail
MODE=""; TITLE=""; SUBTITLE=""; YLABEL=""; WHO=""; WHO_LABEL="WHO 24h 基准"
THEME="light"; WIDTH=960; HEIGHT=480; OUT=""
declare -a SPECS=()

while (( $# )); do
  case "$1" in
    line|bar) MODE="$1"; shift ;;
    --title) TITLE="$2"; shift 2 ;;
    --subtitle) SUBTITLE="$2"; shift 2 ;;
    --ylabel) YLABEL="$2"; shift 2 ;;
    --series|--items) shift; while (( $# )) && [[ "$1" != --* ]]; do SPECS+=("$1"); shift; done ;;
    --who) WHO="$2"; shift 2 ;;
    --who-label) WHO_LABEL="$2"; shift 2 ;;
    --who-color) WHO_C_OVERRIDE="$2"; shift 2 ;;
    --colors) COLORS_OPT="$2"; shift 2 ;;
    --theme) THEME="$2"; shift 2 ;;
    --width) WIDTH="$2"; shift 2 ;;
    --height) HEIGHT="$2"; shift 2 ;;
    --out) OUT="$2"; shift 2 ;;
    *) printf 'render_draw: 未知参数 %s\n' "$1" >&2; exit 1 ;;
  esac
done
[[ -n "$MODE" && -n "$OUT" && ${#SPECS[@]} -gt 0 ]] || { printf 'render_draw: 用法错误, 缺少 mode/series/out\n' >&2; exit 1; }

# 主题配色 (多城对比色板对齐 openaq-explorer 色盲友好色系)
if [[ "$THEME" == "dark" ]]; then
  BG="#111827"; FG="#e5e7eb"; GRID="#374151"; AXIS="#9ca3af"
  S_COLORS=("#60a5fa" "#f87171" "#34d399" "#fbbf24" "#c084fc")
  WHO_C_DEFAULT="#EF4444"
else
  BG="#ffffff"; FG="#111827"; GRID="#e5e5e5"; AXIS="#6b7280"
  S_COLORS=("#2563EB" "#DC2626" "#059669" "#D97706" "#7c3aed")
  WHO_C_DEFAULT="#EF4444"
fi
WHO_C="${WHO_C_OVERRIDE:-$WHO_C_DEFAULT}"
# --colors "c1,c2,..." 显式覆盖序列配色 (如指标专属色板)
if [[ -n "${COLORS_OPT:-}" ]]; then
  IFS=',' read -ra S_COLORS <<< "$COLORS_OPT"
fi

# 把 specs 拆成平行数组传给 awk (名称可能含空格, 用 \x1f 作分隔符)
NAMES=(); FILES=(); VALUES=()
for s in "${SPECS[@]}"; do
  NAMES+=("${s%%:*}"); REST="${s#*:}"
  if [[ "$MODE" == "line" ]]; then FILES+=("$REST"); else VALUES+=("$REST"); fi
done
join_by_us() { local IFS=$'\x1f'; printf '%s' "$*"; }

if [[ "$MODE" == "line" ]]; then
  awk -v title="$TITLE" -v subtitle="$SUBTITLE" -v ylabel="$YLABEL" \
      -v who="$WHO" -v wholabel="$WHO_LABEL" \
      -v bg="$BG" -v fg="$FG" -v grid="$GRID" -v axis="$AXIS" \
      -v colors="${S_COLORS[*]}" -v whoc="$WHO_C" \
      -v W="$WIDTH" -v H="$HEIGHT" \
      -v names="$(join_by_us "${NAMES[@]}")" -v nseries="${#NAMES[@]}" \
      -v files="$(join_by_us "${FILES[@]}")" -v outfile="$OUT" '
  function esc(s) { gsub(/&/,"&amp;",s); gsub(/</,"&lt;",s); gsub(/>/,"&gt;",s); return s }
  function fmt(v) { return (v == int(v)) ? sprintf("%d", v) : sprintf("%.1f", v) }
  BEGIN {
    us = sprintf("%c", 31)
    ns = split(names, name, us); nf = split(files, file, us)
    ncolor = split(colors, color, " ")
    # 读取各序列: val[i, k] (空值=断点), lab[i, k]
    for (i = 1; i <= nf; i++) {
      cnt[i] = 0
      while ((getline line < file[i]) > 0) {
        split(line, a, "\t")
        k = ++cnt[i]
        lab[i, k] = a[1]
        v = a[2]; gsub(/^[ \t]+|[ \t\r]+$/, "", v)
        val[i, k] = v
        if (v != "") {
          x = v + 0
          if (!has || x > ymax) { ymax = x; has = 1 }
          if (!hasmin || x < ymin) { ymin = x; hasmin = 1 }
        }
      }
      close(file[i])
      if (cnt[i] > nmax) { nmax = cnt[i]; axser = i }
    }
    if (!has) { print "render_draw: 没有可绘制的有效数据点" > "/dev/stderr"; exit 5 }
    if (who != "" && who + 0 > ymax) ymax = who + 0
    # 布局
    ml = 78; mr = 26; mt = 64; mb = 58
    pw = W - ml - mr; ph = H - mt - mb
    # 取整 ymax 到 1/2/5*10^k 的 5 等分
    raw = ymax * 1.12 / 5
    mag = 10 ^ int(log(raw) / log(10))
    for (m = 1; m <= 10; m++) { s = m * mag; if (raw <= s) break }
    step = s; ymax = step * 5
    # SVG 头
    printf "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" > outfile
    printf "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"%d\" height=\"%d\" viewBox=\"0 0 %d %d\" font-family=\"system-ui,-apple-system,sans-serif\">\n", W, H, W, H >> outfile
    printf "<rect width=\"%d\" height=\"%d\" fill=\"%s\"/>\n", W, H, bg >> outfile
    # 标题
    printf "<text x=\"%d\" y=\"28\" font-size=\"19\" font-weight=\"700\" fill=\"%s\">%s</text>\n", ml, fg, esc(title) >> outfile
    if (subtitle != "")
      printf "<text x=\"%d\" y=\"48\" font-size=\"12\" fill=\"%s\">%s</text>\n", ml, axis, esc(subtitle) >> outfile
    # 图例 (右上)
    lx = W - mr
    for (i = ns; i >= 1; i--) {
      wlab = 14 + length(name[i]) * 7
      lx -= wlab
      c = color[((i - 1) % ncolor) + 1]
      printf "<line x1=\"%d\" y1=\"24\" x2=\"%d\" y2=\"24\" stroke=\"%s\" stroke-width=\"3\" stroke-linecap=\"round\"/>\n", lx, lx + 14, c >> outfile
      printf "<text x=\"%d\" y=\"28\" font-size=\"12\" fill=\"%s\">%s</text>\n", lx + 20, fg, esc(name[i]) >> outfile
      lx -= 16
    }
    # 网格 + Y 轴刻度
    for (t = 0; t <= 5; t++) {
      y = mt + ph - ph * t / 5
      printf "<line x1=\"%d\" y1=\"%.1f\" x2=\"%d\" y2=\"%.1f\" stroke=\"%s\" stroke-width=\"1\"/>\n", ml, y, ml + pw, y, grid >> outfile
      printf "<text x=\"%d\" y=\"%.1f\" font-size=\"11\" fill=\"%s\" text-anchor=\"end\">%s</text>\n", ml - 8, y + 4, axis, fmt(step * t) >> outfile
    }
    # Y 轴标题 (旋转)
    printf "<text x=\"18\" y=\"%d\" font-size=\"12\" fill=\"%s\" text-anchor=\"middle\" transform=\"rotate(-90 18 %d)\">%s</text>\n", mt + ph / 2, axis, mt + ph / 2, esc(ylabel) >> outfile
    # X 轴
    printf "<line x1=\"%d\" y1=\"%d\" x2=\"%d\" y2=\"%d\" stroke=\"%s\" stroke-width=\"1.5\"/>\n", ml, mt + ph, ml + pw, mt + ph, axis >> outfile
    npts = (axser ? cnt[axser] : nmax)
    nseg = (npts > 1) ? pw / (npts - 1) : pw
    # X 轴刻度: 约 7 个
    tick_every = int((npts + 6) / 7); if (tick_every < 1) tick_every = 1
    for (k = 1; k <= npts; k += tick_every) {
      x = ml + (k - 1) * nseg
      printf "<text x=\"%.1f\" y=\"%d\" font-size=\"11\" fill=\"%s\" text-anchor=\"middle\">%s</text>\n", x, mt + ph + 20, axis, esc(lab[axser, k]) >> outfile
    }
    # WHO 基准虚线
    if (who != "") {
      y = mt + ph - ph * (who + 0) / ymax
      printf "<line x1=\"%d\" y1=\"%.1f\" x2=\"%d\" y2=\"%.1f\" stroke=\"%s\" stroke-width=\"1.5\" stroke-dasharray=\"4,4\"/>\n", ml, y, ml + pw, y, whoc >> outfile
    }
    # 数据折线 (空值为断点)
    for (i = 1; i <= ns; i++) {
      c = color[((i - 1) % ncolor) + 1]
      pts = ""; run = ""
      for (k = 1; k <= cnt[i]; k++) {
        x = ml + (k - 1) * nseg
        if (val[i, k] == "") {
          if (run != "") { pts = pts run; run = "" }
          continue
        }
        y = mt + ph - ph * (val[i, k] + 0) / ymax
        run = run sprintf("%.1f,%.1f ", x, y)
        # 数据点 (序列不太多时画圆点)
        if (cnt[i] <= 40)
          printf "<circle cx=\"%.1f\" cy=\"%.1f\" r=\"2.5\" fill=\"%s\"/>\n", x, y, c >> outfile
      }
      pts = pts run
      if (pts != "") {
        gsub(/ $/, "", pts)
        printf "<polyline fill=\"none\" stroke=\"%s\" stroke-width=\"2\" stroke-linejoin=\"round\" stroke-linecap=\"round\" points=\"%s\"/>\n", c, pts >> outfile
      }
    }
    # WHO 标签最后绘制并加底色衬底, 避免与折线交叠
    if (who != "") {
      y = mt + ph - ph * (who + 0) / ymax
      wl = length(wholabel) * 7 + 10
      printf "<rect x=\"%d\" y=\"%.1f\" width=\"%d\" height=\"15\" fill=\"%s\"/>\n", ml + pw - 6 - wl, y - 17, wl, bg >> outfile
      printf "<text x=\"%d\" y=\"%.1f\" font-size=\"11\" fill=\"%s\" text-anchor=\"end\" font-weight=\"600\">%s</text>\n", ml + pw - 6, y - 6, whoc, esc(wholabel) >> outfile
    }
    printf "</svg>\n" >> outfile
  }'
else
  awk -v title="$TITLE" -v subtitle="$SUBTITLE" -v ylabel="$YLABEL" \
      -v who="$WHO" -v wholabel="$WHO_LABEL" \
      -v bg="$BG" -v fg="$FG" -v grid="$GRID" -v axis="$AXIS" \
      -v colors="${S_COLORS[*]}" -v whoc="$WHO_C" \
      -v W="$WIDTH" -v H="$HEIGHT" \
      -v names="$(join_by_us "${NAMES[@]}")" -v values="$(join_by_us "${VALUES[@]}")" \
      -v outfile="$OUT" '
  function esc(s) { gsub(/&/,"&amp;",s); gsub(/</,"&lt;",s); gsub(/>/,"&gt;",s); return s }
  function fmt(v) { return (v == int(v)) ? sprintf("%d", v) : sprintf("%.1f", v) }
  BEGIN {
    us = sprintf("%c", 31)
    ns = split(names, name, us); nv = split(values, value, us)
    ncolor = split(colors, color, " ")
    vmax = 0
    for (i = 1; i <= nv; i++) { v = value[i] + 0; if (v > vmax) vmax = v }
    if (vmax <= 0) { print "render_draw: 没有可绘制的有效数据" > "/dev/stderr"; exit 5 }
    if (who != "" && who + 0 > vmax) vmax = who + 0
    raw = vmax * 1.12 / 5
    mag = 10 ^ int(log(raw) / log(10))
    for (m = 1; m <= 10; m++) { s = m * mag; if (raw <= s) break }
    step = s; ymax = step * 5
    mt = 64; mb = 30; ml = 24; mr = 24
    pw = W - ml - mr; ph = H - mt - mb
    bh = ph / ns                    # 每项行高
    barh = (bh > 34) ? 22 : bh * 0.55
    labelw = 0
    for (i = 1; i <= ns; i++) { l = length(name[i]); if (l > labelw) labelw = l }
    labelw = labelw * 7 + 12
    plotw = pw - labelw - 60
    printf "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" > outfile
    printf "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"%d\" height=\"%d\" viewBox=\"0 0 %d %d\" font-family=\"system-ui,-apple-system,sans-serif\">\n", W, H, W, H >> outfile
    printf "<rect width=\"%d\" height=\"%d\" fill=\"%s\"/>\n", W, H, bg >> outfile
    printf "<text x=\"%d\" y=\"28\" font-size=\"19\" font-weight=\"700\" fill=\"%s\">%s</text>\n", ml, fg, esc(title) >> outfile
    if (subtitle != "")
      printf "<text x=\"%d\" y=\"48\" font-size=\"12\" fill=\"%s\">%s</text>\n", ml, axis, esc(subtitle) >> outfile
    printf "<text x=\"%d\" y=\"%d\" font-size=\"12\" fill=\"%s\" text-anchor=\"end\">%s</text>\n", ml + pw, 28, axis, esc(ylabel) >> outfile
    # 顶部刻度参考
    for (t = 0; t <= 5; t++) {
      x = ml + labelw + plotw * t / 5
      printf "<line x1=\"%.1f\" y1=\"%d\" x2=\"%.1f\" y2=\"%d\" stroke=\"%s\" stroke-width=\"1\"/>\n", x, mt - 8, x, mt + ph, grid >> outfile
      printf "<text x=\"%.1f\" y=\"%d\" font-size=\"11\" fill=\"%s\" text-anchor=\"middle\">%s</text>\n", x, mt - 12, axis, fmt(step * t) >> outfile
    }
    # 横向柱状
    for (i = 1; i <= ns; i++) {
      y = mt + (i - 1) * bh + (bh - barh) / 2
      v = value[i] + 0
      w = plotw * v / ymax
      c = (ncolor == 1) ? color[1] : color[((i - 1) % ncolor) + 1]
      printf "<text x=\"%d\" y=\"%.1f\" font-size=\"12\" fill=\"%s\" text-anchor=\"end\">%s</text>\n", ml + labelw - 8, y + barh / 2 + 4, fg, esc(name[i]) >> outfile
      printf "<rect x=\"%d\" y=\"%.1f\" width=\"%.1f\" height=\"%.1f\" rx=\"3\" fill=\"%s\"/>\n", ml + labelw, y, (w > 1 ? w : 1), barh, c >> outfile
      printf "<text x=\"%.1f\" y=\"%.1f\" font-size=\"12\" font-weight=\"600\" fill=\"%s\">%s</text>\n", ml + labelw + w + 8, y + barh / 2 + 4, fg, fmt(v) >> outfile
    }
    # WHO 基准竖线
    if (who != "") {
      x = ml + labelw + plotw * (who + 0) / ymax
      printf "<line x1=\"%.1f\" y1=\"%d\" x2=\"%.1f\" y2=\"%d\" stroke=\"%s\" stroke-width=\"1.5\" stroke-dasharray=\"4,4\"/>\n", x, mt - 8, x, mt + ph, whoc >> outfile
      printf "<text x=\"%.1f\" y=\"%d\" font-size=\"11\" fill=\"%s\" text-anchor=\"middle\" font-weight=\"600\">%s</text>\n", x, mt + ph + 18, whoc, esc(wholabel) >> outfile
    }
    printf "</svg>\n" >> outfile
  }'
fi
printf '%s\n' "$OUT"
