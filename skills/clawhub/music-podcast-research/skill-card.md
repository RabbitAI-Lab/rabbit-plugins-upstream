## Description:

Researches music, artists, playlists, and podcasts via the Crawlora API across Spotify, Spotify Podcasts, Apple Podcasts, Discogs, and SoundCloud, returning clean JSON for tracks, albums, artists, playlists, profiles, podcast shows and episodes, charts, record releases, and SoundCloud stats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to research public music, podcast, playlist, profile, chart, and record-release information through Crawlora API calls. It is useful when a user needs normalized JSON about Spotify, Spotify Podcasts, Apple Podcasts, Discogs, or SoundCloud entities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can call broader Crawlora API endpoints beyond the stated music and podcast use case.

Mitigation: Review requested paths before execution and restrict use to the documented music, podcast, Discogs, Spotify, Apple Podcasts, and SoundCloud endpoints when deploying this skill.

Risk: The skill requires a Crawlora API key and sends user queries to an external API.

Mitigation: Use non-sensitive queries and keep the API key only in the CRAWLORA_API_KEY environment variable, as documented.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance, Configuration]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns normalized public catalog, profile, chart, podcast, SoundCloud, and Discogs data.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
