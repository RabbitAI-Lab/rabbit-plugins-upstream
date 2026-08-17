# BidHunter v1.2 升级规划 · 2026-08-11

> 自动化周规划任务 · 由周一 10:00 升级自动化触发（本次于 8-11 周二执行）
> 状态：**规划阶段**，不直接改代码，待涛哥审阅后启动开发

---

## 一、本次目标版本

**v1.2 — 体验优化（"达"：推得到，收得着）**

### 版本顺位核对
| 来源 | 信息 |
|---|---|
| ROADMAP.md | v1.2 标记为 🎯 下次目标（2 周周期） |
| SKILL.md 当前版本号 | `1.1.0` |
| ClawHub 已发布版本 | `1.0.0` + `1.1.0`（latest = `1.1.0`） |
| 下一目标版本 | **v1.2.0**（ROADMAP 顺位 +1，符合预期） |

### ClawHub 当前数据
- 最新版本：1.1.0（2026-08-10 发布）
- 总下载量：128 次
- 评论：0 · Stars：1
- 距上次发布：1 天（本周内尚无外溢反馈）

---

## 二、本周用户反馈数据汇总

### 反馈来源
- ✅ 本地 `bid_cache/` 运行报告：暂无（v1.1 发布仅 1 天，涛哥尚未在本周跑过完整 pipeline）
- ✅ `bid_reports/` 历史报告：无
- ✅ ClawHub 评论区：0 条

### 误报模式分析
- **本周反馈样本 = 0**，无可统计的高频误报
- 上周（v1.0→v1.1 阶段）已通过 `_exclude_contexts` 表覆盖：电气石、广告位、视频监控、设计制造、系统集成等子串误报
- 规则库现状：`scripts/qual_rules.json` 的 `_exclude_contexts` 已含 14 项兜底排除，质量稳定

### 规划建议
- 本周暂无新误报修复优先级
- v1.2 重点放在推送通道升级，体验提升 > 匹配精度（v1.1 已重点优化精度）

---

## 三、核心交付物清单（依据 ROADMAP v1.2）

### 🥇 主交付（按实施优先级）

1. **`scripts/push_history.db`** — SQLite 本地推送历史存储
   - 表结构：`push_log(id, ts, channel, subject, verdict, status, retry_count, error_msg)`
   - 索引：`ts DESC`、`channel`、`status`
   - 30 天滚动清理

2. **`scripts/push_manager.py`** — 推送通道管理器
   - API：`send(channel, payload)` / `retry_failed()` / `get_history(days)` / `get_stats()`
   - 通道适配：钉钉（Webhook 加签）、企微（机器人 + 应用号）、邮件（SMTP）
   - 失败重试：指数退避 3 次 + 备用通道兜底

3. **`scripts/config_wizard.py`** — 交互式配置向导
   - 启动：`python3 scripts/config_wizard.py`
   - 流程：选通道 → 引导输入 Webhook/邮箱/密钥 → 测试连通 → 写入 `~/.config/bidhunter/push.yaml`
   - 支持一键测试 + 失败重试

### 🥈 次交付（体验增强）

4. **多通道并行** — 同一标讯可同时推企微 + 邮件
   - 配置：`push.yaml` 的 `channels: [wechat_bot, email]` 列表
   - 主通道失败自动切换备用通道

5. **推送失败告警** — 连续 3 天推送失败主动通知管理员
   - 检测：`push_manager.py --health-check`（每日 09:00 cron）
   - 告警通道：与推送主通道解耦，强制走邮件兜底

6. **定时任务可视化** — 查看下次执行、手动触发
   - 集成到 `status.py`：`status.py --schedule` 输出 cron 解析
   - `status.py --trigger-now` 立即跑一次 pipeline

### ⏸ 暂不实现（推迟）

- **飞书通道** — 按涛哥 2026-08-10 决策，推迟到 v1.5
- **可视化规则编辑器** — v1.5 任务

---

## 四、预计改动文件列表

### 新增文件
```
scripts/
├── push_manager.py        # 通道管理器（核心）
├── push_history.db        # SQLite 库（运行时自动创建）
└── config_wizard.py       # 交互式配置向导
```

### 修改文件
```
scripts/
├── pipeline.sh            # 接入 push_manager，--push-channel 参数
├── status.py              # 新增 --schedule / --trigger-now / --push-stats 子命令
└── qual_rules.json        # 不动（v1.2 不涉及匹配逻辑）

SKILL.md                   # 版本号升 1.1.0 → 1.2.0；v1.2 新特性章节
ROADMAP.md                 # v1.2 状态 🎯 → 🚧（开发中）；新增 changelog
```

### 不动文件
- `qual_check.py` / `bid_monitor.sh` / `report_html.py` / `report_text.py` / `quote_gen.py`（v1.2 不涉及匹配/采集/报告生成逻辑）

---

## 五、风险提示与规避（结合 ROADMAP 表）

| 风险 | 影响 | 规避策略 |
|---|---|---|
| 钉钉/企微机器人 Webhook 误配 | 推送失败且静默 | `config_wizard.py` 必须做连通性测试，未通过不允许写入配置 |
| SMTP 邮件被识别为垃圾邮件 | 兜底通道失效 | 引导用户用企业邮箱自建 SMTP，避免触发公共反垃圾规则 |
| SQLite 锁竞争（pipeline + push_manager 交叉写） | 推送历史丢失 | push_history.db 启用 WAL 模式；pipeline 写完后立即释放连接 |
| 通道密钥写错配置文件导致泄露 | 凭据外泄 | 配置存 `~/.config/bidhunter/push.yaml`（权限 600），不入 git；推送时不打印密钥 |
| 自动化任务重复触发推送 | 用户被打扰 | push_manager 内置幂等键（日期+主体），同日同标不重复推 |
| 网络抖动导致单次推送失败 | 误判为通道故障 | 重试 3 次后再标记失败，避免一次失败触发告警 |
| v1.1 → v1.2 配置兼容 | 老用户升级后推送配置失效 | push_manager 首次启动检测旧版配置（crontab 直推），自动迁移到 push.yaml |

---

## 六、关键里程碑（2 周周期）

| 时间 | 节点 | 交付标准 |
|---|---|---|
| 8-11（周二） | 规划输出 ✅ | 本文档 |
| 8-12 ~ 8-14 | 开发期 1 | push_history.db + push_manager.py 核心 CRUD + 钉钉通道 |
| 8-15 ~ 8-17 | 开发期 2 | 企微通道 + 邮件通道 + config_wizard.py |
| 8-18（周一） | 测试 + 试推 | 用真实 Webhook 跑一次完整推送，检查重试/告警 |
| 8-19（周二） | 写 changelog + 发布 | ClawHub 发布 v1.2.0 |

---

## 七、下一步动作（涛哥审阅）

1. **审阅本规划**：确认 v1.2 范围符合预期（推送通道 vs 其他）
2. **优先级确认**：是否优先做钉钉（国央企客户主流），还是三通道并行
3. **凭据准备**：涛哥需准备测试用的：
   - 钉钉机器人 Webhook（任一测试群）
   - 企微机器人 Webhook 或 App Key
   - 可用 SMTP 邮箱（QQ/163/企业邮箱）
4. **决策**：是否启动开发，或调整 v1.2 范围

---

## 八、发布检查清单（开发完成后使用）

- [ ] push_manager.py 单元测试通过（mock 三通道）
- [ ] config_wizard.py 在 macOS / Linux 终端可正常交互
- [ ] pipeline.sh 接入 push_manager，向后兼容（未配置推送时不报错）
- [ ] status.py 新增子命令正常返回
- [ ] SKILL.md 版本号 + 新特性章节更新
- [ ] CHANGELOG 写入 v1.2.0 changelog
- [ ] `clawhub skill publish . --slug bidhunter --owner 419597334-sudo --migrate-owner --version 1.2.0 --changelog "..."`
- [ ] ClawHub 上确认 v1.2.0 出现在 versions 列表
- [ ] ROADMAP.md v1.2 状态 🚧 → ✅，v1.5 状态 🎯 下次目标

---

_本规划由 BidHunter 周一升级自动化生成（实际执行日：2026-08-11 周二）。_