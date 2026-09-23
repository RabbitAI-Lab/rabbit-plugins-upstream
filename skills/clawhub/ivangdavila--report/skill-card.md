## Description:

Configure custom recurring reports. User defines data sources, skill handles scheduling and formatting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:


## Use Case:

External users configure recurring or on-demand reports from user-selected data sources, formats, schedules, and delivery channels. The skill helps an agent store report definitions, collect needed inputs, generate report outputs, and deliver them through configured destinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scheduled report jobs can repeatedly access configured data sources or deliver report content after setup.

Mitigation: Review schedules and delivery channels before enabling them, and use on-demand or local file delivery for sensitive reports.

Risk: External delivery through Telegram, webhooks, or email can send report contents off-device.

Mitigation: Verify each destination and recipient before use; keep sensitive reports on the local file channel when external sharing is not intended.

Risk: API credentials may be exposed if stored directly in report configuration.

Mitigation: Provide credentials only through environment variables and store only environment variable names in report configs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/report)
- [Report configuration schema](schema.md)
- [Output formats](formats.md)
- [Delivery channels and scheduling](delivery.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, shell commands, guidance]

**Output Format:** [Markdown guidance with configuration snippets and report outputs in chat, PDF, HTML, or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report data and generated files are stored under ~/report unless the user configures external delivery.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
