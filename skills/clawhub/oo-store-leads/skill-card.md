## Description:

Store Leads helps agents search and read Store Leads ecommerce app, domain, and technology data through the OOMOL Store Leads connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Store Leads details for ecommerce apps, domains, and technologies, and to list those resources with supported filters and pagination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands can execute code on the user's machine during first-time setup.

Mitigation: Review the official installer instructions, prefer a package manager or verified release when available, and avoid running remote install commands automatically or from an elevated shell.

Risk: The skill depends on OOMOL account authentication and an active Store Leads connection.

Mitigation: Run authentication or connection setup only after a command fails for that reason, and rely on the OOMOL connection flow rather than handling raw Store Leads credentials.

## Reference(s):

- [ClawHub Store Leads skill page](https://clawhub.ai/oomol/skills/oo-store-leads)
- [Store Leads homepage](https://storeleads.app)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and meta.executionId when actions run successfully.]

## Skill Version(s):

1.0.2 (source: release evidence and SKILL.md frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
