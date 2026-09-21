## Description:

DACHSER lets agents retrieve delivery order status, shipment history, and shipment status through an OOMOL-connected DACHSER account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to query DACHSER delivery order and shipment status data through OOMOL's DACHSER connector. It supports read-only logistics lookups after the user has installed the oo CLI, signed in, and connected DACHSER.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the OOMOL CLI and a connected DACHSER account, so setup may involve installer and authentication steps.

Mitigation: Verify the OOMOL CLI install source and authenticate only through the official OOMOL connection flow.

Risk: The skill retrieves DACHSER shipment and delivery-order data that may be sensitive.

Mitigation: Use it only in workspaces authorized for the connected DACHSER account and avoid sharing returned shipment details outside approved channels.

## Reference(s):

- [ClawHub DACHSER skill page](https://clawhub.ai/oomol/skills/oo-dachser)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [DACHSER homepage](https://www.dachser.com/)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution so payloads match DACHSER's expected inputs.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
