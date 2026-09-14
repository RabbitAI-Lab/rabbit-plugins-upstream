---
name: cyberscope
version: 2.0.0
description: >
  CyberScope — 可搜索的公开网络攻防/监控/审查方法参考目录：10 类目、62 方法、83 条
  公开来源（MITRE ATT&CK、CISA、NIST、EFF、OWASP、SANS 等）。零依赖 Python 标准库
  离线 CLI：加权搜索（title>keywords>description>resources）、单条明细、导出
  json/csv/md、来源静态验证、目录质量报告（自改进钩子）、校验和锚点。纯参考性
  文档——不含操作性/利用步骤。只读，不联网，确定性输出。
author: orionshaowswmw
license: MIT-0
tags: [cyber-threat-intelligence, surveillance, censorship, threat-modeling, reference, catalog]
metadata: {"openclaw": {"emoji": "🔭"}}
---

# 🔭 CyberScope v2.0.0 — 参考目录 CLI

**一句话**：查询"某网络攻防/监控/审查方法是什么、公开来源在哪"——跑 `search`，
引用结果里的 `resources[].url`。**不要凭记忆编造目录条目；一切以工具输出为准。**

## 何时使用

- 需要某方法的公开定义与权威来源（MITRE ATT&CK / CISA / NIST / EFF / OWASP…）→ `search` / `method`
- 按类目浏览 62 方法 → `categories`
- 全量导出（json/csv/md）供下游处理 → `export`
- 校验目录数据完整性 / 来源链接格式 → `checksums` / `verify-sources`
- 找目录缺口并改进（单源方法、重复 URL、格式问题）→ `catalog-report`

## 加载地图（token 经济）

| 场景 | 读什么 |
|---|---|
| 直接用工具 | 本文 + `python3 scripts/cyberscope.py --help` |
| 评分算法/排序疑问 | `references/search_scoring.md` |
| 数据模型/保真锚点 | `references/catalog_schema.md` |
| 来源验证的边界 | `references/source_verification.md` |

## 命令契约

```bash
python3 scripts/cyberscope.py search Q... [--category SLUG] [--limit N] [--fields basic|all]   # Q 可多词免引号
python3 scripts/cyberscope.py categories
python3 scripts/cyberscope.py method N|标题子串
python3 scripts/cyberscope.py stats
python3 scripts/cyberscope.py export --format json|csv|md --out DIR
python3 scripts/cyberscope.py checksums
python3 scripts/cyberscope.py verify-sources
python3 scripts/cyberscope.py catalog-report
python3 scripts/selftest.py
```

| 命令 | 输出（stdout 单行 JSON） | 退出码 |
|---|---|---|
| search | `{query, n_results, total, results[{id,title,category,category_name,score(,description,keywords,resources when --fields all)}]}`；评分降序、平局 id 升序 | 0 · 2(空查询/未知类目/limit 越界) |
| categories | `{n_categories, n_methods, categories[{numeral,slug,name,count}]}` | 0 |
| method | `{method{id,title,category,category_name,description,keywords,resources[{title,url,source,resourceType,description}]}}` | 0 · 2(不存在/歧义→`candidates`) |
| stats | `{n_categories,n_methods,n_resources,n_sources,methods_per_category,resources_per_type,single_source_method_count}` | 0 |
| export | `{format,file,bytes}`（写 DIR/catalog.json|methods.csv|catalog.md，确定性字节） | 0 · 2(缺 --out) |
| checksums | `{file_sha256, methods_canon_sha256, resources_canon_sha256, 计数}` | 0 |
| verify-sources | `{n_resources, n_errors, n_warnings, issues[{methodNumber,url,code,severity,detail}], limits}` | 0 · 2 · 3(结构性违规) |
| catalog-report | `{single_source_methods, duplicate_urls, attack_slash_format, distribution, recommendations[{methodNumber,action,reason}]}` | 0 |

**值类型**：id/计数/score=JSON number；sha=64 位小写 hex；slug 小写连字符。
**错误**：stderr 单行 JSON `{"status":"error","tool":…,"error":…}`，stdout 保持为空。

## 硬规则（不可违反）

1. **只读**：本工具不修改任何文件；写盘只发生在 `export --out DIR` 显式指定处。
2. **不联网**：所有命令离线；`verify-sources` 是纯静态检查，**不探测 HTTP、不证明链接存活**。
3. **参考性文档**：目录只描述已公开记录的技术（与 MITRE ATT&CK 同类）；**不含操作性步骤、
   载荷或利用指令**，不得用于开展/协助对未授权系统的攻击、监控或破坏。
4. **引用而不放大**：基于目录写作时，链接输出中的 `resources[].url` 公开来源，勿转述为教程。
5. **确定性**：相同输入→相同字节输出（无时间戳/随机）；`export`/`checksums` 结果可复现。

## 自检

`python3 scripts/selftest.py`：10 组检查（数据保真锚点、搜索语义与排序属性、导出确定性、
校验和、来源验证行为、报告行为、退出码纪律、仅标准库、文档幻影）。任何 FAIL 先修工具再交付。

## 边界外（明确不做）

- 不做链接存活探测/内容抓取（沙箱可能离线；需要时由使用者自行打开 URL）。
- 不修改/扩展目录内容——改进走 `catalog-report` 建议 + 人工更新 `data/catalog.json` 后重跑自检。
- 不替代 MITRE ATT&CK 等原始框架；目录是 62 条精选描述+来源的索引层。
