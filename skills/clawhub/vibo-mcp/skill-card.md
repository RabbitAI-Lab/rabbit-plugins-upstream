## Description:

Access your Vibo (vibodj.com) event music planning via MCP. Use when the user asks about their Vibo events, wedding/event timeline, song requests, playlists, or "do not play" list, or wants to add or like songs, join an event from a share link, or export songs to Spotify/Apple Music.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Event hosts and couples use this skill to review Vibo event timelines, song requests, playlists, and planning details, and to manage event music and membership through Vibo.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Vibo credentials or saved session tokens could expose the user's account if configuration or session files are accessed by others.

Mitigation: Protect configuration and saved session files; approve browser pairing only when initiating login capture.

Risk: Changes to event data, including deletions and membership changes, can have lasting effects.

Mitigation: Keep confirmation mode set to ask-user and review the action preview before confirming.

Risk: The supplied artifact contains documentation only, so the downloaded server and browser extension were not verified by the security verdict.

Mitigation: Consider pinning a reviewed package version and use browser capture only when needed for sign-in.

## Reference(s):

- [Vibo](https://vibodj.com)
- [vibo-mcp npm package](https://www.npmjs.com/package/vibo-mcp)
- [vibo-mcp project page (listed in the skill documentation)](https://github.com/chrischall/vibo-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Natural-language event and music information, with confirmation previews for changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include event summaries, song lists, and action previews.]

## Skill Version(s):

2.5.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
