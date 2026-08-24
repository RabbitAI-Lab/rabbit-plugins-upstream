## Description:

Researches music, artists, playlists, and podcasts via the Crawlora API, covering Spotify, Spotify Podcasts, Apple Podcasts, Discogs, and SoundCloud, and returns clean JSON for agent use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to research public music catalogs, artist profiles, playlists, podcast shows and episodes, chart data, Discogs releases, and SoundCloud tracks through Crawlora API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Crawlora helper can send arbitrary paths and data with the user's API key, including endpoints outside the documented music and podcast scope.

Mitigation: Use the helper only with documented Spotify, Spotify Podcasts, Apple Podcasts, Discogs, and SoundCloud paths, and review commands before execution.

Risk: User queries and request data are sent to Crawlora using CRAWLORA_API_KEY.

Mitigation: Avoid private data and personal session tokens, keep the key in the environment, and do not hardcode or commit it.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/music-podcast-research)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands that call a JSON API; API responses are raw JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; calls public catalog, profile, and chart endpoints through Crawlora.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
