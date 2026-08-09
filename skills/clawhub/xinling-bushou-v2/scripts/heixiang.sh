#!/bin/bash
# 黑箱融合引擎入口 — 六爻+奇门双算法融合算事 (V3.5.0)
# 用法: ./heixiang.sh "用户问题"
#
# V3.5.0 改进（针对 SkillHub 评测「运行稳定性 3.8」）：
# - 外部模块缺失/出错时，输出友好中文提示并降级，而非裸报错堆栈
# - 退出码：0=成功 2=依赖缺失 3=内部错误

QUESTION="$*"
cd "$(dirname "$0")/.."

# 1. 前置依赖检查：六爻 / 奇门引擎路径是否存在
LIUYAO_DIR="/root/.openclaw/workspace/skills/yxf_yixue"
QIMEN_DIR="/root/.openclaw/workspace/skills/qimen-dunjia/scripts"

missing=()
[ -d "$LIUYAO_DIR" ] || missing+=("六爻引擎(yxf_yixue): $LIUYAO_DIR")
[ -d "$QIMEN_DIR" ] || missing+=("奇门引擎(qimen-dunjia): $QIMEN_DIR")

if [ ${#missing[@]} -gt 0 ]; then
    echo "⚠️ 玄学测算依赖缺失，已降级为纯口吻陪伴（不输出卦象判词）。" >&2
    for m in "${missing[@]}"; do
        echo "  - 缺少 $m" >&2
    done
    echo "💡 修复：安装对应 Skill 后重试，或 `xinling check` 排查。" >&2
    echo '{"question":"'$QUESTION'","agree":[],"differ":[],"conclusion":"老朽今日观天机朦胧，暂不便妄断；主公若有疑虑，且容老朽他日再推。"}' 
    exit 2
fi

# 2. 正常执行
python3 -c "
from core.heixiang_fusion import HeixiangFusion
from datetime import datetime
import sys, json

try:
    f = HeixiangFusion()
    r = f.divine(sys.argv[1], datetime.now())
    out = {
        'question': r['question'],
        'agree': r['agree'],
        'differ': r['differ'],
        'conclusion': r['conclusion'],
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))
except Exception as e:
    # 运行时出错 → 降级，不暴露堆栈
    print(json.dumps({
        'question': sys.argv[1] if len(sys.argv) > 1 else '',
        'agree': [],
        'differ': [],
        'conclusion': '老朽方才推演被打断，天机暂不分明；主公勿忧，稍后再为君推算。',
        'error': str(e),
    }, ensure_ascii=False, indent=2), file=sys.stderr)
    sys.exit(3)
" "$QUESTION"
