## Description:

面向网络小说作者，按请求协助规划、写作与修改长篇网文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

网络小说作者可用它讨论故事结构、规划设定与大纲，并按明确指定范围起草或修订章节。它按阶段停止，方便作者逐步确认创作方向。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill edits local manuscript files and deletes chapter scratch folders after successful commits.

Mitigation: Use a dedicated writing workspace and keep manuscript backups.

Risk: Saved writing preferences persist, and writing agents receive relevant story material.

Mitigation: Review saved preferences and limit each writing agent to relevant story material.

Risk: Host agents were not audited, and automated writing-quality checks have edge cases.

Mitigation: Review host-agent behavior in the deployment environment and manually review drafts alongside automated checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-long-write)
- [OpenClaw source metadata link](https://github.com/zenstory-ai/oh-story-claudecode)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Chinese prose and Markdown plans or manuscript files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scope follows the author's request; chapter writing begins only when explicitly requested.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
