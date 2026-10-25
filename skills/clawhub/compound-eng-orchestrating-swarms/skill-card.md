## Description:

Coordinate multi-agent swarms for parallel reviews, pipeline workflows, and divide-and-conquer tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to divide work among agents, coordinate parallel implementation and reviews, and verify integrated results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Background agents may act beyond the intended scope if assignments or permissions are too broad.

Mitigation: Give workers bounded tasks and file ownership, review their permissions, and verify their results before integration.

Risk: Team debugging may expose sensitive session details in local agent metadata.

Mitigation: Avoid team-debugging snippets around sensitive sessions unless needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-orchestrating-swarms)
- [Dispatch contract](references/dispatch-contract.md)
- [Orchestration patterns](references/orchestration-patterns.md)
- [Worker lifecycle](references/worker-lifecycle.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown with task assignments and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent availability and permissions depend on the host environment.]

## Skill Version(s):

5.1.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
