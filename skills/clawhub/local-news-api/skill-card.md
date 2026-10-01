## Description:

A read-only local-news research skill that retrieves published coverage, source records, meeting transcripts, and civic events from a Communities News newsroom.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alaskanews](https://clawhub.ai/user/alaskanews)

### License/Terms of Use:

MIT-0

## Use Case:

Journalists, civic writers, and other external users research local reporting, meeting records, people on the record, and upcoming public events before writing or citing a story. The default newsroom is Alaska News.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends requests to the configured newsroom using an API key when required.

Mitigation: Use a read-only key where possible and keep NEWS_SITE and PLATFORM_API_BASE set to trusted destinations.

Risk: Writing a brief with --out can overwrite a local file.

Mitigation: Choose the output path deliberately and check for an existing file before writing.

Risk: Reusing retrieved reporting without checking its terms or attribution can misrepresent the source.

Mitigation: Review the newsroom's current terms and include source attribution and a backlink before republishing.

## Reference(s):

- [Newsroom API specification](https://alaskanews.com/api/v1/openapi.json)
- [Communities News](https://communities.news)
- [Output and next steps](references/output.md)
- [Access verification and limitations](references/verification.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown by default; JSON with --json; optional Markdown brief file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Retrieved results include source links and usage terms; Markdown output also suggests next steps.]

## Skill Version(s):

1.6.0 (source: ClawHub release and skill frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
