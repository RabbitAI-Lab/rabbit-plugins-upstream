## Description:

Helps agents hire human workers for physical errands or remote work, then track submissions and review proof before payment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[getterdone](https://clawhub.ai/user/getterdone)

### License/Terms of Use:

MIT-0

## Use Case:

Agent users and developers can arrange paid human assistance for tasks requiring physical presence or remote creative work, then monitor progress and evaluate submitted proof.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Posting or approving a task can incur charges or release payment.

Mitigation: Confirm the task scope and full cost before posting, retain confirmation for paid decisions, and set low per-task and daily spending caps.

Risk: An exposed agent credential could enable unauthorized task activity.

Mitigation: Use the hosted connector or a secret store rather than pasting the API key into chat; revoke access when no longer needed.

Risk: Task details and attachments may disclose sensitive information to workers.

Mitigation: Review shared details and redact unnecessary personal information before posting or attaching files.

Risk: Automated proof checks may not establish that the requested work was completed.

Mitigation: Review the submitted proof against the task requirements before approving payment; use autonomous review only when explicitly authorized.

## Reference(s):

- [GetterDone skill on ClawHub](https://clawhub.ai/getterdone/skills/getterdone)
- [GetterDone API documentation](https://getterdone.ai/docs/api)
- [GetterDone hosted MCP connector](https://getterdone.ai/mcp)

## Skill Output:

**Output Type(s):** [Guidance, Configuration instructions, Shell commands, API calls]

**Output Format:** [Markdown with configuration and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes task status updates and proof-review guidance.]

## Skill Version(s):

1.39.2 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
