## Description:

Coupang (coupang.com). Use this skill for ANY Coupang request -- reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and commerce operators use this skill to let an agent inspect Coupang seller products, inventory, orders, and return or cancellation requests, then prepare or execute approved price, inventory, and order-related updates through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change Coupang business-account state, including item pricing and inventory quantity.

Mitigation: Confirm the exact action, target item or order, and JSON payload with the user before running any action marked as write or destructive.

Risk: The first-time setup path includes remote shell installation commands for the oo CLI.

Mitigation: Prefer manual verification of the installer or the official install guide before executing remote install scripts.

Risk: Connector payloads can become incorrect if action schemas change.

Mitigation: Fetch the live action schema with `oo connector schema` before constructing each payload.

## Reference(s):

- [Coupang ClawHub skill page](https://clawhub.ai/oomol/skills/oo-coupang)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Coupang homepage](https://www.coupang.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Coupang connector action names, schema-inspection commands, JSON payloads, and user-confirmation prompts for state-changing actions.]

## Skill Version(s):

1.0.0 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
