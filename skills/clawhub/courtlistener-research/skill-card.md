## Description:

Researches public US legal opinions, courts, and judicial people through CourtListener via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and legal-research users use this skill to search public CourtListener opinions, browse court records, and look up public judicial-person records as normalized JSON research leads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Legal-research queries and the Crawlora API key are sent to Crawlora's external API.

Mitigation: Use the skill only when external API processing is acceptable, and avoid submitting confidential client facts or sensitive legal strategy.

Risk: CourtListener results are research leads and may not be sufficient for legal conclusions.

Mitigation: Verify conclusions against the underlying opinion text and the applicable jurisdiction before relying on results.

## Reference(s):

- [CourtListener endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora skill page](https://clawhub.ai/crawlora-org/skills/courtlistener-research)
- [Crawlora publisher profile](https://clawhub.ai/user/crawlora-org)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON from the Crawlora API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and routes requests to documented CourtListener endpoints.]

## Skill Version(s):

1.0.9 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
