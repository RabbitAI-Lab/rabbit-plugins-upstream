## Description:

Use AgentMesh Job Agent for resume-driven job discovery, signed review, user-confirmed delivery and audit on Boss直聘, 猎聘, 智联招聘 and 51Job.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiyangnan](https://clawhub.ai/user/jiyangnan)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to drive the Job Agent CLI for resume-based job discovery, review, user-confirmed delivery, and audit across supported recruiting platforms. It emphasizes user control for credentials, login, target-role and target-city selection, delivery previews, confirmations, and paid credit-consuming steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The install examples use remote shell scripts that are not pinned to a specific release artifact.

Mitigation: Use a pinned, verifiable installer or otherwise verify the release source before installing.

Risk: The CLI can access resumes, authenticated recruiting-site sessions, local browser state, and paid cloud credits.

Mitigation: Install only from a trusted publisher, prefer an isolated browser profile, and review every delivery preview and credit-consuming step before confirming.

Risk: Automated delivery workflows can submit applications or greetings on behalf of the user after confirmation.

Mitigation: Require user confirmation for final delivery lists and follow the skill's preview, authorization, and audit steps before treating a platform as complete.

## Reference(s):

- [AgentMesh Job Agent homepage](https://jobagent.agentmesh360.com/)
- [ClawHub skill page](https://clawhub.ai/jiyangnan/skills/job-agent)
- [Public Codex skill instructions](https://github.com/jiyangnan/AgentMesh-JobAgent/blob/main/skills/codex-job-agent/SKILL.md)
- [AgentMesh360 app](https://agentmesh360.com/app/)
- [AgentMesh360 workbench](https://agentmesh360.com/workbench/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with inline shell commands and structured CLI result guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs often include next-step commands, review summaries, delivery confirmation prompts, audit details, and credit or account status notes.]

## Skill Version(s):

0.6.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
