#!/usr/bin/env bash
# 为 SkillHub 轻量包补齐 vendor 依赖：只使用本包版本 GitHub Release 且带 SHA-256 校验，
# 兼容 full 两种命名；校验文件缺失或哈希不一致一律拒绝解压/执行。
set -euo pipefail
QUIET=0
[ "${1:-}" = "--quiet" ] && QUIET=1
say() { [ "$QUIET" = 0 ] && echo "$*"; }
SHA_BIN="$(command -v shasum || command -v sha256sum || true)"
[ -n "$SHA_BIN" ] || { echo "缺少 sha256sum/shasum 校验工具" >&2; exit 1; }
calc_sha256() {
  if [ "${SHA_BIN##*/}" = "shasum" ]; then "$SHA_BIN" -a 256 "$1" | awk '{print $1}'
  else "$SHA_BIN" "$1" | awk '{print $1}'; fi
}
SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REPO="${CAD_FILE_READER_REPO:-lisong2003-lgtm/cad-file-reader}"
MANIFEST="$SKILL_DIR/manifest.json"
PKG_VER="$(sed -n 's/.*"version"[ ]*:[ ]*"\([^"]*\)".*/\1/p' "$MANIFEST" 2>/dev/null | head -1)"
WANT="${CAD_FILE_READER_VERSION:-${PKG_VER:-0.28.5}}"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT

# ---- 幂等预检：vendor 已解压且含核心库 -> 直接退出，避免重复下载 ----
_DEST="$SKILL_DIR/vendor"
_unpacked_ok() {
  [ -d "$_DEST/ezdwg" ] && [ -d "$_DEST/ezdxf" ] && [ -d "$_DEST/fontTools" ]
}
if _unpacked_ok && [ "${CAD_FORCE_INSTALL:-0}" != "1" ]; then
  echo "vendor 已存在，未变更（如需强制重装：export CAD_FORCE_INSTALL=1）"
  exit 0
fi
if [ -d "$_DEST" ]; then find "$_DEST" -depth -delete; fi


verify_download() {
  # 用同 Release 的 SHA256SUMS 校验完整包，校验失败一律拒绝解压/执行
  local v="$1"
  local exp actual
  for u in \
    "https://github.com/${REPO}/releases/download/v${v}/SHA256SUMS-cad-file-reader-${v}.txt" \
    "https://github.com/${REPO}/releases/download/v${v}/SHA256SUMS.txt"; do
    if curl -sL --http1.1 --fail --max-time "${CAD_DOWNLOAD_TIMEOUT:-600}" "$u" -o "$TMP/sums.txt"; then
      exp="$(grep -E "cad-file-reader-full-${v}\.zip[[:space:]]*$|cad-file-reader-full-${v}\.zip$" "$TMP/sums.txt" | awk '{print $1}' | head -1)"
      if [ -z "$exp" ] && [ "$v" != "0.28.5" ]; then
        exp="$(grep -E "full-${v}\.zip" "$TMP/sums.txt" | awk '{print $1}' | head -1)"
      fi
      if [ -n "$exp" ]; then
        actual="$(calc_sha256 "$TMP/full.zip")"
        if [ "$actual" = "$exp" ]; then
          say "SHA-256 校验通过 ✓ ($v)" >&2
          return 0
        fi
        say "SHA-256 校验失败，拒绝使用下载包 ($v)" >&2
        return 1
      fi
      say "校验文件里缺少 $v 的完整包条目，改用下一命名…" >&2
    fi
  done
  say "未取得 $v 的校验文件，为安全起见不执行未校验下载包。" >&2
  return 1
}

fetch() {
  local v="$1"
  local url
  for url in \
    "https://github.com/${REPO}/releases/download/v${v}/cad-file-reader-full-${v}.zip" \
    "https://github.com/${REPO}/releases/download/v${v}/cad-file-reader-${v}-full.zip"; do
    say "尝试 $url" >&2
    if curl -sL --http1.1 --fail --max-time "${CAD_DOWNLOAD_TIMEOUT:-600}" "$url" -o "$TMP/full.zip"; then
      if verify_download "$v"; then
        if unzip -oq "$TMP/full.zip" "*/vendor/*" -d "$TMP" 2>/dev/null \
           && { [ -d "$TMP/cad-file-reader/vendor" ] || [ -n "$(find "$TMP" -type d -name vendor -print -quit)" ]; }; then
          return 0
        fi
        say "解压后未找到 vendor，继续尝试下一个命名…" >&2
      fi
    fi
  done
  return 1
}

if fetch "$WANT"; then
  :
else
  say "本包版本 v${WANT} 的完整包不可用或未通过 SHA-256 校验，未安装 vendor。" >&2
  say "请先检查网络可访问 https://github.com/${REPO} 后重试，或手动运行：" >&2
  cat >&2 <<'MSG'
  python3 -m pip install "ezdwg==0.12.6" "ezdxf==1.4.4" fonttools pyparsing numpy
再把安装目录加入 PYTHONPATH；或设置 CAD_FILE_READER_REPO 指向带 SHA256SUMS 的发布仓库。
MSG
  exit 3
fi

DEST="$SKILL_DIR/vendor"
if [ -d "$DEST" ]; then find "$DEST" -depth -delete; fi
SRC="$(find "$TMP" -type d -name vendor -print -quit)"
cp -R "$SRC" "$DEST"
echo "vendor 已安装到 $DEST"
echo "许可证与第三方依赖清单见 NOTICE.md（MIT/BSD）"
