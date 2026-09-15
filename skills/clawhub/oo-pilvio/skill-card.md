## Description:

Pilvio lets agents read Pilvio account, billing, location, and virtual machine data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Pilvio account information, billing accounts, available locations, and virtual machines from an already connected Pilvio account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote installer commands that execute downloaded scripts in a shell.

Mitigation: Use the setup path only after an auth or CLI failure, review the installer source first, and prefer a verified package-manager installation path when available.

Risk: The skill depends on an authenticated OOMOL-connected Pilvio account and server-side credential injection.

Mitigation: Run read actions only after confirming the intended account context and fetch each action schema before constructing payloads.

## Reference(s):

- [Pilvio homepage](https://pilvio.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-pilvio)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are returned as JSON with data and meta.executionId fields.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
