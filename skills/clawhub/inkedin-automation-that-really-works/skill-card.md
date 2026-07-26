## Description: <br>
Automates LinkedIn posting with image upload, commenting with mentions, reposting, feed reading, analytics, like monitoring, engagement tracking, and approval-based content calendar workflows through Playwright. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[red777777](https://clawhub.ai/user/red777777) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to manage a LinkedIn account's personal productivity, publishing, engagement analysis, and scheduled content workflow. Account-changing actions should be reviewed before execution because the skill can post, comment, edit, delete, and repost on a real public account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can publish, comment, repost, edit, or delete content on a real LinkedIn account. <br>
Mitigation: Require manual review and explicit approval before every account-changing action. <br>
Risk: The content calendar and webhook flow can support automatic posting through a persistent service. <br>
Mitigation: Disable or avoid cron and webhook auto-posting unless explicit operational safeguards, auditability, and stop procedures are in place. <br>
Risk: The skill uses a persistent browser profile for an authenticated LinkedIn session. <br>
Mitigation: Use a dedicated browser profile and run the service without elevated privileges. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/red777777/skills/inkedin-automation-that-really-works) <br>
- [Content Calendar Integration](references/content-calendar.md) <br>
- [LinkedIn Content Strategy](references/content-strategy.md) <br>
- [LinkedIn Engagement Guide](references/engagement.md) <br>
- [LinkedIn DOM Patterns Reference](references/dom-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python CLI commands and JSON command results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [LinkedIn CLI commands return JSON; account-changing actions should require manual approval before execution.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
