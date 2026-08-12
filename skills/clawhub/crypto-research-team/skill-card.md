## Description:

Tracks on-chain activity, market data, and project fundamentals to produce dated crypto research briefs using a coordinated team of specialized agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[t3ratech](https://clawhub.ai/user/t3ratech)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts, developers, and research teams use this bundle to coordinate crypto market, on-chain, project-fundamental, and risk research into dated briefs. The artifact also defines roles with memory, scheduling, file, event, and trading-rail integration capabilities that should be reviewed before deployment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundle includes an unrelated business-scouting role alongside crypto research roles.

Mitigation: Confirm that the business-researcher role is intentional, or remove or disable it before installation.

Risk: The risk-officer role references trading-rail, kill-switch, flatten-event, and MCP invocation authority that is under-scoped in the artifact.

Mitigation: Restrict trading integrations and require explicit human approval before any MCP trading, kill-switch, or flatten-event action.

Risk: Roles can use scheduling, memory retention, and file-write capabilities.

Mitigation: Run in a controlled workspace with reviewed schedules, bounded memory retention, and explicit approval for file writes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/t3ratech/skills/crypto-research-team)
- [Publisher profile](https://clawhub.ai/user/t3ratech)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown research briefs and agent guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dated crypto research synthesis, role coordination guidance, and configuration-oriented instructions.]

## Skill Version(s):

0.1.1 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
