## Description:

Looks up Amazon keywords associated with up to 10 ASINs via Jungle Scout data and returns search volume, ranking, competition, PPC bid, and relevance metrics across supported marketplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers, e-commerce analysts, and agents supporting external users use this skill to find competitor and target-ASIN search keywords, compare search volume, ranking, competition, and PPC bid metrics, and identify keyword opportunities.

### Deployment Geography for Use:

Global, with data access limited to the supported Amazon marketplaces: US, UK, Germany, India, Canada, France, Italy, Spain, Mexico, and Japan.

## Known Risks and Mitigations:

Risk: The scanner summary reports that the skill handles LinkFox account setup, SMS login, API key generation, billing, payment QR flows, feedback reporting, and broad local persistence.

Mitigation: Install and use it only when those LinkFox flows are intended; do not provide phone codes or start payments unless the user explicitly requests that action.

Risk: Full keyword responses are written to local linkfox session data files and may contain sensitive product, ASIN, or competitive research data.

Mitigation: Review saved linkfox data before sharing a workspace or artifacts, and remove sensitive response files when they are no longer needed.

Risk: The security guidance warns against untrusted environment overrides for LinkFox endpoints.

Mitigation: Use official LinkFox endpoints and avoid setting LinkFox API base URL environment variables from untrusted sources.

Risk: The skill consumes LinkFox credits and documented billing behavior can create payment or cost exposure.

Mitigation: Confirm credit use before additional queries, avoid repeated exploratory calls, and rely on the documented cache for repeated parameter combinations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-junglescout-keyword-by-asin)
- [Jungle Scout ASIN Keyword API Reference](references/api.md)
- [LinkFox Authentication and Billing Onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON files]

**Output Format:** [Markdown summaries and tables, JSON API responses, shell command examples, and local JSON data files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved locally under a linkfox session data directory; large responses print a compact stdout summary unless inline output is requested.]

## Skill Version(s):

1.0.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
