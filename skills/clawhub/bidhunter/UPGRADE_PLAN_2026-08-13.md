# BidHunter v1.2 升级规划 · 2026-08-13

> 自动化周规划任务 · 由周一 10:00 升级自动化触发（本周一 2026-08-13）
> 状态：**开发期**，沿用上周规划路线，本周进入代码实施
> 上次规划：UPGRADE_PLAN_2026-08-11.md（v1.2 范围已确认）

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

### ClawHub 当前数据（vs 上次规划对比）

| 指标 | 8-11 规划 | 8-13 本次 | 增量 |
|---|---|---|---|
| 最新版本 | 1.1.0 | 1.1.0 | — |
| 总下载量 | 128 | **152** | **+24（3 天自然增长 18.7%）** |
| Stars | 1 | 1 | — |
| 评论 | 0 | 0 | — |
| 距上次发布 | 1 天 | 3 天 | 自然下载仍在爬坡期 |

**结论**：v1.1 发布后下载量稳定增长（无负面评论），无紧急修复需求，按 ROADMAP 推进 v1.2。

---

## 二、上周规划回顾（2026-08-11 → 2026-08-13）

✅ **已确认事项**
- v1.2 范围 = 推送通道升级（钉钉🥇 / 企微🥈 / 邮件🥉）
- 飞书通道推迟到 v1.5（按涛哥 8-10 决策）
- 实施优先级：`push_history.db` + `push_manager.py` → `config_wizard.py` → 多通道并行 + 失败告警

⏳ **本周开发启动任务**（按上次规划里程碑）
- [ ] 8-12 ~ 8-13：push_history.db 建表 + push_manager.py 核心 CRUD + 钉钉通道适配
- [ ] 8-14 ~ 8-16：企微通道 + 邮件通道 + config_wizard.py
- [ ] 8-17（周日）：多通道并行 + 失败告警
- [ ] 8-18（周一）：测试 + 真实 Webhook 试推
- [ ] 8-19（周二）：写 changelog + 发布 v1.2.0

---

## 三、本周用户反馈数据汇总

### 反馈来源扫描

| 来源 | 状态 | 样本数 |
|---|---|---|
| 本地 `bid_cache/` 报告 | ❌ 空（v1.1 发布后 3 天未跑完整 pipeline） | 0 |
| `bid_reports/` 历史报告 | ❌ 空 | 0 |
| ClawHub 评论区 | ❌ 无评论 | 0 |
| **本周反馈样本合计** | — | **0** |

### 误报模式分析

- **本周反馈样本 = 0**，无可统计的高频误报
- 规则库现状：`scripts/qual_rules.json` 的 `_exclude_contexts` 已含 14 项兜底排除（电气石 / 广告位 / 视频监控 / 系统集成 / 等），v1.1 已重点优化精度
- **规划建议**：本周无新误报修复优先级，v1.2 集中在推送通道（体验提升 > 匹配精度）

### 历史误报回顾（v1.1 修复存档）

| 模式 | v1.1 修复方案 | 验证状态 |
|---|---|---|
| "电气"误匹配"电气石" | smart_match 右边界 1 字 CJK 阻断 | ✅ 已修复 |
| "广告"误匹配"户外广告设施拆除" | _exclude_contexts 兜底 | ✅ 已修复 |
| "视频监控"误入主体能力词 | 红警冲突检测 + _exclude_contexts | ✅ 已修复 |
| "设计制造"覆盖过宽 | 边界感知 + 上下文排除 | ✅ 已修复 |

---

## 四、核心交付物清单（沿用 ROADMAP v1.2）

### 🥇 主交付（本周实施重点）

#### 1. `scripts/push_history.db` — SQLite 推送历史库

```
表结构：push_log
├── id          INTEGER PRIMARY KEY
├── ts          TIMESTAMP   (发送时间)
├── channel     TEXT        (dingtalk/wecom/email)
├── subject     TEXT        (标讯标题)
├── verdict     TEXT        (可投/不可投/需确认)
├── status      TEXT        (success/failed/retried)
├── retry_count INTEGER     (重试次数)
└── error_msg   TEXT        (失败原因)
```

- 索引：`ts DESC`、`channel`、`status`
- 30 天滚动清理（启动时检查）

#### 2. `scripts/push_manager.py` — 推送通道管理器

```
API 接口：
├── send(channel, payload)      # 单通道发送
├── send_multi(payload)         # 多通道并行
├── retry_failed(days=7)        # 批量重试
├── get_history(days=30)        # 历史查询
├── get_stats()                 # 推送统计
└── health_check()              # 健康检查
```

**通道适配优先级**：
1. 🥇 **钉钉**（Webhook 加签）— 国央企客户主流
2. 🥈 **企微**（群机器人 + 应用号）— 私企主流
3. 📧 **邮件**（SMTP）— 兜底通道

**失败重试**：指数退避 3 次（1s / 5s / 30s）+ 备用通道兜底

#### 3. `scripts/config_wizard.py` — 交互式配置向导

```bash
python3 scripts/config_wizard.py
```

- 流程：选通道 → 输入 Webhook/邮箱/密钥 → 测试连通 → 写入 `~/.config/bidhunter/push.yaml`
- **硬约束**：未通过连通性测试不允许写入配置
- 支持一键测试 + 失败重试

### 🥈 次交付（体验增强，本周可并行）

#### 4. **多通道并行** — 同一标讯可同时推多通道
- 配置：`push.yaml` 的 `channels: [dingtalk, email]`
- 主通道失败自动切换备用通道

#### 5. **推送失败告警** — 连续 3 天推送失败主动通知管理员
- 检测：`push_manager.py --health-check`（每日 09:00 cron）
- 告警通道：与推送主通道解耦，强制走邮件兜底

#### 6. **定时任务可视化** — 集成到 status.py
- `status.py --schedule` 输出 cron 解析
- `status.py --trigger-now` 立即跑一次 pipeline
- `status.py --push-stats` 查看推送统计

### ⏸ 暂不实现（已确认推迟）

- **飞书通道** — v1.5 任务
- **可视化规则编辑器** — v1.5 任务

---

## 五、预计改动文件列表

### 新增文件（3）

```
scripts/
├── push_manager.py        # 通道管理器（核心，约 300 行）
├── push_history.db        # SQLite 库（运行时自动创建）
└── config_wizard.py       # 交互式配置向导（约 150 行）
```

### 修改文件（3）

```
scripts/
├── pipeline.sh            # 接入 push_manager，--push-channel 参数
├── status.py              # 新增 --schedule / --trigger-now / --push-stats 子命令
└── qual_rules.json        # 不动（v1.2 不涉及匹配逻辑）
SKILL.md                   # 版本号升 1.1.0 → 1.2.0；v1.2 新特性章节
ROADMAP.md                 # v1.2 状态 🎯 → 🚧（开发中）；新增 changelog
```

### 不动文件（v1.2 不涉及）

- `qual_check.py` / `bid_monitor.sh` / `report_html.py` / `report_text.py` / `quote_gen.py`

---

## 六、风险提示与规避（结合 ROADMAP 表 + 上周规划延续）

| 风险 | 影响 | 规避策略 |
|---|---|---|
| 钉钉/企微机器人 Webhook 误配 | 推送失败且静默 | `config_wizard.py` 必须做连通性测试，未通过不允许写入配置 |
| SMTP 邮件被识别为垃圾邮件 | 兜底通道失效 | 引导用户用企业邮箱自建 SMTP，避免触发公共反垃圾规则 |
| SQLite 锁竞争（pipeline + push_manager 交叉写） | 推送历史丢失 | push_history.db 启用 WAL 模式；pipeline 写完后立即释放连接 |
| 通道密钥写错配置文件导致泄露 | 凭据外泄 | 配置存 `~/.config/bidhunter/push.yaml`（权限 600），不入 git；推送时不打印密钥 |
| 自动化任务重复触发推送 | 用户被打扰 | push_manager 内置幂等键（日期+主体），同日同标不重复推 |
| 网络抖动导致单次推送失败 | 误判为通道故障 | 重试 3 次后再标记失败，避免一次失败触发告警 |
| v1.1 → v1.2 配置兼容 | 老用户升级后推送配置失效 | push_manager 首次启动检测旧版配置（crontab 直推），自动迁移到 push.yaml |
| 凭据获取依赖涛哥 | 开发阻塞 | 在规划阶段先列出涛哥需准备的凭据清单，避免开发中卡壳 |

---

## 七、涛哥需准备的凭据清单（开发启动前确认）

| 通道 | 需要的凭据 | 状态 |
|---|---|---|
| 钉钉机器人 | 任一测试群 Webhook（含加签密钥） | ⏳ 待涛哥提供 |
| 企微群机器人 | Webhook URL | ⏳ 待涛哥提供 |
| 企微应用号 | App Key + App Secret（备用通道） | ⏳ 按需 |
| 邮件 SMTP | 可用 SMTP 邮箱（QQ / 163 / 企业邮箱） | ⏳ 待涛哥提供 |

> **建议**：涛哥先把任意一个测试通道（如钉钉）的 Webhook 准备好，开发即可启动；其他通道按实现进度陆续补齐。

---

## 八、本周关键里程碑（2 周周期 · 第 1 周）

| 时间 | 节点 | 交付标准 | 状态 |
|---|---|---|---|
| 8-11（周二） | 上周规划 | UPGRADE_PLAN_2026-08-11.md | ✅ |
| 8-13（周一） | **本周规划** | 本文档 | ✅ |
| 8-13 ~ 8-15 | 开发期 1 | push_history.db + push_manager.py 核心 CRUD + 钉钉通道 | 🎯 本周启动 |
| 8-16 ~ 8-17 | 开发期 2 | 企微通道 + 邮件通道 + config_wizard.py | ⏳ 下周 |
| 8-18（周一） | 测试 + 试推 | 用真实 Webhook 跑一次完整推送，检查重试/告警 | ⏳ 下周 |
| 8-19（周二） | 写 changelog + 发布 | ClawHub 发布 v1.2.0 | ⏳ 下周 |

---

## 九、发布检查清单（开发完成后使用）

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

## 十、下一步动作（涛哥审阅）

1. **审阅本规划**：确认 v1.2 范围（推送通道 vs 其他）依然符合预期
2. **凭据准备**：先准备任意一个测试通道 Webhook（建议钉钉），启动开发
3. **优先级确认**：是否三通道并行开发，还是先做钉钉 → 邮件 → 企微
4. **决策**：是否启动开发，或调整 v1.2 范围

---

## 十一、与上次规划（8-11）的差异说明

- ✅ **范围一致**：v1.2 推送通道升级路线未变
- ✅ **飞书推迟**：仍然推迟到 v1.5
- ✅ **实施优先级一致**：push_history.db + push_manager.py → config_wizard.py → 多通道
- 📈 **新增 ClawHub 数据**：下载量 128 → 152（+24），自然增长稳定
- 📅 **里程碑微调**：上次规划"开发期 1 = 8-12 ~ 8-14"，本次按"8-13 ~ 8-15"对齐（实际今天是周一）

---

_本规划由 BidHunter 周一升级自动化生成（执行日：2026-08-13 周一）。_
_日期：2026-08-13_