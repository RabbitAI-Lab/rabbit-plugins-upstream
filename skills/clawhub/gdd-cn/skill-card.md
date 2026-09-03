## Description:

中文游戏系统策划案（GDD）编写。按国内研发流程逐节推进：先对齐定位与竞品，再写规则、公式、配置表结构、边界、依赖、数值可调项、验收标准。数值优先落配置表，落笔前过一遍专家视角自检。触发词：写策划案、做系统策划案、GDD、系统拆解、配置表设计。

This skill is ready for commercial/non-commercial use.

## Publisher:

[sharinchan233](https://clawhub.ai/user/sharinchan233)

### License/Terms of Use:

MIT-0

## Use Case:

Game designers, systems designers, and development teams use this skill to draft Chinese-language single-system GDDs through a confirmation-driven workflow. It gathers project context, asks for decisions, drafts each GDD section, defines configurable values in tables, and checks the result before file updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads nearby project design documents to gather context, which may expose sensitive planning details to the active agent session.

Mitigation: Install and run it only in workspaces where the agent is authorized to inspect the relevant planning documents.

Risk: The skill can create or edit GDD files under the planning document structure.

Mitigation: Keep the documented confirmation workflow enabled and review proposed drafts before approving file writes.

## Reference(s):

- [配置表规范](references/config-table-spec.md)
- [术语对照与文风约束](references/naming-glossary.md)
- [专家视角自检清单](references/review-checklists.md)
- [章节写作细则](references/section-playbook.md)
- [ClawHub skill page](https://clawhub.ai/sharinchan233/skills/gdd-cn)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Chinese Markdown documentation with tables, review findings, and confirmation prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or edit planning documents under the project GDD structure only after explicit user confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
