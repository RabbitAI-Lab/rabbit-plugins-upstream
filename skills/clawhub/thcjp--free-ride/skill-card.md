## Description:

管理并调用 OpenRouter 免费 AI 模型，支持自动化工作流和多场景应用，适合开发者和团队以低成本使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to configure and call free OpenRouter AI models from an agent workflow, including model calls, workflow automation, and status-oriented JSON outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad read/write/exec tool access and unclear automation boundaries could allow unintended file or command actions.

Mitigation: Install in a constrained agent environment, review proposed commands before execution, and limit filesystem and shell permissions to the task.

Risk: The skill asks for an API key and makes unsupported security assurances about encryption and storage.

Mitigation: Provide credentials through environment variables or a secret manager, avoid sensitive inputs, and verify platform storage and transport controls before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/free-ride)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash snippets and JSON result structures]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an API key for model access; avoid sensitive data unless platform controls are documented.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
