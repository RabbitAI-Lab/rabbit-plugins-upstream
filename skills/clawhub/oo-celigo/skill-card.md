## Description:

Celigo (celigo.com). Use this skill for Celigo requests that search or read data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and business users use this skill to inspect Celigo account metadata and retrieve Celigo flows, exports, imports, connections, and token information through the OOMOL oo CLI connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup instructions can execute a remote oo CLI installer script with local user privileges.

Mitigation: Review the installer source and prefer a signed or package-manager installation path before running the installer.

Risk: Connector actions depend on the user's connected Celigo account and live action schemas.

Mitigation: Fetch the action schema before constructing payloads and limit execution to the listed read-only get and list actions unless future actions are explicitly reviewed.

## Reference(s):

- [Celigo homepage](https://www.celigo.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-celigo)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns oo CLI connector responses with data and execution metadata.]

## Skill Version(s):

1.0.4 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
