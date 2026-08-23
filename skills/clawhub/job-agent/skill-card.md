## Description:

Use AgentMesh Job Agent for resume-driven job discovery, signed review, user-confirmed delivery and audit on Boss直聘, 猎聘, 智联招聘 and 51Job.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiyangnan](https://clawhub.ai/user/jiyangnan)

### License/Terms of Use:

MIT-0

## Use Case:

External users and job seekers use this skill to operate the AgentMesh Job Agent CLI for resume analysis, job discovery, signed candidate review, user-confirmed delivery, and audit across supported job platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide paid or cloud workflow steps that consume disclosed credits.

Mitigation: Confirm account balance, credit requirements, and final delivery actions before proceeding with cloud analysis, discovery, or send commands.

Risk: The skill operates through job-site login sessions and local profile or account state.

Mitigation: Use it only on a trusted machine and avoid sharing the managed browser profile or local Job Agent state.

Risk: The skill accepts managed client update recovery during workflow execution.

Mitigation: Review installer and update sources before use and preserve strict confirmation boundaries for final job delivery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jiyangnan/skills/job-agent)
- [AgentMesh Job Agent homepage](https://jobagent.agentmesh360.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and CLI response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the jobagent CLI and may guide user-confirmed cloud workflow steps.]

## Skill Version(s):

0.5.39 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
