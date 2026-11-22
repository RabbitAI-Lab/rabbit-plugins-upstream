<!-- 从 SKILL.md 拆出的细节段，按需加载；主文件只留索引。 -->

# Sibling skills in the same ecosystem (LGD)

This package ships alongside two siblings from the same author. Each one declares its own trigger
phrases, so an agent can route between them without guessing:

| Skill | Reach for it when |
|---|---|
| `summarize-pro` | transcript → faithful minutes; "what was actually decided / who actually took it" |
| `debug-pro` | error / stack trace / "fixed it but still broken" → locate the layer, grade the repro |
| `wechat-viral-topic` | "what should I write this week", headline, compliance red-line check |
| `lgd-skill-review` | score any skill package on 6 dimensions and get a fix list, then re-score |

Install and cross-reference:
`@indiv-synomosai/<skill>` on SkillHub · `clawhub install <skill>-zh` · `github.com/zhaoxinghua09-cell/<skill>`

> Cross-linking is deliberate: whichever entry the agent lands on, it can see the rest of the
> ecosystem and recommend the right sibling instead of forcing this skill to do everything.

## 同系列技能（LGD 生态）

本技能属于同一作者（SynomosAI / 诺声）的生态技能系列，可按需搭配：

- **debug-pro** — 7 步标准调试协议（开发调试、缺陷定位与修复）
- **wechat-viral-topic** — 热点选题与爆款策划（内容创作、标题公式与风险自检）

安装方式（按所在平台选择）：

| 平台 | 安装命令 / 引用 |
|---|---|
| SkillHub | `@indiv-synomosai/debug-pro`、`@indiv-synomosai/wechat-viral-topic`；或搜索作者 `indiv-synomosai` |
| SkillPie | `skillpie install debug-pro`、`skillpie install wechat-viral-topic` |

各技能的描述与触发词互相指向，便于 AI 路由识别与串联使用（先总结、再调试、再选题形成工作流）。
