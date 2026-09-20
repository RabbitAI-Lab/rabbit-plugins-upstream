## Description:

Researches global news and US television coverage via the Crawlora API, including GDELT web-news search, context, timeline, sentiment, and Television 2.0 AI indexes, returning clean JSON for media-monitoring, OSINT, and political or social-science research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, analysts, and developers use this skill to query global news and US television coverage, compare outlets or stations, inspect coverage volume and tone over time, and retrieve normalized JSON for further analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research queries and the Crawlora API key are sent to Crawlora.

Mitigation: Use the skill only when third-party API processing fits the user's privacy requirements, and avoid confidential investigations unless that use is approved.

Risk: The security evidence notes no hidden, persistent, destructive, or privilege-escalating behavior, but the skill still executes a local shell helper that makes outbound API requests.

Mitigation: Review commands before execution and keep CRAWLORA_API_KEY in the environment rather than in prompts, files, or command-line arguments.

Risk: Coverage endpoints have documented limits such as recent-only context search, record caps, station requirements, and mutually exclusive time-window parameters.

Mitigation: Treat outputs as research leads, choose documented endpoint parameters carefully, and verify important claims against primary sources.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/crawlora-org/skills/gdelt-research)
- [Crawlora](https://crawlora.net)
- [Endpoint Reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [JSON API responses with concise guidance and shell command examples when useful]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses documented GET-only Crawlora GDELT routes.]

## Skill Version(s):

1.0.12 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
