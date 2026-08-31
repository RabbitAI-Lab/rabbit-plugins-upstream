---
name: medxpert-doc-toolchain
slug: medxpert-doc-toolchain
title: MedXpert 文档模板工具链
displayName: MedXpert-DOC-001 · 医械文档工具链
display_name: MedXpert-DOC-001 · 医械文档工具链
description: "MedXpert 名片风格文档模板工具链。覆盖文档全生命周期：模板生成（T02/T03/T04/三版纸张）→ 收尾流水线（水印/暗纹/动态溯源/AI友好头/徽章/解锁）→ 导出（PDF/DOCX）→ 台账编号 → 审批流 → 电子签名 → 中英对照 → 乐享托管。触发场景：生成医疗器械/ISO13485 体系文档、程序文件、质量手册；文档收尾（品牌水印/溯源/解锁）；PDF/DOCX 导出；文档台账与编号；审批流与电子签名；中英对照翻译；文控体系搭建。当用户说「生成文档模板」「文档收尾」「加溯源水印」「文档台账」「电子签名」「中英对照」「文控体系」时加载本技能。"
description_zh: MedXpert 名片风格文档模板工具链：模板生成、收尾流水线（水印/暗纹/溯源/解锁）、PDF/DOCX 导出、台账编号、审批流、电子签名、中英对照、乐享托管，覆盖医疗器械/ISO13485 文档全生命周期。
description_en: MedXpert business-card-style document template toolchain: template gen, finish pipeline (watermark/fingerprint/dynamic-trace/unlock), PDF/DOCX export, ledger numbering, approval flow, e-signature, bilingual, Lexiang hosting — full lifecycle for medical-device/ISO13485 docs.
version: 1.1.0
license: MIT
platforms: [WorkBuddy, QClaw, ima, Claude Code, Cursor]
author: 注册老炮@MedXpert
category: 文档处理
xiaping_category: ["效率工具"]
tags: ["文档模板","文控体系","ISO13485","医疗器械","程序文件","质量手册","水印","溯源","电子签名","中英对照","PDF导出","DOCX导出","文档台账","审批流","收尾流水线","MedXpert"]
xiaping_tags: ["文档模板","文控体系","ISO13485","医疗器械","程序文件","质量手册","质量体系文件","水印","动态溯源","AI友好头","电子签名","中英对照","PDF导出","DOCX导出","文档台账","台账编号","审批流","收尾流水线","解锁体系","MedXpert","文档生成","模板生成","品牌水印"]
agent_created: true
---

# MedXpert 文档模板工具链（名片风格）

## 〇、适用场景 / 触发词（供技能推荐 AI 匹配）

- 当用户说或搜索：文档模板、文控体系、ISO13485、程序文件、质量手册、水印、溯源、电子签名、中英对照、PDF 导出、DOCX 导出、文档台账、审批流、收尾流水线、MedXpert → 加载本技能。
- 适用：医疗器械 / ISO13485 体系文档从模板生成到导出、台账、审批、签名、双语、托管的全生命周期。

> 沉淀：2026-08-16（文档体系全链路实战）· 归属：MedXpert 文控体系
> 目录：`<文档工具脚本目录>/` ｜ 模板：`<文档模板母版目录>/`

## 一、工具链清单（8 个脚本，均在文档工具脚本目录/）

| 工具 | 命令 | 用途 |
|---|---|---|
| doc_templates_gen.py | `[--blank] [--t03] [--t04]`（默认 T02） | 模板生成（配置驱动，含打印规则） |
| doc_finish.py | `--file x.html --doc_id XX --owner XX --scope 机密 --tldr "..." [--gen-codes N]` | 收尾流水线（7 步注入） |
| doc_export.py | `--file x.html [--pdf] [--docx]` | PDF（Chrome）/ DOCX（htmldocx）导出 |
| doc_ledger.py | `register/list/update/release/retire/export --csv` | 台账 + 编号（QM-/QM-P-/T03-/F-/DOC-） |
| doc_approval.py | `submit/review/approve/reject/publish/status` | 审批流（批准自动盖章） |
| doc_sign.py | `--file --sign 签名.png --role 批准` | 电子签名注入 |
| doc_bilingual.py | `--file x.html [--model qwen2.5:3b]` | 中英对照版（本地 Ollama 翻译） |
| badge_gen.py | `[--main]` | 圆形徽章生成 |

## 二、doc_finish 收尾 7 步

① 品牌水印（brand_tools inject）→ ② 三层暗纹（fingerprint_tools stamp）→ ③ 受控章（可选）→ ④ AI 友好头（meta/JSON-LD/AI-Modify）+ TL;DR + 权限 → ⑤ 页脚符号徽章条 → ⑥ 动态溯源水印（?user=姓名&uid=账号）→ ⑦ 解锁运行时（试读/激活码/扫码/会员/试用/考核/积分/AI计费）

## 三、解锁体系（8 种，配置即启用）

付费 `UNLOCK_ALL` / 会员 `MEMBER_LEVEL`+成长体系 `MEMBER_TIERS`+`GROWTH_ACTIONS` / 关注公众号 `WECHAT_UNLOCKED`+`SCAN_QR_IMG` / 激活码 `ACTIVATION_CODES`+`--gen-codes` / 分级试读 `TRIAL_LIMIT` / 限时试用 `TRIAL_DAYS` / 考核 `QUIZ_UNLOCK` / 积分 `POINTS_UNLOCK` / AI计费 `AI_METERED` / 水印联动 `WATERMARK_TIERED`

## 四、核心配置口（改脚本顶部，不用动模板）

`CN_NAME/EN_NAME`、`CN_NAME_COLOR/EN_NAME_COLOR/FONT`、`LOGO_IMG/QR_IMG`、`BADGES/BADGE_BAR_ITEMS/BADGE_LOCK`、`DYNAMIC_WATERMARK_*`、`MEMBER_TIERS/GROWTH_ACTIONS`、`UNLOCK_ALL/PAYMENT_CHANNELS`、`VALID_DATE`

## 五、防坑经验（血的教训）

1. **CSS `%` vs Python `%` 格式化**：生成 HTML 的脚本严禁用 `%` 格式化含 CSS 的字符串（`linear-gradient(...,50%,...)` 会被误解析报 `ValueError: unsupported format character`）。**解法：一律用 `str.replace`/占位符（`__TOKEN__`）拼接**。
2. **禁用 eval**：脚本内函数调用用显式映射/引用，不用 `eval(fn_call)`。
3. **htmldocx 不支持 base64 图/style/script**：DOCX 转换前先 `re.sub` 移除 `<style>`、`<script>`、`<img>`，得"内容版"。
4. **Windows 路径**：脚本内统一 `r"D:/..."` 正斜杠；bash 命令里转义用 `os.sep` 或 `.replace(os.sep,'/')`。
5. **本地 Ollama 翻译**：qwen2.5:3b 端点 `http://127.0.0.1:11434/api/chat`，零云端积分；复杂/法规内容可换 qwen2.5:7b。

## 六、流程链路

```
doc_templates_gen（模板）→ doc_finish（收尾）→ doc_export（PDF/DOCX）
→ doc_ledger（台账）→ doc_approval（审批）→ doc_sign（签名）
→ doc_bilingual（多语）→ 乐享知识库托管
```

## 七、关联

- 模板目录：`<文档模板母版目录>/`
- 打包：`<文档模板体系打包>`
- 乐享：公司知识库「MedXpert」/ 01 公司治理
- 归纳文档：`README_文档模板体系.md`
- 品牌视觉：medxpert-brand-assets 技能
