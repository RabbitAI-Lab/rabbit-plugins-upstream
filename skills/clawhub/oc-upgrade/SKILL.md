---
name: "openclaw-upgrade"
description: "OpenClaw版本升级标准流程。每次说\"升级openclaw\"、\"openclaw升级\"、\"更新openclaw\"时必须执行，含Node版本+IPv4/IPv6探测"
---

# OpenClaw 升级技能

每次升级 OpenClaw 都必须严格按此流程执行，不能省步骤。

## Changelog

> description字段只写触发场景，不写变更记录；每次改动的原因/教训记在这里。

- 上次（4.14版本）因为没检查 lossless-claw 兼容性踩过坑
- 上次升级后忘记发完成通知，爸比等了7小时不知道结果
- 2026-07-27：NAS欢欢用自写脚本升级，脚本从gateway进程内部nohup启动，第一步systemctl stop把整个进程组一起杀掉，脚本自己被杀死，npm install根本没跑起来，gateway停了近6小时无人察觉——本skill的流程设计（npm install前不停服务、重启只在最后单独一步、重启前先设好通知cron）天然规避了这个坑，但重启这一步本身如果裸调systemctl也仍有被自身进程树波及的理论风险，已在第八步/回滚方案中改为优先走平台 gateway 工具
- 2026-07-27（同一事故的第二个坑）：NAS欢欢在手动拉起gateway后，agent恢复中断会话继续把npm包升到2026.7.1-2，但机器Node还是22.22.1，openclaw 2026.7.1-2要求Node≥22.22.3，导致gateway直接拒绝启动；排查过程中还发现该NAS访问registry.npmjs.org走IPv6比IPv4慢6倍（4秒 vs 0.66秒），跨版本升级触发的codex插件依赖安装卡在慢速IPv6连接上4分半没有进展——本skill第零步此前完全没有检查Node版本、也没有IPv4/IPv6速度探测，是两个真实缺口，已补入第零步
- 2026-07-27（第三个坑，元问题）：本skill（ClawHub slug: oc-upgrade）连续几次更新提案时，description字段被写成了"这次改了什么"的changelog摘要文风，覆盖掉了原本"每次说升级openclaw时必须执行"这类触发关键词描述。根据OpenClaw官方creating-skills文档："description is shown to the agent and in slash-command discovery"——description是agent判断"该不该调用这个skill"的唯一语义匹配依据，不是变更记录位置。description被写成changelog后，agent在用户说"升级openclaw"时无法语义匹配上这个skill，导致同一台NAS上并存的旧版本`openclaw-upgrade`（本地非ClawHub版本，description里保留了触发关键词）被误当成"唯一入口"，而已经更新到最新内容的`oc-upgrade`因description不含触发语义而从未被自然语言调用触发。教训固化为规则：description字段只写"什么场景触发"，绝不写"这次改了什么"；changelog类内容一律写在本节。

---

## 第零步：环境探测

在任何操作之前，先自动探测并汇报当前环境：

```bash
# === 环境探测 ===
echo "=== OpenClaw 环境 ==="
echo "用户: $(whoami)"
echo "Home: $HOME"

# npm global 路径
NPM_PREFIX=$(npm prefix -g 2>/dev/null || echo "unknown")
echo "npm global: $NPM_PREFIX"

# Node.js 版本检测（2026-07-27新增：NAS欢欢升级openclaw到2026.7.1-2后，
# 因Node版本(22.22.1)低于该版本要求的22.22.3，gateway直接拒绝启动，停机近1小时）
echo ""
echo "=== Node.js 版本 ==="
NODE_VER=$(node --version 2>/dev/null | sed 's/^v//')
echo "当前 Node: v${NODE_VER:-未知}"
if [ -z "$NODE_VER" ]; then
  echo "⚠️ 无法检测 Node 版本，node 命令不可用"
else
  NODE_MAJOR=$(echo "$NODE_VER" | cut -d. -f1)
  if [ "$NODE_MAJOR" -lt 22 ]; then
    echo "⚠️ Node 主版本 ${NODE_MAJOR} 低于 22，多数近期 OpenClaw 版本会拒绝启动"
  else
    echo "Node 主版本 ${NODE_MAJOR} ✅（具体最低子版本要求见第一步「目标版本」核对）"
  fi
fi
echo "⚠️ 注意：仅确认当前 Node 版本不够，必须在第一步拿到目标版本的具体 Node 最低版本要求后，
      两者对比才能判断是否需要先升级 Node。不要假设当前版本一定够用。"

# 代理检测
if curl -s --connect-timeout 3 -x "http://127.0.0.1:7890" https://registry.npmjs.org/ > /dev/null 2>&1; then
  PROXY_OPT="--proxy http://127.0.0.1:7890"
  echo "代理: 127.0.0.1:7890 ✅"
elif curl -s --connect-timeout 3 https://registry.npmjs.org/ > /dev/null 2>&1; then
  PROXY_OPT=""
  echo "代理: 直连 ✅"
else
  echo "⚠️ npm 网络不通，请检查代理"
fi

# IPv4/IPv6 速度探测（2026-07-27新增：NAS欢欢升级触发的codex插件依赖安装
# 卡在慢速IPv6连接上4分半没有进展，IPv6访问registry比IPv4慢6倍，是同一次事故的第二个真实缺口）
echo ""
echo "=== registry IPv4/IPv6 速度探测 ==="
IPV4_TIME=$(timeout 5 curl -4 -s -o /dev/null -w '%{time_total}' https://registry.npmjs.org/ 2>/dev/null)
IPV6_TIME=$(timeout 5 curl -6 -s -o /dev/null -w '%{time_total}' https://registry.npmjs.org/ 2>/dev/null)
echo "IPv4: ${IPV4_TIME:-超时/不可用}s"
echo "IPv6: ${IPV6_TIME:-超时/不可用}s"
if [ -z "$IPV6_TIME" ]; then
  echo "IPv6 不可用或超时，npm install 默认可能仍会尝试 IPv6 优先，建议升级/安装步骤强制 --force-ipv4 兜底"
elif python3 -c "exit(0 if float('$IPV6_TIME') > float('${IPV4_TIME:-999}') * 2 else 1)" 2>/dev/null; then
  echo "⚠️ IPv6 明显慢于 IPv4（超2倍），npm install/npm update 建议强制 IPv4 避免卡顿："
  echo "   npm config set prefer-ipv4 true   # 或临时: npm install --force-ipv4（部分npm版本可能不支持此flag，改用 NODE_OPTIONS='--dns-result-order=ipv4first'）"
  echo "   推荐：export NODE_OPTIONS=\"--dns-result-order=ipv4first\" 后再执行 npm install/update"
else
  echo "IPv4/IPv6 速度接近，无需特殊处理 ✅"
fi

# 可选组件检测
HAS_LOSSLESS=false
[ -d "$HOME/.openclaw/extensions/lossless-claw" ] && HAS_LOSSLESS=true
echo "lossless-claw: $HAS_LOSSLESS"

HAS_OVERRIDE=false
OVERRIDE="$HOME/.config/systemd/user/openclaw-gateway.service.d/override.conf"
[ -f "$OVERRIDE" ] && HAS_OVERRIDE=true
echo "override.conf: $HAS_OVERRIDE"

echo "服务管理: systemd --user"

# 多用户 /tmp/jiti 权限检查（防止 codex EACCES 问题）
if [ -d "/tmp/jiti" ]; then
  JITI_PERM=$(stat -c "%a" /tmp/jiti)
  if [ "$JITI_PERM" != "1777" ]; then
    echo "⚠️ /tmp/jiti 权限为 $JITI_PERM，多用户环境可能导致 codex EACCES 错误"
    echo "建议执行: sudo chmod 1777 /tmp/jiti"
  else
    echo "/tmp/jiti: 1777 ✅"
  fi
else
  echo "/tmp/jiti: 不存在 ✅"
fi

# 扫描其他 OpenClaw 用户（同机不同用户共享 npm global 升级风险）
echo ""
echo "=== 其他 OpenClaw 用户检测 ==="

SAME_HOST_USERS=""
for U in $(ls /home/ 2>/dev/null); do
  if [ "$U" != "$(whoami)" ] && [ -d "/home/$U/.openclaw" ]; then
    echo "用户(同主机): $U"
    SAME_HOST_USERS="$SAME_HOST_USERS $U"
  fi
done

WSL_INSTANCES=""
if command -v powershell.exe &>/dev/null; then
  WSL_LIST=$(powershell.exe -NoProfile -Command "wsl --list --verbose" 2>/dev/null | grep -i -v "NAME\|Windows" || true)
  if [ -n "$WSL_LIST" ]; then
    echo "$WSL_LIST" | while read -r INSTANCE; do
      INSTANCE=$(echo "$INSTANCE" | awk '{print $1}')
      if [ -n "$INSTANCE" ] && [ "$INSTANCE" != "$(hostname)" ]; then
        WSL_INSTANCES="$WSL_INSTANCES $INSTANCE"
        echo "WSL实例: $INSTANCE"
        if [ -d "/mnt/wsl/$INSTANCE/home/" ]; then
          for WU in /mnt/wsl/$INSTANCE/home/*/; do
            WU=$(basename "$WU")
            if [ -d "/mnt/wsl/$INSTANCE/home/$WU/.openclaw" ]; then
              echo "  → 用户 $WU 有 OpenClaw 安装"
              SAME_HOST_USERS="$SAME_HOST_USERS $WU@$INSTANCE"
            fi
          done
        fi
      fi
    done
  else
    echo "WSL列表: 无输出（WSL interop 可能不可用，跳过）"
  fi
else
  echo "WSL列表: powershell.exe 不可用，跳过"
fi

echo "npm global path: $(npm root -g 2>/dev/null)"
echo "npm global openclaw: $(ls -la "$(npm root -g 2>/dev/null)/openclaw/package.json" 2>/dev/null | awk '{print $3":"$4}')"

if [ -z "$SAME_HOST_USERS" ] && [ -z "$WSL_INSTANCES" ]; then
  echo "未发现其他 OpenClaw 用户 ✅"
else
  echo ""
  echo "⚠️ 发现其他 OpenClaw 用户/实例：$SAME_HOST_USERS $WSL_INSTANCES"
  echo "⚠️ npm install -g openclaw 会影响所有用户共享的 npm global 包"
  echo "⚠️ 升级前必须确认其他用户的 openclaw 和目标版本兼容（特别是插件）"
  echo "⚠️ 如果已知有其他用户但检测未命中（如 raven 在独立的 WSL 实例），请在升级前手动确认对方状态"
fi
```

向爸比汇报环境探测结果，确认后继续。

---

## 第一步：确认目标版本

```bash
openclaw --version
npm view openclaw version

GITHUB_TOKEN=*** GITHUB_TOKEN ~/.openclaw/.env | cut -d= -f2)
TARGET_VER=<目标版本，如 2026.5.12>
curl -s -H "Authorization: token $GITHUB_TOKEN" \
  "https://api.github.com/repos/openclaw/openclaw/releases/tags/v${TARGET_VER}" | \
  python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('body','')[:3000])"
```

**Node 版本兼容性核对（2026-07-27新增，与第零步 Node 检测配套）**：
```bash
npm view openclaw@${TARGET_VER} engines.node 2>&1
```
把这个结果和第零步检测到的当前 Node 版本对比：
- 若当前 Node 满足要求 → 正常继续
- 若不满足 → **必须在第六步执行升级前先升级 Node**（同机器同大版本线内的 apt/nvm 升级即可，不要跨大版本线），否则升级完 openclaw 包后 gateway 会直接拒绝启动

向爸比汇报：当前版本、目标版本、release highlights 摘要、**Node 版本是否满足要求**，等爸比确认目标版本（若 Node 不满足，一并确认是否同意先升级 Node）。

---

## 第二步：检查插件兼容性

```bash
openclaw plugins list 2>/dev/null | grep "enabled"
```

针对**每个 enabled 插件**，在 release notes 里搜索对应关键词：

```bash
GITHUB_TOKEN=*** GITHUB_TOKEN ~/.openclaw/.env | cut -d= -f2)
curl -s -H "Authorization: token $GITHUB_TOKEN" \
  "https://api.github.com/repos/openclaw/openclaw/releases/tags/v${TARGET_VER}" | \
  python3 -c "
import json,sys
d=json.load(sys.stdin)
body = d.get('body','')
keywords = ['feishu', 'lossless', 'minimax', 'anthropic', 'deepseek', 'openai', 'memory-core']
for kw in keywords:
    lines = [l.strip() for l in body.split('\n') if kw.lower() in l.lower() and l.strip()]
    if lines:
        print(f'=== {kw} ===')
        for l in lines[:5]: print(' ', l)
"
```

重点关注：
- **lossless-claw**：手动装的 global 插件，历史上踩过坑，必须关注
- **@openclaw/feishu**：openclaw 自管 npm，升级可能改版本
- 其余 stock 插件随主包升级，通常无需额外处理

向爸比汇报兼容性评估，有⚠️风险说清楚。

---

## 第三步：记录插件快照

```bash
openclaw plugins list 2>/dev/null > /tmp/plugins-before-${TARGET_VER}.txt
echo "✅ 插件快照已保存 → /tmp/plugins-before-${TARGET_VER}.txt"
```

---

## 第四步：备份

```bash
CURRENT_VER=$(openclaw --version 2>/dev/null | grep -oP '[\d.]+' | head -1)
OVERRIDE="$HOME/.config/systemd/user/openclaw-gateway.service.d/override.conf"
FEISHU_DIR="$HOME/.openclaw/npm/node_modules/@openclaw/feishu"
LOSSLESS_DIR="$HOME/.openclaw/extensions/lossless-claw"

cp ~/.openclaw/openclaw.json ~/.openclaw/openclaw.json.bak-${CURRENT_VER}
echo "1/5 openclaw.json ✅"

if [ -f "$OVERRIDE" ]; then
  cp "$OVERRIDE" "${OVERRIDE}.bak-${CURRENT_VER}"
  echo "2/5 override.conf ✅"
else
  echo "2/5 override.conf 不存在，跳过 ✅"
fi

cp ~/.openclaw/.env ~/.openclaw/.env.bak-${CURRENT_VER}
echo "3/5 .env ✅"

if [ -d "$LOSSLESS_DIR" ]; then
  LOSSLESS_VER=$(cat "$LOSSLESS_DIR/package.json" | \
    python3 -c "import json,sys;print(json.load(sys.stdin)['version'])")
  LOSSLESS_NM_SIZE=$(du -sm "$LOSSLESS_DIR/node_modules/" 2>/dev/null | cut -f1)
  LOSSLESS_BAK="$HOME/.openclaw/extensions/lossless-claw.bak-${LOSSLESS_VER}"
  mkdir -p "$LOSSLESS_BAK"
  if [ "${LOSSLESS_NM_SIZE:-0}" -gt 500 ]; then
    cp "$LOSSLESS_DIR/package.json" "$LOSSLESS_BAK/"
    cp "$LOSSLESS_DIR/openclaw.plugin.json" "$LOSSLESS_BAK/"
    cp -r "$LOSSLESS_DIR/dist" "$LOSSLESS_BAK/"
    echo "4/5 lossless-claw (dist only, node_modules=${LOSSLESS_NM_SIZE}MB 过大跳过) ✅"
  else
    cp -r "$LOSSLESS_DIR/." "$LOSSLESS_BAK/"
    echo "4/5 lossless-claw (完整备份) ✅"
  fi
else
  echo "4/5 lossless-claw 不存在，跳过 ✅"
fi

if [ -d "$FEISHU_DIR" ]; then
  mkdir -p "${FEISHU_DIR}.bak-${CURRENT_VER}"
  cp "$FEISHU_DIR/package.json" "${FEISHU_DIR}.bak-${CURRENT_VER}/"
  echo "5/5 feishu ✅"
else
  echo "5/5 feishu 插件目录不存在，跳过 ✅"
fi

echo ""
echo "=== 备份清单 ==="
ls ~/.openclaw/openclaw.json.bak-${CURRENT_VER} 2>/dev/null && echo "✅ openclaw.json"
ls ~/.openclaw/.env.bak-${CURRENT_VER} 2>/dev/null && echo "✅ .env"
[ -f "${OVERRIDE}.bak-${CURRENT_VER}" ] && echo "✅ override.conf" || echo "⏭ override.conf (不存在)"
ls -d "$HOME/.openclaw/extensions/lossless-claw.bak-"* 2>/dev/null | tail -1 | xargs -I{} echo "✅ {}" || echo "⏭ lossless-claw (不存在)"
ls -d "${FEISHU_DIR}.bak-${CURRENT_VER}" 2>/dev/null && echo "✅ feishu" || echo "⏭ feishu (不存在)"
```

确认核心备份（openclaw.json + .env）存在后再继续。

---

## 第五步：设好重启后通知 cron（先于重启执行）

gateway 重启会中断当前 session，重启后欢欢是全新上下文，不会记得升级完成这件事。
**必须在重启前设好一次性 systemEvent cron，重启后自动触发通知爸比。**

用 `cron` 工具创建：
- `schedule`: `at`，时间 = 当前时间 + 3 分钟
- `payload.kind`: `systemEvent`
- `payload.text`: 升级完成通知（含版本号、插件状态、耗时）
- `sessionTarget`: `main`
- `deleteAfterRun`: `true`

示例通知文本：
```
🎉 OpenClaw 升级完成！v<旧版本> → v<新版本>，插件全部正常（lossless-claw ✅ feishu ✅），耗时约X分钟。
```

> ⚠️ **3分钟是经过实践的安全值**，90秒有时会在 gateway 恢复前触发导致通知失败。

cron 创建成功后，再执行下一步。

---

## 第六步：执行升级

**等爸比说「执行」才动手。**

> ⚠️ 如果第零步检测到其他 OpenClaw 用户，向爸比汇报后再执行。
> ⚠️ 如果第一步核对发现当前 Node 版本不满足目标版本要求，**必须先升级 Node**，确认 `node --version` 达标后再继续本步骤。

```bash
if curl -s --connect-timeout 3 -x "http://127.0.0.1:7890" https://registry.npmjs.org/ > /dev/null 2>&1; then
  export HTTP_PROXY=http://127.0.0.1:7890
  export HTTPS_PROXY=http://127.0.0.1:7890
  echo "使用代理: 127.0.0.1:7890"
else
  echo "直连安装"
fi

if [ "${IPV6_SLOWER:-0}" = "1" ]; then
  export NODE_OPTIONS="--dns-result-order=ipv4first"
  echo "已强制 DNS 优先 IPv4（IPv6 检测偏慢）"
fi

npm install -g openclaw@${TARGET_VER}
```

---

## 第七步：验证

```bash
openclaw --version
node --version

openclaw doctor --fix 2>&1 | tail -5
openclaw doctor

FAILED=$(openclaw plugins list 2>/dev/null | grep -i "fail\|error" | grep -v "grep")
if [ -n "$FAILED" ]; then
  echo "⚠️ 检测到插件加载失败："
  echo "$FAILED"
  if echo "$FAILED" | grep -qi "feishu"; then
    echo "🔧 feishu 插件失败，强制重装..."
    openclaw plugins install --force @openclaw/feishu 2>&1
    echo "⚠️ 重装后需要重启 gateway"
  fi
else
  echo "✅ 所有插件加载正常"
fi

diff /tmp/plugins-before-${TARGET_VER}.txt <(openclaw plugins list 2>/dev/null)
```

验收标准（全部通过才继续）：
- ✅ 版本 = 目标版本
- ✅ Node 版本满足目标版本 engines.node 要求
- ✅ lossless-claw（若存在）仍在 enabled 列表
- ✅ feishu（若存在）仍在 enabled 列表
- ✅ doctor Errors = 0
- ✅ 无插件加载失败

有任何一项不通过 → 立即执行回滚，不继续。

---

## 第八步：重启 gateway

**优先用平台 `gateway` 工具（action=restart）执行重启，而不是裸调 `systemctl restart`。**

```
优先：gateway 工具，action=restart，并带上 note 说明"OpenClaw 升级完成，重启生效"
```

若无 `gateway` 工具可用，才退回裸调：

```bash
systemctl --user restart openclaw-gateway.service
```

**重启后如果新版本触发了插件依赖首次安装（如新版 codex 插件），日志会出现类似 `npm install` 子进程且短时间内端口不监听是正常现象**；观察其 node_modules 增长/CPU占用判断是否卡死，若卡在慢速 IPv6 上超过 3 分钟无进展，可参考第零步的 IPv4 强制方案排查，不要贸然 kill 掉该子进程。

第五步设好的 cron 会在重启后 90 秒内自动触发，通知爸比升级完成。

---

## ⏪ 回滚方案

任一步骤出问题立即执行：

```bash
PREV_VER=<回退版本，如 2026.5.6>
OVERRIDE="$HOME/.config/systemd/user/openclaw-gateway.service.d/override.conf"
FEISHU_DIR="$HOME/.openclaw/npm/node_modules/@openclaw/feishu"
LOSSLESS_BAK=$(ls -d "$HOME/.openclaw/extensions/lossless-claw.bak-"* 2>/dev/null | sort | tail -1)

if curl -s --connect-timeout 3 -x "http://127.0.0.1:7890" https://registry.npmjs.org/ > /dev/null 2>&1; then
  export HTTP_PROXY=http://127.0.0.1:7890
  export HTTPS_PROXY=http://127.0.0.1:7890
fi
npm install -g openclaw@${PREV_VER}

cp ~/.openclaw/openclaw.json.bak-${PREV_VER} ~/.openclaw/openclaw.json
cp ~/.openclaw/.env.bak-${PREV_VER} ~/.openclaw/.env

if [ -f "${OVERRIDE}.bak-${PREV_VER}" ]; then
  cp "${OVERRIDE}.bak-${PREV_VER}" "$OVERRIDE"
  echo "override.conf 已还原 ✅"
else
  echo "override.conf 备份不存在，跳过 ✅"
fi

if [ -n "$LOSSLESS_BAK" ] && [ -d "$LOSSLESS_BAK" ]; then
  rm -rf "$HOME/.openclaw/extensions/lossless-claw"
  cp -r "$LOSSLESS_BAK" "$HOME/.openclaw/extensions/lossless-claw"
  echo "lossless-claw 已还原 ✅"
else
  echo "lossless-claw 备份不存在，跳过 ✅"
fi

systemctl --user daemon-reload
```
优先：gateway 工具，action=restart，并带上 note 说明"OpenClaw 回滚完成，重启生效"

若无 gateway 工具可用，才退回：
```bash
systemctl --user restart openclaw-gateway.service
```

等飞书收到「欢欢重启完毕，在线了 🐾」，告知爸比回滚完成及原因。

---

## 注意事项

- **不要用 `gateway update.run` 升级**，npm 手动指定版本更可控
- **重启一律优先走平台 `gateway` 工具（action=restart）**，不裸调 systemctl
- **升级前必须核对目标版本的 Node 最低要求**（`npm view openclaw@<版本> engines.node`），不满足要先升级 Node 再装 openclaw
- **npm install 卡顿优先排查 IPv4/IPv6 速度差异**（`curl -4`/`curl -6` 对比测速），若 IPv6 明显慢，用 `NODE_OPTIONS="--dns-result-order=ipv4first"` 强制优先 IPv4
- **skill description字段只写触发场景，不写变更记录**（2026-07-27元教训：description是agent discovery语义匹配依据，写成changelog会导致agent无法自然语言触发这个skill，历史更新记录见上方Changelog小节）
- **feishu 插件路径**：`~/.openclaw/npm/node_modules/@openclaw/feishu`（openclaw 自管，非 npm global）
- **lossless-claw 路径**：`~/.openclaw/extensions/lossless-claw`（openclaw 自管）
- **systemd service 不读 .bashrc**，代理若需在 service 中生效，需配置 override.conf 或 EnvironmentFile
- **lossless-claw 踩坑**：2026-04-14 升级 4.14 不兼容，回退 4.11 解决，每次升级必须检查
- **MiniMax 不调用 message 工具**，涉及发消息的 cron 不要用 MiniMax
- **brave 插件外部化（2026.5.12 起）**：升级后如果遇到 "web_search provider is not available: brave"，执行 `openclaw plugins install --force @openclaw/brave-plugin` 后重启
- **feishu 插件不兼容**：升级后 feishu 注册失败时，执行 `openclaw plugins install --force @openclaw/feishu` 后重启
- **codex EACCES 错误**：多用户同机时，`/tmp/jiti/` 目录需要 sticky bit（`sudo chmod 1777 /tmp/jiti`），否则不同用户的 codex 会互相冲突
- **多用户兼容风险**：`npm install -g openclaw` 会覆盖全局包，影响同机所有 OpenClaw 用户
- **升级完成通知 cron**：设置 3 分钟而非更短，防止 gateway 还未完全恢复时触发

---

## 开源版说明

- 技能适配 OpenClaw 所有标准部署（WSL2/Linux VM/原生 Linux）
- 如果使用代理，自动检测 127.0.0.1:7890，也可在执行前手动 `export HTTP_PROXY=http://your-proxy:port`
- lossless-claw / override.conf 均为可选组件，不存在时自动跳过，不会报错中断
- 服务管理默认 `systemd --user`，如使用其他方式（如 pm2、docker）请修改第八步的重启命令
- 首次使用前建议先执行第零步（环境探测），确认环境配置正确
