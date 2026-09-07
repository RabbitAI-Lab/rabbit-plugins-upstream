## Description:

Searches Chinese tender, bidding, procurement, company, and market data by keyword, location, amount, time window, industry, project stage, and related company signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users, procurement teams, sales teams, and market researchers use this skill to find tender opportunities, retrieve bid details, analyze companies, identify competitors or suppliers, and summarize procurement market activity.

### Deployment Geography for Use:

Global, with China-focused procurement data coverage.

## Known Risks and Mitigations:

Risk: Auto-registration may send a stable hashed MAC-derived device identifier to the provider.

Mitigation: Prefer manually supplying a scoped ZLBX_API_KEY; use auto-registration only after user consent.

Risk: The skill may store an API key in ~/.zlbx/config.json.

Mitigation: Check local file permissions and avoid sharing the configuration file or exposing the API key in conversation.

Risk: The skill may add promotional referral links to answers.

Mitigation: Review generated responses before sharing them externally and remove referral content when it is not appropriate.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhiliaobiaoxun/skills/smart-tender-procurement-search)
- [Publisher Profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [Search API Reference](artifact/references/api-search.md)
- [Company API Reference](artifact/references/api-company.md)
- [Market API Reference](artifact/references/api-market.md)
- [Account API Reference](artifact/references/api-account.md)
- [Auto-Registration Reference](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, configuration, guidance]

**Output Format:** [Markdown summaries with tables, links, JSON request examples, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API-derived procurement records, company profiles, market aggregations, account status, and one-time onboarding or quota guidance.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
