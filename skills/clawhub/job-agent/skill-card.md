## Description:

Use AgentMesh Job Agent for resume-driven job discovery, signed review, user-confirmed delivery and audit on Boss直聘, 猎聘, 智联招聘 and 51Job.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiyangnan](https://clawhub.ai/user/jiyangnan)

### License/Terms of Use:

MIT-0

## Use Case:

Job seekers and their assisting agents use this skill to operate the AgentMesh Job Agent CLI for resume analysis, job discovery, signed review, delivery confirmation, and audit across supported job platforms while keeping the user in control of credentials and final sends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI can preserve and use browser sessions, API keys, resumes, cloud credits, and job-platform state.

Mitigation: Use a dedicated account or profile where possible, inspect commands before execution, and keep explicit user approval in the loop for purchases, updates, retries, recovery commands, and application delivery.

Risk: Automatic update, retry, and workflow-continuation behavior can advance the job workflow after a command completes.

Mitigation: Follow only signed CLI next-step guidance, stop on user-action prompts, and review status, preview, and audit output before continuing.

Risk: Application delivery actions can affect external job-platform accounts.

Mitigation: Require the displayed delivery preview and authorization identifiers before any send command, and preserve the audit trail for attempted, delivered, failed, and skipped jobs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jiyangnan/skills/job-agent)
- [AgentMesh Job Agent homepage](https://jobagent.agentmesh360.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and structured confirmation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes CLI command sequences, status interpretation, user-action prompts, and audit-report guidance.]

## Skill Version(s):

0.5.25 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
