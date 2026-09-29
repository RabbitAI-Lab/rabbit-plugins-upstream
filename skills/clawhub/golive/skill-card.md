## Description:

Helps developers deploy agent-written apps to their own cloud accounts, with human approval of provider changes and explicit verification results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mikehasa](https://clawhub.ai/user/mikehasa)

### License/Terms of Use:

MIT

## Use Case:

Developers use GoLive to plan and carry out app deployments on accounts they control, connect hosting and supporting services, and review what was verified or requires a manual handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud access may affect the user's own accounts and production resources.

Mitigation: Use scoped, expiring provider tokens where possible and review each plan before approving changes.

Risk: Production, DNS, live-payment, or deletion actions may be difficult to reverse.

Mitigation: Approve the relevant confirmation flags only after checking the named destination and intended changes.

## Reference(s):

- [GoLive on ClawHub](https://clawhub.ai/mikehasa/skills/golive)
- [Planning and verification reference](references/plan-and-verify.md)
- [Guided provider setup](references/guided.md)
- [Updates and rollback](references/updates.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with commands, deployment plans, and verification summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports checked outcomes and identifies unverified manual handoffs.]

## Skill Version(s):

0.1.0-alpha.7 (ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
