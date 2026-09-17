## Description:

Coordinate multi-step detached tasks as one durable TaskFlow job with owner context, state, waits, and child tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use TaskFlow to coordinate durable, multi-step background jobs that need persistent state, child task linkage, wait and resume handling, and a single owner return context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Example workflows show automated messaging and repository-changing actions based on untrusted LLM classifications.

Mitigation: Add strict output schemas, destination allowlists, least-privilege tokens, audit logs, and human approval before sending messages, closing PRs, requesting changes, or modifying branches.

Risk: The included Gmail and pull-request examples could affect real accounts or repositories if copied directly into production workflows.

Mitigation: Review and adapt the examples before use, replace placeholders with controlled tools, and test against non-production accounts or repositories first.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/azizbrownint/skills/taskflow)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with TypeScript and Lobster examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes orchestration patterns for managed task flows, revision-safe mutations, child task linkage, waits, resumes, cancellation, and example automation lanes.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
