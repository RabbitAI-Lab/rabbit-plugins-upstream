## Description:

Procurement and public-sector bidding assistant for bid notice search, bid/no-bid decision support, opportunity discovery, company intelligence, and account balance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business development teams use this skill to search Chinese tender and award notices, assess whether to bid on specific opportunities, find early procurement opportunities, and produce procurement-focused company intelligence reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist an API key in ~/.zlbx/config.json after registration.

Mitigation: Prefer providing ZLBX_API_KEY directly when possible, restrict local file access, and remove ~/.zlbx/config.json when automatic authentication is no longer desired.

Risk: The opt-in auto-registration flow sends a hashed device identifier to the zhiliaobiaoxun service.

Mitigation: Use the documented consent gate before registration, or skip auto-registration by preconfiguring ZLBX_API_KEY or manually obtaining a key.

Risk: Generated HTML reports and platform URLs may contain signed login-bypass links.

Mitigation: Treat exported reports and links as sensitive, avoid broad forwarding, and regenerate expired links only for the intended user.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bailianai/skills/zlbx-ai-platform)
- [Auto-registration flow](references/auto-register.md)
- [Tender search overview](references/tender-search/overview.md)
- [Tender search API reference](references/tender-search/api-search.md)
- [Tender market API reference](references/tender-search/api-market.md)
- [Tender company API reference](references/tender-search/api-company.md)
- [Account API reference](references/tender-search/api-account.md)
- [Bid decision overview](references/bid-decision/overview.md)
- [Bid decision workflow](references/bid-decision/workflow.md)
- [Bid decision report template](references/bid-decision/report-template.md)
- [Opportunity radar overview](references/opportunity-radar/overview.md)
- [Opportunity radar workflow](references/opportunity-radar/workflow.md)
- [Opportunity radar report template](references/opportunity-radar/report-template.md)
- [Company intelligence overview](references/company-intel/overview.md)
- [Company intelligence workflow](references/company-intel/workflow.md)
- [Company intelligence report template](references/company-intel/report-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses, API call guidance, and optional HTML report files generated from structured JSON inputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call zhiliaobiaoxun APIs using ZLBX_API_KEY, may store an API key in ~/.zlbx/config.json after opt-in registration, and may create shareable HTML reports.]

## Skill Version(s):

1.1.1 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
