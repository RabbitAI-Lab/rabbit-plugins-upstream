# 触发词让渡登记表

> P1 修复（三框架审计抓到）：oss-workflow 声明「唯一入口」但 oss-voice/oss-contribution/oss-format 的 description 同时持有场景触发词，导致三方命中。
> 原则：**场景词归 oss-workflow 独有；能力词归各 skill 自有**。场景词 = 用户在什么情况下需要帮助；能力词 = skill 具体做什么。

## 让渡规则

| 冲突词 | 归属（唯一 owner） | 让渡方 | 让渡后怎么触发 |
|---|---|---|---|
| README | oss-workflow（场景入口） | oss-voice ~~README~~ → 改「仓库文档写作」 | oss-workflow S3 调度 oss-voice |
| CHANGELOG | oss-workflow | oss-voice ~~CHANGELOG~~ → 并入「仓库文档写作」 | oss-workflow S3 调度 |
| CONTRIBUTING | oss-workflow | oss-voice + oss-format → 改「贡献指南写作」/「贡献指南排版」 | oss-workflow S3 调度 |
| 提 PR / PR | oss-workflow | oss-contribution ~~提PR~~ → 改「P0-P9 管线」 | oss-workflow S2 调度 |
| issue | oss-workflow | oss-contribution → 改「提交后 review 应答」 | oss-workflow S2 调度 |
| docs | oss-workflow | oss-voice → 并入「仓库文档写作」 | oss-workflow S3 调度 |
| 建仓 | oss-workflow | oss-scaffold ~~建仓~~ → 改「脚手架生成」 | oss-workflow S5 调度 oss-scaffold |
| LICENSE | oss-format（能力词：许可证排版规范） | oss-workflow 不持有 | 用户问「许可证怎么排」直接命中 oss-format |
| SECURITY.md | oss-format + oss-security（能力词） | oss-workflow 不持有 | 直接命中 |

## 能力词保留（各 skill 自有，不冲突）

| Skill | 能力词（保留） |
|---|---|
| oss-workflow | （全部场景词：PR/issue/push/commit/建仓/README/CHANGELOG/docs/开源/fork） |
| oss-voice | 仓库文档写作 · 写作风格 · 文档风格 · 多语言文档 |
| oss-format | 排版 · 格式化 · LICENSE 选择 · SECURITY.md 格式 · Issue/PR 模板 · 行为准则 |
| oss-contribution | P0-P9 · 管线门禁 · 开源贡献管线 · review 应答 · 提交后应答 |
| oss-persona | 维护者回复 · 声纹 · 以维护者身份 |
| oss-design | 设计系统选择 · 组件库规范 · 设计审查 · UI/UX 路由 |
| oss-scaffold | 脚手架生成 · 从 0 生成 · 初始化组件 |

## 验收方式

```powershell
# 场景词只命中 oss-workflow
foreach ($word in @("README","CHANGELOG","提 PR","建仓")) {
  $hits = Get-ChildItem D:\xiangmu\dsh\skills-src\local\oss-*\SKILL.md |
    Where-Object { (Get-Content $_.FullName -Raw) -match $word -and $_.Name -ne "oss-workflow" }
  # 期望：0（description 中不含场景词）
}
```

> 例外：SKILL.md 正文的说明段可以引用场景词（说明与 oss-workflow 的关系），但 frontmatter description 不可持有。
