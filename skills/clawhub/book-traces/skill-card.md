## Description:

编排从选书、对话式挖掘阅读素材到梳理脉络与沉淀内容、方法和工具成果的完整读书工作流。

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

读者可用它把认真阅读一本书的过程转化为与自身经验相关的笔记、脉络梳理和多平台草稿。它适合希望深入阅读并形成成果的人，不适合快速查书或在缺少本人素材时代写观点。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reading notes, personal reflections, and book-page photos may be saved in the workspace and retained across the workflow.

Mitigation: Review saved files and exclude sensitive personal or financial information before storing them.

Risk: Content may be sent to external checking services or draft accounts through companion skills.

Mitigation: Review each destination and companion skill before sending content; keep sensitive material out of external submissions.

Risk: The packaged frontmatter may need correction before the skill loads correctly.

Mitigation: Check that the frontmatter parses successfully before loading or editing the skill.

## Reference(s):

- [0号样本复盘：下一代学校](references/0号样本-下一代学校复盘.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown reading notes, book outlines, reflection prompts, and platform-specific draft text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ground outputs in the reader's supplied highlights and reflections; review drafts before publication.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata; SKILL.md frontmatter lists 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
