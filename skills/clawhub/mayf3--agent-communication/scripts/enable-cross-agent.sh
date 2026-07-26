#!/bin/bash
# 启用跨Agent通信权限

CONFIG_FILE="$HOME/.openclaw/openclaw.json"

# 备份
cp "$CONFIG_FILE" "$CONFIG_FILE.backup.$(date +%Y%m%d_%H%M%S)"

# 添加sessions.visibility配置
jq '.tools.sessions.visibility = "all"' "$CONFIG_FILE" > /tmp/openclaw_config.json

# 验证
if [ $? -eq 0 ]; then
  mv /tmp/openclaw_config.json "$CONFIG_FILE"
  echo "✅ 已启用跨Agent通信权限"
  echo ""
  echo "配置已添加："
  jq '.tools.sessions' "$CONFIG_FILE"
  echo ""
  echo "⚠️  需要重启Gateway生效："
  echo "   openclaw gateway restart"
else
  echo "❌ 配置修改失败"
  exit 1
fi
