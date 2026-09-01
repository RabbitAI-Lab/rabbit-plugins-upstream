#!/bin/bash
# 渲染 skill2 user-research-assistant 功能与样例说明 PDF
# 环境：WSL 无 Linux Chromium → 用 Windows Edge --print-to-pdf（已验证可行）
# 用法：bash render-sample.sh [--check]   （--check 只做每页高度溢出检查）
set -e
DOCS="/mnt/e/大三下/用户研究/skills/skill2/user-research-assistant/docs"
ROOT="/mnt/e/大三下/用户研究/skills/skill2/user-research-assistant"
HTML="$DOCS/sample-guide.html"
OUT="$ROOT/user-research-assistant-功能与样例说明.pdf"
EDGE="/mnt/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
PS="/mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe"
WIN_HTML='E:\大三下\用户研究\skills\skill2\user-research-assistant\docs\sample-guide.html'
PROFILE="C:\\temp\\ura-edge-profile"
TMP_PDF="C:\\temp\\ura-out.pdf"

cd "$DOCS"
cp "$HTML" /tmp/ura-html.bak

if [ "$1" = "--check" ]; then
  python3 - <<'EOF'
html = open('sample-guide.html', encoding='utf-8').read()
inject = '<script>document.title = [...document.querySelectorAll(".page")].map((p,i)=>i+1+":"+Math.round(p.getBoundingClientRect().height)).join(",");</script>'
open('sample-guide.html', 'w', encoding='utf-8').write(html.replace('</body>', inject + '</body>'))
EOF
  "$PS" -NoProfile -Command "& '$EDGE' --headless=new --disable-gpu --no-first-run --user-data-dir='$PROFILE' --dump-dom '$WIN_HTML'" 2>/dev/null \
    | grep -o '<title>[^<]*</title>' | head -1
  cp /tmp/ura-html.bak "$HTML"
  echo "(检查用 HTML 已还原)"
else
  rm -f /mnt/c/temp/ura-out.pdf
  "$PS" -NoProfile -Command "& '$EDGE' --headless=new --disable-gpu --no-first-run --no-pdf-header-footer --user-data-dir='${PROFILE}2' --print-to-pdf='$TMP_PDF' '$WIN_HTML'" 2>&1 | grep -E "bytes written" || true
  for i in $(seq 1 20); do [ -f /mnt/c/temp/ura-out.pdf ] && S=$(stat -c%s /mnt/c/temp/ura-out.pdf 2>/dev/null) && [ "$S" -gt 100000 ] && break; sleep 1; done
  sleep 2
  cp /mnt/c/temp/ura-out.pdf "$OUT"
  echo "PDF: $OUT ($(stat -c%s "$OUT") bytes)"
fi
