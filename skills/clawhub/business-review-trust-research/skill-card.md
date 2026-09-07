## Description:

Researches software and SaaS products, business reputation, verified startup revenue, and crowdfunding campaigns through the Crawlora API, returning normalized JSON from Product Hunt, Trustpilot, TrustMRR, Capterra, BBB, and Kickstarter sources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, buyers, and business analysts use this skill for vendor due diligence, product launch research, software review comparison, startup revenue checks, business reputation checks, and Kickstarter campaign assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can expose the Crawlora API key if CRAWLORA_API_BASE is set to an untrusted host.

Mitigation: Use the default Crawlora API base or a trusted, validated host, and do not run the helper with an untrusted CRAWLORA_API_BASE value.

Risk: Lookup terms are sent to Crawlora when the skill calls the API.

Mitigation: Avoid submitting sensitive or confidential search terms unless sharing them with Crawlora is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/business-review-trust-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns paginated public business, review, launch, revenue, and campaign data.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
