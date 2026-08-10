## Description:

Fetches recent HKEXnews Daily Targeted Leverage Factor announcements for HKEX-listed Leveraged & Inverse products, extracts factor data from announcement PDFs, and returns a Telegram-ready digest grouped by applicable date with source links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[joeyiptk](https://clawhub.ai/user/joeyiptk)

### License/Terms of Use:

MIT-0

## Use Case:

External operators or developers use this skill to monitor HKEX L&I factor announcements and produce a ready-to-post Telegram digest for manual or scheduled OpenClaw runs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional scheduled job runs with exec access on weekdays.

Mitigation: Install the OpenClaw cron schedule only after user confirmation, and review the 18:30 Asia/Hong_Kong timing before enabling it.

Risk: Local configuration and scratch storage may not match an operator's storage controls.

Mitigation: Review the resolved config path and tmp_dir before use, and override them with HKEX_LI_MONITOR_HOME or config settings when tighter local storage control is needed.

Risk: HKEX PDF download or factor extraction can fail because the workflow depends on live HKEX availability and readable announcement PDFs.

Mitigation: Use the readiness checks, fail loudly on discovery, download, parse, or pattern-extraction errors, and avoid emitting partial or empty digests.

Risk: HKEX PDFs are copyrighted and should not be retained beyond the run.

Mitigation: Download PDFs only to the configured scratch directory and delete PDFs, extracted text, and discovery scratch files after parsing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/joeyiptk/skills/hkex-li-daily-factor-monitor)
- [HKEXnews](https://www1.hkexnews.hk)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Plain text Telegram digest with a Markdown-style monospace code block and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Downloads HKEX PDFs per run, extracts text, and deletes scratch files after parsing; normal digest output is designed to stay within Telegram message limits.]

## Skill Version(s):

1.0.0 (source: frontmatter, changelog, release evidence, version.txt)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
