## Description:

Analyzes Amazon keyword Share of Voice using Jungle Scout data, returning brand visibility across organic, sponsored, and combined results, 30-day search volume, PPC bid median, and top ASIN click/conversion metrics across 10 marketplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, brand analysts, and e-commerce operators use this skill to understand which brands occupy Amazon search results for a keyword and compare organic, sponsored, and combined visibility. It helps assess brand dominance, ad competition, PPC bid context, and top ASIN click/conversion performance for supported marketplaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles Amazon keyword queries, account identifiers, API keys, and an optional phone/SMS login flow.

Mitigation: Install only if LinkFox is trusted, keep API keys and OTPs private, and use the onboarding path only when intentionally configuring access.

Risk: The skill can guide payment orders and billing actions for LinkFox credits.

Mitigation: Confirm plan selection, payment method, and each order step before proceeding.

Risk: Saved LinkFox output and cache files may contain sensitive keyword or business data.

Mitigation: Review local output locations and delete LinkFox output or cache files when they contain sensitive data.

Risk: Repeated calls or multi-keyword comparisons can consume paid credits.

Mitigation: Use the documented one-call-per-parameter posture, rely on the 24-hour cache for repeats, and ask before additional paid queries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-junglescout-keyword-share-of-voice)
- [Jungle Scout Share of Voice API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [LinkFox skills catalog](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown or text summaries with JSON API responses and saved JSON data files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill uses one keyword per API call, supports 10 Amazon marketplaces, caches repeated parameter combinations for 24 hours, and may require LinkFox API-key configuration and paid credits.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
