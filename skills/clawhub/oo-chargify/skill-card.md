## Description:

Maxio Advanced Billing lets agents search and read customer, product, and subscription data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve and list Maxio Advanced Billing customers, products, and subscriptions from an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup tells users to execute remote installer scripts directly in a shell.

Mitigation: Review the installer before use; prefer an official package manager or a version-pinned download with checksum or signature verification.

Risk: The oo CLI may access Maxio billing data through an authenticated OOMOL connection.

Mitigation: Install and run the CLI only in an environment appropriate for accessing Maxio billing data.

## Reference(s):

- [Maxio Advanced Billing homepage](https://www.maxio.com/product/advanced-billing)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands inspect live action schemas before running connector actions.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
