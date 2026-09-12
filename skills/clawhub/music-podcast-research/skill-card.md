## Description:

Researches music, artists, playlists, and podcasts via the Crawlora API -- Spotify tracks/albums/artists/playlists/profiles, Spotify Podcasts, Apple Podcasts, Discogs, and SoundCloud tracks/profiles/playlists -- returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to look up public music, artist, playlist, podcast, Discogs, and SoundCloud information and return normalized JSON for research workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Music and podcast lookup inputs are sent to Crawlora using the user's Crawlora API key.

Mitigation: Use a scoped private API key, set it only through CRAWLORA_API_KEY, and monitor credit usage.

Risk: Authenticated POST requests and undocumented nested paths may exceed the documented read-only endpoint expectations.

Mitigation: Use documented endpoint paths and GET requests by default; avoid POST or undocumented nested paths unless the publisher documents and justifies them.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora API Base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/music-podcast-research)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends requests to the Crawlora API.]

## Skill Version(s):

1.0.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
