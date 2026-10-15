## Description:

帮助用户撰写和检查中文文档，并在保留事实与原意的前提下诊断、改写中文文章和文案。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huiyonghkw](https://clawhub.ai/user/huiyonghkw)

### License/Terms of Use:

MIT-0

## Use Case:

中文内容创作者和文档编写者可用它整理、修订和检查方案、报告等文档，或诊断并改写公众号文章和文案；重要事实及数字仍需核实。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad writing triggers may activate the workflow for requests outside its intended scope.

Mitigation: Confirm the user's intended task and review the proposed scope before applying changes.

Risk: Supplied documents may contain private details, and skill-local learning notes may persist details from past work.

Mitigation: Review document access and learning notes; omit secrets and redact identifying details.

Risk: Time-sensitive facts may be unverified; optional git hooks or edits to installed skill files change the working environment.

Mitigation: Verify consequential claims against current sources, and review optional hooks and skill-file edits before enabling them.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/huiyonghkw/skills/hekouwang-writer-skill)
- [Project homepage (release metadata)](https://github.com/huiyonghkw/hekouwang-writer-skill)
- [Writing workflow](references/write-flow.md)
- [Evidence and delivery guidance](references/evidence-and-delivery.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese prose or Markdown with review findings and revision notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a change list and items requiring factual verification.]

## Skill Version(s):

1.2.0 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
