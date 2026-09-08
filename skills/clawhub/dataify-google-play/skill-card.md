## Description:

Search Google Play for apps, rankings, or store results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn Google Play app-search, category, ranking, language, country, and device requests into Dataify Scraper API calls and receive compact app-result summaries or requested raw output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a Dataify API token from the environment and sends Google Play search parameters to Dataify.

Mitigation: Configure DATAIFY_API_TOKEN as an environment variable, do not paste it into chat, and install only if this token and request-data flow is acceptable.

Risk: Broad, multi-page, media-download, or ambiguous requests can materially change scope or credit usage.

Mitigation: Ask for confirmation when scope, cost, or required search input is unclear; show only user-facing values that affect target, scope, output, or cost.

## Reference(s):

- [Dataify Google Play API Reference](references/google_play_api.md)
- [Dataify Dashboard](https://dashboard.dataify.com?utm_source=skill)
- [Dataify Dashboard Login](https://dashboard.dataify.com/login?utm_source=skill)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries, shell command snippets, parameter tables, JSON, or HTML depending on the user's requested output mode.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Google Play search parameters and a Dataify API token; raw JSON or HTML is returned only when explicitly requested.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
