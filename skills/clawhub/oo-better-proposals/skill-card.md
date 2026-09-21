## Description:

Better Proposals helps an agent search and read Better Proposals account data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent inspect Better Proposals account data, including proposals, quotes, templates, companies, currencies, document types, merge tags, brand settings, and account settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup guidance includes remote installer commands for the oo CLI.

Mitigation: Review the CLI installation source before installation and prefer installing the CLI manually from a verified OOMOL source.

Risk: Using the connector can expose proposal, company, quote, template, settings, and billing-related data from the connected Better Proposals account.

Mitigation: Connect only a Better Proposals account whose data the user is comfortable exposing through this connector.

## Reference(s):

- [Better Proposals homepage](https://betterproposals.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-better-proposals)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect the live connector schema before running read-only Better Proposals actions.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
