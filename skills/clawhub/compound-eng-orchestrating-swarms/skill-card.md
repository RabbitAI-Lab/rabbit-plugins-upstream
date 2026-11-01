## Description:

Coordinate multi-agent swarms for parallel and pipeline workflows. Use when coordinating multiple agents, running parallel reviews, building pipeline workflows, or implementing divide-and-conquer patterns with subagents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this workflow to split independent work across agents, run parallel reviews or staged pipelines, and coordinate handoffs while tracking ownership and verifying delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Delegated work may introduce unintended changes or leave workers running after their tasks are complete.

Mitigation: Review worker diffs, confirm workers have reached terminal states, and clean up only resources the user authorized.

Risk: Optional external agents, tools, and host runtime behavior are outside the artifact's security review.

Mitigation: Check the active tool capabilities and limits before dispatch, and apply the host's controls to external agents and tools.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-orchestrating-swarms)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Task briefs, Coordination and review reports]

**Output Format:** [Markdown text with task assignments, handoffs, status updates, and review summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Coordinates parallel or staged work through the available agent tools; supported capabilities depend on the host.]

## Skill Version(s):

5.1.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
