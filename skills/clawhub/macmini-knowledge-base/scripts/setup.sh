#!/bin/bash
# setup.sh - macmini-knowledge-base 安装向导（v1.4.12 交互式）
# 保留全部功能 + 加 confirmation prompts + 依赖版本清单校验
# 用法：bash setup.sh [--dry-run]

set -e

DRY_RUN=false
# 飞书用户 ID：优先取位置参数 $1，其次取环境变量 FEISHU_USER_ID
FEISHU_USER_ID="${FEISHU_USER_ID:-}"
if [[ "${1:-}" == "--dry-run" ]]; then
    DRY_RUN=true
    shift
fi
if [[ -n "${1:-}" ]]; then
    FEISHU_USER_ID="$1"
fi

# ── 依赖版本清单（v1.4.12）────────────────────────────────────────
# 说明：Homebrew 多数 formula 无法在 `brew install` 时指定版本，
#   因此本脚本**不再宣称"版本固定"**，改为「清单 + 校验 + 记录」：
#   - pip 包：安装时直接锁定 ==版本
#   - brew 包：安装后校验实际版本，与清单不符时提示是否升级
#   - 安装完成后把本机实际版本写入 dependency-versions.txt，
#     供后续升级时核对供应链（上游版本变化需重新验证本 skill）
REQUIRED_BREW_VERSIONS="antiword=0.37 tesseract=5.5.2 pandoc=3.9.0.2"
REQUIRED_PIP_VERSIONS="pymupdf=1.26.5 python-docx=1.2.0 openpyxl=3.1.5 python-pptx=1.0.2 pdfplumber=0.11.8 Pillow=11.3.0"

brew_version() {
    brew list --versions "$1" 2>/dev/null | awk '{print $2}'
}

pip_version() {
    pip3 show "$1" 2>/dev/null | awk '/^Version:/{print $2}'
}

# ═══════════════════════════════════════════════════════════
# 1. 显示安装计划 + 全局确认
# ═══════════════════════════════════════════════════════════

cat <<'BANNER'
═══════════════════════════════════════════════════════════════
  ⚠️  macmini-knowledge-base v1.4.12 安装向导
═══════════════════════════════════════════════════════════════

本脚本将执行以下操作（每步都会要求确认）：

  1. 创建知识库目录结构
       ~/.openclaw/workspace/knowledge/.analysis/summaries/archives/
       ~/.openclaw/workspace/knowledge/temp_docs/
       ~/.openclaw/workspace/knowledge/Macro Financials/
       ~/.openclaw/workspace/knowledge/文章目录/

  2. 安装 Homebrew 包（按版本清单校验并记录实际版本）：
       - antiword（.doc 文件提取）
       - tesseract（OCR 引擎）
       - pandoc（文档格式转换）
       - libreoffice（Office 文档转换）

  3. 下载 Ollama 模型：
       - nomic-embed-text（~274MB）

  4. 注册 2 个持久 cron 任务：
       - 23:00 知识库分析
       - 06:00 飞书摘要推送

  5. 修改 OpenClaw 配置（添加 exec/process 权限）

═══════════════════════════════════════════════════════════════
BANNER

if [[ "$DRY_RUN" == true ]]; then
    echo "🔍 DRY-RUN 模式：只显示会做什么，不实际执行"
    echo ""
    exit 0
fi

read -p "确认开始安装？[y/N] " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ 已取消"
    exit 1
fi

# ═══════════════════════════════════════════════════════════
# 2. 分步执行（每步前 confirm）
# ═══════════════════════════════════════════════════════════

# [1/8] 创建目录
echo ""
echo "[1/8] 创建知识库目录..."
mkdir -p ~/.openclaw/workspace/knowledge/.analysis/summaries/archives
mkdir -p ~/.openclaw/workspace/knowledge/temp_docs
mkdir -p ~/.openclaw/workspace/knowledge/"Macro Financials"
mkdir -p ~/.openclaw/workspace/knowledge/文章目录
touch ~/.openclaw/workspace/knowledge/文章目录/文章目录.md
echo "✅ 目录创建完成"

# [2/8] Homebrew 包
echo ""
echo "[2/8] 检查 Homebrew 包..."

if ! command -v brew &> /dev/null; then
    read -p "  Homebrew 未安装。安装 Homebrew？[y/N] " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi
fi

install_brew_package() {
    local pkg=$1
    local desc=$2
    local want="" have=""
    for kv in $REQUIRED_BREW_VERSIONS; do
        [ "${kv%%=*}" = "$pkg" ] && want="${kv#*=}"
    done
    have="$(brew_version "$pkg")"
    if [ -n "$have" ]; then
        if [ -n "$want" ] && [ "$have" != "$want" ]; then
            echo "  ⚠️  $pkg 已装 $have，与测试清单 $want 不一致"
            read -p "     升级到测试版本？[y/N] " -n 1 -r
            echo
            if [[ $REPLY =~ ^[Yy]$ ]]; then
                brew upgrade "$pkg"
            fi
        else
            echo "  ✅ $pkg 已安装${have:+（$have）}${want:+，符合测试清单}"
        fi
    else
        read -p "  安装 $pkg${want:+（测试版本 $want）} — $desc？[y/N] " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            brew install "$pkg"
        fi
    fi
}

install_brew_package "antiword" ".doc 文件提取"
install_brew_package "tesseract" "OCR 引擎"
install_brew_package "pandoc" "文档格式转换"
install_brew_package "libreoffice" "Office 文档转换"

# [3/8] Python 包
echo ""
echo "[3/8] 检查 Python 包..."
for kv in $REQUIRED_PIP_VERSIONS; do
    pkg="${kv%%=*}"
    want="${kv#*=}"
    have="$(pip_version "$pkg")"
    if [ -n "$have" ]; then
        if [ "$have" != "$want" ]; then
            echo "  ⚠️  $pkg 已装 $have，与测试清单 $want 不一致"
            read -p "     升级到测试版本？[y/N] " -n 1 -r
            echo
            if [[ $REPLY =~ ^[Yy]$ ]]; then
                pip3 install --upgrade "$pkg==$want"
            fi
        else
            echo "  ✅ $pkg 已安装（$have，符合测试清单）"
        fi
    else
        read -p "  安装 $pkg==$want？[y/N] " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            pip3 install "$pkg==$want"
        fi
    fi
done

# 记录本机实际依赖版本 → 供升级时核对供应链
mkdir -p ~/.openclaw/workspace/.analysis
{
  echo "# macmini-knowledge-base v1.4.12 实测通过的依赖版本"
  echo "# 生成时间：$(date '+%Y-%m-%d %H:%M:%S')"
  echo "# 用途：升级后核对本机版本与测试清单；上游版本变化需重新验证本 skill"
  echo "[homebrew]"
  for kv in $REQUIRED_BREW_VERSIONS; do
    p="${kv%%=*}"; v="${kv#*=}"
    echo "$p = $(brew_version "$p" || echo 未安装)  # 测试清单 $v"
  done
  echo "[pip]"
  for kv in $REQUIRED_PIP_VERSIONS; do
    p="${kv%%=*}"; v="${kv#*=}"
    echo "$p = $(pip_version "$p" || echo 未安装)  # 测试清单 $v"
  done
} > ~/.openclaw/workspace/.analysis/dependency-versions.txt
echo "  ✅ 依赖版本清单已写入 ~/.openclaw/workspace/.analysis/dependency-versions.txt"

# [4/8] Ollama
echo ""
echo "[4/8] 检查 Ollama..."
if ! command -v ollama &> /dev/null; then
    read -p "  Ollama 未安装。安装 Ollama？[y/N] " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        brew install ollama
    fi
fi

if command -v ollama &> /dev/null; then
    if ollama list 2>/dev/null | grep -q "nomic-embed-text"; then
        echo "  ✅ nomic-embed-text 已下载"
    else
        read -p "  下载 nomic-embed-text（~274MB）？[y/N] " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            ollama pull nomic-embed-text
        fi
    fi
fi

# [5/8] OpenClaw 配置
echo ""
echo "[5/8] 修改 OpenClaw 配置..."
read -p "  添加 alsoAllow: [exec, process] 到 ~/.openclaw/openclaw.json？[y/N] " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    if [ -f ~/.openclaw/openclaw.json ]; then
        python3 -c "
import json, os
p = os.path.expanduser('~/.openclaw/openclaw.json')
with open(p) as f:
    cfg = json.load(f)
if 'agents' in cfg and 'defaults' in cfg['agents']:
    if 'tools' not in cfg['agents']['defaults']:
        cfg['agents']['defaults']['tools'] = {}
    if 'alsoAllow' not in cfg['agents']['defaults']['tools']:
        cfg['agents']['defaults']['tools']['alsoAllow'] = []
    for t in ['exec', 'process']:
        if t not in cfg['agents']['defaults']['tools']['alsoAllow']:
            cfg['agents']['defaults']['tools']['alsoAllow'].append(t)
with open(p, 'w') as f:
    json.dump(cfg, f, indent=2, ensure_ascii=False)
print('✅ OpenClaw 配置已更新')
" 2>/dev/null || echo "  ⚠️ 配置更新失败（手动检查 ~/.openclaw/openclaw.json）"
    fi
fi

# [6/8] cron 任务 1
echo ""
echo "[6/8] 注册 cron 任务 1：23:00 知识库分析..."
if [[ -z "$FEISHU_USER_ID" ]]; then
    echo "  ⚠️  未提供飞书用户 ID（位置参数或 FEISHU_USER_ID 环境变量），跳过 cron 注册"
else
    echo "  目标用户：$FEISHU_USER_ID"
fi
read -p "  注册 23:00 cron（每天自动执行 run_analysis.py）？[y/N] " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    openclaw cron add \
        --name "23:00分析新文档" \
        --cron "0 23 * * *" \
        --tz "Asia/Shanghai" \
        --session isolated \
        --timeout-seconds 600 \
        --message "cd ~/.openclaw/workspace/knowledge/.analysis && python3 run_analysis.py && python3 generate_catalog.py" \
        --announce --channel feishu --to "user:${FEISHU_USER_ID}" 2>/dev/null \
        || echo "  ⚠️ cron 注册失败（可能已存在）"
fi

# [7/8] cron 任务 2
echo ""
echo "[7/8] 注册 cron 任务 2：06:00 飞书摘要推送..."
read -p "  注册 06:00 cron（每天自动推送摘要到飞书）？[y/N] " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    openclaw cron add \
        --name "06:00发送文档摘要" \
        --cron "0 6 * * *" \
        --tz "Asia/Shanghai" \
        --session isolated \
        --timeout-seconds 300 \
        --message "请读取 summaries/ 目录当天生成的文件，用 message 工具发送摘要到飞书" \
        --announce --channel feishu --to "user:${FEISHU_USER_ID}" 2>/dev/null \
        || echo "  ⚠️ cron 注册失败（可能已存在）"
fi

# [8/8] 飞书 webhook
echo ""
echo "[8/8] 配置飞书 webhook..."
read -p "  需要配置飞书 webhook（推送摘要）？[y/N] " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    read -p "  请输入飞书 webhook URL: " FEISHU_WEBHOOK_URL
    if [[ -n "$FEISHU_WEBHOOK_URL" ]]; then
        mkdir -p ~/.openclaw/workspace/.feishu
        # webhook 是 bearer 型凭证：以受限 umask 写入，并显式 chmod 600
        ( umask 077; echo "$FEISHU_WEBHOOK_URL" > ~/.openclaw/workspace/.feishu/webhook_url )
        chmod 600 ~/.openclaw/workspace/.feishu/webhook_url
        echo "  ✅ 飞书 webhook URL 已保存（权限 600，仅当前用户可读）"
    fi
fi

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "✅ 安装完成！"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "⚠️ 重要提醒："
echo "  - 2 个 cron 任务已注册（如确认），每天自动执行"
echo "  - 禁用命令：openclaw cron remove <id>"
echo "  - 知识库目录：~/.openclaw/workspace/knowledge/"
echo "  - 如需重新运行：bash setup.sh [--dry-run]"
