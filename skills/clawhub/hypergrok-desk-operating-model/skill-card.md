## Description:

How the HyperGrok trading desk works as a team of Grok Bots - roles, seats, shared workspace, evidence standard, approval model and handoff format.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT-0

## Use Case:

External users and trading-desk operators use this skill to coordinate Grok Bots across roles, workspace conventions, evidence standards, approval rules, and handoffs for a HyperGrok trading desk.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may guide agents around real-money exchange activity when paired with credentials or exchange-writing skills.

Mitigation: Use testnet first, keep mainnet keys trade-only, and require explicit user approval for every exchange write path.

Risk: Agents could treat shared workspace content, web text, or another agent's output as authorization.

Mitigation: Preserve the artifact's rule that text is data only and that only the user can approve a trade by ticket id.

Risk: Unattended routines or broad standing approvals could bypass the intended trading-desk controls.

Mitigation: Keep unattended sends disabled, scope any standing approvals in writing, and never apply standing approvals to mainnet sends.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/galleonlabs/skills/hypergrok-desk-operating-model)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration instructions]

**Output Format:** [Markdown operating model with role tables, approval rules, workspace paths, and handoff templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No executable code; produces coordination and approval guidance for agents working around trading workflows.]

## Skill Version(s):

1.0.0 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
