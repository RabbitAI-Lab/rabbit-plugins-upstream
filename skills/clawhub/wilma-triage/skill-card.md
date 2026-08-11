## Description:

Daily triage of Wilma school notifications for Finnish parents, including exams, messages, news, schedules, homework, lesson notes, important attachments, Google Calendar sync, and concise chat reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aikarjal](https://clawhub.ai/user/aikarjal)

### License/Terms of Use:

MIT-0

## Use Case:

External users, especially Finnish parents and their household agents, use this skill to review school notifications, surface actionable items, and keep a school-event calendar current.

### Deployment Geography for Use:

Finland

## Known Risks and Mitigations:

Risk: The skill needs access to Wilma school data for all configured students and may inspect selected school attachments.

Mitigation: Install only for agents trusted with that school data, review the configured Wilma credentials, and keep attachment handling limited to high-value school documents.

Risk: The skill can add or remove school-related Google Calendar events.

Mitigation: Review the stored calendar ID and event naming conventions, and use a dedicated school calendar when easier review or rollback is needed.

Risk: Stored triage preferences and schedules may influence which notifications are reported or skipped.

Mitigation: Review saved preferences and any daily schedule periodically, especially after feedback changes what the agent should report.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aikarjal/skills/wilma-triage)
- [ClawHub publisher profile](https://clawhub.ai/user/aikarjal)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Concise Markdown chat report with inline shell commands and configuration notes when setup or calendar sync is needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read school attachments and propose or perform Google Calendar updates when the required local credentials and calendar configuration are present.]

## Skill Version(s):

1.3.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
