## Description:

Enables agents to query and analyze Chinese tender, bidding, award, company, supplier, market, price, and account data through the ZhiLiao BiaoXun APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and business analysts use this skill to search bid notices, retrieve tender details, analyze companies and competitors, identify potential suppliers, aggregate market activity, and generate structured procurement intelligence.

### Deployment Geography for Use:

Global; data coverage and account flows are focused on the ZhiLiao BiaoXun Chinese tender-data platform.

## Known Risks and Mitigations:

Risk: Tender queries and analysis requests are sent to the vendor's external APIs.

Mitigation: Use the skill only for data you are comfortable sharing with the vendor service, and avoid submitting confidential procurement strategy or sensitive internal identifiers unless approved.

Risk: The auto-registration flow can send a persistent MAC-derived hash and store an API key in plaintext under ~/.zlbx/config.json.

Mitigation: Prefer manually setting ZLBX_API_KEY; if auto-registration is used, require user consent first and protect the local config file as a credential store.

Risk: Login and recharge URLs produced by the account flow may act like temporary credentials.

Mitigation: Treat generated account links as sensitive, share them only with the intended user, and regenerate them rather than reusing expired links.

Risk: Broad routing and promotional redirects may lead agents to use vendor account or marketing flows during normal analysis.

Mitigation: Limit account setup and recharge flows to explicit authentication, quota, or billing needs; keep ordinary tender analysis focused on the documented data APIs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/bid-data-intelligent-agent)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [Bid search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Auto-registration flow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured text with JSON API payloads, REST request examples, and occasional shell commands for account setup.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a ZLBX_API_KEY or an approved auto-registration flow before calling vendor APIs.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
