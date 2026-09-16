## Description:

Google Ads helps agents read, create, update, and delete Google Ads data through the OOMOL googleads connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Google Ads accounts from an agent, including campaign lookup, customer and customer-list listing, GAQL search, and approved write workflows for campaigns, ad groups, and Customer Match lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users or agents to run remote installer scripts directly in a shell.

Mitigation: Prefer a pinned installer or package-manager install with checksum or signature verification before installing the oo CLI.

Risk: Write and destructive Google Ads actions can change campaigns, ad groups, customer lists, or Customer Match membership.

Mitigation: Review the live action schema, exact payload, target account, and expected effect, then require explicit user approval before execution.

Risk: Google Ads operations and credentials are handled through OOMOL server-side services.

Mitigation: Install only when the user accepts OOMOL handling Google Ads operations and credentials, and verify account connection and scope before use.

## Reference(s):

- [ClawHub Google Ads Skill](https://clawhub.ai/oomol/skills/oo-googleads)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Google Ads](https://ads.google.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May run OOMOL googleads connector actions that return JSON data and an execution ID.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
