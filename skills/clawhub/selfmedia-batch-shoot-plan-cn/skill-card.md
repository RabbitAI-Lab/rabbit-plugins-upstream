## Description:

将已定稿脚本按场景机位合并成现场拍摄顺序与素材命名表。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xxjrq](https://clawhub.ai/user/xxjrq)

### License/Terms of Use:

MIT-0

## Use Case:

短视频创作者和制作团队可以用它把已定稿的多条脚本整理成按场地和机位安排的拍摄顺序，并生成素材命名表。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional npx installer can fetch changing upstream content because its version is not pinned.

Mitigation: Review the CLI version and repository revision before installing.

Risk: A shoot plan may miss production constraints when supplied details are incomplete or outdated.

Mitigation: Provide only production information intended for the agent to process, then review the generated order against current on-set conditions.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/xxjrq/skills/selfmedia-batch-shoot-plan-cn)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown tables, checklists, and example filenames]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports up to 100 script or scene records per batch; missing core fields are listed, and unsupported clock times remain pending.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
