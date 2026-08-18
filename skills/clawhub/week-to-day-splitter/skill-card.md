## Description:

Splits a tagged weekly work plan into five daily Markdown plans, supports checkbox-based progress carryover, and can provide scheduled Feishu daily-plan reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seairteng](https://clawhub.ai/user/seairteng)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and operations teams use this skill to convert one weekly project plan into weekday-specific daily plans, then carry completed checkbox items back into the next weekly plan. It is suited to recurring Monday-Friday project coordination where task tags drive scheduling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recurring cron jobs can read and modify local work-plan files without a fresh prompt each time.

Mitigation: Review the configured paths and schedules before enabling cron jobs, run the splitter in dry-run mode first, and remove scheduled jobs when they are no longer needed.

Risk: Daily plans may contain customer names, deadlines, locations, responsible people, notes, or other sensitive business information.

Mitigation: Treat Feishu reminders as external sharing, use only approved internal Feishu destinations, and avoid pushing sensitive daily-plan content.

Risk: A Feishu webhook or recipient misconfiguration could expose daily-plan content to unintended parties.

Mitigation: Store webhook values securely, rotate leaked webhooks, and verify recipients before enabling reminder automation.

Risk: Generated daily-plan files overwrite planned output files in the configured day-plan directory.

Mitigation: Confirm the output directory points to the intended workspace and keep backups or sync history enabled before running non-dry-run writes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/seairteng/skills/week-to-day-splitter)
- [SKILL.md](artifact/SKILL.md)
- [CHANGELOG.md](artifact/CHANGELOG.md)
- [README.md](artifact/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown daily-plan files, plain text command output, and setup guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces five weekday daily plans from a weekly plan; dry-run mode can preview assignments before writing files.]

## Skill Version(s):

1.1.0 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
