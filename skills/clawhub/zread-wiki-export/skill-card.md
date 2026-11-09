## Description:

将 zread.ai 上指定 GitHub 仓库的既有 Wiki 保存为本地 Markdown、目录索引和 Git 历史。用于导出、完整保存、更新或续导 Zread 仓库文档；不以重新生成的 Wiki、其他 Wiki 平台或 README 替代原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mc0571](https://clawhub.ai/user/mc0571)

### License/Terms of Use:

MIT-0

## Use Case:

开发者可使用此技能，将 Zread 上指定仓库的 Wiki 完整导出为本地 Markdown 文档库，并维护目录、续导进度与本地 Git 历史。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The extraction repair workflow can make persistent changes to the skill's own instructions.

Mitigation: Review the proposed changes and their source before accepting them; keep edits limited to verified extraction rules.

## Reference(s):

- [正文提取、转换与规则修复](references/extraction.md)
- [ClawHub skill page](https://clawhub.ai/mc0571/skills/zread-wiki-export)

## Skill Output:

**Output Type(s):** [Markdown files, Configuration, Git history]

**Output Format:** [Markdown documentation with an index.md, plus JSON configuration when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves source language and chapter content; reports incomplete exports and failed chapters.]

## Skill Version(s):

0.3.0 (source: SKILL.md frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
