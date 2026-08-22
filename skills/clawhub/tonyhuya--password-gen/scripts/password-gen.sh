#!/usr/bin/env bash
# password-gen: 安全密码生成器（纯本地，无网络依赖）
# 用法:
#   password-gen                  # 16位强密码（大小写+数字+符号）
#   password-gen 20               # 20位强密码
#   password-gen --no-symbol 16   # 不含符号
#   password-gen --pin 6          # 6位数字 PIN
#   password-gen --passphrase 4   # 4个单词的密码短语
set -euo pipefail

LEN=16
MODE="strong"

# 解析参数
while [ $# -gt 0 ]; do
  case "$1" in
    --no-symbol) MODE="nosym"; shift ;;
    --pin) MODE="pin"; shift ;;
    --passphrase) MODE="phrase"; shift ;;
    --help|-h) sed -n '2,9p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *)
      if [[ "$1" =~ ^[0-9]+$ ]]; then LEN="$1"; fi
      shift ;;
  esac
done

case "$MODE" in
  pin)
    [ "$LEN" -gt 18 ] && LEN=18
    echo "🔢 PIN（$LEN 位）：$(tr -dc '0-9' < /dev/urandom | head -c "$LEN")"
    ;;
  nosym)
    [ "$LEN" -gt 60 ] && LEN=60
    echo "🔐 密码（$LEN 位，字母+数字）：$(tr -dc 'A-Za-z0-9' < /dev/urandom | head -c "$LEN")"
    ;;
  phrase)
    WORDS="apple banana cherry dragon eagle forest grape honey island jungle kiwi lemon mango night ocean peach queen river silver tiger umbrella violet water yellow zebra"
    PHRASE=$(echo "$WORDS" | tr ' ' '\n' | shuf -n "$LEN" | tr '\n' '-')
    echo "🔑 密码短语：${PHRASE%-}"
    echo "（由 $LEN 个常见单词组成，易记难破）"
    ;;
  strong)
    [ "$LEN" -gt 60 ] && LEN=60
    echo "🔐 强密码（$LEN 位，含符号）：$(tr -dc 'A-Za-z0-9!@#$%^&*()_+-=' < /dev/urandom | head -c "$LEN")"
    ;;
esac
