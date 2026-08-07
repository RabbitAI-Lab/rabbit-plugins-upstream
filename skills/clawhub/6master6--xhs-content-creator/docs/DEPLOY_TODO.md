# workspace skill 自包含部署流程

目标机器：

- Ubuntu 24.04.4 LTS
- root 用户
- skill 根目录：`~/.openclaw/workspace/skills/xhs-content-creator/`

> 本文档配套 skill：`xhs-content-creator`。skill 完全自包含，所有路径基于 `__file__` 自动推导。

## 第一步：放置 skill 代码

确认代码位于（用环境变量简写）：

```bash
XHS_SKILL_ROOT="${XHS_SKILL_ROOT:-$HOME/.openclaw/workspace/skills/xhs-content-creator}"
test -d "$XHS_SKILL_ROOT" || { echo "❌ skill not found at $XHS_SKILL_ROOT"; exit 1; }
```

如需从仓库拉取或同步，由 agent 触发（git pull / clawhub sync）。

## 第二步：安装系统依赖

执行：

```bash
bash "$XHS_SKILL_ROOT/deploy/install_system_ubuntu.sh"
```

完成后回报：

- `xvfb` 是否安装成功
- 系统依赖是否安装成功
- 是否有报错

## 第三步：OpenClaw systemd 内存上限调整（关键）

Xvfb(~50MB) + Chromium(~500MB-1GB) 启动时会撞穿 OpenClaw cgroup 2GB 硬上限，整个 service 被 OOM kill，连带 background exec session 一锅端（**2026-08-03 踩过这个坑**）。

执行：

```bash
sudo mkdir -p /etc/systemd/system/openclaw.service.d
sudo tee /etc/systemd/system/openclaw.service.d/override.conf <<'EOF'
[Service]
MemoryMax=2.4G
EOF
sudo systemctl daemon-reload
sudo systemctl restart openclaw.service
```

验证：

```bash
systemctl show openclaw.service | grep -E 'MemoryMax|MemoryCurrent'
```

预期：`MemoryMax=2415919104`（2.4G），`MemoryCurrent` 跑通后峰值 ~1.4GB。

## 第四步：初始化 skill 环境（项目级）

执行：

```bash
cd "$XHS_SKILL_ROOT"
bash deploy/bootstrap_project.sh
```

完成后回报：

- `.venv` 是否创建成功
- `pip install -r requirements.txt` 是否成功
- `python -m playwright install chromium` 是否成功

## 第五步：环境变量（可选）

skill 默认通过命令行参数传递 `MODE`，**不需要创建 `.env` 文件**。

如需覆盖默认值（如自定义 LOGIN_TIMEOUT），可在 `$XHS_SKILL_ROOT/.env`（skill 外部，不提交 git）写入：

```env
MODE=draft
LOGIN_TIMEOUT=300
```

说明：

- `MODE=draft`：只走到草稿（推荐日常使用）
- `MODE=publish`：真正触发发布
- `LOGIN_TIMEOUT`：等待扫码秒数（默认 300）

## 第六步：手动验证

执行：

```bash
cd "$XHS_SKILL_ROOT"
bash deploy/run_with_xvfb.sh
```

观察结果：

- 是否成功启动浏览器
- 是否生成二维码截图
- 是否生成 lobster 通知 payload
- 是否生成 `runtime/runs/<timestamp>/`

关键文件：

- `runtime/runs/<run_id>/screenshots/login_qr.png`
- `runtime/lobster-notify/<run_id>/login_qr.payload.json`

## 第七步：Agent 转发飞书群

agent 需要读取：

```text
$XHS_SKILL_ROOT/runtime/lobster-notify/<run_id>/login_qr.payload.json
```

然后：

1. 读取 `delivery.path`
2. 把这张二维码图片发到飞书群
3. 把 `delivery.caption_lines` 一并发出

协议文档：[LOBSTER_NOTIFY_PROTOCOL.md](./LOBSTER_NOTIFY_PROTOCOL.md)

## 第八步：托管为 systemd 服务（可选）

如果手动验证通过，可把发布链路托管为 systemd 服务：

```bash
sudo cp "$XHS_SKILL_ROOT/deploy/systemd/xhs-content-creator-cloud.service" /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable xhs-content-creator-cloud.service
```

如需手动启动：

```bash
sudo systemctl start xhs-content-creator-cloud.service
```

查看日志：

```bash
journalctl -u xhs-content-creator-cloud.service -n 200 --no-pager
```

> service 文件中的 `WorkingDirectory` / `ExecStart` 已指向 `~/.openclaw/workspace/skills/xhs-content-creator/`，无需手动改 service 内容。

## 回报格式

每完成一步，请回报：

1. 执行了什么命令
2. 成功还是失败
3. 如果失败，贴关键报错
4. 当前卡在哪一步