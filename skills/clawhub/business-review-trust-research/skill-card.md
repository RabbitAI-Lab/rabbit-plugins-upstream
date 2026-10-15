## Description:

Researches software products, business reputation, startup revenue, and crowdfunding campaigns through Crawlora's public-data API and returns structured results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Business researchers, buyers, and developers use this skill to compare software reviews, check business reputation, examine startup revenue profiles, and assess crowdfunding campaigns before decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Business names, URLs, locations, and campaign terms sent for lookup are shared with Crawlora.

Mitigation: Use only for targets your organization permits sharing; avoid confidential vendor lists and sensitive due-diligence targets without approval.

Risk: The skill requires a Crawlora API key.

Mitigation: Keep the key in CRAWLORA_API_KEY; do not place it in prompts, query parameters, or committed files.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/business-review-trust-research)
- [Crawlora endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON API results with optional plain-language summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public listing and review results may be paginated.]

## Skill Version(s):

1.0.20 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
