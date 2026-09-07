## Description:

Researches global news and US television coverage through the Crawlora API, returning JSON for GDELT search, context, timeline, sentiment, transcript, caption, on-screen text, and visual-label workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, OSINT researchers, media-monitoring teams, and political or social-science researchers use this skill to query public GDELT web-news and US television indexes for coverage search, co-occurrence context, trends, sentiment, and broadcast comparisons.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shell wrapper can send the user's Crawlora API key to an overridden API host.

Mitigation: Use only trusted environments, keep CRAWLORA_API_BASE unset unless intentionally testing, and prefer a release that hardcodes or validates the Crawlora host.

Risk: Queries may disclose sensitive research topics to an external API.

Mitigation: Use non-sensitive queries and a limited Crawlora API key, as recommended by the security guidance.

Risk: The wrapper accepts broader paths than the documented GDELT endpoints.

Mitigation: Restrict use to documented /gdelt endpoints and review commands before execution.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API Base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY for authenticated Crawlora requests and returns raw JSON suitable for jq or downstream analysis.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
