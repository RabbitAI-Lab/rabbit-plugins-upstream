## Description:

Builds an evidence-backed journalist shortlist for a story or PR brief using Crawlora's journalist dataset, news search, and public author pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

PR and communications teams use the skill to find reporters whose published coverage matches a story, verify recent bylines, and assemble a sourced media shortlist. Sending pitches is a separate action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research queries, story context, target URLs, and the API key are sent to Crawlora.

Mitigation: Use the skill only when that disclosure is acceptable; omit confidential launch details and sensitive personal data from searches.

Risk: Outdated profiles or search snippets can misstate affiliation, coverage, or contact availability.

Mitigation: Verify bylines, article dates, affiliation, and public contact sources on original pages; mark unverified matches explicitly and do not invent email addresses.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/journalist-media-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, CSV]

**Output Format:** [Sourced media shortlist as a Markdown table or CSV]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes outlet, beat, article links and dates, public contact source, retrieval time, and verification status.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
