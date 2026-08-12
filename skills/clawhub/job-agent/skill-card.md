## Description:

Use AgentMesh Job Agent for resume-driven job discovery, signed review and automatic selected delivery on Boss直聘, 猎聘, 智联招聘 and 51Job.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiyangnan](https://clawhub.ai/user/jiyangnan)

### License/Terms of Use:

MIT-0

## Use Case:

Job seekers and agents acting on their behalf use this skill to run the AgentMesh Job Agent CLI for resume analysis, multi-platform job discovery, selected application delivery, and audit reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to spend AgentMesh360 credits during resume analysis and job discovery.

Mitigation: Review credit requirements and CLI-reported balances before starting cloud commands, and stop when the CLI reports insufficient credits or required user action.

Risk: The skill can guide an agent to submit selected job applications after showing previews.

Mitigation: Inspect each delivery preview before platform action and rely on the CLI's signed selected list, review files, preview IDs, and audit output.

Risk: The skill uses job-site sessions, browser profile state, resume data, and a Job Agent API key.

Mitigation: Install only when comfortable granting that access, keep credentials under user control, and preserve account-bound state instead of manually editing profile files.

Risk: Managed client updates or recovery steps may continue without a separate approval prompt.

Mitigation: Monitor update and recovery messages, stop on update failure, and use only the official CLI-provided next command.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jiyangnan/skills/job-agent)
- [AgentMesh360 Job Agent Homepage](https://jobagent.agentmesh360.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and concise CLI status reporting]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides the agent to show delivery previews, relay required user prompts, and follow signed CLI workflow recommendations.]

## Skill Version(s):

0.5.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
