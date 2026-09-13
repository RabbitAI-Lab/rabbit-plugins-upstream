## Description:

Researches products, prices, availability, and search suggestions on Amazon (amazon.com) using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and external users use this skill to search Amazon products, inspect ASIN-level price and availability data, and gather Amazon keyword suggestions through the Crawlora API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Amazon queries, ASINs, and the Crawlora API key are sent to Crawlora.

Mitigation: Use non-sensitive Amazon research inputs, keep the key in CRAWLORA_API_KEY, and avoid passing secrets or private conversation content to the helper.

Risk: The security summary reports that the helper can send arbitrary POST bodies to Crawlora even though the documented Amazon operations are GET-only.

Mitigation: Prefer the documented GET examples and review any POST/body use before execution until POST/body support is removed or tightly validated.

## Reference(s):

- [Amazon Endpoint Reference](reference/endpoints.md)
- [Crawlora API Base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY and returns normalized Amazon data scoped to amazon.com.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
