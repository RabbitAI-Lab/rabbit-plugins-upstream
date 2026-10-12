## Description:

Curates Apple Music playlists and recommendations from listening history, and helps explore music taste, import playlists, and schedule optional updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[and3rn3t](https://clawhub.ai/user/and3rn3t)

### License/Terms of Use:

MIT-0

## Use Case:

Apple Music listeners use this skill to discover songs, build and import playlists, review listening insights, and optionally automate recurring recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to personal listening history, library, ratings, and playlists exposes sensitive music preferences.

Mitigation: Grant Apple Music access only if comfortable sharing those data; review locally cached taste information before sharing it.

Risk: Playlist creation, library additions, and ratings change the user's Apple Music account.

Mitigation: Inspect previews and request explicit confirmation before any account write.

Risk: Enabled cron schedules keep running, and the weekly mix can create playlists unattended.

Mitigation: Review the proposed schedule before enabling it, opt into unattended playlist creation deliberately, and remove jobs when no longer needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/and3rn3t/skills/apple-music-dj)
- [Project homepage (publisher metadata; import provenance unavailable)](https://github.com/and3rn3t/apple-music-dj)
- [Apple Music API reference](artifact/references/api-reference.md)
- [Apple Music authorization setup](artifact/references/auth-setup.md)
- [Spotify playlist import guidance](artifact/references/spotify-import.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with recommendations, summaries, and optional commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can offer optional taste-card visuals and playlist previews.]

## Skill Version(s):

3.4.0 (source: ClawHub release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
