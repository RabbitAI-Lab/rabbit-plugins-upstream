## Description:

Use AgentMesh Job Agent for resume-driven job discovery, signed review, user-confirmed delivery and audit on Boss直聘, 猎聘, 智联招聘 and 51Job.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiyangnan](https://clawhub.ai/user/jiyangnan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and job seekers use this skill to run the AgentMesh Job Agent CLI for resume analysis, multi-platform job discovery, reviewed application delivery, and audit reporting while preserving user confirmation points.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI can maintain browser sessions and account-bound local state.

Mitigation: Use a dedicated machine or browser profile and verify account ownership before continuing account-state recovery or switching actions.

Risk: Managed updates, recovery commands, retries, and some cloud workflow steps may continue automatically.

Mitigation: Install only when this automation is acceptable, keep signature and recovery checks enabled, and stop on failed update or account/context mismatch messages.

Risk: Resume analysis and job discovery can consume credits, and delivery actions may contact job platforms or employers.

Mitigation: Review charges, credits, selected jobs, delivery previews, and each platform's final confirmation before sending applications.

## Reference(s):

- [Skill page](https://clawhub.ai/jiyangnan/skills/job-agent)
- [AgentMesh Job Agent homepage](https://jobagent.agentmesh360.com/)
- [AgentMesh360 application portal](https://agentmesh360.com/app/)
- [macOS/Linux installer](https://raw.githubusercontent.com/jiyangnan/AgentMesh-JobAgent/main/scripts/install.sh)
- [Windows installer](https://raw.githubusercontent.com/jiyangnan/AgentMesh-JobAgent/main/scripts/install.ps1)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Markdown]

**Output Format:** [Markdown with inline shell commands and structured confirmation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the jobagent CLI and may rely on JOBAGENT_API_BASE when set.]

## Skill Version(s):

0.5.17 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
