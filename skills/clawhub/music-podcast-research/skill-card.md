## Description:

Researches music, artists, playlists, and podcasts via the Crawlora API for Spotify, Spotify Podcasts, Apple Podcasts, and Discogs, returning clean JSON for catalog, profile, podcast, chart, and release lookups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to look up public music, podcast, chart, profile, playlist, and release metadata through Crawlora endpoints and receive normalized JSON for research or agent workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup inputs and API usage are sent to Crawlora using the user's API key.

Mitigation: Use the skill only when sending music, podcast, profile, URL, or release lookup inputs to Crawlora is acceptable, and keep the API key in CRAWLORA_API_KEY.

Risk: The helper script can call arbitrary Crawlora API paths beyond the music and podcast endpoints described by the skill.

Mitigation: Prefer the documented Spotify, Spotify Podcasts, Apple Podcasts, and Discogs endpoints, and review shell commands before execution.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API Base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON responses with Markdown command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends lookup inputs to the Crawlora API.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
