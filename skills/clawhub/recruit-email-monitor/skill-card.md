## Description:

Recruit Email Monitor checks configured mailboxes for recruiting messages, lets an agent classify them, records results to a spreadsheet, sends Feishu notifications, and generates daily briefings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haoxianniu528-bit](https://clawhub.ai/user/haoxianniu528-bit)

### License/Terms of Use:

MIT-0

## Use Case:

Job seekers or recruiting workflow users use this skill to monitor configured QQ/163-style mailboxes for recruiting-related messages, have an agent classify deadlines and categories, and keep an Excel tracking sheet plus daily Feishu briefings current.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill needs POP3 access to configured mailboxes and processes sensitive recruiting-message content.

Mitigation: Use mailbox authorization codes rather than account passwords, keep scripts/config.json local and private, and install only for mailboxes whose contents may be processed by the agent workflow.

Risk: Recruiting-message details may be sent to the configured Feishu target.

Mitigation: Verify feishu_target and cron announce delivery before importing or enabling the scheduled jobs.

Risk: The skill automatically updates the recruiting spreadsheet and archives pending items older than 30 days.

Mitigation: Verify excel_path and the 30-day auto-archive behavior against the user's workflow, and keep a recoverable copy of the spreadsheet.

Risk: Artifact installation guidance contains obsolete references to email-heartbeat-check.py.

Mitigation: Follow the current SKILL.md flow using fetch-emails.py, agent judgment into pending_judged.json, record-emails.py, and email-daily-briefing.py.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/haoxianniu528-bit/skills/recruit-email-monitor)
- [Skill Instructions](artifact/SKILL.md)
- [README](artifact/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Agent-facing guidance with shell commands, JSON decision files, spreadsheet updates, Feishu notification text, and daily briefing text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates pending_candidates.json and pending_judged.json, updates an Excel workbook, writes a daily briefing text file, and can deliver announcements through configured cron delivery.]

## Skill Version(s):

1.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
