## Description:

Defines roles, shared workspace practices, evidence standards, approvals, and handoffs for a HyperGrok trading desk of Grok Bots.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT

## Use Case:

Trading desk operators and their agents use this skill to assign work, document evidence, coordinate handoffs, and enforce approvals before exchange actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unverified approval gate could leave exchange-write routes open to unauthorized sends.

Mitigation: Verify native user-approval enforcement across SDK, script, and direct HTTP writes; remain research-only without an API wallet key until coverage is confirmed.

Risk: Mainnet trading can result in real-money losses.

Mitigation: Move to mainnet only by the user's decision, use a trade-only API wallet, and require risk sign-off and explicit ticket approval for each send.

## Reference(s):

- [HyperGrok Desk Operating Model on ClawHub](https://clawhub.ai/galleonlabs/skills/hypergrok-desk-operating-model)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration instructions]

**Output Format:** [Markdown reports, trade tickets, and handoff messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cites sources and UTC timestamps for material trading facts; names the next owner for handoffs.]

## Skill Version(s):

1.6.1 (source: ClawHub release metadata; embedded skill frontmatter says 1.1.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
