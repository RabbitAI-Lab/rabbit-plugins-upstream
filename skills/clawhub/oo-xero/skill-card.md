## Description:

Xero (xero.com). Use this skill for ANY Xero request: reading, creating, and updating data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect live Xero connector schemas, read accounting records and reports, and create or update contacts and invoices through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup may direct an agent to execute remote installer scripts in a shell.

Mitigation: Install the oo CLI through a reviewed and verified method before using the skill; do not let an agent run curl-to-bash or irm-to-iex installer commands automatically.

Risk: Write actions can change Xero contacts or invoices.

Mitigation: Require explicit user confirmation of the exact payload and intended effect before creating contacts, creating invoices, or updating invoice status.

Risk: Xero account access is brokered through OOMOL.

Mitigation: Confirm that the deployment is comfortable with OOMOL brokering access to Xero data before installing or using the connector.

## Reference(s):

- [Xero homepage](https://www.xero.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before requests and returns oo CLI JSON responses when actions are run.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
