# CHANGELOG

## 2.0.0 (2026-09-06)

**BREAKING**：移除 v1 引用但不存在的脚本（`skill_add.sh` / `manage_system_prompt.py`——v2 不再在文档中引用任何包外脚本）；移除"每域截断 10 条"。

**新增**
- `scripts/skill_memory.py` — stdlib-only 离线确定性 CLI：`index` / `prompt` / `inject` / `verify` / `stats` / `hook`；stdout 单行 JSON，stderr `{tool,error,hint}`，退出码 0/2/3。
- `scripts/selftest.py` — 全合成 9 夹具自检：frontmatter 边界（`>`/`|`/引号/CRLF/BOM/无 frontmatter/空文件）、`(owner,slug)` 去重、10 域分类、注入幂等（双注入字节不变、哨兵保留、半开/多对/倒序 rc2、不创建缺失文件）、verify 漂移 rc3 + 自愈、hook 三步（成功路径重索引、失败路径退出码透传）、退出码纪律、stdlib-only、文档幻影检查。
- `references/frontmatter_parsing.md` / `references/categorization.md`（完整关键词表 + 工作示例）/ `references/injection_semantics.md`（状态判定工作示例）。
  两处工作示例来自多模型审计（pass-1b，cohere/gemini 对同两例的误判）：分类按优先级扫描（勿按"最强关联"猜）；已有标记对的文件再注入 = replaced/unchanged 而非 appended。

**变更**
- 注入索引 = 每非空域一个头行 `[domain]` + 域内名字各占一行（域优先级序、域内名升序、不截断、无 description）；行格式保证含逗号/引号/冒号的名字可原样往返（逗号拼接做不到）。
- 分类 = 固定 10 域优先级关键词表 + `general` 兜底，first-match-wins。
- 去重键 `(owner, slug)`：owner = 相对路径首个 `@` 段（无则空串），同键保留字典序首路径。
- frontmatter 支持 `>`/`|` 块标量（含 `-`/`+` 变体）、引号标量、BOM 剥离、CRLF 归一；name 缺省=目录名，description 缺省=首个 `#` 标题。
- README 精简（不再逐字复述 SKILL.md，省 ~4KB token）。

**修复**
- v1 "文档引用不存在脚本" 幻影（模型照做必失败的幻觉源 #1）。
