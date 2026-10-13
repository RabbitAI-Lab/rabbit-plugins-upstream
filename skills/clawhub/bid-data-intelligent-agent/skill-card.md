## Description:

Helps agents search and analyze Chinese procurement notices, company bidding activity, suppliers, and market trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and analysts use this skill to find procurement opportunities, review tender and award notices, profile companies and competitors, and summarize purchasing trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Procurement and company-analysis queries are sent to an external service.

Mitigation: Avoid submitting confidential information without authorization and review the service's data handling before use.

Risk: Optional account registration collects device attributes and stores an API key locally.

Mitigation: Prefer your own ZLBX_API_KEY; obtain informed consent before registration, review the device fields, and protect ~/.zlbx/config.json.

Risk: Contact information and auto-login links may expose personal or account access data.

Mitigation: Respect masked contact data, avoid bulk contact exports, and share auto-login links only with intended recipients.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhiliaobiaoxun/skills/bid-data-intelligent-agent)
- [Publisher skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Search API reference](artifact/references/api-search.md)
- [Company API reference](artifact/references/api-company.md)
- [Business registry API reference](artifact/references/api-registry.md)
- [Market API reference](artifact/references/api-market.md)
- [Account API reference](artifact/references/api-account.md)
- [Optional account registration](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Natural-language summaries and structured Markdown reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include notice links, company details, market statistics, and contact data subject to account-level masking.]

## Skill Version(s):

1.0.7 (source: skill frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
