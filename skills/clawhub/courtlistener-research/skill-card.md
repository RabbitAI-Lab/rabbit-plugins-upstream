## Description:

Researches public US legal opinions, courts, and judicial people through CourtListener via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search public CourtListener opinions, browse courts, and look up public judicial-person records as an initial legal-research shortlist.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CourtListener search queries and the Crawlora API key are sent to Crawlora when the helper is used.

Mitigation: Install only when that data flow is acceptable, keep the API key scoped to intended use, and avoid exposing it in shared logs or transcripts.

Risk: Legal-research results may be incomplete or misleading if treated as legal conclusions.

Mitigation: Use returned results as research leads and verify conclusions against primary sources and the applicable jurisdiction.

## Reference(s):

- [courtlistener-research endpoint reference](artifact/reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/courtlistener-research)
- [Crawlora API key setup](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the CRAWLORA_API_KEY environment variable and returns CourtListener research results as leads to verify against primary sources.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
