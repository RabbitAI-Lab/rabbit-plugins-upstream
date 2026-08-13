## Description:

Use AgentMesh Job Agent for resume-driven job discovery, signed review, user-confirmed delivery and audit on Boss直聘, 猎聘, 智联招聘 and 51Job.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiyangnan](https://clawhub.ai/user/jiyangnan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and job-seeking users use this skill to guide the Job Agent CLI through resume analysis, job discovery, signed review, user-approved delivery and audit workflows across supported job platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Job Agent API key and persistent browser sessions for job platforms.

Mitigation: Install and run it only when the user is comfortable granting those credentials and sessions to the Job Agent workflow.

Risk: Cloud resume analysis, discovery and retry behavior can affect credit usage.

Mitigation: Check CLI-reported costs, balance status, billing status and previews before continuing paid or consequential steps.

Risk: Final delivery confirmations may send real applications, resumes or greetings from the user's accounts.

Mitigation: Require the CLI's structured preview and authorization IDs before send commands, and stop whenever user action or confirmation is required.

Risk: Managed updates and transient cloud recovery can resume commands after failures.

Mitigation: Follow only the signed CLI next-suggested recovery command and preserve existing profiles, sessions, audits and account-bound state.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jiyangnan/skills/job-agent)
- [AgentMesh Job Agent Homepage](https://jobagent.agentmesh360.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and user-facing status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user confirmation before delivery actions that submit applications or greetings.]

## Skill Version(s):

0.5.9 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
