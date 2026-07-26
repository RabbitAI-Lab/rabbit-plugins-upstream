## Description: <br>
Automated daily security audits for OpenClaw agents with DM delivery and optional email reporting. Runs deep audits, creates or updates a recurring cron job, and sends formatted reports to configured recipients. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[davida-ps](https://clawhub.ai/user/davida-ps) <br>

### License/Terms of Use: <br>
AGPL-3.0-or-later <br>


## Use Case: <br>
Developers, operators, and security teams use this skill to schedule recurring OpenClaw security audits, summarize findings, and deliver reports to configured DM and optional email recipients. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill creates or updates an unattended recurring OpenClaw cron job when enabled. <br>
Mitigation: Before enabling it, verify the schedule, timezone, install directory, and required runtime; remove or disable the cron job if only a one-time audit was intended. <br>
Risk: Audit reports are delivered to configured DM and optional email recipients. <br>
Mitigation: Review the DM channel, recipient, optional email address, and SMTP or sendmail settings before enabling delivery. <br>
Risk: Suppression settings can exclude reviewed findings from critical and warning totals. <br>
Mitigation: Use suppressions only with both the explicit enable flag and the audit config sentinel, and keep suppressed findings visible in report review. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/davida-ps/skills/openclaw-audit-watchdog) <br>
- [ClawSec homepage](https://clawsec.prompt.security) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands, configuration examples, and text audit reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates or updates a recurring OpenClaw cron job when setup is run; reports are delivered to the configured DM target and optional email recipient.] <br>

## Skill Version(s): <br>
0.1.6 (source: frontmatter, skill.json, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
