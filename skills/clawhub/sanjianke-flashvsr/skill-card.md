## Description:

This skill wraps the a7w flashvsr submit and query APIs so an agent can submit and monitor video super-resolution tasks with the user's own api.a7w.cn API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[2253128](https://clawhub.ai/user/2253128)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and agent operators use this skill to configure an a7w API key, inspect the flashvsr API schema, submit video super-resolution jobs, and query asynchronous task results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The client can use authenticated a7w marketplace access beyond the narrow flashvsr workflow.

Mitigation: Use only an API key that is acceptable for broader a7w marketplace access, monitor account usage, and revoke or rotate the key if exposure is suspected.

Risk: Host override options can send the API key to a domain other than the default a7w API host.

Mitigation: Keep the default api.a7w.cn host unless the alternate endpoint is trusted and expected.

Risk: Submitting or repeating jobs can consume the user's paid a7w points.

Mitigation: Review requests before execution, avoid duplicate submissions, and check account balance or task usage when troubleshooting.

## Reference(s):

- [Getting started with a7w API keys](references/getting-started.md)
- [flashvsr submit API](references/api-submit.md)
- [flashvsr query API](references/api-query.md)
- [ClawHub skill page](https://clawhub.ai/2253128/skills/sanjianke-flashvsr)
- [a7w compute marketplace](https://api.a7w.cn/)
- [a7w AI plugin marketplace](https://aigc.a7w.cn/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API calls, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided a7w API key; asynchronous calls may poll until the task reaches a terminal state.]

## Skill Version(s):

1.0.5 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
