## Description:

BidHunter helps agents collect public Chinese tender notices, compare them against local qualification rules, generate bid-readiness reports, manage reminders and filters, and optionally use MiniMax-powered document reading, risk review, and bid-strategy guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[419597334-sudo](https://clawhub.ai/user/419597334-sudo)

### License/Terms of Use:

MIT-0

## Use Case:

Business development, bidding, and operations teams use this skill to monitor tender opportunities, score qualification fit, prepare concise reports, track deadlines, and review tender documents before human bid decisions. Developers and operators can also configure local data sources, push channels, and a local query API.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Optional AI commands can send tender documents, and in some cases local qualification rules, to the MiniMax API configured by the user.

Mitigation: Use AI commands only for documents approved for that provider, keep the MiniMax configuration private, and leave AI unconfigured when third-party processing is not permitted.

Risk: Push, webhook, and SMTP settings may contain sensitive secrets or destination endpoints.

Mitigation: Store push configuration privately, avoid publishing configuration files, and use no-push or local report generation when testing.

Risk: Document parsing dependencies process untrusted PDFs and Word files.

Mitigation: Pin or update parsing dependencies before processing untrusted files and review extracted content before acting on bid recommendations.

## Reference(s):

- [BidHunter setup guide](artifact/references/setup-guide.md)
- [Supported platforms and custom data sources](artifact/references/platforms.md)
- [Filter rules and qualification logic](artifact/references/filter_rules.md)
- [Tender field standard](artifact/references/field_standard.md)
- [BidHunter FAQ](artifact/scripts/docs/FAQ.md)
- [MiniMax API provider](https://www.minimaxi.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and terminal-oriented text with shell commands, JSON configuration examples, text reports, HTML reports, and JSONL cache files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional AI features can send tender text and local qualification rules to the configured MiniMax API; push features can send reports to user-configured DingTalk, WeCom, email, or webhook endpoints.]

## Skill Version(s):

1.5.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
