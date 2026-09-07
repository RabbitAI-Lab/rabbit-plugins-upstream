## Description:

BidHunter monitors tender notices, compares them with user-defined qualification rules, produces bidability judgments and reports, and optionally adds AI document reading, risk scanning, bid strategy guidance, push notifications, a local API, and signed webhooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[419597334-sudo](https://clawhub.ai/user/419597334-sudo)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement, sales, and bid operations teams use this skill to collect tender notices, evaluate fit against their own qualification rules, prioritize opportunities, prepare review reports, and receive reminders or notifications. Optional AI features can summarize tender documents, flag risk clauses, and suggest bid strategy for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender text and internal qualification rules may be sensitive, and optional AI features can send tender content to an external MiniMax API configured by the user.

Mitigation: Use AI features only with an approved API account, review the data flow before enabling them, and redact sensitive content or skip AI commands when external processing is not acceptable.

Risk: Custom source files and logged-in scraping workflows can expand network access or import untrusted endpoints.

Mitigation: Do not import untrusted sources.json files, review each configured endpoint, and use an isolated low-privilege browser profile for any logged-in scraping.

Risk: Webhook and SMTP settings can expose secrets or send reports outside the local environment.

Mitigation: Use HTTPS-only webhooks, enter SMTP and webhook secrets only in a private terminal, keep config files permission-restricted, and review destinations before enabling push delivery.

Risk: Local tools such as the rule editor and API server expose bid data and configuration through localhost services while running.

Mitigation: Run local services only when needed, keep them bound to localhost, and close the rule editor or API server when finished.

## Reference(s):

- [BidHunter ClawHub release](https://clawhub.ai/419597334-sudo/skills/bidhunter)
- [Field standard](references/field_standard.md)
- [Filter rules](references/filter_rules.md)
- [Supported platforms and custom sources](references/platforms.md)
- [Setup guide](references/setup-guide.md)
- [FAQ](scripts/docs/FAQ.md)
- [MiniMax API](https://www.minimaxi.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain-text guidance with shell commands; generated local reports may include text, HTML, JSONL, calendar output, API responses, and webhook payloads.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are advisory and require human confirmation for bid decisions; optional AI features may process tender text through the user's configured MiniMax API.]

## Skill Version(s):

2.5.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
