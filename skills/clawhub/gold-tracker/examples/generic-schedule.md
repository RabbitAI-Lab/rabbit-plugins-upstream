# 通用定时任务调度（平台无关）

gold-tracker 不绑定任何特定调度器。唯一要求：**周期性调用一个幂等入口**，
推荐每 30 分钟执行一次 `sh examples/run_cycle.sh`（抓取 → 检测 → 发送）。

## 核心原则
1. 所有周期命令都幂等、可重复执行，重复运行无副作用（去重 + 冷却 + 状态机保证）。
2. 提醒检测是否「真的在跑」由 `verify.py check` 通过**心跳文件**判断，与用哪种调度器无关。
3. 市场分析（写日志、跑 analyze_check）消耗 token，不应放入高频调度，应由 Agent 在关键时段主动触发。

## 三种调度方式示例

### 1. cron
见 `examples/crontab.example`。

### 2. systemd timer
```bash
sudo cp examples/gold-tracker.service /etc/systemd/system/
sudo cp examples/gold-tracker.timer /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now gold-tracker.timer
```

### 3. Agent 平台 / CI / 任意定时任务
只要能在固定间隔执行一条命令即可，例如：
- Agent 平台自带定时任务：调度 `python3 scripts/fetch.py && python3 scripts/alert_manager.py detect && python3 scripts/notify.py send alerts`
- GitHub Actions / GitLab CI / cron 容器：`sh examples/run_cycle.sh`

## 验证「到底有没有在跑」
```bash
python3 scripts/verify.py check
```
若输出含「提醒检测 已 X 分钟未运行」或「从未运行」，说明调度未正确挂载。
