## Description:

MPAS Proposer helps an agent propose protected MCP tool calls through MPAS multi-party approval workflows without holding protected credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oma3](https://clawhub.ai/user/oma3)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to have proposer-role agents route protected MCP operations through an MPAS bridge, monitor the resulting task, and coordinate approval without self-approving or handling protected credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Protected action details are shared for approval.

Mitigation: Configure the MPAS bridge and maintainer channels before use, and share the Action ID, operation, resources, arguments, and reason only through approved channels.

Risk: Repeating a governed application tool call can create a new Action instead of checking progress.

Mitigation: Record the Task ID and bridge, then observe the existing Task with tasks/get rather than resubmitting the tool call.

Risk: Cancelling a Task may not reverse an operation already dispatched upstream.

Mitigation: Treat cancellation as cooperative and verify the target system when execution timing is uncertain.

## Reference(s):

- [MPAS project repository](https://github.com/oma3dao/mpas)
- [ClawHub skill page](https://clawhub.ai/oma3/skills/mpas-proposer)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [Plain text status updates and maintainer notifications]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Action ID, application, operation, target resources, arguments, reason, authorization state, and task outcome.]

## Skill Version(s):

1.0.0 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
