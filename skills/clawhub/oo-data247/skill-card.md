## Description:

Data247 routes Data247 lookup requests through schema inspection and connector calls with the OOMOL oo CLI instead of direct API access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to query Data247 phone, DNC, carrier, balance, and name-gender inference actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions run remote installer scripts directly from the shell.

Mitigation: Review the installer path before use and prefer a pinned, signed, or checksum-verified installer.

Risk: Connector calls depend on a correctly authenticated and connected OOMOL account.

Mitigation: Only run setup or connection recovery steps after an action fails with the matching authentication, connection, scope, or billing error.

## Reference(s):

- [Data247 homepage](https://www.data247.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-data247)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing Data247 action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
