## Description:

A runnable local credential vault skill that helps consolidate scattered passwords, keys, and authorizations into a recoverable vault with tiered access, time-bound token concepts, audit support, CLI tooling, tests, and reference diagrams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and security-minded users use this skill to design and operate a local credential vault, consolidate secrets, and test credential handling workflows with the bundled CLI. Treat it as a local, user-operated vault unless stronger controls are added for agent-facing credential brokerage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Secret values can be exposed through command-line arguments, terminal history, or captured stdout when retrieving credentials.

Mitigation: Use protected input for secrets, avoid logging retrieval output, and require explicit confirmation before revealing stored passwords.

Risk: Dependency risk can increase if local Python packages are installed globally or left unpinned.

Mitigation: Install in an isolated virtual environment, pin and audit dependencies, and review package updates before deployment.

Risk: The release should not be treated as an agent-safe credential broker without stronger controls.

Mitigation: Use it as a local, user-operated vault unless adding stronger authorization boundaries, least-privilege access, and explicit approval flows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/credential-vault-design)
- [Security audit report](SECURITY_AUDIT_云鼎_2026-08-26.md)
- [Security test results](tools/security_results.json)
- [Credential vault panorama](references/panorama.svg)
- [Security radar diagram](references/panorama-security-radar.svg)
- [Capability diagram](references/panorama-capabilities.svg)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with CLI commands and optional Python code or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May respond in the user's language; examples focus on local vault operations.]

## Skill Version(s):

2.0.0 (source: frontmatter, manifest, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
