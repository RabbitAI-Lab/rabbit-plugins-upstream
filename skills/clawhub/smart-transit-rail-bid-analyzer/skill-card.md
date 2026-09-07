## Description:

Analyzes smart-transit and rail-procurement opportunities by querying Zhiliaobiaoxun bid, company, market, and account data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement, sales, market-analysis, and business-development users use this skill to search transportation infrastructure bid notices, analyze buyers and suppliers, review company procurement activity, find potential bidders, and summarize market or price trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Procurement queries and related account requests are sent to Zhiliaobiaoxun services.

Mitigation: Use the skill only for queries appropriate to that third-party service and avoid sending confidential procurement strategy or unnecessary sensitive context.

Risk: Auto-registration may send a device-derived MAC hash and persist an API key locally.

Mitigation: Prefer a user-configured ZLBX_API_KEY when device tracking is a concern, and require explicit user consent before auto-registration.

Risk: Contact lookup can return project contact details, with masking dependent on account status.

Mitigation: Show contact data as returned, do not attempt to unmask or enrich masked phone numbers, and avoid bulk contact export.

Risk: The skill includes account, recharge, and vendor referral flows.

Mitigation: Keep recharge and referral links clearly attributable to the publisher and avoid presenting them as NVIDIA-owned services.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/smart-transit-rail-bid-analyzer)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [Bid search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Auto-registration flow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, API Calls, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with tables, JSON request examples, REST API call guidance, and concise configuration instructions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a ZLBX_API_KEY or user-approved auto-registration before data calls; contact details may be masked for free or trial accounts.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
