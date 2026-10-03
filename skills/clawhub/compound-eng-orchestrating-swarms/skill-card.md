## Description:

Guides agents in coordinating parallel reviews, multi-agent implementation, and pipeline workflows with clear task ownership and verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to delegate independent tasks to agents, coordinate parallel reviews and implementation, and verify integrated results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Delegated agents may change files or coordinate tasks outside the intended scope.

Mitigation: Authorize bounded tasks and file ownership, inspect returned changes, and verify integrated work before reporting completion.

Risk: Team-state inspection during Claude team debugging may expose unrelated agent information.

Mitigation: Limit inspection to current-session team state and keep sensitive unrelated agent profiles out of scope.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-orchestrating-swarms)
- [Orchestration patterns](artifact/references/orchestration-patterns.md)
- [Dispatch contract](artifact/references/dispatch-contract.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands]

**Output Format:** [Text or Markdown, with task assignments, reviews, and implementation artifacts as applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the available agent collaboration tools and assigned verification.]

## Skill Version(s):

5.0.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
