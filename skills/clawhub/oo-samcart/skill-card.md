## Description:

Operate SamCart through an OOMOL-connected account using the oo CLI to inspect schemas and retrieve or list customers, orders, products, and subscriptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate SamCart through an OOMOL-connected account. It helps agents inspect live connector schemas and run SamCart customer, order, product, and subscription actions with documented setup recovery steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup includes remote installer commands for the OOMOL CLI.

Mitigation: Prefer a version-pinned, checksum- or signature-verified install path before running CLI setup commands.

Risk: The get_order action is tagged as write while its description says it retrieves an order.

Mitigation: Treat get_order as potentially state-changing until the publisher clarifies it, and confirm the payload and expected effect before execution.

Risk: SamCart actions operate through a connected OOMOL account and can access marketplace data.

Mitigation: Inspect the live action schema before submitting payloads and apply the documented confirmation rules for write or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-samcart)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [SamCart homepage](https://www.samcart.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions return JSON responses with data and meta.executionId when run through the oo CLI.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
