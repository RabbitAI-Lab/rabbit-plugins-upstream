# xhs-content-creator

小红书图文自动发布端到端 skill，把几张图变成一篇小红书笔记（草稿或真发）。

skill 完全自包含：所有路径基于 `__file__` 自动推导。安装位置：`~/.openclaw/workspace/skills/xhs-content-creator/`。

## 适合什么场景

适合：

- 已有自己授权的小红书账号
- 在飞书 DM 里发几张图，要求 agent 生成小红书草稿
- 把图文内容发布流程放到云端执行
- 能接受扫码登录这一步由人处理
- 希望保留运行截图、DOM 快照、结果 JSON、登录缓存

不适合：

- 绕过验证码、滑块、人机校验
- 批量互动、批量养号
- 操作未授权账号

## 当前默认链路

1. 用户在飞书 DM 发图片 → 输入"发小红书"
2. agent 调用 `image` 工具分析图片氛围
3. agent 生成标题（≤20 字）/ 正文（5 段）/ 话题（5-7 个）
4. agent 调用 `scripts/generate_and_publish.py`（默认 mode=draft）
5. 脚本 staging 图片到 `runtime/inbound/`、写 `runtime/my_content.json`
6. 调 `deploy/run_with_xvfb.sh` 启 Xvfb + Playwright
7. 调 `scripts/publish_xhs.py` 走 src/ 下的发布逻辑
8. 遇登录生成 `runtime/lobster-notify/<run_id>/login_qr.payload.json`
9. agent 把二维码图片发到飞书群 → 用户扫码 → 继续
10. 产出 `runtime/runs/<run_id>/{actions.jsonl,result.json,content.normalized.json,screenshots/,dom/}`

## 仓库结构

```text
config/                 平台配置与选择器（app.json / selectors.json）
src/                    核心发布逻辑（publisher / browser_session / audit 等 10 模块）
scripts/                CLI 入口（generate_and_publish.py / publish_xhs.py）
deploy/                 云端安装、运行、systemd 脚本
docs/                   部署文档、执行清单、通知协议
examples/               示例内容与素材
runtime/                运行目录（browser-profile / runs / lobster-notify / inbound）
SKILL.md                Skill 技术说明（agent 视角）
README.md               本文件（上手视角）
```

运行后会在本地产生：

```text
runtime/browser-profile/      持久化 Chromium profile（保留登录态）
runtime/runs/                 每次执行产物
runtime/lobster-notify/       龙虾消费通知 payload
runtime/inbound/              agent staging 进来的图片
```

这些目录默认不提交到 Git。

## 快速开始（手动）

### 1. 确认 skill 已就位

```bash
XHS_SKILL_ROOT="$HOME/.openclaw/workspace/skills/xhs-content-creator"
test -d "$XHS_SKILL_ROOT" || { echo "❌ skill not found"; exit 1; }
```

### 2. 安装系统依赖

```bash
bash "$XHS_SKILL_ROOT/deploy/install_system_ubuntu.sh"
```

### 3. 初始化项目环境（建 .venv + Playwright Chromium）

```bash
cd "$XHS_SKILL_ROOT"
bash deploy/bootstrap_project.sh
```

### 4. （可选）创建 .env 覆盖默认 MODE

skill 默认通过命令行参数传 MODE，**不需要 .env**。要覆盖 LOGIN_TIMEOUT 等参数时可写：

```bash
cd "$XHS_SKILL_ROOT"
cp deploy/env.example .env
# 编辑 .env
```

```env
MODE=draft
LOGIN_TIMEOUT=300
```

### 5. 手动跑一次（生成二维码）

```bash
cd "$XHS_SKILL_ROOT"
bash deploy/run_with_xvfb.sh
```

## agent 触发流程

agent 收到飞书图片 + "发小红书"后，调：

```bash
python3 "$XHS_SKILL_ROOT/scripts/generate_and_publish.py" \
  --image <图1绝对路径> \
  --image <图2绝对路径> \
  --image <图3绝对路径> \
  --title "🌇 西丽湖绿道｜夕阳和夏天的尾巴" \
  --body "绕了半个深圳，就为追这场日落。\n…" \
  --topic 西丽湖绿道 --topic 深圳散步 --topic 夏日氛围感 \
  --mode draft
```

stdout 返回 JSON 含 `status` / `mode` / `publisher_status` / `publisher_run_id`，agent 转发给用户。

## 关键文件

- [SKILL.md](./SKILL.md) — agent 视角的技术说明（收图 + 文案 + 调用链 + 已知坑）
- [docs/DEPLOY_TODO.md](./docs/DEPLOY_TODO.md) — workspace skill 自包含部署流程
- [docs/cloud_deploy.md](./docs/cloud_deploy.md) — 云端部署说明
- [docs/LOBSTER_NOTIFY_PROTOCOL.md](./docs/LOBSTER_NOTIFY_PROTOCOL.md) — 龙虾通知协议

## OpenClaw 运维注意

skill 启动 Chromium 时峰值 ~1.4GB。OpenClaw systemd cgroup 默认 MemoryMax=2G 会 OOM kill，**必须**调整为 2.4G：

```bash
sudo mkdir -p /etc/systemd/system/openclaw.service.d
sudo tee /etc/systemd/system/openclaw.service.d/override.conf <<'EOF'
[Service]
MemoryMax=2.4G
EOF
sudo systemctl daemon-reload
sudo systemctl restart openclaw.service
```

## 当前结论

当前这版是单机、单浏览器、单任务顺序执行方案：

- 云服务器负责跑浏览器
- skill 负责生成内容 + 截图 + 写 payload
- agent 负责把图片发到飞书群
- 你负责扫码

简单，够用，也最稳。