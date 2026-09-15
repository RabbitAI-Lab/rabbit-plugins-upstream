## Description:

Cert Spotter (sslmate.com) helps an agent inspect schemas and operate monitored-domain and certificate-issuance workflows through the OOMOL `oo` CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to list, retrieve, create, update, and delete Cert Spotter monitored-domain configurations and to search certificate issuance records for monitored domains.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of mutable remote installer scripts.

Mitigation: Use an official package manager or a verified download with a pinned version and checksum or signature before installation.

Risk: The skill can modify or delete Cert Spotter monitored-domain configurations.

Mitigation: Review write and delete payloads and require explicit approval before running actions that change account data.

Risk: The integration uses OOMOL as an intermediary for Cert Spotter account access.

Mitigation: Install only when the user accepts OOMOL-mediated access to read or modify monitored-domain data.

## Reference(s):

- [Cert Spotter homepage](https://sslmate.com/certspotter/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Cert Spotter ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sslmate-cert-spotter-api)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include confirmation prompts for write or destructive Cert Spotter actions.]

## Skill Version(s):

1.0.3 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
