## Description:

Build a non-custodial, unsigned Base token swap using the public Jarvis best-execution router when the buyer wants an opt-in live comparison between the existing 0x and OKX routes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yl124915300-dot](https://clawhub.ai/user/yl124915300-dot)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to build exact-input Base token swap routes through Jarvis while keeping wallet signing, broadcast, custody, and gas payment outside the skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wallet address and intended swap details are sent to the Jarvis routing service for quotes.

Mitigation: Use the skill only when the buyer is comfortable sharing those quote details with Jarvis.

Risk: Unsigned transaction data can still encode an unexpected recipient, token amount, fee, or slippage.

Mitigation: Review the returned transaction in the wallet before approval and rely on the host wallet for signing and broadcast.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yl124915300-dot/skills/jarvis-smart-route)
- [Jarvis Router homepage](https://jarvis-orderflow-router.yl124915300.workers.dev/)
- [Jarvis route endpoint](https://jarvis-orderflow-router.yl124915300.workers.dev/v1/route)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON route result with unsigned transaction data or a no-route decision, plus Markdown usage guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are unsigned, non-custodial, Base-only route proposals requiring independent wallet review and approval.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
