## Description:

Provides auth patterns for API keys, OAuth, and token management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill for implementation guidance when integrating external services, verifying credentials, handling API keys or OAuth, and documenting authentication failure recovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Copy-pasted subprocess and shell examples could be unsafe if arbitrary service names or provider CLIs are accepted without review.

Mitigation: Treat examples as implementation guidance, allowlist expected provider CLIs, and review commands before execution.

Risk: Authentication examples involve API keys, tokens, and local auth caches that may expose credentials on shared or CI machines.

Mitigation: Protect API keys and tokens, prefer short-lived CI secrets, and clear local authentication caches on shared systems.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-leyline-authentication-patterns)
- [Clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python, shell, and YAML examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only guidance; no automatic command execution.]

## Skill Version(s):

1.9.19 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
