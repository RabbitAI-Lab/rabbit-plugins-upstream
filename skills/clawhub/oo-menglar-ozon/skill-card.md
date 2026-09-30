## Description:

Menglar Ozon Data helps agents search and read Ozon marketplace sales, demand, traffic, and competitive data through the OOMOL Menglar Ozon connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to research Ozon marketplace products, shops, brands, categories, keywords, traffic, and historical sales trends through an OOMOL-connected Menglar Ozon account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow may use a remote installer for the oo CLI.

Mitigation: Confirm the installation source is trusted and use organization-approved checksum, signature, or package-manager controls when required.

Risk: Connector runs access data through the user's OOMOL-connected Menglar Ozon account.

Mitigation: Verify the intended account connection and requested action before running commands, and rely on live schema inspection to keep payloads scoped to the request.

Risk: Billing or account connection failures may block connector access.

Mitigation: Only follow authentication, connection, or billing setup steps after a command fails with the matching error.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-menglar-ozon)
- [Menglar Ozon Data Homepage](https://ozon.menglar.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing JSON payloads.]

## Skill Version(s):

1.0.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
