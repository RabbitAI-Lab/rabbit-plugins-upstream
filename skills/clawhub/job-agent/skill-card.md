## Description:

Use AgentMesh Job Agent for resume-driven job discovery, signed review, user-confirmed delivery and audit on Boss直聘, 猎聘, 智联招聘 and 51Job.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiyangnan](https://clawhub.ai/user/jiyangnan)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to operate the AgentMesh Job Agent CLI for resume-based job discovery, candidate review, user-confirmed application delivery, and audit workflows across supported recruiting platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutable remote installers and managed update behavior can change the code an agent runs after initial review.

Mitigation: Review the installer before use and prefer pinned or signed releases when available; pay attention to update messages before continuing job-site actions.

Risk: The CLI may access job-site sessions, resume data, API-key-backed cloud credits, and application delivery flows.

Mitigation: Install only after accepting that access, keep the user in control of credentials and confirmations, and review delivery previews before any send command.

Risk: Automatic retries and managed updates may continue without an extra prompt.

Mitigation: Monitor CLI output for retry and update events, preserve explicit confirmation boundaries, and stop when the CLI reports required user action.

## Reference(s):

- [AgentMesh360 Job Agent Homepage](https://jobagent.agentmesh360.com/)
- [ClawHub Skill Page](https://clawhub.ai/jiyangnan/skills/job-agent)
- [AgentMesh360 App](https://agentmesh360.com/app/)
- [AgentMesh360 Workbench](https://agentmesh360.com/workbench/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell command examples and CLI workflow steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the jobagent CLI; JOBAGENT_API_BASE is an optional testing override.]

## Skill Version(s):

0.6.14 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
