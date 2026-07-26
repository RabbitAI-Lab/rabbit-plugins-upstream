#!/bin/bash
# Jimeng AI Free API 启动脚本
# 由 Skill 管理，请勿手动修改

cd "$(dirname "$0")"

# 加载配置
export AUTHORIZATION=$(python3 -c "import json; print(json.load(open('config.json'))['sessionid'])")
export PORT=$(python3 -c "import json; print(json.load(open('config.json')).get('port', 8000))")

# 启动服务
nohup node dist/index.cjs > server.log 2>&1 &
echo $! > .service.pid

echo "服务启动中... (PID: $!)"
sleep 2

# 检查是否成功
if curl -s http://127.0.0.1:${PORT}/ping > /dev/null 2>&1; then
    echo "✅ 服务启动成功 (端口: ${PORT})"
else
    echo "⚠️ 服务可能未完全启动，请稍后检查状态"
fi
