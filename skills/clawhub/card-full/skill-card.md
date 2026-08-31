## Description:

Return a compact full report for one major-US credit card - fees, welcome offer, earning rates, redemption, credits, travel benefits, protections, mechanics, eligibility, and strategy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiahongc](https://clawhub.ai/user/jiahongc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to research major US credit cards and produce compact full-card reports covering costs, offers, rewards, benefits, protections, eligibility, strategy, and comparable cards. It is intended for research support and directs users to verify important offer terms directly with issuers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credit-card offers and issuer terms can change quickly, and third-party finance pages may be stale or inconsistent.

Mitigation: Verify important offer terms directly with the issuer before applying, and use confidence notes to flag unresolved or conflicting welcome-offer claims.

Risk: The skill may use web search or an optional Brave API key and may consult third-party finance sites during research.

Mitigation: Treat outputs as research rather than financial advice, and avoid supplying sensitive personal or account information while researching cards.

## Reference(s):

- [Chase Sapphire Preferred 2026 Refresh / Offer Extraction Note](references/chase-sapphire-preferred-2026-refresh.md)
- [Delta Reserve Offer Staleness - Anchoring Failure](references/delta-reserve-2026-offer-staleness.md)
- [ClawHub Skill Page](https://clawhub.ai/jiahongc/skills/card-full)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Compact Markdown report with sourced links and confidence notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses current web research and may include issuer pages, approved secondary finance sources, offer conflict notes, and historical offer context when available.]

## Skill Version(s):

1.0.12 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
