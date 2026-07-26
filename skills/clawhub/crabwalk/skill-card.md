## Description: <br>
Real-time companion monitor for OpenClaw agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luccast](https://clawhub.ai/user/luccast) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use Crabwalk to install and run a real-time monitor for OpenClaw agents, share the monitor with a human reviewer, and collect feedback on the monitoring experience. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The monitor may expose agent activity, workspace files, and OpenClaw gateway-backed access to anyone who can reach the server. <br>
Mitigation: Bind to localhost unless LAN viewing is truly needed, share access only with intended reviewers, and treat the monitor URL as sensitive. <br>
Risk: The installation guidance downloads a release and can attempt an automatic sudo-based dependency installation. <br>
Mitigation: Review or pin the downloaded release before installing, and avoid the automatic sudo QR-code dependency step unless the user explicitly approves it. <br>


## Reference(s): <br>
- [Crabwalk on ClawHub](https://clawhub.ai/luccast/skills/crabwalk) <br>
- [Crabwalk homepage](https://crabwalk.app) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes installation, verification, server startup, update, and feedback-submission guidance for the agent to present or execute with user approval.] <br>

## Skill Version(s): <br>
0.1.2 (source: ClawHub release metadata; artifact frontmatter lists 1.0.10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
