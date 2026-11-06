## Description:

通过每周探索和反思，帮助学生区分短暂喜好与愿意在困难中继续投入的兴趣。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

学生可用它进行每周兴趣探索，记录吸引自己的内容、面对困难的反应、时间感和具体反馈，并回顾这些线索。跨周追踪前需说明记录与共享方式并取得适当同意；也可选择只进行单次、不保存的探索对话。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cross-week interest summaries may be retained until deletion, and sharing can expose selected information to parents or other skills.

Mitigation: Explain what is recorded, how long it is kept, and who may see it; obtain the required consent, use session-only exploration when preferred, and enable each sharing option separately.

Risk: The host platform and dependent skills may not implement the privacy controls described by the skill.

Mitigation: Confirm that the host and connected skills support the stated consent, access, sharing, pause, export, and deletion controls before enabling persistent tracking.

## Reference(s):

- [兴趣探索记录模板](references/interest-exploration-template.md)
- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-interest-explorer)

## Skill Output:

**Output Type(s):** [Text, Guidance, Structured data]

**Output Format:** [Conversational guidance and structured interest summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce a saved, cross-week interest summary when tracking is enabled and consent is given; otherwise, session-only exploration.]

## Skill Version(s):

2.12.6 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
