---
name: bidhunter
version: "1.2.0"
description: "国央企招投标信息监控与研判技能 v1.2。自动采集多个央企/公共资源交易平台公告，按资质规则比对可投性（可投/不可投/需确认），生成带研判的简报并推送。支持边界感知智能匹配（防子串误匹配）、规则库健康检查、精华版/完整版双报告模式，以及钉钉/企业微信/邮件多通道推送（含推送历史、失败告警、配置向导）。适用于投标代理、供应商资质管理、招投标情报收集等场景。触发词：抓招投标、今日哪些能投、标讯监控、标书研判、招投标公告、央企招标、投标资质匹配。"
agent_created: true
---

# 标讯猎手 BidHunter v1.2

> 采集国央企招投标公告 → 按资质规则比对可投性 → 生成带研判的简报 → **多通道推送**。
> 自包含、已脱敏：不含任何私有主体、个人联系方式、公司档案。使用者按自己的营业执照与业务规则填充配置即可。

## v1.2 新特性（"达"：推得到，收得着）

- **多通道推送**：🥇 钉钉（加签） / 🥈 企业微信（群机器人） / 📧 邮件（SMTP 兜底），同一标讯可并行多通道
- **推送配置向导**：`config_wizard.py` 交互式配通道，未通过连通性测试不允许写入配置
- **推送历史库**：SQLite（`push_history.db`，WAL 模式）记录 30 天推送日志，可查历史、统计、重试失败
- **失败自动兜底**：主通道失败自动切备用通道；指数退避重试 3 次（1s/5s/30s）
- **失败告警**：连续 3 天推送失败且无成功记录时，强制走邮件告警管理员
- **幂等保护**：同日同题已成功则不重复推送，避免打扰
- **状态增强**：`status.py --push-stats` 查看推送统计与告警状态

## v1.1 新特性（已发布）

- **智能匹配**：边界感知算法，"电气"不会误匹配"电气石"，"广告"不会误匹配"户外广告设施拆除"
- **规则健康检查**：`--validate-rules` 一键检查规则库配置问题
- **精华版报告**：`--summary` 输出 Top 5，适合企业微信/钉钉 IM 推送
- **状态查看**：`status.py` 查看今日采集状态、近7天趋势、规则库摘要
- **干跑模式**：`--dry-run` 预览全流程，不推送，不采集
- **反馈机制**：报告内置反馈引导，用户按序号反馈帮助优化规则库

## 何时使用

- 用户说"抓一下招投标" / "今日哪些能投" / "重新分析一遍标讯"
- 需要判断某条公告是否可投、归属哪个投标主体
- 需要监控特定央企/政府采购平台的招标公告
- 搭建或优化招投标监控工作流时参考

## 安装与初始化

安装后 scripts/ 已随 skill 就位。首次使用前需完成配置：

1. 复制 scripts/ 到工作目录（或直接使用 skill 内路径）：
   ```bash
   SCRIPT_DIR=~/.workbuddy/skills/bidhunter/scripts
   ```

2. 编辑 `scripts/qual_rules.json`，填入使用者自己的投标主体和资质能力词。配置后运行健康检查：
   ```bash
   python3 scripts/qual_check.py --validate-rules scripts/qual_rules.json
   ```

3. 确认目标平台是否在 `references/platforms.md` 的支持清单中。如需新增平台，参考 `references/platforms.md` 的"自定义数据源"章节。

## 系统组件（位于 `scripts/`）

| 文件 | 作用 |
|---|---|
| `bid_monitor.sh` | 采集公告（支持多平台适配，默认取当天发布，跳过非投标类） |
| `qual_rules.json` | 资质规则库（主体能力词 + 红色预警 + special_rules），**使用者必须自定义** |
| `qual_check.py` | 资质比对引擎（Python 标准库，无第三方依赖） |
| `pipeline.sh` | 全链路汇总（采集 → 比对 → 报告） |
| `report_html.py` | 生成 HTML 可视化简报 |
| `report_text.py` | 生成纯文字研判简报（适配微信/邮箱/IM） |
| `quote_gen.py` | 报价表底稿生成（仅 `--quote` 时调用） |
| `push_manager.py` | **v1.2** 多通道推送管理器（钉钉/企微/邮件 + SQLite 历史 + 重试兜底） |
| `config_wizard.py` | **v1.2** 交互式推送配置向导，连通性测试后写入 `~/.config/bidhunter/push.json`（权限 600） |

运行时目录（自动创建）：
- `bid_cache/`：采集缓存
- `bid_reports/`：生成的报告
- `bid_quotes/`：报价底稿（按需）

## 标准流程

### 1. 采集 + 比对

```bash
bash $SCRIPT_DIR/pipeline.sh
```

- 默认使用缓存优先策略。
- `--fresh`：强制重新采集当天数据。
- `--platform cnooc`：指定平台（不指定则采集所有已配置平台）。

### 2. 查看报告

```bash
# 纯文字版（适配 IM 推送）
cat $SCRIPT_DIR/bid_reports/report_YYYY-MM-DD.txt

# HTML 版（浏览器查看）
open $SCRIPT_DIR/bid_reports/report_YYYY-MM-DD.html
```

### 3. 推送简报（v1.2）

首次使用先配置通道（钉钉/企微/邮件任一即可，未通过连通性测试不写入）：

```bash
python3 $SCRIPT_DIR/config_wizard.py
```

配置完成后，`pipeline.sh` 在生成报告后**自动推送**文字版简报（取前 60 行，精华版取前 25 行）。手动推送报告：

```bash
python3 $SCRIPT_DIR/push_manager.py send-file $SCRIPT_DIR/bid_reports/report_YYYY-MM-DD.txt --summary
python3 $SCRIPT_DIR/push_manager.py test          # 测试全部通道
python3 $SCRIPT_DIR/push_manager.py history       # 查看 30 天推送历史
python3 $SCRIPT_DIR/push_manager.py stats         # 推送统计
python3 $SCRIPT_DIR/push_manager.py health-check  # 失败告警检查
```

关闭推送：`pipeline.sh --no-push`。未配置推送时 `pipeline.sh` 静默跳过，完全向后兼容。

## 资质比对逻辑（核心）

**判定优先级（高 → 低）**：

1. **special_rules 覆盖**：如"某类标外找资质可投"、"某类标垫资不参与 → skip"
2. **红色预警命中** → 不可投 + 原因
3. **主体能力匹配** → 可投（按主体能力词归属投标公司）
4. **都不命中** → 需确认

**红色预警（通用类型，使用者按需增删）**：
车辆维修、机动车维修、劳务派遣、食品生产、食品加工、医疗器械、建筑施工、消防、危险品、房地产开发、电信、互联网信息服务、爆破、保安、安保、测绘、勘察、特种设备、压力容器、电梯、制药、矿产、采掘、冶炼、钻井、修井。

**主体能力词**：在 `qual_rules.json` 的 `entities` 中按营业执照经营范围填写。默认提供两个示例主体 `entity_a` / `entity_b`，capabilities 填对应经营类目关键词。

详细规则结构参考 `references/filter_rules.md`。

## 使用者的业务规则（示例，按需替换）

- 不直接自动生成报价文件（默认 `GEN_QUOTE=0`，仅 `--quote` 出 CSV）
- 采集只取当天发布（部分平台 list API 无截止日字段，靠此近似排除已开标标）
- 采购/采办/询价类不参与（垫资风险）
- 资质缺口清单：把确认不具备的资质列在规则库注释或独立配置文件，分析中遇此类标人工提示

## 投标主体确权（按实际情况配置）

- 传媒/活动类 → 主体 A（全国交付，需先入供应商库）
- 通用/设备/维修类 → 主体 B（已入库）
- 某类标资质可外找 → 不依赖自有资质，正常推进

## 文字版输出模板

```
【可投简报·研判 YYYY-MM-DD】总N｜可投a｜不可投b｜需确认c
研判（按优先级）
一、重点地区专项（建议重点投）
- 标题(id) 地区·品类｜判断+风险
  链接
二、核心能力类（稳）
...
三、需确认（研判）
...
重点提醒（需点开核资质门槛）
```

## 定时任务

- 每日 10:00：自动化运行 pipeline 生成简报
- 每日 10:30：IM 文字版推送
- 避免多个 agent 重复推送同一份简报

## 已知坑点

- **IM 发文件失败**：个人 IM 不支持发文件，只能文字。可视化网页供电脑浏览器看。
- **list API 无截止日**：部分平台返回仅 id/title/createdTime/updatedTime，截止日需 detail 接口（常 401），故只采集当天近似。
- **IP 限流**：连发约 20 次后可能 401/403，翻页 sleep 2s + 失败重试冷却 10s。
- **规则库与记忆不一致**：某些类未入库红警是主动决定（人工留意），非遗漏，需文档说明。

## 参考文档

- `references/platforms.md`：支持平台清单、各平台采集参数、自定义数据源指南
- `references/filter_rules.md`：筛选规则结构、条件维度、冲突处理
- `references/field_standard.md`：标讯字段标准化 schema
