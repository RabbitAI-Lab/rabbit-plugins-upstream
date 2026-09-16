## Description:

Fidel API helps agents search and read Fidel API data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Fidel API connector schemas and fetch brand, card, and transaction records through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote shell installer commands without integrity verification.

Mitigation: Review the oo CLI installation path before installing, prefer official package-manager or version-pinned instructions with checksum or signature verification, and do not let an agent run the remote installer automatically.

Risk: Connector calls depend on a live authenticated OOMOL account, a connected Fidel API credential, and sufficient billing credit.

Mitigation: Run setup or account recovery only after a matching authentication, connection, scope, credential, app, or billing error occurs.

Risk: Incorrect payloads can cause failed or misleading Fidel API calls.

Mitigation: Fetch the live connector schema for the selected action before constructing each payload.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-fidel-api)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Fidel API homepage](https://fidel.uk)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId when oo CLI actions are run.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
