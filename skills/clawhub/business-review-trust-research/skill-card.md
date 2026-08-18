## Description:

Researches software and SaaS product launches, business reputation, revenue-verified startups, and software reviews through Crawlora API endpoints, returning clean JSON for buying or partnership research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and business teams use this skill for vendor due diligence, Product Hunt launch research, Trustpilot reputation checks, TrustMRR revenue research, and Capterra review or alternatives research before buying or partnering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A real Crawlora API key could be sent with arbitrary requests outside the stated review and reputation research scope because the helper accepts arbitrary paths and methods and allows CRAWLORA_API_BASE overrides.

Mitigation: Use only the documented Product Hunt, Trustpilot, TrustMRR, and Capterra endpoints; do not set CRAWLORA_API_BASE unless you control the endpoint; review commands before execution.

Risk: Public review, listing, launch, and revenue data can be incomplete, stale, or misleading for business decisions.

Mitigation: Use the JSON results as due-diligence inputs, validate important conclusions against primary sources, and avoid submitting sensitive business data.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/business-review-trust-research)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; responses are based on public product, launch, reputation, revenue, and review data available through Crawlora.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
