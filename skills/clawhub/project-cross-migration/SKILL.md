---
name: "project-cross-migration"
description: "跨平台迁移项目资料包（含对话原文、记忆、人格、工具与环境）的免费版。支持入口校验、JSONL 校验、可读还原。需要五道确认闸门、环境快照、脱敏分享包 → 获取完整版 <https://wzyp.cn/item/p0r2lb>"
author: zhou
license: MIT
version: "2.4.2"
keywords:
  - 项目迁移
  - 对话迁移
  - 跨平台迁移
  - 备份恢复
  - raw-conversation-backup
  - conversation-migration
  - project-cross-migration
  - jsonl
  - 数据自持
  - 脱敏
  - desensitize
  - 凭据管理
  - 环境快照
  - 确认闸门
  - 框架迁移
  - Agent 迁移
tested:
  date: "2026-09-20"
  os: macOS 15.8
  platform: "免费版 v2.4.2（preflight / restore / validate 核心流程验证）"
  verified: "v2.4.2 免费版核心流程验证通过：preflight 入口校验 / restore_dialogue 还原 / validate_jsonl 校验 三条链路可跑通。confirm_gate / environment_snapshot / desensitize 在免费版中被锁定。"
---

# 📦 项目资料跨平台迁移 · Project Cross Migration（免费版 v2.4.2）

> **备份 → 搬运 → 还原：把一个项目（含 Agent 人格、工具与环境）的全部资料完整搬到新框架 / 新机器。**
> 本 Skill 是 raw-conversation-backup v1.x 的**项目级升级版**：JSONL schema 完全兼容，范围覆盖项目工作状态全量。
>
> ⚠️ **当前为免费版 v2.4.2**。以下能力已锁定，需获取完整版解锁：
> - 五道分步确认闸门（`confirm_gate.py`）
> - 框架环境快照采集（`environment_snapshot.py`）
> - 分享包脱敏器（`desensitize.py`）
>
> **获取完整版**：<https://wzyp.cn/item/p0r2lb>

## 〇、主作用声明（先读这个）

**这个 Skill 的主作用：跨平台迁移某个项目的全部资料。**

> **平台边界（v2.2.1 明示）**：Coze / Dify / 扣子 / 腾讯元器 等**在线 SaaS 平台架构性不支持**——对话数据在服务侧、无本地文件形态。preflight 命中此类框架名会给 warning 但不拦截（用户可先走平台自带导出/API 落地为本地文件，再进入备份流程）。

迁移的不是"聊天记录"，而是"项目工作状态"：

| 资产 | 回答的问题 |
|---|---|
| 对话原文 | 每个决策是怎么做出来的（真相源） |
| 记忆文件 | 我们做到哪了、踩过什么坑（上下文） |
| 人格与工具 | 这个 Agent 是谁、怎么干活（身份与操作约定） |
| 框架环境 | 当时跑在什么框架/工具/配置上（换机后能不能跑起来） |
| 项目产出 | 已经拿出了什么成果（资产） |

验收标准：**零丢失 + 可续聊 + 环境可复现**——新 Agent 读完资料包，用户不需要重新交代背景，也不需要重新摸索环境。

> **人类层说明**：对 Agent 说「迁移项目」「对话搬家」「从备份恢复」即可。资料只走本地，不上传云端。

## 一、迁移范围：五层模型 + 环境快照（v2.3 修订）

| 层 | 内容 | 备份 | 还原策略 |
|---|---|:---:|---|
| L1 对话原文层 | raw-v1.0 JSONL 分片 + 双索引 | ✅ | 必还原，100% 逐字 |
| L2 项目记忆层 | `memory/*.md`（项目快照、日志） | ✅ | 必还原 |
| L3 长期蒸馏层 | `MEMORY.md` | ✅ 原档随包 | 目标侧重写：**蒸馏不搬运**（旧结论 → 新环境认知） |
| L4 人格层 | `SOUL.md` / `IDENTITY.md` / `USER.md` / `AGENTS.md` | ✅ | **按迁移模式**（见下表） |
| L5 工具与环境层 | `TOOLS.md`、自装 `skills/`、`HEARTBEAT.md`、非敏感 config、**`_environment.json`** | ✅ | 跨框架时逐项评估兼容性后恢复；环境项按快照对照补齐 |
| 附带 | 项目产出 `output/`、**凭据文件（私有场景）** | ✅ 选迁 | 项目资产；私有迁移凭据随包，恢复即用 |

### L4 人格层：两种迁移模式（v2.1 核心修订）

还原向导第一步必须确认模式：

| 模式 | 适用场景 | 还原动作 |
|---|---|---|
| `persona-follow`（**默认**） | 换机 / 重装 / 换框架 / 全新 agent——人格应随项目走 | L4 四件全量恢复为 live 文件 |
| `persona-keep` | 目标 agent 已有自己的人格，本次是注入旧项目经历 | L4 存档至 `_archive/persona/`（可查不可用），live 人格不动，仅在 SOUL.md 记忆章节增补「记忆来源约定」：只吸收结论与方法，不复制语气 |

> v2.0 的"L4 不覆盖"仅适用于 persona-keep 场景；把它当默认是场景假设错误，v2.1 已修正——大多数迁移（换机/换框架）人格恰恰是最需要恢复的资产。

**兼容性边界（v2.2.0）**：与 raw-conversation-backup v1.0.1（WorkBuddy 管道）完全兼容；与 MindVault OpenClaw/Marvis 模式导出包**兼容还原**（其 tool 条目仅含 key_param/args_summary，校验器按兼容模式放行并输出 INFO 说明）。

### L5 工具与环境层细则（v2.1 新增，v2.2 扩环境快照）

- **打包内容**：`TOOLS.md`（工具约定与本地环境备注）、`skills/`（自装技能源目录）、`HEARTBEAT.md`（定时任务清单）、config 片段、`_environment.json`（框架环境快照）。
- **还原纪律**：跨框架时工具格式/路径可能不兼容——逐项评估后恢复，不盲目覆盖目标框架的现有工具；技能类按目标框架的目录规范安装。
- **凭据纪律（v2.2 重新划线，见 §二）**：私有迁移场景**凭据随包、恢复即用**，不再强制生成凭据缺口清单；只有**分享包**才脱敏并出 `_credentials_needed.md`。

### 框架环境快照 `_environment.json`（v2.2 新增）

**回答的问题**：这套资料当年跑在什么框架、什么版本、装了哪些工具、config/hooks/权限规则在哪、模型怎么配的、系统是什么。
**为什么需要**：资料搬过去了、环境对不上，等于没迁——尤其换机后 Node/Python 版本、CLI 依赖、hooks 路径常常是隐形的坑。

字段结构（`scripts/environment_snapshot.py` 采集，纯 Python 标准库，mac/win/linux 尽力采集）：

| 字段 | 内容 | 纪律 |
|---|---|---|
| `frameworks` | 源框架名+版本、目标框架名+版本 | 必填（运行入口已校验） |
| `os` | 系统 / 版本 / 架构 / shell / `os_detail`（macOS 15.7.9 这类可读串） | — |
| `tools` / `tools_missing` | python3 / pip3 / node / npm / git / ffmpeg / rg / jq / curl 的**路径与版本**；缺失项单独登记 | 只记可执行文件路径，不读其配置 |
| `config_paths` | config / hooks / 权限规则的**文件路径清单** | **只列路径，绝不列文件内容或值**（上限各 50 条） |
| `model_config` | 模型名 / base_url / endpoint / provider / max_tokens 等**白名单键** | 键名白名单 + 凭据键黑名单（key/token/secret/password/auth/cookie…）双保险，凭据值一律丢弃 |
| `agent_home_hints` | 探测到的 agent 安装/数据目录线索（环境变量与常见路径） | 仅作路径线索，不写入 |
| `warnings` | 成品自检结果 | 序列化后对全文跑敏感模式扫描，命中即打码并登记 |

采集命令：

```bash
python3 scripts/environment_snapshot.py --task-name "<任务名称>" \
    --source-framework "Marvis@2.2.0" --target-framework "OpenClaw@1.4" \
    --scan-root ~/WorkBuddy/<项目> --config-file ~/WorkBuddy/<项目>/config.json \
    --out <备份目录>/_environment.json
```

> 三道防线说明：路径发现只 walk 指定根目录且只登记文件名命中项（不读内容）；模型配置走白名单提取；成品再跑一次自检打码。**该文件永远不承载凭据**——凭据只走私有包或将由用户在目标端配置。

### 备份打包清单（v2.2）

```
<任务名称>_<时间戳>/
├── _index.json / _index_unified.json   # 对话索引（v1 兼容）
├── _manifest.json                      # 逐文件 sha256
├── _environment.json                   # 框架环境快照（v2.2 新增）
├── *_rounds-*.jsonl                    # L1 对话分片
├── memory/                             # L2 项目记忆
├── persona/                            # L4 人格四件（SOUL/IDENTITY/USER/AGENTS）
├── tools/                              # L5 工具与环境（TOOLS.md、skills/、HEARTBEAT.md、config 片段）
├── credentials/                        # 凭据文件（私有备份：随包，恢复即用；分享包：剔除）
├── output/                             # 项目产出（选迁）
└── _share/                             # 仅"生成分享包"时出现：脱敏副本
    └── _credentials_needed.md          # 仅分享包携带：被脱敏凭据项清单
```

> **私有包与分享包的区别只有一处**：`credentials/` 与 `_share/`。私有迁移**不带 `_share/`**、凭据原样在包内；分享场景**不带 `credentials/`**、改出 `_share/` 与 `_credentials_needed.md`。

## 二、隐私脱敏规范（v2.2 重定位：脱敏是可选分享配件）

**原则（v2.2 重写）：默认不脱敏。** 私有备份、本机还原、自己换机这类"资料不出自己设备/账号"的场景，**原文照搬、凭据随包、恢复即用**——脱敏只服务于"资料要给到别人"的分享场景。

| 场景 | 动作 | 凭据 | 凭据缺口清单 |
|---|---|---|---|
| 私有备份 / 本机还原 / 自己换机（**默认**） | **完全不脱敏**，原文照搬 | **随包**，恢复即用 | ❌ 不生成 |
| 生成分享包（发他人 / 发布示例 / 跨人传递） | 显式加 `--share`，另出 `_share/` 脱敏副本，**原包不出门** | 替为占位符，实体剔除 | ✅ `_credentials_needed.md` |
| 还原进多人可见上下文（群聊 / 共享会话） | 结构化字段用脱敏值；raw 层不进共享上下文 | 不外传 | 视场景 |

> **为什么改**：v2.1 把"脱敏 + 凭据永不入包 + 生成缺口清单"写成了通用流程，导致纯粹的私人换机备份也要倒腾一遍凭据、还原后还得手工回填——把分享场景的约束误当成了迁移必经步骤（与 v2.0 的 L4 缺陷同类）。
> **安全边界不变**：一旦资料要离开你的私有环境，`_share/` 是唯一出口。

脱敏规则（`scripts/desensitize.py` 实现，v2.2 起**必须显式 `--share`** 才执行）：

| 类型 | 识别方式 | 处理为 |
|---|---|---|
| API Key / Token | `sk-`、`vda_`、`rk-` 前缀长随机串；`api_key/token/secret/password:` 赋值 | `KEY***<hash4>` |
| 手机号 | `1[3-9]xxxxxxxxx` | `1**phone<hash4>` |
| 邮箱 | 标准邮箱正则 | `首字母***<hash4>@域名` |
| 用户 ID | `ou_` / `u_` / `on_` 开头的十六进制串 | `ou_***<hash4>` |
| 本机用户路径 | `/Users/<name>/`、`C:\Users\<name>\` | `~/` |

- `<hash4>` = 原值 sha256 前 4 位：同一原值 → 同一占位符（可对账），不可逆。
- **v2.2.0 修复 F9**：apikey / email / openid 三类正则原用 `\b` 词边界，在中文/全角字符紧邻敏感值时**静默失效**（Python 3 中 CJK 属 `\w`，`apikey是sk-xxxx` 里 `sk` 前取不到词边界）——现改为负向断言 `(?<![A-Za-z0-9])`。
- 映射清单 `_desensitize_map.json`（占位符 ↔ 原值指纹）**只留本地**，不随分享包走。
- 发布 Skill 文档 / 示例 / 截图时一律用虚构值；真实 key、open_id、本机路径不得出现在任何对外产物里。

## 三、JSONL 数据规范（raw-v1.0 兼容速查）

| 字段 | 必填 | 说明 |
|---|:---:|---|
| `schema_mode` | 否 | `"raw-v1.0"`；缺省按兼容模式解析 |
| `timestamp` | ✅ | ISO 8601 GMT+8，禁止 Unix 毫秒 |
| `role` | ✅ | `user / agent / tool / system / scheduled` |
| `round` | ✅ | 轮次号，用户新消息开新轮 |
| `seq` | 建议 | 全局递增序号，还原保序的唯一依据 |
| `content` | ✅ | 消息正文（完整，不截断） |
| `raw` | 建议 | 源框架原始消息对象完整 JSON，**原文真相源** |
| 其他扩展 | 否 | `reasoning / tool_calls / attachments / key_params / ts_inherited …` |

> 存储层完整、展示层可截断；写盘不改编、不删除任何消息。

## 四、备份侧 Step 0-6.5（v2.3 修订）

### Step 0 运行入口校验（v2.2 新增，**不通过不许开工**）

迁移事故大多发生在动手之前：框架没对齐、任务名随手起、备份目录落在 agent 安装目录里被卸载连坐。**备份第一件事是跑入口校验**：

```bash
python3 scripts/preflight_check.py --task-name "<任务名称>" \
    --source-framework "<源框架[@版本]>" --target-framework "<目标框架[@版本]>"
```

- **平台框架**：源框架 + 目标框架**都要确认**（框架名必填，版本尽力提供）；同名（同框架换机）不算错，仅提示。
- **任务名称**：**缺失即停止并向用户索要**，不得自行编造 `backup` / `new` / `test` 之类占位名；名称需 ≤64 字符且不含 `<>:"/\|?*`。
- **目录落位**：备份目录 = `~/Desktop/<任务名称>_<时间戳>/`（**默认桌面**，所见即所得；`--backup-root` 可改到文档等其他显眼位置），脚本**显式打印绝对路径**。
- **硬性禁止**（命中即拒绝，退出码 3）：不得写入 agent 安装目录 / 数据目录 / 系统保护路径 / `skills`、`node_modules`、`site-packages` 等安装型目录。**原因**：这些位置会随 agent 卸载或重装被一并删除，"备份"备份了个寂寞。
- 落位被拒时的正确做法：换到用户自己的显眼位置（默认**桌面**，或文档等其他显眼位置），**不要把备份藏进 agent 目录**。

### 免费版锁定项

以下三个脚本在免费版中功能被锁定，所有子命令均输出统一提示并退出：

| 脚本 | 锁定的功能 |
|------|-----------|
| `confirm_gate.py` | 五道分步确认闸门（G1-G5 逐道确认 + 打包闸门） |
| `environment_snapshot.py` | 框架环境快照采集 → `_environment.json` |
| `desensitize.py` | 分享包脱敏器（`--share` 模式） |

**获取完整版**：<https://wzyp.cn/item/p0r2lb>

### Step 1-6.5

1. **Step 1 定范围**：会话级 / 项目级（默认项目级：L1+L2+L4+L5+output+凭据）。
2. **Step 2 建目录**：用 Step 0 输出的绝对路径建 `<任务名称>_<时间戳>/`，**建前复算一次禁止位置**。
3. **Step 3 全量导出**：逐条写全字段 + `raw`；源无时间戳则继承上一条并置 `ts_inherited`。
4. **Step 4 切割写盘**：每 15 轮一个 `{task}_<日期>_rounds-{起}-{止}.jsonl`，追加式，永不覆盖。
5. **Step 5 双索引**：更新 `_index.json` 与 `_index_unified.json`。
6. **Step 6 校验**：`validate_jsonl.py` 全文件跑通（退出码 0）+ 抽查 ≥3 条一致性。
7. **Step 6.4 环境快照（完整版）**：跑 `environment_snapshot.py` 生成 `_environment.json`。> **免费版锁定。**
8. **Step 6.5 打包（完整版）**：**前置条件——五道确认闸门全通过**。> **免费版锁定。**
9. **Step 7 脱敏分享包（完整版）**：仅当用户主动要求时，跑 `desensitize.py --share` 生成 `_share/` 脱敏副本。> **免费版锁定。**

## 五、还原侧 Phase A-E（v2.3 修订）

### Phase A 源端自检 + 模式确认 + 环境预读
读 `_index.json` 获知轮次 / 条数 / 文件清单；有 `_manifest.json` 先做完整性校验；有 `_environment.json` 先读**框架版本 / 工具 / 系统 / `source_model`** 四项，与目标环境做一次对照；有 `_confirm_gates.json` 时回看五道闸门的确认轨迹（当时确认的范围 / 落位 / 附件选项 / 模型），据此复现用户原始意图。
**确认迁移模式**：persona-follow（默认）还是 persona-keep？向用户二选一确认，未答则按默认。

### Phase B 转移落地

> ⚠️ **实战坑 ①（沙箱）**：目标框架的文件工具常被限制在 workspace 内，读不了外部 backup_root。
> 正确姿势：`cp -R` 整目录复制进目标工作区，**源目录原样保留**。

校验先行三步：
1. `validate_jsonl.py` 跑全部数据文件 → 必须 0 问题；
2. **三方对账**：JSONL 实际行数 = `_index.total_messages` = `files[].entries` 累加；
3. 有 `_manifest.json` → 逐文件核对 sha256。

### Phase C 全量还原

> ⚠️ **实战坑 ②（排序）**：数据文件按**文件名里的 rounds 范围**排序，不要按 mtime（复制会改 mtime）。
> ⚠️ **实战坑 ③（顺序）**：行序即真实对话流。源数据存在轮内毫秒级时间回退，**禁止按时间戳重排**。

流程：
1. 收集全部 `*rounds-*.jsonl`，按 rounds 范围升序；
2. 逐行读入，seq 连续性校验（断点记录告警，不中断）；
3. 统计角色分布与轮次连续性（1..max 无缺轮）；
4. `raw` 字段存在时以 `raw` 为原文真相源，结构化字段仅作索引展示；
5. 产出可读还原稿 `_restored_dialogue.md` + 统计报告 `_restored_stats.json`（v2.2 起自动附带环境快照摘要与补齐提示；v2.3 起含 `model_consistency_hint` 模型一致性提示）。

> ⚠️ **实战坑 ④（如实还原）**：源对话里的"上下文摘要注入轮""API 超时重试痕迹"是当时的原始状态，逐字保留并标注，不算迁移损失。
> ⚠️ **实战坑 ⑤（大文件）**：还原稿 2MB+ 属正常，阅读用分片 / 按轮定位。

### Phase D 记忆与人格写入（v2.1 修订）

| 步 | 模式 | 写什么 |
|---|---|---|
| 1 | 两者 | 原文层就位（工作区内的备份目录，真相源，不动） |
| 2 | 两者 | 项目快照 → `memory/<project>-context.md`：本质 / 关键决策与纠正 / 待办 |
| 3 | 两者 | 长期蒸馏 → `MEMORY.md`：协作画像 / 被纠正的坑 / 领域知识 / 挂起事项 / 环境备忘（蒸馏不搬运） |
| 4a | follow | **人格四件恢复为 live 文件**（SOUL/IDENTITY/USER/AGENTS） |
| 4b | keep | L4 存档至 `_archive/persona/`；live 人格不动；SOUL.md 仅增补「记忆来源约定」 |
| 5 | 两者 | 工具与环境恢复（见 Phase E） |

### Phase E 工具与环境恢复（v2.1 新增，v2.2 扩环境对照）

1. `TOOLS.md` → 恢复为 live 工具约定文件；
2. `skills/` → 按目标框架的技能目录规范逐个安装；跨框架时先比对格式，不兼容的列清单告知用户；
3. `HEARTBEAT.md` → 恢复定时任务清单；
4. config / hooks / 权限规则 → **按 `_environment.json` 的路径清单**找回对应文件，按目标框架 config 结构合并，不整文件覆盖；
5. **环境对照补齐（v2.2 新增，v2.3 扩模型一致性）**：按 `_environment.json` 逐项核对——框架版本、`tools` / `tools_missing`、OS 差异、模型配置项（模型名/端点），缺口列清单交给用户补齐；**`source_model` 提示**：本次备份由该模型完成，恢复时建议使用同一模型（减少语气/行为漂移，闸门 G5）；
6. **凭据交接（v2.2 改）**：
   - 私有迁移（默认）→ 包内 `credentials/` **恢复即用**，无需用户回填；如目标框架要求重新授权，按框架流程逐项确认；
   - 分享包场景 → `_credentials_needed.md` 交给用户，逐项在目标框架配置（Skill 永不代填凭据）。

### 还原完成验收清单（v2.3 扩至十五项，缺一不可）

| # | 检查项 | 通过标准 |
|---|---|---|
| 1 | 文件数与大小 | 与 `_index.json` / `_manifest.json` 一致 |
| 2 | 消息总数三方对账 | 行数 = 索引声明 = 分片累加 |
| 3 | 轮次连续 | 1..max 无缺轮 |
| 4 | seq 连续 | 全局递增无缺口（告警需逐条解释） |
| 5 | 角色分布 | user/agent/tool/system 计数合理 |
| 6 | 时间跨度 | 首尾时间戳与索引一致 |
| 7 | 关键内容抽查 ≥3 | 用**全文 grep** 定位已知关键决策原文（别用窄窗口 grep，会漏检） |
| 8 | 校验脚本 | validate 全文件退出码 0 |
| 9 | 源目录未动 | 源备份原样保留 |
| 10 | 四层写入完成 | L1 就位 / L2 快照 / L3 蒸馏 / L4 按模式处理 |
| 11 | L5 工具恢复完成 | TOOLS/skills/HEARTBEAT 按兼容性恢复，缺口有清单 |
| 12 | **环境快照对照完成（v2.2 新增）** | `_environment.json` 在包内；框架版本/工具/OS/模型配置已逐项对照，缺口列清单 |
| 13 | **凭据按场景处置正确（v2.2 改写）** | 私有包：凭据完整随包、恢复即用（不做无谓脱敏）；分享包：`credentials/` 已剔除、`_share/` 与 `_credentials_needed.md` 已生成 |
| 14 | **入口校验与目录落位（v2.2 新增）** | preflight 通过（框架 + 任务名称 + 目录在 `~/Desktop/<任务名称>_<时间戳>/`，未落入 agent 安装/数据目录），结果中已打印绝对路径 |
| 15 | **五道确认闸门全通过（v2.3 新增）** | `_confirm_gates.json` 在包内且 G1-G5 全部 `confirmed`（含 G2 抽检轮号、G3 落位路径、G4 附件选项、G5 模型名）；打包前 `confirm_gate.py --check` 退出码 0；还原侧已回看确认轨迹 |

> **验收操作提醒**：凡涉及 `***xxxx` 形态占位符的核对，一律以**文件级 / hex 级**比对为准——部分平台展示层会对"疑似脱敏痕迹"做二次遮盖，直接看终端输出会误判"脚本丢了哈希"（实测教训，2026-09-15 测评 F8）。

## 六、故障排查（十六条）

| # | 现象 | 解决 |
|---|---|---|
| 1 | 迁移后消息顺序乱 | 按 seq 升序还原；老文件用 round+行序 |
| 2 | 少消息 | 逐行 read 全量读取，勿用框架一键导入 |
| 3 | 丢工具调用/附件 | 检查 `tool_calls` / `attachments` / `raw` |
| 4 | 时间戳对不上 | 统一 +08:00；缺失继承并置 `ts_inherited` |
| 5 | 老文件缺新字段 | 按默认值解析，无需重导 |
| 6 | 恢复后背景丢失 | Phase D 写入没做完 |
| 7 | 沙箱读外部路径被拒 | `cp -R` 进工作区再处理，源不动 |
| 8 | 文件顺序错乱 | 按文件名 rounds 范围排序，勿按 mtime |
| 9 | 还原稿含"摘要注入轮 / 重试痕迹" | 原始态，如实保留，非迁移损失 |
| 10 | 抽查 grep 计数为 0 但内容存在 | 换全文 grep；窄窗口（-A/-B）会漏检 |
| 11 | 还原稿太大读不动 | 分片读 / 按轮 grep 定位 |
| 12 | 换机后人格/工具没跟上 | v2.0 的 L4 设计缺陷：确认用了 v2.1+，按 persona-follow 重做 Phase D/E |
| 13 | **中文/全角紧跟 key 或邮箱，脱敏没生效** | v2.1.1 及更早的 `\b` 词边界在 CJK 旁失效；v2.2.0 已改负向断言 `(?<![A-Za-z0-9])`（F9） |
| 14 | **备份目录找不到了 / 随 agent 卸载消失** | 备份被写进 agent 安装或数据目录，卸载被连坐删除。v2.2 起 preflight 硬性拦截；重做备份到 `~/AgentConversationBackup/` |
| 15 | **换机后跑不起来（版本/依赖对不上）** | 未采 `_environment.json`，或采了没对照。按 Phase A 预读 + Phase E 第 5 步逐项补齐 |
| 16 | **备份包内容串了项目 / 事后查不出搬错哪段** | 未走五道确认闸门就打包：范围没界定、内容也没抽检。v2.3 起打包前 `confirm_gate.py --check` 硬性拦截（rc=2）；重做时用 G1 界定范围、G2 抽检核对 |

## 七、配套文件

| 文件 | 用途 |
|---|---|
| `scripts/preflight_check.py` | **运行入口校验**：平台框架 + 任务名称 + 备份目录落位（禁写 agent 目录；默认落位桌面） |
| `scripts/confirm_gate.py` | 五道分步确认闸门（**免费版锁定**） |
| `scripts/environment_snapshot.py` | 框架环境快照采集（**免费版锁定**） |
| `scripts/validate_jsonl.py` | schema + seq 连续性校验（还原前必跑） |
| `scripts/desensitize.py` | 仅分享场景：生成 `_share/` 脱敏副本（**免费版锁定**） |
| `scripts/restore_dialogue.py` | 还原为可读对话稿 + 统计报告（附环境快照摘要） |

## 完整版能力简介

免费版提供**备份 → 搬运 → 还原**的核心流程（L1/L2 备份校验还原），覆盖项目工作状态基础迁移。

**完整版解锁以下能力**：
- 五道分步确认闸门（G1-G5 逐道确认 + 随机抽检 + 打包前置校验）
- 框架环境快照采集（生成 `_environment.json`，含框架版本 / 工具 / OS / 模型配置）
- 分享包脱敏器（`--share` 模式，生成脱敏副本 + 本地映射清单）
- 完整验收清单 15 项、故障排查 16 条全量覆盖

**获取完整版**：<https://wzyp.cn/item/p0r2lb>


