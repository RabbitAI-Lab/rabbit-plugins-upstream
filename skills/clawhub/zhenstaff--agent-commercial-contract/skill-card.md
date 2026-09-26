## Description:

Agent Commercial Contract helps AI agents negotiate, sign, execute, and manage commercial agreements with digital identity, escrow, milestones, audit trails, and dispute workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhenstaff](https://clawhub.ai/user/zhenstaff)

### License/Terms of Use:

MIT-0

## Use Case:

Developers building agent marketplaces, API networks, data exchanges, or multi-agent services use this skill to add contract lifecycle, signature, escrow, milestone payment, and dispute workflows between autonomous agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Autonomous signing, escrow deposits, payment release, refunds, or dispute rulings could create financial or legal exposure without adequate oversight.

Mitigation: Require explicit human approval for contract signatures, fund movements, refunds, and dispute rulings, and test all flows in a sandbox or staging environment before production use.

Risk: Mutable npm or Git-based installation paths may be difficult to verify before deployment.

Mitigation: Pin and verify the npm package or Git commit, and disable install scripts during inspection when possible.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhenstaff/skills/agent-commercial-contract)
- [npm Package](https://www.npmjs.com/package/agent-commercial-contract)
- [Project GitHub Link Listed in Artifact](https://github.com/ZhenRobotics/agent-commercial-contract)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with TypeScript and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API and CLI workflows for contract, identity, escrow, and dispute operations.]

## Skill Version(s):

1.0.0 (source: server release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
