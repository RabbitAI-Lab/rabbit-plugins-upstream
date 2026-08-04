## Description: <br>
Agent Canary plants decoy credentials in an OpenClaw workspace and alerts when canary tokens are read, copied, modified, or exfiltrated. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thomaszhou22](https://clawhub.ai/user/thomaszhou22) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and security-minded OpenClaw users use this skill to deploy fake credential files, monitor them for access or tampering, and receive alerts that may indicate malicious skill behavior. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill intentionally plants credential-shaped decoy files in workspace and home-directory paths. <br>
Mitigation: Install only when decoy secret files are intended, verify target paths before deployment, and add the generated canary files to ignore rules as needed. <br>
Risk: The skill sets up recurring monitoring that may continue after the initial deployment. <br>
Mitigation: Confirm that the monitoring cron job can be removed, and run cleanup to remove canary files and remaining incident logs when monitoring is no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thomaszhou22/skills/agent-canary) <br>
- [Publisher profile](https://clawhub.ai/user/thomaszhou22) <br>
- [OpenClaw documentation](https://docs.openclaw.ai) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown status messages with shell command execution and alert details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local canary files, a manifest, an incident log, and recurring monitoring instructions.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
