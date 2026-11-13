## Description:

设计、审查和重构面向 AI Agent 的 CLI。检查可预测性、纵深防御和上下文效率，并用实际证据评分。用于开发 Agent DX CLI 或检视现有 CLI。

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

开发者和 CLI 工程师使用此技能设计、审查或重构面向智能体的命令行工具，并根据实际契约和验证证据评估结果。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Google Drive metadata example may not fit a CLI-review task.

Mitigation: Check whether the example applies before using it, and keep conclusions grounded in the target CLI and task.

Risk: A local path-like reference was unresolved, so the available scan evidence does not establish that every referenced item was reviewed.

Mitigation: Resolve and review that referenced item before relying on it.

## Reference(s):

- [CLI 工程原则与正反例](references/agent-dx-patterns.md)
- [GWS 实践](references/gws.md)
- [SKILL+CLI 技能编写](references/skill-cli.md)
- [Google Workspace CLI 0.22.5 source reference](https://github.com/googleworkspace/cli/tree/a3768d0e82ad83cca2da97724e46bea4ff0e6dbd/crates/google-workspace-cli/src)
- [ClawHub release page](https://clawhub.ai/agenticweb4/skills/agent-dx-cli-cn)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with code blocks and structured evidence]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports changes, evidence-based scores, validation results, and unresolved limitations.]

## Skill Version(s):

0.4.2 (source: artifact/SKILL.md frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
