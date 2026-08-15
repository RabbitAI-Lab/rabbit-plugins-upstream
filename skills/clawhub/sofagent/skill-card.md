## Description:

FDE Skill helps front-line deployment engineers diagnose enterprise AI workflows, constrain agent behavior, audit changes, and retain deployment knowledge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kongfangxun](https://clawhub.ai/user/kongfangxun)

### License/Terms of Use:

MIT-0

## Use Case:

Front-line deployment engineers and enterprise AI teams use this skill to structure FDE discovery, quantify automation opportunities, orchestrate sub-agents, audit changes, and package operational knowledge for deployment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can support broad enterprise orchestration, external commands, persistent local history, and auto-triggered workflows.

Mitigation: Install first in a scoped test workspace, review enabled MCP and CLI tools, and require explicit confirmation before shell commands, activation, market operations, or persistent writes.

Risk: Task logs, reflections, and knowledge files may retain operational context from enterprise deployments.

Mitigation: Define approved storage locations, retention expectations, and cleanup procedures before using the skill with sensitive workflows.

## Reference(s):

- [ClawHub skill release: sofagent](https://clawhub.ai/kongfangxun/skills/sofagent)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and configuration-oriented instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.3.4 (source: release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
