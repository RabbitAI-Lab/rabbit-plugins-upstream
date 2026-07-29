## Description: <br>
Use AgentMesh Job Agent for resume-driven job discovery, signed review and automatic selected delivery on Boss直聘, 猎聘, 智联招聘 and 51Job. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiyangnan](https://clawhub.ai/user/jiyangnan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Job seekers and career-support agents use this skill to run AgentMesh Job Agent for resume analysis, job discovery, review of selected postings, and delivery across supported Chinese recruiting platforms. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can submit selected job applications after preview without a separate per-platform confirmation. <br>
Mitigation: Review every delivery preview before continuing, monitor attempted and delivered counts in audits, and stop when the CLI requests user action. <br>
Risk: Cloud resume analysis and platform discovery can consume AgentMesh360 credits. <br>
Mitigation: Check account balance and paid-pass status with the CLI before starting a round, and review credit usage in completion reports. <br>
Risk: Saved browser sessions, login state, API keys, and account-bound local state may be reused. <br>
Mitigation: Use a dedicated browser profile or account boundary, confirm account ownership when prompted, and preserve account-state files instead of editing them manually. <br>
Risk: Installation and recovery flows fetch remote installer scripts and perform managed updates. <br>
Mitigation: Install only when the remote installer and update trust model are acceptable, and do not bypass signature, tag, commit, archive, or hash checks. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jiyangnan/skills/job-agent) <br>
- [AgentMesh Job Agent homepage](https://jobagent.agentmesh360.com/) <br>
- [AgentMesh360 app](https://agentmesh360.com/app/) <br>
- [macOS/Linux installer](https://raw.githubusercontent.com/jiyangnan/AgentMesh-JobAgent/main/scripts/install.sh) <br>
- [Windows PowerShell installer](https://raw.githubusercontent.com/jiyangnan/AgentMesh-JobAgent/main/scripts/install.ps1) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and compact status tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill relays structured CLI prompts, previews, audit summaries, and next-step commands.] <br>

## Skill Version(s): <br>
0.5.4 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
