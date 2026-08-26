## Description:

Researches software/SaaS products, business reputation, and crowdfunding campaigns via the Crawlora API, returning clean JSON for Product Hunt, Trustpilot, TrustMRR, Capterra, BBB, and Kickstarter research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and business users use this skill to gather public product launch history, customer review signals, verified startup revenue details, software alternatives, BBB reputation data, and Kickstarter campaign status before buying, partnering, investing, or backing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public business, product, campaign, or target URL queries are sent to Crawlora.

Mitigation: Use the skill only for public targets and avoid submitting internal, confidential, or sensitive lookup terms.

Risk: The Crawlora API key could be exposed if it is hardcoded, committed, or placed in URLs.

Mitigation: Keep the key in CRAWLORA_API_KEY, do not commit it, and do not pass it as a query parameter.

Risk: A custom CRAWLORA_API_BASE could route requests somewhere other than the official Crawlora API.

Mitigation: Leave CRAWLORA_API_BASE unset or confirm that it points to the official Crawlora API before use.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends public lookup terms or target URLs to the Crawlora API.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
