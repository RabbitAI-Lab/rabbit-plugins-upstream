## Description:

BidHunter monitors procurement notices, compares them with user-defined qualification rules, generates bid-fit reports, and supports document review, strategy guidance, compliance scanning, and notifications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[419597334-sudo](https://clawhub.ai/user/419597334-sudo)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement, bid, and sales operations teams use this skill to monitor tender opportunities, assess fit against internal qualification rules, prepare review reports, and run pre-submission compliance checks. Developers and operators can configure local sources, notification channels, optional AI document reading, and local API/webhook integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI document review can send tender text and qualification rules to MiniMax when optional AI features are enabled.

Mitigation: Enable AI features only when the user is authorized to send that data to MiniMax, and use approved API credentials for that account.

Risk: Webhook, push, email, and API integrations can expose bid reports or credentials if pointed at untrusted endpoints.

Mitigation: Use HTTPS trusted hosts, dedicated low-privilege API and email credentials, and disable auto-push when previewing or testing sensitive reports.

Risk: Generated HTML reports may be unsafe when they include untrusted source data.

Mitigation: Avoid opening generated HTML reports from untrusted data until escaping is fixed; prefer text or JSON review outputs for untrusted inputs.

## Reference(s):

- [Field Standard](artifact/references/field_standard.md)
- [Filter Rules](artifact/references/filter_rules.md)
- [Supported Platforms](artifact/references/platforms.md)
- [Setup Guide](artifact/references/setup-guide.md)
- [FAQ](artifact/scripts/docs/FAQ.md)
- [ClawHub Release Page](https://clawhub.ai/419597334-sudo/skills/bidhunter)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON, HTML reports, shell commands, and local configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include tender-fit summaries, qualification verdicts, calendars, compliance findings, notification payloads, and configuration guidance.]

## Skill Version(s):

2.5.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
