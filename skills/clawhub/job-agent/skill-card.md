## Description:

Use AgentMesh Job Agent for resume-driven job discovery, signed review, user-confirmed delivery and audit on Boss直聘, 猎聘, 智联招聘 and 51Job.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiyangnan](https://clawhub.ai/user/jiyangnan)

### License/Terms of Use:

MIT-0

## Use Case:

Job seekers and their agents use this skill to operate AgentMesh Job Agent for resume analysis, job discovery, reviewed delivery, and audit across supported job sites. It is designed to keep credentials, target inputs, paid actions, and final application sends under explicit user control.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI can access AgentMesh360 account state, job-site browser sessions, resume data, and paid credits.

Mitigation: Install only when that access is acceptable, keep account state bound to the intended user, and monitor credit use during each workflow.

Risk: The skill can send job applications after workflow confirmations.

Mitigation: Review each generated preview, use explicit exclude or cancel choices when needed, and authorize delivery only after the final candidate list is correct.

Risk: Managed client updates and one recovery installer path may run without a separate prompt.

Mitigation: Use the official signed update and recovery flow, preserve local state, and stop on update failures instead of disabling signature or archive checks.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jiyangnan/skills/job-agent)
- [AgentMesh360 Job Agent Homepage](https://jobagent.agentmesh360.com/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the jobagent CLI and may use JOBAGENT_API_BASE as an optional testing override.]

## Skill Version(s):

0.5.40 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
