## Description:

Use AgentMesh Job Agent for resume-driven job discovery, signed review, user-confirmed delivery and audit on Boss直聘, 猎聘, 智联招聘 and 51Job.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiyangnan](https://clawhub.ai/user/jiyangnan)

### License/Terms of Use:

MIT-0

## Use Case:

Job seekers use this skill to search four recruiting platforms using their resume, review shortlisted jobs and personalized greetings, confirm any application delivery, and audit outcomes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An external installer runs code on the user's machine.

Mitigation: Review the installer or download and inspect a local copy before running it.

Risk: The CLI handles resume data, an API key and job-board browser sessions.

Mitigation: Install only if comfortable granting that access; keep credentials private and use the intended browser profile.

Risk: Searches may consume credits and application delivery contacts employers.

Mitigation: Review costs and the complete job preview; explicitly confirm each final delivery list.

## Reference(s):

- [Job Agent ClawHub release](https://clawhub.ai/jiyangnan/skills/job-agent)
- [AgentMesh360 Job Agent homepage](https://jobagent.agentmesh360.com/)
- [Job Agent CLI repository and installation guidance](https://github.com/jiyangnan/AgentMesh-JobAgent)
- [Codex Job Agent instructions](https://github.com/jiyangnan/AgentMesh-JobAgent/blob/main/skills/codex-job-agent/SKILL.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown with CLI commands, review cards and audit summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Shows full delivery previews and requires user confirmation before application delivery.]

## Skill Version(s):

0.6.18 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
