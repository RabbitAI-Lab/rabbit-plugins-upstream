## Description:

BTCPay Server skill for reading, creating, and updating BTCPay Server data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate BTCPay Server through an OOMOL-connected account, including listing stores and invoices, creating invoices, updating invoice metadata, and marking invoice status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that could be unsafe if run blindly.

Mitigation: Review the setup path before installing and prefer a verified, pinned, or package-manager based oo CLI installation when available.

Risk: Write actions can create invoices, update invoice metadata, or manually change invoice status.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [BTCPay Server skill page](https://clawhub.ai/oomol/skills/oo-btcpay-server)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [BTCPay Server homepage](https://btcpayserver.org)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions return JSON data from the OOMOL connector, including execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
