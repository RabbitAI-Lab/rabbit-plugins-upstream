## Description:

百炼智能 · 招投标全能助手 helps agents search tender notices, assess bid decisions, discover procurement opportunities, investigate companies from a tendering perspective, and check account balance for the 知了标讯 platform.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement, sales, and bidding teams use this skill to retrieve tender and award data, evaluate whether to bid, find early-stage public-sector opportunities, and prepare company intelligence reports grounded in procurement records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses vendor-hosted procurement APIs and may process sensitive business queries, procurement reports, and contact details.

Mitigation: Treat generated reports and contact data as sensitive business information, and share them only with intended recipients.

Risk: The skill supports persistent account setup through local credential storage and an auto-registration flow that uses device characteristics.

Mitigation: Prefer a user-supplied ZLBX_API_KEY when available; use auto-registration only after informed user consent and protect the local credential file.

Risk: Some report and platform links can contain shareable sk parameters or login-bypass links.

Mitigation: Do not post exported reports or links containing sk parameters publicly, and remove or restrict such links before broader distribution.

Risk: The skill can generate local HTML reports on disk.

Mitigation: Store exported reports in an appropriate location, avoid syncing them to public folders, and delete them when no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/bailianai/skills/zlbx-ai-platform)
- [ClawHub Publisher Profile](https://clawhub.ai/user/bailianai)
- [Main Skill Definition](SKILL.md)
- [Tender Search Overview](references/tender-search/overview.md)
- [Tender Search API Reference](references/tender-search/api-search.md)
- [Tender Account API Reference](references/tender-search/api-account.md)
- [Bid Decision Overview](references/bid-decision/overview.md)
- [Opportunity Radar Overview](references/opportunity-radar/overview.md)
- [Company Intelligence Overview](references/company-intel/overview.md)
- [Auto-Registration Flow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, API-backed analysis, shell commands for optional HTML report rendering, and local configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can generate local HTML reports for bid decisions, opportunity radar results, and company intelligence when the relevant report script is used.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
