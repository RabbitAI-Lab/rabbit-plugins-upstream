## Description:

Researches music, artists, playlists, and podcasts via the Crawlora API across Spotify, Spotify Podcasts, Apple Podcasts, Discogs, and SoundCloud, returning normalized JSON for agent use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to look up public music catalog, artist, playlist, podcast, Discogs release, and SoundCloud profile or track information through Crawlora. It is suited for research workflows that need structured JSON from supported public music and podcast sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crawlora receives the API key and lookup terms submitted through the skill.

Mitigation: Use the skill only when sharing those terms with Crawlora is acceptable, and avoid sensitive personal data, private account tokens, session cookies, and optional session-token parameters such as sp_t.

## Reference(s):

- [music-podcast-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/music-podcast-research)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples that return JSON from the Crawlora API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends supported lookup requests to Crawlora.]

## Skill Version(s):

1.0.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
