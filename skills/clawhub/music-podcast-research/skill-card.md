## Description:

Researches music, artists, playlists, and podcasts through the Crawlora API for Spotify, Spotify Podcasts, Apple Podcasts, Discogs, and SoundCloud, returning normalized JSON for catalog, profile, chart, episode, release, and track lookups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to look up public music, podcast, playlist, profile, chart, SoundCloud, and Discogs release data through Crawlora and receive normalized JSON suitable for agent responses or follow-up analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup terms and public profile URLs are sent to Crawlora's external API.

Mitigation: Use the skill only for public music, podcast, Discogs, Spotify, and SoundCloud lookups, and avoid sensitive or private profile information.

Risk: The skill requires a Crawlora API key.

Mitigation: Keep CRAWLORA_API_KEY in the environment and do not hardcode, query-string, or commit it.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/music-podcast-research)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON responses with Markdown guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a Crawlora API key from CRAWLORA_API_KEY and is limited to documented read-only GET routes.]

## Skill Version(s):

1.0.18 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
