## Description:

Use AgentMesh Job Agent for resume-driven job discovery, signed review, user-confirmed delivery and audit on Boss直聘, 猎聘, 智联招聘 and 51Job.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiyangnan](https://clawhub.ai/user/jiyangnan)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to operate the AgentMesh Job Agent CLI for resume-based job discovery, review, user-confirmed application delivery, and audit across supported Chinese job platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands can execute fetched scripts during setup.

Mitigation: Install only when the publisher is trusted; inspect or pin the installer before running it.

Risk: Automatic update, retry, or next_suggested steps may spend credits or advance job-application activity.

Mitigation: Review CLI output before continuation and require explicit user confirmation for delivery or credit-sensitive actions.

Risk: The skill manages resumes, API keys, browser sessions, and local profile state.

Mitigation: Use a dedicated Job Agent key and browser profile, and stop when the CLI reports required user action or account ambiguity.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jiyangnan/skills/job-agent)
- [AgentMesh Job Agent Homepage](https://jobagent.agentmesh360.com/)
- [AgentMesh360 App](https://agentmesh360.com/app/)
- [AgentMesh360 Workbench](https://agentmesh360.com/workbench/)
- [Codex Skill Reference](https://github.com/jiyangnan/AgentMesh-JobAgent/blob/main/skills/codex-job-agent/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with CLI commands and structured user-confirmation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference Job Agent CLI workflow fields, confirmations, audit outcomes, and recovery commands.]

## Skill Version(s):

0.6.13 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
