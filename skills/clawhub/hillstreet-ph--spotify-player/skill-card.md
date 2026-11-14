## Description:

Terminal Spotify playback/search via spogo (preferred) or spotify_player.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hillstreet-ph](https://clawhub.ai/user/hillstreet-ph)

### License/Terms of Use:

MIT-0

## Use Case:

Spotify users can use terminal commands to search for music, control playback, choose Spotify Connect devices, check playback status, and like tracks. A Spotify Premium account and either spogo or spotify_player are required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The referenced Spotify authentication setup imports browser session cookies; scanner review did not establish the importer's scope or credential-storage protections and was partial.

Mitigation: Before installing, consider whether you are comfortable allowing the referenced tool to import browser session cookies for Spotify authentication.

## Reference(s):

- [Spotify](https://www.spotify.com)
- [ClawHub skill release](https://clawhub.ai/hillstreet-ph/skills/spotify-player)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides command examples and setup guidance; requires a Spotify Premium account and an installed supported CLI.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
