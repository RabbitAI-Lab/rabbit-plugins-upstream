## Description:

邮件雷达 MailRadar turns the last 7 days of Feishu mailbox activity into an offline HTML workboard and daily Feishu reminder cards for store-opening and task follow-up workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenzhe223-tech](https://clawhub.ai/user/chenzhe223-tech)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and operations teams use this skill to summarize recent Feishu email threads, track deadlines, generate a local dashboard, and push daily Feishu updates. It is especially tailored to DREAME/MOVA European store-opening and related Spain/Portugal business follow-up workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill accesses Feishu mailbox content through lark-cli and generates email-derived local files.

Mitigation: Run a local preview with --no-push first, keep generated JSON and HTML files in a controlled workspace, and delete them when they are no longer needed.

Risk: Generated summaries and HTML attachments can be sent to the configured Feishu open_id.

Mitigation: Verify the configured open_id and review preview output before enabling pushes.

Risk: install.py can create a recurring full-access WorkBuddy automation.

Mitigation: Avoid install.py unless recurring automation is intended, or run it with --no-automation and configure schedules manually.

## Reference(s):

- [Deployment and sharing guide](references/deploy.md)
- [Chinese translation layer guide](references/cn-translate.md)
- [ClawHub skill page](https://clawhub.ai/chenzhe223-tech/skills/mailradar)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON configuration, generated local JSON data, a self-contained HTML dashboard, and Feishu message cards.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated outputs may include email-derived local plaintext JSON/HTML files and Feishu card or attachment pushes.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
