## Description:

Coordinates multi-agent work across parallel reviews, pipelines, and divide-and-conquer tasks while keeping ownership and verification explicit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to coordinate agents for parallel implementation, independent reviews, and staged workflows with clear ownership, handoffs, and completion checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent delegation or task updates may expose sensitive project context to additional workers.

Mitigation: Review worker prompts and task scope before dispatching agents on sensitive projects.

Risk: Shutdown or cleanup decisions may affect active shared work.

Mitigation: Confirm ownership and authorization before closing workers or cleaning up shared resources.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-orchestrating-swarms)
- [Dispatch contract](artifact/references/dispatch-contract.md)
- [Worker lifecycle](artifact/references/worker-lifecycle.md)
- [Claude Code subagent documentation](https://code.claude.com/docs/en/sub-agents)

## Skill Output:

**Output Type(s):** [Guidance, Task assignments, Review summaries]

**Output Format:** [Markdown text with structured handoffs and status updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Worker actions depend on available agent tools and user authorization.]

## Skill Version(s):

5.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
