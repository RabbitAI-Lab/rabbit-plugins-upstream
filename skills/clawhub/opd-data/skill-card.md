## Description:

Queries OPD financial data APIs for A-share company profiles, securities classifications, trading data, financial statements and indicators, financing activity, corporate events, shareholders, management, and governance data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[originp-data](https://clawhub.ai/user/originp-data)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and financial analysts use this skill to retrieve subscribed OPD A-share market, listed-company, financial, financing, event, shareholder, management, and governance data through scoped API queries. It supports answering stock and listed-company data questions with explicit fields, filters, pagination, and rate-limit awareness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to an OPD API key.

Mitigation: Use the interactive --set-key flow or an environment variable, avoid pasting the key into chat, and rotate the key if it was exposed in a conversation.

Risk: Selected query parameters are sent to api.originp.com.

Mitigation: Submit only the fields and filters needed for the task and confirm that the required OPD interfaces are subscribed before use.

Risk: Some company information interfaces can return contact or registration fields when broad field selections are used.

Mitigation: Use explicit, minimal field lists instead of broad or default-heavy queries.

Risk: Optional chart generation may create local HTML and open it in a browser through a separate chart workflow.

Mitigation: Review or skip the optional chart workflow when local HTML rendering is not desired.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/originp-data/skills/opd-data)
- [OPD data platform](https://data.originp.com/)
- [OPD API endpoint](https://api.originp.com)
- [Basic information catalog](artifact/references/catalog_basic.md)
- [Trading information catalog](artifact/references/catalog_trading.md)
- [Financial information catalog](artifact/references/catalog_finance.md)
- [Financing and distribution catalog](artifact/references/catalog_financing.md)
- [Corporate events catalog](artifact/references/catalog_events.md)
- [Equity and governance catalog](artifact/references/catalog_governance.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an OPD API key; API queries use explicit fields, filters, pagination, and a documented 60 requests per minute limit.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
