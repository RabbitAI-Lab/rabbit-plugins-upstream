#!/bin/bash
# 修正已有竖版 per-game cfg 的方向映射：只精确替换 4 行，其余保持原样。
# 默认 dry-run；加 --apply 才写入。遵守 HARD_RULES 第 7/10/11 条。
set -euo pipefail
source "$(dirname "$0")/kpa_env.sh"
require_device

APPLY=0
[ "${1:-}" = "--apply" ] && APPLY=1
[ "$APPLY" = "1" ] || echo "DRY-RUN：仅报告，不写入。确认后加 --apply 重跑。"

cat > /tmp/kpa_vertical_dev.sh <<'EOS'
#!/system/bin/sh
APPLY="$1"
CONF=/sdcard/RetroArch/config
need=0; changed=0
for f in $(find "$CONF" -type f -name '*.cfg' 2>/dev/null); do
  grep -q '^video_rotation = "[13]"' "$f" || continue
  grep -q '^input_player1_up_btn' "$f" || continue
  cur=$(grep '^input_player1_up_btn' "$f" | head -1)
  case "$cur" in *h0right*) continue;; esac
  need=$((need+1))
  if [ "$APPLY" = "1" ]; then
    sed -e 's/^input_player1_up_btn = .*/input_player1_up_btn = "h0right"/' \
        -e 's/^input_player1_down_btn = .*/input_player1_down_btn = "h0left"/' \
        -e 's/^input_player1_left_btn = .*/input_player1_left_btn = "h0up"/' \
        -e 's/^input_player1_right_btn = .*/input_player1_right_btn = "h0down"/' \
        "$f" > "$f.kpatmp" && mv "$f.kpatmp" "$f"
    changed=$((changed+1))
  else
    [ "$need" -le 10 ] && echo "  would fix: $f  [$cur]"
  fi
done
echo "RESULT vertical_cfg_need_fix=$need changed=$changed apply=$APPLY"
EOS

"$ADB" push /tmp/kpa_vertical_dev.sh /sdcard/kpa_vertical_dev.sh >/dev/null
sh "sh /sdcard/kpa_vertical_dev.sh $APPLY"
sh "rm -f /sdcard/kpa_vertical_dev.sh" >/dev/null
rm -f /tmp/kpa_vertical_dev.sh
[ "$APPLY" = "1" ] && echo "完成。按禁令：先在实机用 1941 单点验证方向，确认后再推广。"
exit 0
