## Description:

Coupang lets an agent read and update Coupang seller products, inventory, prices, orders, and return or cancellation requests through an OOMOL-connected Coupang account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce operators use this skill to inspect Coupang seller catalog, inventory, order, receiver, return, and cancellation data and to make confirmed price or inventory updates through their connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive Coupang seller, order, and receiver data through a third-party connector.

Mitigation: Install only when the user trusts OOMOL with the connected Coupang account, retrieve receiver details only when needed, and avoid exposing returned order data beyond the requested task.

Risk: The artifact includes pipe-to-shell installation commands for the oo CLI.

Mitigation: Prefer a reviewed, pinned, or checksum-verified CLI installation path before using the connector.

Risk: Price and inventory actions can change live Coupang seller state.

Mitigation: Inspect the live action schema and confirm exact targets, payload values, and expected effects with the user before any state-changing action.

## Reference(s):

- [Coupang Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-coupang)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Coupang homepage](https://www.coupang.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include live schema inspection results, connector execution responses, execution IDs, and confirmation prompts for state-changing actions.]

## Skill Version(s):

1.0.2 (source: artifact frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
