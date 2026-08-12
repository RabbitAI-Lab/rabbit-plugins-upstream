## Description:

API网关管理器(专业版) helps agents generate guidance, configuration, and commands for enterprise API gateway management, including multi-tenant rate limiting, circuit breaking, canary release, dynamic configuration, observability, and plugin workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and platform engineers use this skill to plan, validate, and operate API gateway configurations across Kong, APISIX, Nginx, or Envoy environments. It is intended for agent-assisted gateway governance tasks such as routing, throttling, rollback, observability setup, and dry-run validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can ask an agent to manage live API gateway infrastructure with command and write authority.

Mitigation: Confirm the target environment, scope, and intended change before running commands or writing configuration files.

Risk: Gateway apply, rollback, login, observability, and traffic replay commands can affect production behavior or expose credentials.

Mitigation: Prefer dry-run or validation first and require explicit approval for apply, rollback, login, credential, observability, or replay commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/gateway-manager)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON, YAML, and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose live gateway operations and file writes; users should require confirmation before execution.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
