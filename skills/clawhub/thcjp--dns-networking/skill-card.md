## Description:

DNS网络管理工具 helps agents debug DNS resolution, TLS certificate details, and network connectivity for authorized systems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and automation agents use this skill to troubleshoot DNS failures, inspect certificate chains, and test network connectivity during development, deployment, and incident response.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill broadens into generic command, file, API, and credential handling without clear boundaries.

Mitigation: Review the skill before installing, keep use within DNS, certificate, and network checks, and do not provide credentials unless the publisher documents the exact service and reason.

Risk: DNS and network checks may target systems the user is not authorized to test.

Mitigation: Use the skill only against systems you are authorized to inspect and review proposed shell commands before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/dns-networking)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review commands before execution and keep use within the stated DNS and networking scope.]

## Skill Version(s):

1.0.2 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
