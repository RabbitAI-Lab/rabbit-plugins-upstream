## Description:

Researches global news and US television coverage via the Crawlora API, including GDELT web-news search, context, timeline, sentiment, and Television 2.0 AI indexes, returning clean JSON for OSINT, media-monitoring, and political or social-science research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, researchers, and media-monitoring teams use this skill to query GDELT news and US television coverage through Crawlora for coverage search, trend analysis, tone/sentiment review, sentence-level co-occurrence checks, and station or show comparisons.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, filters, and the Crawlora API key are transmitted to Crawlora's external API.

Mitigation: Avoid private or sensitive material in queries unless that transmission is intended, and install the skill only when use of the Crawlora API is acceptable.

Risk: The skill requires a Crawlora API key for requests.

Mitigation: Provide the key only through CRAWLORA_API_KEY, and do not hardcode, pass as a query parameter, or commit the credential.

Risk: Some GDELT endpoints have time-window and parameter constraints that can affect research completeness.

Mitigation: Use the endpoint reference before running a query, especially for the 72-hour context limit, TV station and channel requirements, and mutually exclusive timespan versus from/to filters.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/gdelt-research)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands that call the Crawlora API and return JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY from the environment and a fixed Crawlora API base URL; endpoint results are raw JSON suitable for inspection or jq processing.]

## Skill Version(s):

1.0.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
