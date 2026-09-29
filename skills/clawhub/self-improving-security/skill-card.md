## Description:

Helps agents record security findings and incidents in local Markdown logs and turn reviewed lessons into reusable security guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jose-compu](https://clawhub.ai/user/jose-compu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to document vulnerabilities, access issues, compliance gaps, and incident lessons, then review recurring findings for inclusion in security guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security logs or generated lessons could disclose secrets or personal information.

Mitigation: Redact sensitive details before logging and review learning entries before sharing or promotion.

Risk: Persistent hooks could run outside the intended project or generate unwanted reminders.

Mitigation: Keep hooks opt-in and project-scoped, with narrow matchers.

Risk: Unreviewed security notes could become misleading agent instructions.

Mitigation: Require reviewed diffs and explicit approval before promoting notes or extracted skills into instruction files.

Risk: An insecure TLS test pattern could be copied into routine use.

Mitigation: Do not reuse the curl -k test pattern outside isolated testing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/jose-compu/skills/self-improving-security)
- [Security logging examples](artifact/references/examples.md)
- [Project hook setup](artifact/references/hooks-setup.md)
- [OpenClaw integration](artifact/references/openclaw-integration.md)

## Skill Output:

**Output Type(s):** [Markdown, Security guidance, Shell commands, Configuration guidance]

**Output Format:** [Markdown logs and text guidance, with optional shell commands and hook configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-local records; optional reminders; extracted skills require human review.]

## Skill Version(s):

1.2.2 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
