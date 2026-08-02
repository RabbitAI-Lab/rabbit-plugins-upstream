## Description: <br>
Use AgentMesh Job Agent for resume-driven job discovery, signed review and automatic selected delivery on Boss直聘, 猎聘, 智联招聘 and 51Job. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiyangnan](https://clawhub.ai/user/jiyangnan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External job seekers and their agents use this skill to drive the AgentMesh360 Job Agent CLI for resume analysis, job discovery, review previews, selected application delivery, and audit reporting across supported job platforms. <br>

### Deployment Geography for Use: <br>
Global, with practical use focused on the supported Boss直聘, 猎聘, 智联招聘, and 51Job platforms. <br>

## Known Risks and Mitigations: <br>
Risk: The skill can automatically submit real job applications and messages using saved job-site sessions after preview, without a final approval step. <br>
Mitigation: Review every delivery preview item and the selected list before starting a round; use a dedicated environment or browser profile when possible. <br>
Risk: The skill depends on job-platform logins and an AgentMesh360 API key. <br>
Mitigation: Use the official initialization flow, protect saved sessions and API keys, and stop whenever the CLI reports that user action is required. <br>
Risk: Installation and updates rely on a remote GitHub repository. <br>
Mitigation: Use the expected installer and update flow, and do not disable the signature, tag, commit, archive, or hash checks described by the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jiyangnan/skills/job-agent) <br>
- [Job Agent homepage](https://jobagent.agentmesh360.com/) <br>
- [AgentMesh360 app](https://agentmesh360.com/app/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and structured CLI result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance directs the agent to surface required user actions, delivery previews, selected/review/rejected counts, audit evidence, and remaining platform status.] <br>

## Skill Version(s): <br>
0.5.5 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
