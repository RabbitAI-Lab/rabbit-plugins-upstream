## Description:

Helps users search and analyze bid notices, procurement opportunities, company records, and market trends, defaulting searches to Guangdong unless the user specifies another region.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement and business-development teams use this skill to find tender and award notices, evaluate suppliers and competitors, and review company and market data. Guangdong is the default search region, not an access restriction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bid searches and account-linked information are sent to Zhiliaobiaoxun.

Mitigation: Use only if that sharing is acceptable; avoid submitting sensitive search terms or account details unnecessarily.

Risk: If no API key is configured, onboarding may collect device characteristics, create an external account, and save a returned API key locally.

Mitigation: Configure your own ZLBX_API_KEY to avoid automatic registration, or review the consent prompt before allowing it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/bailianai/skills/tender-guangdong)
- [Zhiliaobiaoxun service](https://ai.zhiliaobiaoxun.com/?ch=s150)
- [Search API reference](references/api-search.md)
- [Company API reference](references/api-company.md)
- [Market API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Automatic registration reference](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the search scope and presents relevant bid, company, and market findings.]

## Skill Version(s):

1.0.5 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
