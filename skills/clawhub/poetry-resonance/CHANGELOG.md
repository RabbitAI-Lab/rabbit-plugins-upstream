# CHANGELOG

> **语言范围 / Language scope**：本文件与整个 skill 一样，有意仅用中文——服务对象是唐诗宋词，非中文语种没有对应素材。理由见 `SKILL.md` →「语言范围 / Language scope」。
> This changelog is intentionally Chinese-only for the same reason the skill is: its subject matter is classical Chinese poetry.

## v1.4.6 — 2026-09-13

修正 v1.4.5 里一处**表述与行为不一致**的问题（ClawHub 重新扫描后 ClawScan 新指出的点）：

- v1.4.5 的隐私段写成"只读写两个文件"，但 skill 的**扩库流程**会把新诗追加进 `references/poems.md`（skill 自身目录内）。两处说法矛盾，ClawScan 因此把结论换成「对已安装 reference 库有持久写权限，却声称只写两个数据文件」。
- 修正为**如实分列两个位置**：① 用户数据 = `~/.workbuddy/poetry-resonance/` 下的 `profile.md` / `progress.json`；② skill 自带的 `references/*.md` = **仅在用户明确要求扩库时追加**，不自动写、不删条目、不触碰目录外文件。
- 模式 B 第 9 步由"顺手入库"改为**先问用户是否入库**，同意后再写——消除"自动写 skill 自身目录"的观感。
- 「使用规则 · 扩库流程」与「约束」同步改为准确表述。

SkillSpector 侧在 v1.4.5 已从 11 条 findings 归零（返回 `null`），静态分析 clean，本次不再有变化。

## v1.4.5 — 2026-09-13

安全扫描修复。依据 ClawHub 扫描报告 `skill:poetry-resonance:1.4.4`（ClawScan 判 `suspicious` + SkillSpector 11 条 findings）。本次不改动任何诗词内容与输出质量，只调整行为边界与文档。

**主因修复**
- **日签二维码改为按需嵌入（默认不带）**：原先要求每张卡片固定嵌入 `references/seal_qr.svg`，被 ClawScan 判为「forced promotion / output redirection，对诗词任务非必要且无 opt-in 控制」，是本次被判 suspicious 的唯一 unexpected finding。现在只在用户明确要求分享、或 `profile.md` 设 `qr: true` 时嵌入。

**其余 findings**
- **新增「语言范围 / Language scope」中英双语声明**：说明本 skill 有意仅支持中文（服务对象为唐诗宋词），无多语言版本也无相关计划 → 处理 SQP-3 语言类 6 条。
- **新增「本地数据与隐私 / Local data & privacy」**：表格化说明 `profile.md` 与 `progress.json` 存什么、存在哪、做什么用；首次写入前必须先告知并取得同意，否则进入无持久化模式；提供查看 / 停止 / 删除入口 → 处理 SQP-2 隐私类 2 条。
- **联网部分补充可信性与数据边界**：两个外部接口均只读、免 key、不读环境变量；表格列出各自"发出去的字段"（诗名/作者/诗句/城市名）；明确不传凭证与任何本地文件内容；新增 `online: false` 全局关闭开关 → 处理 E1（External Transmission）。
- **安装命令锁版本**：`npx clawhub@0.23.3 install poetry-resonance` → 处理 RP1（MCP Rug Pull）与 T08。
- **触发词收窄为词组**：`复习`/`周报`/`拆解` 这类会与日常用语重叠的通用词，改为「背诗复习」「读诗周记」「诗词拆解」等词组，并在 description 中注明单独出现的通用词不触发 → 处理 SQP-1（Overly Broad Trigger）。
- **全部 references 文件补中英双语范围标注**（themes.md / weather_map.md / poems.md / poets_profile.md / seal_qr.svg / 两个 json）；天气映射去掉不必要的 `?lang=zh` 参数（映射本就用英文关键词）。

**未改动**：五种模式的工作流、文案风格模板、精读库与底库内容、诗人档案与主题索引条目。

## v1.4.2 — 2026-09-03

体检后调整（基于线上 v1.4.1，正文与线上一致，仅门面优化）：

- 精简 frontmatter `description`：删除冗余修辞、将模式 A–E 描述改为紧凑短语、合并同类信息；匹配入口不变。
- 新增 `version` 字段（frontmatter），建立版本号管理习惯。注册表版本以发布时的 semver 为准。

### 后续待办

- 精读库（references/poems.md）由当前 45 首逐步扩充至 60+ 首。
- 养成版本迭代记录习惯：每次变更同步更新本 CHANGELOG 与 `version`。
