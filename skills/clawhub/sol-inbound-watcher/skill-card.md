## Description:

Watch a Solana address for new inbound SOL/USDC transfers and alert via webhook or stdout.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kateryna-sprintcx](https://clawhub.ai/user/kateryna-sprintcx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to monitor a Solana receiving address and emit payment events after inbound SOL payments meet a configured minimum.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release claims USDC or SPL-token payment support, but the included script does not implement token-transfer detection.

Mitigation: Use the skill only for native SOL inbound balance increases unless token-transfer detection is implemented or the documentation is narrowed.

Risk: Webhook endpoints receive payment event details.

Mitigation: Configure webhooks only to endpoints the operator trusts to receive transaction signatures, addresses, amounts, and timing details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kateryna-sprintcx/skills/sol-inbound-watcher)
- [Solana mainnet RPC endpoint](https://api.mainnet-beta.solana.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payment events]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The runtime script emits JSON lines to stdout and can POST payment event details to a configured webhook.]

## Skill Version(s):

0.1.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
