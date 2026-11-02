## Description:

Compare user-supplied candidate locations for a local business using nearby competitors, public access signals, review samples, and available city-level context. Use for an early screen, not a lease or viability recommendation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Small-business owners, prospective operators, and advisors use the skill to compare a fixed shortlist of candidate sites using competition, access, review, and public-context evidence before deciding what warrants deeper diligence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Precise locations and search details may be shared with Crawlora and its data providers.

Mitigation: Share only details the user is comfortable disclosing; use neighborhood-level queries for confidential plans.

Risk: External lookups can consume API credits.

Mitigation: Use a dedicated API key and monitor credit usage.

Risk: Map, review, route, and city-level signals are preliminary and do not establish demand, lease terms, or property suitability.

Mitigation: Treat the comparison as an early screen and verify property, traffic, demographic, cost, licensing, and zoning details with appropriate official or property-specific sources before making a lease decision.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/crawlora-org/skills/business-location-screening)
- [Endpoint reference](artifact/reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown evidence matrix with source notes and caveats]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Candidate-by-candidate comparison; no single score unless the user supplies criteria and weights.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
