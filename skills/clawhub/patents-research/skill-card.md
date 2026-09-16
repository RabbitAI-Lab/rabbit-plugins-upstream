## Description:

Researches patents and patent applications through the Crawlora API across Google Patents and USPTO Patent Public Search, returning normalized JSON for searches, patent details, classifications, citations, families, and recent publications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, patent researchers, and legal or product teams use this skill to run public patent prior-art, portfolio, classification, citation, family, and freedom-to-operate research through Crawlora-backed Google Patents and USPTO Patent Public Search endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent search terms, patent identifiers, and API-key-authenticated requests are sent to Crawlora.

Mitigation: Avoid confidential invention details or sensitive business strategy unless Crawlora is approved for that data.

Risk: Incorrect or incomplete public patent results could mislead prior-art, portfolio, or freedom-to-operate research.

Mitigation: Cross-check important findings across Google Patents and USPTO Patent Public Search results and have qualified reviewers assess consequential conclusions.

Risk: Crawlora API credentials could be exposed if copied into commands, source files, or logs.

Mitigation: Keep the key in CRAWLORA_API_KEY and do not hardcode, commit, or pass it as a query parameter.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/patents-research)
- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and raw JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; sends user-directed patent queries and patent identifiers to Crawlora's API.]

## Skill Version(s):

1.0.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
