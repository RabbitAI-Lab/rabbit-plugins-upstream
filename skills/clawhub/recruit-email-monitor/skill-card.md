## Description:

Monitors configured mailboxes for recruitment-related emails, has an agent classify candidates, records results to an Excel workbook, sends Feishu notifications, and generates a daily briefing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haoxianniu528-bit](https://clawhub.ai/user/haoxianniu528-bit)

### License/Terms of Use:

MIT

## Use Case:

Individuals or teams managing recruiting workflows use this skill to check QQ, 163, or similar mailboxes, classify recruiting messages, track deadlines, and receive Feishu summaries. The agent reads candidate email metadata and previews, decides whether each item is recruitment-related, and writes structured judgment results for the local scripts to record.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires mailbox authorization codes and reads private email previews.

Mitigation: Use the local scripts/config.json setup flow, keep config.json out of version control, restrict file permissions, and grant access only to intended mailboxes.

Risk: Scheduled automation stores recruitment details locally and can forward summaries through Feishu.

Mitigation: Review cron-jobs.json, Feishu target settings, Excel and briefing output paths, and message contents before enabling recurring jobs.

Risk: Setup guidance differs between files, which can lead to running obsolete scripts or hard-coded paths.

Mitigation: Prefer the current SKILL.md and README.md config.json workflow and verify script names and paths before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haoxianniu528-bit/skills/recruit-email-monitor)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples; runtime scripts produce JSON working files, Excel workbook updates, Feishu message text, and a daily briefing text file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires local mailbox configuration, Python 3, openpyxl, OpenClaw cron for scheduled runs, and a Feishu target when notifications are enabled.]

## Skill Version(s):

1.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
