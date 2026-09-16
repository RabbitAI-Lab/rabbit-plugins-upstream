## Description:

Polar (polar.sh) lets an agent retrieve Polar customers, customer state, orders, organizations, products, and subscriptions through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and support teams use this skill to inspect Polar commerce data and run supported Polar connector actions without calling the Polar API directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to execute remote installer scripts in a shell.

Mitigation: Review setup before installation and prefer a trusted, pinned, or otherwise verifiable oo CLI release path.

Risk: The connected Polar account can expose customer, order, organization, product, and subscription data.

Mitigation: Confirm the intended Polar account and permissions before use, and inspect the live connector schema before constructing action payloads.

Risk: Some actions are documented as write or destructive operations.

Mitigation: Confirm the exact payload, target, and expected effect with the user before running state-changing actions, and require explicit approval for destructive actions.

## Reference(s):

- [Polar homepage](https://polar.sh)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-polar)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands run through the oo CLI and may return JSON data from Polar connector actions.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
