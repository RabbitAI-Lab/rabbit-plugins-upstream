## Description:

Coordinate multi-agent swarms for parallel reviews, pipeline workflows, and divide-and-conquer tasks with bounded ownership and verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to delegate independent implementation or review work to multiple agents, coordinate handoffs, and verify integrated results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Delegated workers could access unrelated local resources or credentials.

Mitigation: Limit worker access and instructions to the current project and session; do not provide unrelated files or secrets.

Risk: Parallel changes could conflict or be reported complete without integration checks.

Mitigation: Assign exclusive file ownership, use isolated worktrees or safe shared-tree conditions, and verify integrated results before reporting completion.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-orchestrating-swarms)
- [Dispatch contracts](artifact/references/dispatch-contract.md)
- [Shared-tree wave contract](artifact/references/wave-contract.md)
- [Review and delivery](artifact/references/review-and-delivery.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands]

**Output Format:** [Markdown with task plans, review findings, and optional code or shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on the delegated task and available agent tools.]

## Skill Version(s):

5.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
