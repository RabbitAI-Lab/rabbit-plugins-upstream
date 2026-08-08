# xhs-content-creator 云端部署说明

本 skill 自包含部署在 workspace 目录下，所有路径基于 `__file__` 自动推导，无需独立项目根。

## 1. 目标

skill 自包含部署：

- skill 根目录：`~/.openclaw/workspace/skills/xhs-content-creator/`
- 运行方式：Xvfb + Playwright + Chromium
- 登录方式：人工扫码接管
- 通知方式：agent 读取 lobster-notify payload 代发飞书群图片消息

## 2. 服务器最低要求

- Ubuntu 22.04+（Ubuntu 24.04.4 LTS 实测）
- 2 vCPU
- 4G 左右内存（OpenClaw cgroup MemoryMax 调整到 2.4G 后跑单任务顺序执行够用）
- 20G 以上剩余磁盘
- root 权限

## 3. 需要装什么

分两层看。

### 系统级（整台机器）

- `python3`
- `python3-venv`
- `python3-pip`
- `xvfb`
- Playwright/Chromium 依赖库

### 项目级（skill 目录内）

- `.venv`（`deploy/bootstrap_project.sh` 自动建）
- `requirements.txt` 里的 Python 依赖
- Playwright Chromium（`bootstrap_project.sh` 自动装）
- `runtime/` 运行目录（已建好骨架 + `.gitkeep`）

## 4. 目录结构

```text
~/.openclaw/workspace/skills/xhs-content-creator/
├── config/
├── src/
├── scripts/
├── deploy/
├── docs/
├── examples/
├── runtime/                   # 运行产物（默认不提交 git）
│   ├── browser-profile/
│   ├── runs/
│   ├── lobster-notify/
│   └── inbound/
├── .venv/                     # 由 bootstrap_project.sh 建
└── SKILL.md
```

说明：

- `runtime/browser-profile/` 持久化保存（保留登录态）
- `runtime/runs/` 每次执行的截图、日志、结果
- `runtime/lobster-notify/` 给 agent 消费通知 payload
- `runtime/inbound/` agent 暂存飞书图片

## 5. 登录二维码接管方式

云端默认流程：

1. 打开小红书登录页
2. 截图保存二维码
3. 写出 `runtime/lobster-notify/<run_id>/login_qr.payload.json`
4. agent 读取这个 payload
5. agent 把二维码图片直接发到飞书群
6. 你手机扫码
7. 继续发布

重点：

- 不是靠公网链接扫码
- 是靠"图片直接发群"扫码

## 6. 当前默认通知机制

配置文件 [`config/app.json`](../config/app.json) 里默认：

```json
{
  "notify_qr_via": "lobster_channel"
}
```

表示 skill 不会自己发飞书 webhook，只生成 payload，由 agent 代发。

## 7. Agent 需要做什么

agent 只要实现下面这件事：

1. 监听或读取 `runtime/lobster-notify/<run_id>/login_qr.payload.json`
2. 取出其中的 `delivery.path`
3. 把这张图片发到飞书群
4. 把 `delivery.caption_lines` 一并作为说明文字发出

协议说明见：

- [LOBSTER_NOTIFY_PROTOCOL.md](./LOBSTER_NOTIFY_PROTOCOL.md)

## 8. 部署步骤

### 第一步：确认 skill 已就位

```bash
XHS_SKILL_ROOT="$HOME/.openclaw/workspace/skills/xhs-content-creator"
test -d "$XHS_SKILL_ROOT" || { echo "❌ skill not found"; exit 1; }
```

### 第二步：调整 OpenClaw systemd MemoryMax（关键）

Xvfb+Chromium 启动峰值 ~1.4GB，会撞穿 OpenClaw cgroup 默认 2GB 上限，整个 service 被 OOM kill，连带 background exec session 一锅端。**必须**先调：

```bash
sudo mkdir -p /etc/systemd/system/openclaw.service.d
sudo tee /etc/systemd/system/openclaw.service.d/override.conf <<'EOF'
[Service]
MemoryMax=2.4G
EOF
sudo systemctl daemon-reload
sudo systemctl restart openclaw.service
```

### 第三步：安装系统依赖

```bash
bash "$XHS_SKILL_ROOT/deploy/install_system_ubuntu.sh"
```

### 第四步：初始化 skill 环境（建 .venv + Playwright Chromium）

```bash
cd "$XHS_SKILL_ROOT"
bash deploy/bootstrap_project.sh
```

### 第五步：（可选）准备环境变量

skill 默认通过命令行传 MODE，**不需要 .env**。要覆盖时：

```bash
cd "$XHS_SKILL_ROOT"
cp deploy/env.example .env
```

当前常用项：

```env
MODE=draft
LOGIN_TIMEOUT=300
```

- `MODE=draft`：到草稿/发布前停下
- `MODE=publish`：真正触发发布
- `LOGIN_TIMEOUT`：扫码等待秒数

### 第六步：手动跑一次

```bash
cd "$XHS_SKILL_ROOT"
bash deploy/run_with_xvfb.sh
```

检查是否出现：

- 浏览器正常拉起
- `runtime/runs/<run_id>/screenshots/login_qr.png`
- `runtime/lobster-notify/<run_id>/login_qr.payload.json`

### 第七步：接通 agent 转发

agent 收到 payload 后，应直接把二维码图片发到飞书群。

这一步接通后，你就可以在飞书群里扫码登录。

### 第八步：托管为 systemd 服务（可选）

```bash
sudo cp "$XHS_SKILL_ROOT/deploy/systemd/xhs-content-creator-cloud.service" /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable xhs-content-creator-cloud.service
```

## 9. 风险点

- 云服务器 IP 可能触发小红书额外风控
- 登录态可能比本机更容易失效
- 扫码二维码有时效
- 小红书页面结构变化时，需要更新 selectors 和发布逻辑

## 10. 当前结论

对当前这套来说，最合适的方案就是：

- 云服务器负责跑浏览器
- skill 负责截二维码和写 payload
- agent 负责把图片发到飞书群
- 你负责扫码

简单，够用，也最稳。