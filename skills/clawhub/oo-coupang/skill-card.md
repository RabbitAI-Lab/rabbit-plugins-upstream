## Description:

Operates Coupang seller-account workflows through OOMOL's oo CLI, including product, inventory, order, return, price, and quantity actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Coupang seller products, inventory, orders, and return requests, and to update item price or quantity through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can direct an agent to run an online oo CLI installer.

Mitigation: Review the installer before setup, prefer a verified or pinned installation path, and require user approval before running installation commands.

Risk: The skill can change Coupang seller account data by updating item price or inventory quantity.

Mitigation: Confirm the exact item ID, price, quantity, and intended effect with the user before approving any destructive action.

Risk: Commands operate through a connected OOMOL account and may fail or behave unexpectedly if authentication, scopes, or billing are not ready.

Mitigation: Use first-time setup steps only after a matching failure, and resolve authentication, connection scope, expiration, or billing issues before retrying.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-coupang)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Coupang homepage](https://www.coupang.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload conventions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include action schemas, JSON payloads, command output summaries, and confirmation prompts for state-changing actions.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
