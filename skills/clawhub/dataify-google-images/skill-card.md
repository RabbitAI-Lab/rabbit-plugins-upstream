## Description:

Search Google Images for image results. Do not use for Google Lens reverse-image search or general web results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn Google Images search requests into Dataify Scraper API calls and receive compact image-result summaries or raw responses when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image search queries and related request parameters are sent to Dataify.

Mitigation: Avoid sensitive queries or parameters unless sharing them with Dataify is acceptable.

Risk: The Dataify API token could be exposed if pasted into chat or printed in logs.

Mitigation: Keep DATAIFY_API_TOKEN in the agent environment and do not paste or display the token value.

## Reference(s):

- [Dataify Google Images API Reference](references/google_images_api.md)
- [Dataify Google Images Skill Page](https://clawhub.ai/dataify-server/skills/dataify-google-images)
- [Dataify Scraper API Endpoint](https://scraperapi.dataify.com/request)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries, parameter tables, shell commands, and raw JSON or HTML when explicitly requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an image query and a DATAIFY_API_TOKEN supplied through the agent environment.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
