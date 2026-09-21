## Description:

Build a relevant journalist and media shortlist for a story or PR brief using Crawlora's journalists dataset, news search, and public author pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Communications, PR, and research teams use this skill to identify reporters whose recent public coverage fits a story angle, then produce an evidence-backed media shortlist with affiliation, article, contact-source, and verification status fields.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Journalist search terms, public page URLs, and scrape requests are sent to Crawlora under the user's Crawlora API key.

Mitigation: Use only when this data sharing is acceptable under the user's policy, keep the API key in the environment, and avoid sensitive unpublished campaign details in search terms.

Risk: Dataset records, beat labels, affiliations, article dates, and public contact channels can be incomplete or stale.

Mitigation: Verify current affiliation and recent bylined work on source pages, mark bio-only matches as unverified, and keep unknown dates or contacts explicit.

Risk: A published email or social contact does not imply that the person wants a pitch.

Mitigation: Review generated contact details before outreach, do not invent addresses from outlet patterns, and send pitches only after the user explicitly requests that action.

## Reference(s):

- [Crawlora publisher profile](https://clawhub.ai/user/crawlora-org)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/journalist-media-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown table or CSV, with optional shell commands and JSON evidence from Crawlora API calls.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The intended media list includes name, outlet, title, beat, profile URL, relevant article URLs, article dates, fit reason, public contact, contact source URL, retrieval time, and verification status.]

## Skill Version(s):

1.0.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
