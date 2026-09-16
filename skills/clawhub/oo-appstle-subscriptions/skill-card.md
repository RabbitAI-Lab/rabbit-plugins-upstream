## Description:

Appstle Subscriptions helps agents read customer, subscription, and contract data through an OOMOL-connected Appstle Subscriptions account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search and read Appstle Subscriptions customer, subscription contract, and Shopify customer contract ID data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup points users to remote installer scripts for the oo CLI.

Mitigation: Review the setup path before installing and prefer a verified package or signed, versioned release.

Risk: The connected OOMOL account can access Appstle customer and subscription data.

Mitigation: Confirm the connected OOMOL account is authorized for the target Appstle data before running connector actions.

## Reference(s):

- [ClawHub Appstle Subscriptions Skill](https://clawhub.ai/oomol/skills/oo-appstle-subscriptions)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Appstle Subscriptions Homepage](https://appstle.com)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses include Appstle data returned by the connector and execution metadata; no raw credential output is expected.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
