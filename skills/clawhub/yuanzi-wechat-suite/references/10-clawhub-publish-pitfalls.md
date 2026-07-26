# 10. ClawHub 发布踩坑（fork / AMBIGUOUS / CLI 限制）

> 来源：MEMORY.md「skill_workshop 工具踩坑 + SOP」（同源教训）
> 来源：memory/2026-07-04.md（元子系列发布实战）

## 7 大踩坑（发技能必读）

### 1. AMBIGUOUS_SKILL_SLUG（最关键）

**症状：** 同一 slug 多个 owner 时，`clawhub install <slug>` 失败。

**根因：** ClawHub 允许多 owner 同 slug，但 CLI `install` 无 `--owner` 选项。

**CLI 限制：**
- `install` / `update` / `hide` / `delete` / `rename` 均无 `--owner` flag
- `normalizeSkillSlugOrFail` 拒斜杠（`golikegod/slug` 视为非法）
- 多种 URL 形式（`@owner/slug`、`owner/slug`、完整 URL）均失败

**解决：** 用独特 slug 前缀重发（如 `yuanzi-`）。

### 2. `clawhub skill rename` 二次 JSON.stringify

**源码：** `dist/cli/commands/ownership.js:38`
```js
body: JSON.stringify({ newSlug }),  // 已被 stringified，再 stringify
```

**症状：** rename 失败，「newSlug required」

**根因：** `args.body` 已是 stringified 结果，再 `JSON.stringify` 导致 server 拒收。

**解决：** CLI bug，需等官方修复或绕过（直接发新 slug）。

### 3. fork-of 不可用

`--fork-of <slug[@version]>` 在原 slug AMBIGUOUS 时失败（server 无法解析 fork 目标）。

**解决：** 跳过 `--fork-of`，在 changelog 写明「Fork 自 <owner>@<ver>」+ 原 URL。

### 4. package.json 误判 plugin

`package.json` 含 `openclaw: { type: "skill" }` 时，clawhub 视为 plugin，拒发 skill。

**解决：** 精简 package.json，删 `openclaw` 段，仅保留 name/version/keywords/author/license/repository。

### 5. skill-card.md 禁直发

`skill-card.md` 是 ClawHub 自动生成，禁止直接发布。

**解决：** 发布前删除。

### 6. clawhub sync 卡 slug 冲突

`clawhub sync --all` 扫全 50+ skill，遇到 `self-improving-agent` slug 冲突卡住。

**解决：** 走单次 `clawhub skill publish`，可控。

### 7. install / update 缺 owner 消歧

CLI 设计缺陷：owner 必须从 auth token 推断，AMBIGUOUS 时无法选择。

**解决：** 新用户用独特 slug 安装（`clawhub install yuanzi-...`）；本机 `update` 仍走哈希匹配，不受影响。

## 端到端发技能流程

```
1. 清冗余（删 node_modules / 临时数据 / token_cache / skill-card.md）
2. SKILL.md 加系列标识 + 元数据
3. clawhub skill publish <dir> --slug <unique-slug> --name "..." --version X.Y.Z --changelog "..."
   - 3 fork 必须用独特 slug（避开原 owner）
   - 3 fork 省略 --fork-of（AMBIGUOUS 时失败），改在 changelog 写明
4. 验证：clawhub install <slug> --dir <tmp> --force
5. 更新本地 .clawhub/origin.json：slug + previousSlugs
```

## 老板教训

> 元子系列 1.0 首发踩了 6 个坑，全写在 MEMORY.md 防止下次重蹈 — 老板 2026-07-04

---

*🦞 元子公众号图文系列 · 知识舱 · 10 ClawHub 发布踩坑*