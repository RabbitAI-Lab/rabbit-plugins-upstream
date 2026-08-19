# 安全与数据保障说明

本技能已实现以下加固。修改脚本时请保持这些行为不回退，改动后逐项验证。

1. `query_tracking.py` 延迟加载配置：`--help`、参数校验和纯本地测试不依赖密钥文件。
2. 配置和订阅文件权限为 `0600`；任何输出不得包含 `app_key`、手机号尾号或 webhook。
3. 保存订阅时使用同目录临时文件 + `os.replace` 原子替换；Linux/macOS 下用文件锁（`fcntl`）避免定时检查与人工增删互相覆盖，Windows 下无 `fcntl` 时退化为无锁，原子替换仍保证文件不损坏。
4. 轨迹按 `AcceptTime` 解析后排序，不依赖 API 数组顺序；格式化和 `latest_trace` 共用同一实现。
5. `check_changes.py` 返回 `errors` / `error_count`；`--quiet` 只在"无变化且无错误"时静默；查询失败不覆盖已有成功基线。
6. `subscribe_tracking.py` 使用 argparse 子命令与命名参数，同时保留旧位置参数兼容期；带空格备注和平台/尾号解析有歧义时报错而不是猜。
7. JSON 模式保持 stdout 仅 JSON，诊断信息写 stderr；失败时返回非零退出码。
8. 公共逻辑集中在 `kuaidi_common.py`（状态映射、取件码提取、订阅读写）；`daily_check.py` 仅作为弃用兼容入口保留。
9. 损坏的 JSON 配置先报错并保留原文件，禁止以空数据覆盖。
10. 隐私策略在缺少群 ID 或配置异常时安全回退为脱敏（见 `privacy_settings.py`）。

## 发布前回归测试清单

无配置 `--help`、无订阅 list、重复添加、单个 check 不丢其他订阅、API 失败不覆盖成功基线、`--quiet` 下错误仍可见、并发写、乱序轨迹、取件码提取、JSON 可解析。
