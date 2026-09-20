# project-cross-migration 免费版 v2.4.2 — 锁口引导说明

## 本包性质

本包为 **project-cross-migration 标准免费版（v2.4.2）**，免费、零付费、无付费拆分。
本包为免费开源版本，无任何付费限制。

## 已锁定的功能

以下三个脚本在免费版中功能被锁定，所有子命令均输出统一提示并退出：

| 脚本 | 锁定的功能 |
|------|-----------|
| `scripts/confirm_gate.py` | 五道分步确认闸门（G1-G5 逐道确认 + 打包闸门） |
| `scripts/environment_snapshot.py` | 框架环境快照采集 → `_environment.json` |
| `scripts/desensitize.py` | 分享包脱敏器（`--share` 模式） |

## 如何获取完整版

完整版解锁全部功能，包括五道确认闸门、环境快照、脱敏分享包等。

**获取完整版**：<https://wzyp.cn/item/p0r2lb>

## 已可用的功能

免费版已可用：

- `scripts/preflight_check.py` — 运行入口校验（平台框架 + 任务名称 + 备份目录落位）
- `scripts/validate_jsonl.py` — JSONL schema + seq 连续性校验（还原前必跑）
- `scripts/restore_dialogue.py` — 还原为可读对话稿 + 统计报告
- `scripts/desensitize.py` — 仅分享场景：生成 `_share/` 脱敏副本（**免费版锁定**）
- `scripts/restore_dialogue.py` — 还原为可读对话稿 + 统计报告（附环境快照摘要）

## 核心流程

**备份 → 搬运 → 还原**：
1. `preflight_check.py` 确认平台、任务名称、备份目录
2. `restore_dialogue.py` 导出 JSONL 到备份目录
3. `validate_jsonl.py` 校验 JSONL 文件
4. `restore_dialogue.py` 将备份还原为可读对话稿

## 获取完整版

完整版解锁全部功能，包括五道确认闸门、环境快照、脱敏分享包等。

**获取完整版**：<https://wzyp.cn/item/p0r2lb>
