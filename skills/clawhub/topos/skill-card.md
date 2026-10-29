## Description:

Evaluate and improve code with Topos. Use for complexity reduction, security checks, refactor verification, and PLATINUM/GOLD goals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[krv-labs](https://clawhub.ai/user/krv-labs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI coding agents use Topos to evaluate structural code quality, reduce complexity, review structural security concerns, and verify refactors. It guides iterative improvements toward GOLD or PLATINUM while recommending tests and human review for behavioral correctness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installation instructions run a remote installer.

Mitigation: Review the installer before running it, and configure only the agent integrations you want.

Risk: Structural scores do not establish behavioral correctness or full security assurance.

Mitigation: Review proposed changes and run project tests; use dedicated security tooling when assurance requirements call for it.

## Reference(s):

- [Topos documentation](https://docs.krv.ai/topos/)
- [Topos agent contract](https://docs.krv.ai/topos/agents.html)
- [ClawHub listing](https://clawhub.ai/krv-labs/skills/topos)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands]

**Output Format:** [CLI tables and ranked file lists; structured MCP payloads and per-function inspection details]

**Output Parameters:** [Medal verdict, pillar scores, ranked refactor targets, and assessment status]

**Other Properties Related to Output:** [May create local dependency-graph files; source edits are agent-directed.]

## Skill Version(s):

1.0.25 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
