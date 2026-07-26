## Description: <br>
Runs a scheduled Saturday operational self-check that gathers system, cron, skill framework, data-layer, and known-issue status, then prepares a report and can send it to Feishu. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[colbertlee](https://clawhub.ai/user/colbertlee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to run a weekly operational self-check across local system health, cron jobs, skill metrics, and data-layer status, producing a concise status report for follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The default sending path can share operational details with a hardcoded Feishu destination. <br>
Mitigation: Review and edit the workspace, Feishu account, and receive_id before installation; use --dry-run or --no-send first. <br>
Risk: Feishu credentials and report delivery may expose sensitive operational status if the app is overprivileged or the recipient is wrong. <br>
Mitigation: Use least-privilege Feishu app credentials and enable real sending only after confirming the destination and report contents are acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/colbertlee/skills/weekend-self-check) <br>
- [Publisher profile](https://clawhub.ai/user/colbertlee) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown-style operational report and Feishu post content, with optional command-line dry-run output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes dry-run, no-send, and skip-sync modes; the default path can send operational details to a configured Feishu recipient.] <br>

## Skill Version(s): <br>
1.4.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
