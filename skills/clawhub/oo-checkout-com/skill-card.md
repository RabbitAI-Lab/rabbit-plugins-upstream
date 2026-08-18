## Description:

Checkout.com helps agents read, create, update, and delete Checkout.com customer records through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Checkout.com customer records via the OOMOL checkout_com connector, including read, create, update, and delete actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Create and update actions can change Checkout.com customer records.

Mitigation: Confirm the exact payload and intended effect with the user before running write actions.

Risk: The delete_customer action removes a customer and linked payment instruments.

Mitigation: Confirm the target customer and obtain explicit approval before running destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-checkout-com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Checkout.com homepage](https://www.checkout.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches the live connector schema before payload construction; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
