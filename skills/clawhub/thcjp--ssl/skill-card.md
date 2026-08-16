## Description:

SSL证书工具 helps agents set up HTTPS, manage TLS certificates, and debug secure connection issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to plan HTTPS setup, TLS certificate application, renewal, deployment, connection debugging, and security checks for domains and servers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may propose command execution, file changes, certificate requests, renewals, or deployment steps with broad authority.

Mitigation: Require explicit user approval for each command, file write, certificate operation, renewal, and deployment action before execution.

Risk: TLS private keys, API credentials, or certificate authority account material could be exposed during certificate management workflows.

Mitigation: Do not send private keys or API credentials to external services unless the user deliberately approves the exact disclosure and destination.

Risk: Incorrect HTTPS or certificate guidance could affect live server availability or security.

Mitigation: Review proposed configuration and renewal changes in a staging environment or maintenance window before applying them to production systems.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ssl)
- [SkillHub skill listing](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with optional shell commands and JSON-style assessment summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include domain, certificate type, TLS assessment details, and remediation suggestions.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter states 1.0.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
