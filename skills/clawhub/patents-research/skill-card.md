## Description:

Researches patents and patent applications through the Crawlora API across Google Patents and USPTO Patent Public Search, returning normalized JSON for searches, document details, claims, citations, families, classifications, recent publications, and coverage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, patent researchers, and legal or product teams use this skill to run prior-art, portfolio, claims, citations, family, classification, recent-publication, and freedom-to-operate research against public patent sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent search terms, inventor or assignee names, document identifiers, and the Crawlora API key are sent to Crawlora.

Mitigation: Use the skill only when that data sharing is acceptable, and avoid confidential invention details unless disclosure to Crawlora is approved.

Risk: Patent research results can be incomplete if only the first page is reviewed or if USPTO query syntax is used incorrectly.

Mitigation: Walk paginated results, use the documented USPTO field-code syntax, and cross-check important findings across Google Patents and USPTO Patent Public Search.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON API responses with concise Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; results are paginated and limited to public patent data.]

## Skill Version(s):

1.0.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
