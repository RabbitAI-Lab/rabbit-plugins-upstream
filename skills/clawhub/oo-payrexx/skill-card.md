## Description:

Payrexx enables agents to operate Payrexx payment gateways, transactions, and payment-provider data through an OOMOL-connected account using the oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Payrexx payment workflows through an OOMOL-connected account. It supports creating hosted checkout gateways, retrieving gateways and transactions, and listing configured payment providers or transactions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path can execute remote oo CLI installer scripts.

Mitigation: Use a trusted official install path, verify checksum or signature information when available, and avoid running installer commands from an elevated shell.

Risk: The skill can expose Payrexx transaction data or create hosted payment gateways through the connected account.

Mitigation: Review the requested data scope and confirm the exact create_gateway payload and expected effect before execution.

## Reference(s):

- [ClawHub Payrexx Skill Page](https://clawhub.ai/oomol/skills/oo-payrexx)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Payrexx Homepage](https://payrexx.com)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May run Payrexx connector actions through the oo CLI; write actions require payload and effect confirmation before execution.]

## Skill Version(s):

1.0.2 (source: server evidence and skill metadata frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
