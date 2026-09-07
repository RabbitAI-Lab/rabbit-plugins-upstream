## Description:

Researches patents and patent applications through the Crawlora API across Google Patents and USPTO Patent Public Search, returning normalized JSON for prior-art, portfolio, claims, citations, family, classification, and freedom-to-operate research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, patent researchers, and technical teams use this skill to search public patent sources, inspect claims and citations, compare Google Patents and USPTO results, and gather patent landscape or freedom-to-operate evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shell helper can send the Crawlora API key and request data through a broad Crawlora API surface, including endpoints outside the patent workflow.

Mitigation: Review the endpoint path before running helper commands, keep CRAWLORA_API_BASE unset unless the destination is trusted, and use a limited or disposable Crawlora key where possible.

Risk: Patent searches may include confidential invention details that are sent to Crawlora or to a configured API endpoint.

Mitigation: Avoid submitting confidential invention details unless Crawlora and any configured endpoint are approved for that data.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; search endpoints may require pagination for full coverage.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
