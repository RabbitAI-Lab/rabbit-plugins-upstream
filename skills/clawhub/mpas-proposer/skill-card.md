## Description:

MPAS Proposer guides an agent to propose governed MCP write operations through an MPAS bridge and wait for separate multi-party approval before execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oma3](https://clawhub.ai/user/oma3)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to make an agent propose protected MCP write operations, notify a separate maintainer, and wait for multi-party approval before execution. It is for proposer-role agents, not maintainer or approver agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A proposer agent could be configured with the wrong bridge, maintainer identity, or notification channel.

Mitigation: Install this only on proposer agents and verify the MPAS bridge, maintainer identity, and approved notification channel before use.

Risk: Repeating a governed application tool call to check progress can create a new Action instead of observing the original proposal.

Mitigation: Track the original Task ID and use the same bridge's task observation flow to inspect status.

Risk: Cancellation may not reverse an operation that has already been dispatched upstream.

Mitigation: Treat cancellation as cooperative and verify the target system when execution timing is uncertain.

## Reference(s):

- [MPAS project source](https://github.com/oma3dao/mpas)
- [ClawHub skill page](https://clawhub.ai/oma3/skills/mpas-proposer)

## Skill Output:

**Output Type(s):** [guidance, markdown, configuration, text]

**Output Format:** [Markdown guidance with MCP task and maintainer-notification text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces proposal context, Action IDs, maintainer notifications, and status reports; does not approve actions.]

## Skill Version(s):

1.0.2 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
