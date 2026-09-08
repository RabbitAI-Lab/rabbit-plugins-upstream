## Description:

Search Bing Maps for places or map results, not Bing web search or Google Maps structured details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn natural-language Bing Maps place searches into Dataify Bing Maps API calls and receive compact map/place results, raw JSON, or HTML when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Map searches, including provided coordinates, are sent to Dataify.

Mitigation: Install only if this data sharing is acceptable for the intended use case, and avoid submitting sensitive location queries.

Risk: Live requests require a Dataify API token from the execution environment.

Mitigation: Configure DATAIFY_API_TOKEN as an environment variable and do not paste the token into chat or expose its value in logs.

## Reference(s):

- [Dataify Bing Maps API Reference](references/api.md)
- [Dataify Bing Maps ClawHub Skill Page](https://clawhub.ai/dataify-server/skills/dataify-bing-maps)
- [Dataify Bing Maps API Endpoint](https://scraperapi.dataify.com/request)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance]

**Output Format:** [Markdown summaries or raw JSON/HTML when requested, with shell commands for dry runs and token setup guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses DATAIFY_API_TOKEN from the environment for live requests; dry runs produce JSON payloads without network calls.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
