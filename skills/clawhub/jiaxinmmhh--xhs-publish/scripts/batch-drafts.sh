#!/bin/zsh
# 批量把若干期存进小红书草稿箱（不发布）
# 用法: zsh batch-drafts.sh 16 17 18 ...
# 系列三: SERIES=xip3 COLLECTION=怎么赚得更聪明 zsh batch-drafts.sh 01 02 03 ...
# 注意 EP 必须传两位数（02 而非 2），脚本按 ${SERIES}-ep${EP} 拼路径
cd /Users/jx/Downloads/.workbuddy/macros
export NO_PROXY='127.0.0.1,localhost'
export NODE_PATH=/Users/jx/.workbuddy/binaries/node/workspace/node_modules
# node 路径会漂移，先 ls /Users/jx/.workbuddy/binaries/node/versions/*/bin/node 确认
NODE=/Users/jx/.workbuddy/binaries/node/versions/22.22.2-6/bin/node

export SERIES=${SERIES:-xip}
export COLLECTION=${COLLECTION:-怎么活得更好}
echo "系列: $SERIES | 合集: $COLLECTION | 共 $# 期"
OK=()
FAIL=()
for ep in "$@"; do
  echo ""
  echo "########## ep$ep 开始 $(date '+%H:%M:%S') ##########"
  if EP=$ep SERIES=$SERIES COLLECTION=$COLLECTION NO_CHAPTER=1 $NODE xhs-draft-ep.js \
     && EP=$ep SERIES=$SERIES COLLECTION=$COLLECTION $NODE xhs-save-draft.js; then
    OK+=("$ep")
    echo "✅✅ ep$ep 完成 $(date '+%H:%M:%S')"
  else
    FAIL+=("$ep")
    echo "❌❌ ep$ep 失败 $(date '+%H:%M:%S')"
  fi
  sleep 3
done
echo ""
echo "================ 汇总 $(date '+%H:%M:%S') ================"
echo "成功 (${#OK[@]}): ${OK[*]}"
echo "失败 (${#FAIL[@]}): ${FAIL[*]}"
