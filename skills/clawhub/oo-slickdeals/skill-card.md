## Description:

Slickdeals lets agents search and read Slickdeals deals, coupons, stores, brands, categories, deal types, and shopping articles through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve Slickdeals shopping data, including current deals, coupons, stores, brands, categories, deal types, and shopping articles. It is suited for deal discovery, coupon lookup, and shopping research workflows that need read-only Slickdeals data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the external OOMOL oo CLI, an OOMOL account connection, and possible OOMOL connector billing credits.

Mitigation: Review the OOMOL CLI and Slickdeals connection setup before installing, and run sign-in, connection, or billing steps only when the corresponding command failure occurs.

Risk: Connector payloads can become incorrect if the current Slickdeals action schema changes.

Mitigation: Fetch the live connector schema before each action and build JSON payloads against that schema.

## Reference(s):

- [Slickdeals ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-slickdeals)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Slickdeals](https://slickdeals.net/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-focused Slickdeals connector results are returned as JSON through the oo CLI; the live action schema should be checked before building payloads.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
