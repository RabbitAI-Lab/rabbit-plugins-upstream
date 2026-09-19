## Description:

Use this skill for Gumroad requests: reading, creating, and updating data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a connected Gumroad account through the OOMOL oo CLI, including retrieving user, product, subscriber, and sales data. The skill can also guide state-changing sale actions such as marking shipments, refunds, and receipt resends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Refunds and buyer receipt resends can affect customers, payments, or post-purchase communication.

Mitigation: Require explicit user confirmation of the sale ID, payload, and intended effect before running refund_sale or resend_sale_receipt.

Risk: First-time setup includes remote installer commands for the oo CLI.

Mitigation: Prefer a verified or manually inspected oo CLI installation path before executing installer commands.

Risk: The skill relies on an OOMOL-connected Gumroad account with server-side credential handling.

Mitigation: Use the skill only when the user trusts OOMOL with the Gumroad connection and has connected the intended account.

## Reference(s):

- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Gumroad](https://gumroad.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches the live action schema before constructing connector payloads.]

## Skill Version(s):

1.0.4 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
