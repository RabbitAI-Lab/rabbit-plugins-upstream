## Description:

Jira PAT管理器 is a Chinese-language agent skill for managing Jira personal access tokens, including token creation, revocation, permission configuration, API-call handling, and structured error responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, Jira administrators, and automation teams use this skill to guide agent workflows for creating, revoking, and configuring Jira personal access tokens, with structured API-response handling and troubleshooting guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill concerns Jira token creation, revocation, and permission changes, which are sensitive administrative actions.

Mitigation: Require explicit user confirmation before revoking tokens or changing permissions, and run only in environments where those Jira operations are intended.

Risk: Server security evidence flags broad API, analytics, file, and command-execution language around a sensitive token-management purpose.

Mitigation: Avoid granting shell, broad file, or generic API access unless the publisher narrows and documents those capabilities for the deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/jira-pat-manager)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Guidance, Configuration, Shell commands, JSON]

**Output Format:** [Markdown guidance with JSON examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API-response structures and error-handling steps.]

## Skill Version(s):

1.0.0 (source: server release evidence; artifact frontmatter lists 0.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
