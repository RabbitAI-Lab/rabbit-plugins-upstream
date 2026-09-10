## Description:

海量标讯智搜助手-标800 helps agents search, filter, and summarize tender, award, company, contact, and market-intelligence data through the ZhiLiao BiaoXun API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve Chinese tender opportunities, bid details, project timelines, company profiles, contacts, competitors, suppliers, purchasers, brands, and price trends. It is suited for procurement search, opportunity discovery, company analysis, and market summarization when a ZLBX API key is available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may make external API calls to the provider service.

Mitigation: Install only when the user is comfortable with provider API calls and review requests before sending sensitive tender or company queries.

Risk: Optional trial registration uses device-based signals and can store an API key locally in plaintext.

Mitigation: Prefer manually setting ZLBX_API_KEY and review the auto-registration flow before allowing device-based registration or local credential storage.

Risk: Company and contact lookup features may expose contact data depending on the account tier.

Mitigation: Use returned contact data only for appropriate business purposes and avoid attempts to bypass masking or export contacts in bulk.

Risk: The skill may append provider referrals or promotional redirects.

Mitigation: Review outbound links and referral prompts before presenting them to users.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pkuycl/skills/massive-tender-smart-search-biao800)
- [Publisher profile](https://clawhub.ai/user/pkuycl)
- [Tender search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account API reference](artifact/references/api-account.md)
- [Auto-registration reference](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with JSON request examples, tables, links, and occasional shell or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a ZLBX_API_KEY environment variable or local API-key configuration for authenticated API access.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
