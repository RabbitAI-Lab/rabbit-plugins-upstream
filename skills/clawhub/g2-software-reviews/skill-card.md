## Description:

Search G2, the B2B software review site, read a full product profile with pricing and features, and pull faceted reviews with exact per-star counts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent builders use this skill to search G2 software listings, retrieve product profiles, and analyze faceted customer reviews for SaaS research, competitive intelligence, and voice-of-customer workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Calls go to Scavio's external API and consume credits, with each G2 request costing 5 credits.

Mitigation: State the expected credit cost before making calls and confirm larger or multi-page review pulls before spending credits.

Risk: The Scavio API key could be exposed if copied into source files or shared logs.

Mitigation: Load SCAVIO_API_KEY from the environment or a secret store and keep it out of source control.

Risk: Filtered review calls can return zero results because a filter matched nothing, not because a product segment has no opinion.

Mitigation: Re-check filtered zero-result findings against an unfiltered review call before reporting them as conclusions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/scavio-ai/skills/g2-software-reviews)
- [Scavio G2 documentation](https://scavio.dev/docs/g2-search)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration, API calls, JSON]

**Output Format:** [Markdown guidance with shell commands, Python and JavaScript examples, and JSON API response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY. G2 endpoints use Scavio credits, with each request costing 5 credits.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
