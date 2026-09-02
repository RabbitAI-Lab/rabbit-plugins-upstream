## Description:

Search G2, the B2B software review site, read a full product profile with pricing and features, and pull faceted reviews with exact per-star counts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, agents, and research teams use this skill to search G2 software listings, retrieve product profiles, and analyze structured review data for competitive intelligence, vendor comparison, pricing research, and voice-of-customer work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a user-provided SCAVIO_API_KEY for a paid API.

Mitigation: Store the key in the environment or a secret store, avoid hardcoding it, and install the skill only when Scavio access is intended.

Risk: G2 requests cost 5 credits each, and multi-page review pulls can consume credits quickly.

Mitigation: Plan requests before running them, state the intended credit cost up front, and avoid broad loops over products or review pages.

Risk: Filtered review queries can produce ambiguous zero-result responses.

Mitigation: Re-check unfiltered review data before presenting zero filtered results as a product or segment finding.

Risk: Product profile responses do not include review text.

Mitigation: Use the reviews endpoint when the user asks for customer sentiment or review content.

## Reference(s):

- [Scavio G2 Search Documentation](https://scavio.dev/docs/g2-search)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/g2-software-reviews-api)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Markdown, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with JSON API responses and inline shell, Python, or JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SCAVIO_API_KEY and Scavio G2 endpoints; search, product, and review requests each cost 5 credits.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
