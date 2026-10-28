#!/bin/zsh
# 抖音批量定时排期
# 用法: zsh batch-dy.sh            → 默认排 ep03–ep29（10-15 19:00 起，每天 07:00/19:00）
#       START_EP=03 END_EP=29 zsh batch-dy.sh
set -u
cd "$(dirname "$0")"

unset http_proxy https_proxy all_proxy HTTP_PROXY HTTPS_PROXY ALL_PROXY NODE_OPTIONS
export NO_PROXY='127.0.0.1,localhost'
export NODE_PATH=/Users/jx/.workbuddy/binaries/node/workspace/node_modules
NODE=/Users/jx/.workbuddy/binaries/node/versions/22.22.2-6/bin/node

START_EP=${START_EP:-04}
END_EP=${END_EP:-29}
START_DAY=${START_DAY:-16}     # 起始日期
START_HOUR=${START_HOUR:-07}   # 起始槽位（07 或 19），之后自动交替
LOG=/Users/jx/Downloads/.workbuddy/macros/dy-batch.log
: > "$LOG"

ep=$((10#$START_EP))
end=$((10#$END_EP))

echo "=== 抖音批量排期 ep${START_EP}–ep${END_EP} ===" | tee -a "$LOG"

# 生成槽位：从 START_DAY START_HOUR 起，07:00 / 19:00 交替，最多到 10-28
declare -a TIMES
TIMES=()
d=$START_DAY
h=$START_HOUR
while [ ${#TIMES[@]} -lt 40 ]; do
  TIMES+=("2026-10-$(printf %02d $d) $(printf %02d $h):00")
  if [ "$h" = "7" ] || [ "$h" = "07" ]; then h=19; else h=07; d=$((d+1)); fi
  [ $d -gt 28 ] && break
done
echo "槽位: $TIMES[1] … $TIMES[${#TIMES[@]}] 共 ${#TIMES[@]} 个" | tee -a "$LOG"

i=1   # zsh 数组下标从 1 开始
ok=0; failn=0
for e in $(seq $ep $end); do
  t=${TIMES[$i]}
  if [ -z "$t" ]; then echo "⚠️ 排期槽位用尽，ep$(printf %02d $e) 未排" | tee -a "$LOG"; break; fi
  echo "" | tee -a "$LOG"
  echo "--- [$(date '+%H:%M:%S')] ep$(printf %02d $e) → $t ---" | tee -a "$LOG"
  if $NODE dy-publish.js --ep $(printf %02d $e) --time "$t" 2>&1 | tee -a "$LOG" | grep -qE "发布成功|enter_from=publish"; then
    ok=$((ok+1)); echo "✅ ep$(printf %02d $e) $t" | tee -a "$LOG"
  else
    failn=$((failn+1)); echo "❌ ep$(printf %02d $e) $t 失败" | tee -a "$LOG"
  fi
  i=$((i+1))
  sleep 5
done

echo "" | tee -a "$LOG"
echo "=== 完成: 成功 $ok / 失败 $failn ===" | tee -a "$LOG"
