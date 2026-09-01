## Description:

Designs a reusable method for authorization-code and local credential-broker flows that give AI agents short-lived, scoped, revocable access without placing secrets in model context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and security engineers use this skill to design local credential-broker patterns for AI agents and local programs. It is most relevant when credentials need short TTLs, narrow scopes, audit records, device-aware revocation, and a boundary that keeps secrets out of model prompts and persistent logs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included broker handles vault secrets and should be reviewed before use with real credentials.

Mitigation: Treat it as a prototype, run it only in an isolated environment, and perform security review before connecting real vault data.

Risk: The dashboard PIN can be exposed through URL query strings and startup output.

Mitigation: Remove PINs from URLs and console output; prefer header-based or session-based local authentication.

Risk: The audit log records credential titles, scopes, devices, and activity metadata.

Mitigation: Protect audit logs and audit keys with local access controls and review retention expectations before deployment.

Risk: The broker is intended for local-only use.

Mitigation: Keep the service bound to 127.0.0.1 and avoid exposing it to network interfaces.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/authz-code-design)
- [Broker architecture diagram](artifact/references/broker-arch.svg)
- [Security test results](artifact/tools/security_results.json)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with optional code, shell commands, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local credential-broker design patterns, prototype commands, audit and revocation guidance, and security caveats.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
