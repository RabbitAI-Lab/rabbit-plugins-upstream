## Description:

Researches music, artists, playlists, and podcasts via the Crawlora API -- Spotify tracks/albums/artists/playlists/profiles, Spotify Podcasts, Apple Podcasts, Discogs, and SoundCloud tracks/profiles/playlists -- returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research public music catalog, playlist, podcast, Discogs release, and SoundCloud profile data through Crawlora API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Music and podcast search terms, public profile URLs, resource IDs, and supplied request bodies are sent to Crawlora.

Mitigation: Use the skill only with public or non-sensitive inputs and avoid private links or confidential research data.

Risk: The helper script can expose the Crawlora API key if CRAWLORA_API_BASE is overridden by untrusted code.

Mitigation: Run the helper in a trusted shell environment and ensure CRAWLORA_API_BASE is unset or points only to the intended Crawlora API base.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/music-podcast-research)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends requests to the Crawlora API.]

## Skill Version(s):

1.0.9 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
