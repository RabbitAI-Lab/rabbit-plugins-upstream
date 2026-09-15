## Description:

Researches global news and US television coverage through the Crawlora API, using GDELT web-news search, context, timeline, tone, and Television 2.0 AI endpoints to return normalized JSON for media monitoring, OSINT, and political or social-science research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, analysts, journalists, and developers use this skill to query global news and US TV coverage for search results, coverage-volume trends, sentiment/tone histograms, outlet or station comparisons, and sentence-level co-occurrence context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: News and TV search terms, filters, and related request parameters are sent to Crawlora under the user's Crawlora API key.

Mitigation: Use the skill only when sending those queries to Crawlora is acceptable, and avoid submitting sensitive or regulated search content.

Risk: The Crawlora API key could be exposed if it is hardcoded, committed, or logged.

Mitigation: Store the key only in CRAWLORA_API_KEY and keep it out of source control, command-line arguments, and logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/gdelt-research)
- [Crawlora](https://crawlora.net)
- [Endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [JSON from Crawlora API calls, usually summarized or cited in Markdown with optional shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided CRAWLORA_API_KEY environment variable and sends query terms and filters to Crawlora.]

## Skill Version(s):

1.0.11 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
