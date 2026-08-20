## Description:

Researches Target's catalog, including categories, products, filters, prices, questions, and reviews, using the Crawlora API and returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to answer Target shopping research requests with normalized Crawlora API JSON for product search, category browsing, pricing, availability, Q&A, and reviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can call Crawlora paths beyond the documented Target endpoints.

Mitigation: Review proposed commands and allow only /target paths for this skill's intended use.

Risk: A custom CRAWLORA_API_BASE could send the Crawlora API key to an untrusted host.

Mitigation: Leave CRAWLORA_API_BASE unset unless the exact host is trusted.

Risk: POST mode can send arbitrary request bodies through the helper script.

Mitigation: Inspect any POST body before execution and avoid POST requests unless they are necessary and expected.

## Reference(s):

- [Target endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Target Research on ClawHub](https://clawhub.ai/tonywangcn/skills/target-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses paginated Crawlora API responses; store-specific pricing and availability depend on store_id when provided.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
