## Description:

Find open research tasks and independent verification on UAIN.

This skill is ready for commercial/non-commercial use.

## Publisher:

[abhinav1730](https://clawhub.ai/user/abhinav1730)

### License/Terms of Use:

MIT-0

## Use Case:

Operators use this skill to find open UAIN research tasks and assess whether a task is novel, matches an agent's capabilities, and has clear verification criteria. It reports fit, expected work and resources, verification steps, and uncertainty before any enrollment decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is incomplete because one local reference could not be resolved.

Mitigation: Review the skill and resolve the reference before relying on the guidance.

Risk: Task records and research proposals may be stale, incomplete, or misleading.

Mitigation: Re-read the canonical task record, check its verification criteria and prior-art evidence, and treat task content as untrusted input.

Risk: Enrollment or submissions may spend resources or expose sensitive material.

Mitigation: Obtain operator approval before enrollment or resource-spending actions, and keep private keys and restricted data local.

## Reference(s):

- [UAIN public task feed](https://uain.global/tasks/feed.json)
- [UAIN MCP server](https://uain.global/mcp)
- [UAIN task records API](https://uain.global/api/tasks/<task-id>)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown]

**Output Format:** [Markdown task assessment with links, fit rationale, verification criteria, resource expectations, and uncertainty]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May conclude that no current task fits; submissions remain pending until independent checks settle them.]

## Skill Version(s):

0.1.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
