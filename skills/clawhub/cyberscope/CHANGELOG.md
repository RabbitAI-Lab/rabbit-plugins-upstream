# Changelog

## v2.0.0 — 2026-09-06

**形态变更**：Next.js + PostgreSQL 应用（33 文件，沙箱不可运行）→ 零依赖 Python 标准库
离线 CLI + `data/catalog.json` 单一数据源（9 文件）。目录数据（10 类目 / 62 方法 /
83 来源）与 v1 `src/lib/seed-data.ts` 语义一致，以规范摘要 SHA-256 锚定
（见 references/catalog_schema.md）。

新增（v1 全部缺失）：
- `search` 加权评分：title 1000 / keywords 500 / description 200 /
  resources.title 100 / resources.description 50 + 短语加分；AND 语义；
  score 降序、平局 methodNumber 升序；`--fields basic|all` token 经济投影。
  **修复 v1 召回缺失**：v1 搜索忽略 keywords 数组（如 "solarwinds" 只能命中 m13 的
  keyword，v1 返回 0 结果；v2 正确命中）。
- `method`：数字或标题子串；歧义时 rc 2 + `candidates` 列表。
- `export`：json/csv/md 确定性字节导出（csv 63 行、md 72 个标题、json=源字节）。
- `checksums`：文件 sha + 方法/资源规范内容 sha（对排版不敏感）。
- `verify-sources`：83 URL 纯静态检查（scheme/host/路径/域分类/ATT&CK 格式），
  9 个已知 WARN 基线，输出自带"证明什么/不证明什么"声明。
- `catalog-report`：自改进钩子——43 个单源方法、1 个重复 URL
  （freedomhouse.org/report/freedom-net 用于 m33+m41）、2 个 ATT&CK 斜杠格式
  （m30/m48）→ 机器可执行建议列表。
- `selftest.py`：10 组离线自检（数据保真锚点、搜索语义与排序属性测试、导出确定性、
  校验和、验证/报告行为、退出码纪律、仅标准库、文档幻影）。
- `CYBERSCOPE_CATALOG` 环境变量指向自定义 catalog（测试/扩展）。

移除（v1 缺陷/风险）：
- 搜索历史入库与 `/api/stats` 暴露查询词（隐私风险，skill-card 自述）→ 无状态无历史。
- 死表 `indexed_content`（无写入方）、`drizzle`/`pg`/`next` 依赖、`DATABASE_URL` 需求。
- `package.json` 名残留 "nextjs-postgresql-template" 等模板痕迹。

## v1.0.0 — 2026-04-22

（历史版本：Next.js + PostgreSQL 应用版。见 ClawHub 版本历史。）
