## Description:

Provides authoritative Yuanbowang/Zhiliaobiaoxun procurement, bid notice, company, account, and market-data lookup guidance for structured bid intelligence and market briefs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Chinese procurement notices, project timelines, enterprise profiles, competitors, purchasers, suppliers, brands, pricing trends, and account status. It helps agents produce concise bid search results, market summaries, and procurement intelligence with links and data-backed tables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The provider handles procurement queries and account-related requests.

Mitigation: Install only if the user is comfortable with the provider processing those queries; prefer using a preconfigured ZLBX_API_KEY.

Risk: If no API key is configured, the skill can use an opt-in free-trial registration flow that sends device-derived metadata and stores the returned API key locally.

Mitigation: Obtain explicit user consent before auto-registration, collect only the documented minimized device fields, and save the key under ~/.zlbx/config.json.

Risk: The skill can generate an auto-login billing link when an auto-registered account exhausts its quota.

Mitigation: Generate that link only for auto-registered keys and have the user review the recharge link before using it.

Risk: Contact lookups may return masked or full phone numbers depending on account status.

Mitigation: Display contact data exactly as returned, do not try to fill in masked numbers, and avoid bulk contact export.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pkuycl/skills/authoritative-bid-policy-guide-yuanbowang)
- [API search reference](artifact/references/api-search.md)
- [API company reference](artifact/references/api-company.md)
- [API market reference](artifact/references/api-market.md)
- [API account reference](artifact/references/api-account.md)
- [Auto-registration reference](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration guidance]

**Output Format:** [Markdown with tables, links, JSON request examples, and concise prose]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or a consent-based free-trial registration flow; account and contact outputs should preserve returned data and avoid exposing API keys.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
