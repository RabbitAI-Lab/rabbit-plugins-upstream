## Description:

Use AgentMesh Job Agent for resume-driven job discovery, signed review, user-confirmed delivery and audit on Boss直聘, 猎聘, 智联招聘 and 51Job.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiyangnan](https://clawhub.ai/user/jiyangnan)

### License/Terms of Use:

MIT-0

## Use Case:

Job seekers and their agents use this skill to find and review resume-matched jobs on four Chinese recruiting platforms, confirm applications before sending, and audit delivery outcomes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI and cloud service receive resume data and access to job-site sessions and application workflows.

Mitigation: Grant access only if comfortable with those permissions; review the full preview and confirm each platform's application list before sending.

Risk: Remote installers and managed updates may run code on the user's machine.

Mitigation: Review or pin and verify the installer before running it; pause if an unexpected resume or update is requested.

Risk: Resume analysis and job discovery can consume paid account credits.

Mitigation: Check the current account balance and credit quote before authorizing paid steps.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/jiyangnan/skills/job-agent)
- [AgentMesh Job Agent homepage](https://jobagent.agentmesh360.com/)
- [AgentMesh360 workbench](https://agentmesh360.com/workbench/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown with CLI commands, review previews and audit summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Application delivery requires a separate user confirmation for each platform.]

## Skill Version(s):

0.6.20 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
