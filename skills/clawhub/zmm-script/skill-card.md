## Description:

协助知识型创作者通过脚本类型选择、内容单元装配和逐段共创来撰写知识付费口播稿，而不是一次性生成成稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External content creators and solo knowledge-business operators use this skill to turn topics, personal material, and content units into talking-head video scripts with shot notes, alternate hooks, and material collection checklists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can direct an agent to read broadly from a local content vault, which may expose private drafts, business notes, or personal material.

Mitigation: Use it only with vaults intended for script collaboration, and require the agent to summarize which paths it needs before reading sensitive areas.

Risk: The skill directs draft saves and write-backs to framework, content-library, and memory files, which could modify shared working knowledge without enough review.

Mitigation: Require explicit approval before every file write, including the exact target path and a reviewable diff.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-script)
- [Concept-style talking-head script reference](artifact/references/概念型口播.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Files]

**Output Format:** [Markdown tables and prose with talking-head script copy, shot notes, alternate hooks, and material collection checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or create local draft, framework, content-library, and memory updates when the user permits those writes.]

## Skill Version(s):

0.2.4 (source: server release metadata; artifact frontmatter says 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
