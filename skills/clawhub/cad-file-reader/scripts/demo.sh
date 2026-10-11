#!/usr/bin/env bash
# 快速演示：用内置样例 DXF 跑一次完整识图，展示首屏 JSON（证据坐标/置信度/复核原因）。
# 用法：scripts/demo.sh [OUTPUT_DIR]
set -euo pipefail
SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="${1:-}"
if [[ -z "$OUT" ]]; then OUT="$(mktemp -d /tmp/cad-demo.XXXXXX)"; fi
mkdir -p "$OUT"
SAMPLE="$SKILL_DIR/examples/sample_room.dxf"
if [[ ! -f "$SAMPLE" ]]; then
  cat <<'EOF'
本轻量包不包含样例 DXF（SkillHub 不允许 .dxf 附件）。
请下载 GitHub 完整包运行 30 秒演示：
  https://github.com/lisong2003-lgtm/cad-file-reader/releases/download/v0.27.0/cad-file-reader-full-0.27.0.zip
将其中 examples/sample_room.dxf 复制到本技能 examples/ 后重跑 demo.sh。
EOF
  exit 1
fi
echo "样例: $SAMPLE"
"$SKILL_DIR/scripts/cad_scan.sh" "$SAMPLE" --only 墙,柱 --with-mtext --with-geom --cache-dir "$OUT/cache" --detail-json "$OUT/detail.json" --format json -o "$OUT/scan" --concise
"$SKILL_DIR/scripts/cad_measure.sh" "$OUT/detail.json" --out-dir "$OUT/measure" >/dev/null 2>&1 || true
echo ""
echo "==== 首屏 JSON（证据坐标/置信度/复核原因）===="
if [ -f "$OUT/measure/cad-measurement-candidates.json" ]; then
  if "$SKILL_DIR/scripts/cad_validate.sh" "$OUT/measure/cad-measurement-candidates.json" >/dev/null 2>&1; then
    echo "契约校验: 通过"
  else
    echo "契约校验: 未通过（见验证输出）"
  fi
  python3 "$SKILL_DIR/scripts/_demo_preview.py" "$OUT/measure/cad-measurement-candidates.json"
else
  echo "（未生成测量候选，直接展示扫描详情）"
  python3 "$SKILL_DIR/scripts/_demo_preview.py" "$OUT/detail.json"
fi
echo ""
echo "输出目录: $OUT"
echo "结果文件: $(find "$OUT" -type f -not -path "*/cache/*" | sort | tr '\n' ' ')"
