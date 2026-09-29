## Description:

Use AgentMesh Job Agent for resume-driven job discovery, signed review, user-confirmed delivery and audit on Boss直聘, 猎聘, 智联招聘 and 51Job.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiyangnan](https://clawhub.ai/user/jiyangnan)

### License/Terms of Use:

MIT-0

## Use Case:

External job seekers and their agents use this skill to drive the AgentMesh Job Agent CLI for resume-based discovery, signed review, user-confirmed delivery and audit across supported job platforms. It emphasizes explicit user handoff for credentials, paid credits, browser login sessions and final delivery decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide installation of a CLI through a direct remote installer and includes automatic update or retry flows.

Mitigation: Install only if the publisher is trusted, and review or pin the installer source before running installation or update commands.

Risk: The CLI workflow may use a resume, API key, browser login sessions, job-site accounts and paid credits.

Mitigation: Configure credentials only in trusted private contexts, run environment checks before paid or browser actions, and stop when the CLI reports required user action.

Risk: Job delivery actions can affect real job-site accounts after user approval.

Mitigation: Require the CLI's preview, authorization identifiers and explicit final-list confirmation before any send command, then audit completed actions.

## Reference(s):

- [Job Agent homepage](https://jobagent.agentmesh360.com/)
- [ClawHub skill page](https://clawhub.ai/jiyangnan/skills/job-agent)
- [AgentMesh360 app](https://agentmesh360.com/app/)
- [AgentMesh360 workbench](https://agentmesh360.com/workbench/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown guidance with CLI commands and structured handoff steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the jobagent CLI; JOBAGENT_API_BASE is an optional testing override.]

## Skill Version(s):

0.6.16 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
