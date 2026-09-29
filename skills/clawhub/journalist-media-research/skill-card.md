## Description:

Build a relevant journalist and media shortlist for a story or PR brief using Crawlora's journalists dataset, news search, and public author pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Communications and PR professionals use this skill to find journalists whose recent reporting fits a story, verify bylines and affiliations, and prepare a sourced media shortlist. Sending pitches is a separate user-directed action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research queries, public page scrape requests, and the Crawlora API key are sent to Crawlora.

Mitigation: Use only when comfortable sharing those requests and credentials with Crawlora; keep the API key in the environment.

Risk: Media records or contact details may be outdated or mistaken for verified interest in a pitch.

Mitigation: Check current bylines, affiliations, article dates, and published contact sources before outreach; send pitches only when the user requests it.

## Reference(s):

- [Skill release on ClawHub](https://clawhub.ai/crawlora-org/skills/journalist-media-research)
- [Crawlora endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, CSV]

**Output Format:** [Sourced media shortlist as a Markdown table or CSV]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes article links and dates, public contact sources, retrieval dates, fit rationale, and verification status.]

## Skill Version(s):

1.0.11 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
