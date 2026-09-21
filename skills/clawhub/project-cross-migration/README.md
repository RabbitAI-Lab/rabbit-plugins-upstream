# 项目资料跨平台迁移 · Project Cross Migration（免费版 v2.4.2）

> **备份 → 搬运 → 还原：把一个项目的全部资料（含人格、工具与环境）完整搬到新框架 / 新机器。**
> 免费版 v2.4.2 — 免费、零付费、无付费拆分。需要确认闸门、环境快照、脱敏分享包 → 获取完整版 <https://wzyp.cn/item/p0r2lb>

## ⚠️ 当前为免费版

以下能力在免费版中被锁定，需获取完整版解锁：

- 五道分步确认闸门（`confirm_gate.py`）
- 框架环境快照采集（`environment_snapshot.py`）
- 分享包脱敏器（`desensitize.py`）

**获取完整版**：<https://wzyp.cn/item/p0r2lb>

## 这个 Skill 解决什么问题

换 Agent 框架 / 换机器时，"一键导入"经常丢对话、丢工具调用、丢记忆；更常见的是**只迁了聊天记录，项目的记忆、产出和环境没跟上**，到新环境一切从头交代。

**project-cross-migration** 的解法：把一个项目的全部工作状态——对话原文（raw-v1.0 JSONL）、记忆文件、人格、工具与环境快照、项目产出——打包成一个可搬运资料包，经校验后迁入目标框架，还原为记忆通道 + 可复现环境。迁移的验收标准是**零丢失 + 可续聊 + 环境可复现**：新 Agent 读完资料包，你不需要重新交代任何背景，也不需要重新摸索依赖。

## 快速开始

1. **入口校验**（v2.2 新增，必须先跑）：`preflight_check.py` 确认**源/目标框架**与**任务名称**，并打印备份目录绝对路径（默认桌面）；任务名称缺失会直接停下要你补。
2. **五道确认闸门**（v2.3 新增）：备份过程中 Agent 会**逐道**找你确认——G1 备份范围 → G3 落位（默认桌面）→ G4 附件与成果 → G5 模型 → G2 内容抽检（随机 3 轮对话给你过目）；**没全确认不允许打包**。
3. **备份**（源框架）：对 Agent 说「备份项目」，得到 `~/Desktop/<任务名称>_<时间戳>/`（含 `_environment.json` 环境快照与 `_confirm_gates.json` 确认记录）。
4. **迁移**（目标框架）：放入本 Skill，说「迁移项目」或「对话搬家」——Agent 自检 → 校验 → 全量还原 → 写入记忆通道 → 按环境快照补齐（并提示用同一模型恢复）。
5. **分享**（可选，默认不做）：需要把资料包发给别人 / 发布示例时，才用 `scripts/desensitize.py --share` 生成脱敏副本，原包不出门。

## 核心设计

| 设计点 | 说明 |
|------|------|
| 五层模型 + 环境快照 | L1 对话原文 / L2 项目记忆 / L3 长期蒸馏（重新蒸馏）/ L4 人格（follow 默认全量恢复，keep 存档不覆盖）/ L5 工具与环境（TOOLS/skills/HEARTBEAT/config + `_environment.json`）/ output 选迁 |
| 运行入口闸门 | 备份前先校验平台框架（源+目标）与任务名称；备份目录以任务名命名、落显眼位置（默认桌面），**硬性禁止**写入 agent 安装/数据目录（随卸载连坐删除） |
| 五道确认闸门（v2.3） | G1 备份范围 / G2 内容抽检（随机 3 轮过目）/ G3 落位 / G4 附件与成果 / G5 模型一致性——**逐道向用户确认、逐道落库**；打包前 `--check` 未全确认直接拒绝（rc=2），杜绝"一把梭打包"与串项目 |
| 模型一致性（v2.3） | `_environment.json` 记 `source_model`；还原侧提示"本次备份由该模型完成，建议用同一模型恢复"，减少语气/行为漂移 |
| 框架环境快照 | `_environment.json` 记框架版本、依赖工具版本、config/hooks/权限规则**路径清单**、模型配置白名单键 + `source_model`、OS 版本——只列路径与配置项，不含凭据值 |
| 脱敏定位（v2.2 改） | 脱敏是**可选分享配件**：私有备份 / 本机还原 / 换机默认**完全不脱敏**，凭据随包、恢复即用；仅分享场景出 `_share/` 与 `_credentials_needed.md` |
| raw-v1.0 schema | 与 raw-conversation-backup v1.0.1 / MindVault v3.1 完全兼容，老包直接还原 |
| 还原终点 | 还原的终点是记忆通道 + 环境可跑，不是生成一个 MD 就完了 |
| 十五项验收清单 | 三方对账 / seq 连续 / 轮次完整 / 关键内容抽查 / L5 工具恢复 / 环境对照 / 凭据按场景处置 / 入口校验与目录落位 / 五道确认闸门全通过，缺一不可 |

## 目录结构

```
project-cross-migration/
├── SKILL.md                          # 核心指令集（字段规范 + 备份/还原流程 + 隐私分层 + 验收清单）
├── README.md                         # 本文件
├── LICENSE                           # MIT
├── scripts/
│   ├── preflight_check.py            # 运行入口校验：框架 + 任务名称 + 备份目录落位（默认桌面，v2.2 新增）
│   ├── confirm_gate.py               # 五道分步确认闸门 + 随机抽检 + 打包闸门（v2.3 新增）
│   ├── environment_snapshot.py       # 框架环境快照采集 → _environment.json（v2.2 新增）
│   ├── validate_jsonl.py             # schema + seq 连续性校验（还原前必跑）
│   ├── desensitize.py                # 分享包脱敏器（需显式 --share）+ 本地映射清单
│   └── restore_dialogue.py           # 还原可读对话稿 + 统计报告（附环境快照摘要）
└── examples/
    └── sample-desensitized.jsonl     # 脱敏示例行（全部虚构值）
```

## 脚本用法速查

**运行环境**：Python 3.8+（六个脚本仅依赖标准库，无第三方依赖；macOS / Linux / Windows 均可直接运行）。

```bash
# 0) 运行入口校验（备份前第一步；不通过不许开工）
python3 scripts/preflight_check.py --task-name "<任务名称>" \
    --source-framework "WorkBuddy@1.0.1" --target-framework "OpenClaw@1.4"
# → 输出 backup_dir 绝对路径（默认 ~/Desktop/）；任务名缺失退出码 2，目录落位违规（agent 目录）退出码 3

# 0.5) 五道确认闸门（v2.3 新增；逐道确认、逐道落库，打包前 --check 必须通过）
python3 scripts/confirm_gate.py --list                                        # 看五道闸门定义与状态
python3 scripts/confirm_gate.py --backup-dir <备份目录> --sample --rounds 3   # G2 抽检：随机 3 轮完整对话
python3 scripts/confirm_gate.py --backup-dir <备份目录> --gate G1 --set --value "范围: 项目级…"
python3 scripts/confirm_gate.py --backup-dir <备份目录> --check                # 未全确认 → rc=2，拒绝打包

# 1) 环境快照（随备份包落位）
python3 scripts/environment_snapshot.py --task-name "<任务名称>" \
    --source-framework "Marvis@2.4.0" --target-framework "OpenClaw@1.4" \
    --scan-root <项目目录> --config-file <config.json> --model "<本次所用模型>" \
    --out <备份目录>/_environment.json     # --model 落顶层 source_model（闸门 G5 用）

# 2) 校验（多文件按文件名 rounds 范围排序后传入）
python3 scripts/validate_jsonl.py <dir>/*_rounds-*.jsonl

# 3) 还原为可读对话稿 + 统计报告（平铺或 conversations/ 子目录均可）
python3 scripts/restore_dialogue.py --backup-dir <dir> --label <label>

# 4) 仅分享场景：生成脱敏分享包（映射清单只留本地）
python3 scripts/desensitize.py --share --package <备份目录> --out-dir <分享包目录>
# 无 --share → 直接拒绝（私有备份/还原不脱敏）
```

## 私有备份 vs 分享包

| | 私有备份 / 本机还原 / 换机（默认） | 分享包（发他人 / 发布示例） |
|---|---|---|
| 脱敏 | **完全不脱敏**，原文照搬 | 生成 `_share/` 脱敏副本 |
| 凭据 | **随包**，恢复即用 | 剔除实体，替为占位符 |
| 凭据清单 | 不生成 | `_credentials_needed.md` |
| 命令 | 什么也不用加 | `desensitize.py --share …` |

## 兼容性边界

- **完全兼容**：raw-conversation-backup v1.0.1（WorkBuddy 管道）——tool 条目带完整 content
- **兼容还原**：MindVault OpenClaw/Marvis 模式导出包——tool 条目仅含 key_param/args_summary，校验器按兼容模式放行（INFO 说明），还原不受影响
- **老包兼容**：v2.1.x / v2.0.x 备份包无 `_environment.json` 时，restore 只提示"包内无环境快照（老版本备份包，可忽略）"，不影响还原

## 实测记录

- 2026-09-17 · **v2.4.0 全量实测（六脚本 23 组用例，全通过）**：v2.3.0 的 20 组回归全部复跑通过，另加 3 组一致性断言——
  - X1 六脚本 `VERSION` 常量统一 `2.4.0`（含此前无 VERSION 常量的 `restore_dialogue.py` / `validate_jsonl.py`）
  - X2 六脚本运行时可自报版本（`--list` / 启动横幅 / 结果 generator 字段）
  - X3 文档一致性：README 含 Python 3.8+ · SKILL `version: "2.4.0"` · CHANGELOG 含 v2.4.0 条目且历史条目保留 · 六脚本无残留 2.3.0 版本标注
- 2026-09-17 · **v2.3.0 全量实测（六脚本 20 组用例，全通过）**：
  - preflight 5 组：正常 rc=0（默认落位 `~/Desktop/<任务名>_<时间戳>/`，结果含 confirm_gate 指引）／ 任务名缺失 rc=2 ／ 框架缺失 rc=2 ／ 目录落位违规（agent 数据目录）rc=3 ／ 任务名非法字符 rc=2
  - confirm_gate 6 组：仅列定义 rc=0 ／ 未确认 `--check` 拒绝打包 rc=2 ／ `--sample --rounds 3 --seed 7` 随机抽检 3 轮 ／ G1·G3·G4·G5·G2 逐道落库 + `--reset` 打回 + 重新确认（G5 自动取 `source_model`）／ 五道全确认 `--check` 放行 rc=0 ／ 目录不存在 rc=2
  - environment_snapshot 2 组：`--model deepseek-chat` → 顶层 `source_model` 落档 ／ `--config-file` 白名单取模型 `gpt-4o-mini`，同文件里的 `api_key` 样例值不入档（无泄露）
  - restore 2 组：含快照 → 控制台"模型提示" + `_restored_stats.json` 写入 `model_consistency_hint` ／ 无快照老包友好提示不阻断
  - validate 2 组：合规 rc=0 ／ 损坏 rc=1 精确到行
  - desensitize 3 组：无 `--share` 拒绝 rc=2 ／ 中文紧邻五类敏感值（apikey·邮箱·手机·本机路径）脱敏正确 ／ `--share --package` 出 `_share/` + `_credentials_needed.md`
- 2026-09-16 · **v2.2.0 全量实测（五脚本 12 组用例）**：
  - preflight 5 组：正常 rc=0 ／ 任务名缺失 rc=2 ／ 框架缺失 rc=2 ／ 目录落位违规（写 agent 数据目录）rc=3 ／ 任务名非法字符 rc=2
  - desensitize 3 组：无 `--share` 默认拒绝 rc=2 ／ `--share` 单文件——中文紧邻 apikey·邮箱·openid·手机·本机路径全部正确脱敏（F9 修复确认）／ `--share --package` 整目录出 `_share/` + `_credentials_needed.md`，非文本文件登记待人工确认，映射清单留本地
  - environment_snapshot 1 组：macOS 15.7.9 采集跑通，工具探测/缺失登记正确，成品自检无凭据泄露
  - restore 2 组：含 `_environment.json` → `_restored_stats.json` 写入 `environment_snapshot` 摘要并打印补齐提示 ／ 无快照老包友好提示不阻断
  - validate 2 组：合规 jsonl rc=0 ／ 损坏包 rc=1 并精确定位错误行
- 2026-09-15 · **v2.2.0**：三项改造落地（脱敏降级为可选分享配件 + 环境快照 + preflight 入口校验），文档同步
- 2026-09-15 · 测评修复版 v2.1.1：依据第三方测评（8 组实测）修复 F1-F5，F6-F8 落文档；全部用例复验通过
- 2026-09-12 · macOS 15.7.9 · WorkBuddy → OpenClaw/AutoClaw
- 单项目 146 轮 / 1418 条消息零丢失还原；validate 10 分片全通过；seq 全局连续；三方对账一致
- 脱敏器自测：API Key / 手机号 / 邮箱 / open_id / 本机路径五类占位符全部正确替换

## 协议

- MIT License
- 数据完全本地自持，不上传任何云端
- 备份 / 迁移 / 分享均由用户明确指令触发；分享包是资料离开私有环境的唯一出口
