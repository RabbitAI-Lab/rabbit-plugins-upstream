## Description:

Researches global news and US television coverage via the Crawlora API, including GDELT web-news search, sentence-level context search, coverage and tone timelines, sentiment histograms, and GDELT Television 2.0 AI transcript, caption, on-screen text, and visual-label search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, analysts, OSINT practitioners, and media-monitoring teams use this skill to query GDELT-backed news and US television coverage through Crawlora and receive normalized JSON for search results, timelines, sentiment, co-occurrence, station/show comparisons, and word clouds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends research terms, filters, and usage metadata to Crawlora under the user's API key.

Mitigation: Use only non-confidential research terms and avoid submitting secrets, private investigations, or sensitive identifiers.

Risk: The included shell helper can call arbitrary Crawlora API paths, not only the documented GDELT endpoints.

Mitigation: Constrain use to the documented /gdelt endpoints unless the broader Crawlora API behavior has been separately reviewed.

Risk: GDELT endpoint behavior includes limits such as recent-only context search, search-window caps, required TV station or channel parameters, and max-record limits.

Mitigation: Check the endpoint reference before interpreting incomplete results or comparing coverage across sources and time windows.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/gdelt-research)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are expected to be clean JSON from Crawlora GDELT endpoints; some endpoints have documented time-window, station, channel, and max-record constraints.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
