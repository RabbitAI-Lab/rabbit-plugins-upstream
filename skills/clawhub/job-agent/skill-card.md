## Description:

Use AgentMesh Job Agent for resume-driven job discovery, signed review, user-confirmed delivery and audit on Boss直聘, 猎聘, 智联招聘 and 51Job.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiyangnan](https://clawhub.ai/user/jiyangnan)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to operate AgentMesh Job Agent for resume analysis, job discovery, signed review, user-confirmed delivery, and audit across supported job platforms.

### Deployment Geography for Use:

Global, with workflows centered on supported China job platforms.

## Known Risks and Mitigations:

Risk: The workflow uses resumes, job-site logins, browser sessions, and AgentMesh360 credits.

Mitigation: Keep the API key and managed browser profile protected, review CLI status carefully, and proceed only when the returned workflow indicates readiness.

Risk: Delivery actions can submit greetings or applications to real job postings.

Mitigation: Review every delivery preview, exclude unwanted jobs through the provided confirmation flow, and send only after explicit user authorization.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jiyangnan/skills/job-agent)
- [AgentMesh Job Agent Homepage](https://jobagent.agentmesh360.com/)
- [Publisher Profile](https://clawhub.ai/user/jiyangnan)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with CLI commands and structured confirmation prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user review and confirmation before delivery actions; relays CLI prompts and audit outcomes.]

## Skill Version(s):

0.5.26 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
