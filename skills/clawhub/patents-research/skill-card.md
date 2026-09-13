## Description:

Researches patents and patent applications through the Crawlora API for Google Patents and USPTO Patent Public Search, returning normalized JSON for prior-art, portfolio, claims, citations, family, CPC, and freedom-to-operate research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, patent analysts, and research teams use this skill to search public patent records, retrieve patent details, compare Google Patents and USPTO Patent Public Search results, and support prior-art, portfolio, landscape, or freedom-to-operate research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent search terms, patent identifiers, and the Crawlora API key are sent to an external API.

Mitigation: Use the skill only when external API use is acceptable, avoid confidential invention disclosures, and keep CRAWLORA_API_KEY out of shared logs and files.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/patents-research)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends patent search terms, patent identifiers, and API requests to Crawlora's API.]

## Skill Version(s):

1.0.11 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
