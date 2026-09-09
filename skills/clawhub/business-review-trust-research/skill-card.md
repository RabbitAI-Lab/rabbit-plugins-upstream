## Description:

Researches software and SaaS products, business reputation, verified startup revenue, software reviews, and crowdfunding campaigns through the Crawlora API, returning normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, procurement teams, and other external users can use this skill to research vendor trust, product launch history, review signals, BBB reputation, verified startup revenue, and Kickstarter campaign status before buying, partnering, or backing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can send the Crawlora API key to a configurable API base.

Mitigation: Keep CRAWLORA_API_BASE unset unless the destination is fully trusted, and rotate the API key if it was ever used with an untrusted API base.

Risk: The bundled helper behaves as a generic authenticated Crawlora client, broader than the stated business-review use case.

Mitigation: Review requested endpoints before execution and restrict use to the business-review, software-review, BBB, Trustpilot, TrustMRR, Product Hunt, Capterra, and Kickstarter endpoints documented for this skill.

Risk: Reputation and review data can be incomplete, stale, or misleading when used as a sole basis for decisions.

Mitigation: Use the returned public-data signals as due-diligence inputs and cross-check important buying, partnering, or backing decisions with additional sources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/business-review-trust-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns paginated public-data results from selected Crawlora endpoints.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
