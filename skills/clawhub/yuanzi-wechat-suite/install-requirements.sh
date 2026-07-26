#!/usr/bin/env bash
# yuanzi-wechat-suite 一键装依赖（macOS / Linux）

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_ROOT="$SCRIPT_DIR"

echo "==============================================="
echo "  yuanzi-wechat-suite v2.0.0 — 一键装依赖"
echo "==============================================="
echo ""

# 1) python3
if ! command -v python3 &>/dev/null; then
  echo "[X] python3 未装。请先装 Python 3.8+"
  exit 1
fi
echo "[OK] python3: $(python3 --version)"

# 2) node
if ! command -v node &>/dev/null; then
  echo "[X] node 未装。请先装 Node.js 14+"
  exit 1
fi
echo "[OK] node: $(node --version)"
echo ""

# 3) Python 依赖（master / publisher / image-gen）
echo "[1/3] 装 Python 依赖..."
python3 -m pip install --upgrade \
  markdown \
  requests \
  Pillow \
  beautifulsoup4 \
  pyyaml \
  keyring
echo "[OK] Python 依赖 OK"

# 4) Node 依赖（extractor）
echo ""
echo "[2/3] 装 Node 依赖（extractor）..."
EXT_DIR="$SKILL_ROOT/scripts/extractor"
cd "$EXT_DIR"
if [ -f "package.json" ]; then
  npm install
  echo "[OK] Node 依赖 OK"
else
  echo "[X] 未找到 scripts/extractor/package.json"
  exit 1
fi

# 5) 自检（4 个 wrapper）
echo ""
echo "[3/3] 自检..."
cd "$SKILL_ROOT"
bash "$SKILL_ROOT/yuanzi-extract" --check
bash "$SKILL_ROOT/yuanzi-image" --check
bash "$SKILL_ROOT/yuanzi-publish" --check
python3 "$SKILL_ROOT/scripts/yuanzi.py" --check

echo ""
echo "==============================================="
echo "  全部装完"
echo "==============================================="
echo ""
echo "下一步："
echo "  bash yuanzi-image --check        # 配图帆自检"
echo "  bash yuanzi-publish --check      # 发布桨自检"
echo "  bash yuanzi-extract --check      # 读稿锚自检"
echo "  python3 scripts/yuanzi.py --check # 总调度自检"
echo "  python3 scripts/yuanzi.py --help  # 总调度命令"
echo ""
echo "读稿配置（发布前）："
echo "  bash yuanzi-publish --install    # 装 Python 依赖"
echo "  python3 -c \"import keyring; keyring.set_password('wechat-article-publisher', '<AppID>', '<secret>')\""
echo ""
