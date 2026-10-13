## Description:

Helps agents find and analyze construction and municipal tender notices, awards, companies, project opportunities, and procurement trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams, bidders, and market analysts use this skill to search Chinese construction and municipal tenders, track project stages, examine company bidding history, and compare buyers, suppliers, and award prices. User-specified industries and regions take precedence over its default construction focus.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-use registration can send a hashed device identifier and create an account.

Mitigation: Review before installing, especially on shared machines; provide your own ZLBX_API_KEY securely to avoid auto-registration and device collection.

Risk: Registration can save an API credential on the local machine.

Mitigation: Review local credential storage before enabling registration; prefer a securely supplied environment variable when local storage is undesirable.

Risk: Ambiguous company expansions or mismatched amount filters can mislead bidding decisions.

Mitigation: Confirm company identities, amount units, filters, and underlying notices before relying on results.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bailianai/skills/tender-construction)
- [Publisher profile](https://clawhub.ai/user/bailianai)
- [Tender data service](https://ai.zhiliaobiaoxun.com/?ch=s155)
- [Tender search reference](artifact/references/api-search.md)
- [Company data reference](artifact/references/api-company.md)
- [Market analysis reference](artifact/references/api-market.md)
- [Account and registration reference](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Markdown answers with linked tender results and summary tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the actual search scope and identifies missing result fields; data queries require an API key and may consume account credits.]

## Skill Version(s):

1.0.3 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
