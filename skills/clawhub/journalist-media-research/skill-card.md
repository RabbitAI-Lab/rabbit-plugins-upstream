## Description:

Builds a sourced journalist and media shortlist for a story or PR brief using Crawlora's journalist records, news search, and public author pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

PR and communications teams use this skill to find reporters whose recent work fits a story, verify their coverage, and assemble a sourced media shortlist with public work contact channels. Sending pitches is a separate action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media-research queries, story angles, journalist names, and public page URLs are sent to Crawlora's API.

Mitigation: Avoid embargoed or sensitive PR strategy in queries unless you intend to share it with Crawlora.

Risk: Public contact records or inferred editorial fit may be outdated or misleading.

Mitigation: Check current bylines, affiliations, article dates, and published contact sources before outreach; mark unverified matches clearly.

## Reference(s):

- [Journalist media research endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Markdown, CSV]

**Output Format:** [Markdown table or CSV]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes profile and article sources, publication dates, fit rationale, public contact sources, and verification status.]

## Skill Version(s):

1.0.12 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
