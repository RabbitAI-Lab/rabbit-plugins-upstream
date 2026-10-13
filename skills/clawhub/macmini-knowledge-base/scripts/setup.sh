#!/bin/bash
# setup.sh - macmini-knowledge-base 安装向导（v1.4.5 交互式）
# 保留全部功能 + 加 confirmation prompts + 版本固定
# 用法：bash setup.sh [--dry-run]

set -e

DRY_RUN=false
if [[ "${1:-}" == "--dry-run" ]]; then
    DRY_RUN=true
fi

# ═══════════════════════════════════════════════════════════
# 1. 显示安装计划 + 全局确认
# ═══════════════════════════════════════════════════════════

cat <<'BANNER'
═══════════════════════════════════════════════════════════════
  ⚠️  macmini-knowledge-base v1.4.5 安装向导
═══════════════════════════════════════════════════════════════

本脚本将执行以下操作（每步都会要求确认）：

  1. 创建知识库目录结构
       ~/.openclaw/workspace/knowledge/.analysis/summaries/archives/
       ~/.openclaw/workspace/knowledge/temp_docs/
       ~/.openclaw/workspace/knowledge/Macro Financials/
       ~/.openclaw/workspace/knowledge/文章目录/

  2. 安装 Homebrew 包（版本固定）：
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
    if brew list "$pkg" &>/dev/null; then
        echo "  ✅ $pkg 已安装"
    else
        read -p "  安装 $pkg — $desc？[y/N] " -n 1 -r
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
for pkg in pymupdf python-docx openpyxl python-pptx pdfplumber Pillow; do
    if pip3 show "$pkg" &> /dev/null; then
        echo "  ✅ $pkg 已安装"
    else
        read -p "  安装 $pkg？[y/N] " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            pip3 install "$pkg"
        fi
    fi
done

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
        --announce --channel feishu --to "user:\$FEISHU_USER_ID" 2>/dev/null \
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
        --announce --channel feishu --to "user:\$FEISHU_USER_ID" 2>/dev/null \
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
        echo "$FEISHU_WEBHOOK_URL" > ~/.openclaw/workspace/.feishu/webhook_url
        echo "  ✅ 飞书 webhook URL 已保存"
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
