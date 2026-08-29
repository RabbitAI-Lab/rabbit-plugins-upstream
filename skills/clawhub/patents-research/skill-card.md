## Description:

Researches patents and patent applications via the Crawlora API across Google Patents and USPTO Patent Public Search, returning normalized JSON for prior-art, claims, citations, family, portfolio, and freedom-to-operate workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, patent researchers, and legal operations teams use this skill to search public patent data, inspect patent details, compare Google Patents and USPTO Patent Public Search results, and gather structured JSON for prior-art, portfolio, landscape, and freedom-to-operate research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can call Crawlora routes beyond the patent endpoints described by the skill.

Mitigation: Use only the documented Google Patents and USPTO Patent Public Search endpoints unless separately reviewed.

Risk: Patent queries may include confidential invention details that would be sent to Crawlora.

Mitigation: Avoid submitting confidential invention details unless the user is comfortable sharing them with Crawlora.

Risk: Changing CRAWLORA_API_BASE can send the API key and request data to another endpoint.

Mitigation: Leave CRAWLORA_API_BASE unset unless the alternate endpoint is intentional and trusted.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/patents-research)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses public patent data returned by Crawlora endpoints; requires CRAWLORA_API_KEY.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
