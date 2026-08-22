# 快递变化检查调度说明

本文件只说明推荐配置，**不代表当前已经存在定时任务**。创建、更新或删除调度前必须先检查 OpenClaw 当前任务，并获得用户明确请求。

## 检查命令

```bash
python3 ~/.openclaw/workspace/skills/kuaidi-query/scripts/check_changes.py --quiet
```

退出和输出约定：

- 无变化且无错误：退出码 `0`，无 stdout。
- 有变化：退出码 `0`，stdout 输出 JSON，读取 `changes[].message` 后通知。
- 有查询或数据错误：非零退出码，stdout 输出 JSON，读取 `errors[]` 后报告；不能当成“无变化”。

## 推荐频率

物流运输期间通常每 30 分钟检查一次即可。是否启用、通知到哪个会话以及何时停用，都由用户决定。

## 手动验证

```bash
# 查询但不更新基线
python3 ~/.openclaw/workspace/skills/kuaidi-query/scripts/check_changes.py --dry-run

# 模拟调度静默模式
python3 ~/.openclaw/workspace/skills/kuaidi-query/scripts/check_changes.py --quiet

# 新订阅首次查询也作为变化返回
python3 ~/.openclaw/workspace/skills/kuaidi-query/scripts/check_changes.py --include-first-seen
```

订阅数据：`~/.openclaw/subscribe/kuaidi.json`。脚本使用锁和原子替换更新该文件。
