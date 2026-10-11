## Description:

Curates Apple Music playlists and recommendations from listening history, supports music discovery and insights, and offers a token-free demo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[and3rn3t](https://clawhub.ai/user/and3rn3t)

### License/Terms of Use:

MIT

## Use Case:

Apple Music listeners use this OpenClaw skill to explore their listening habits, discover music, and curate or import playlists. Account changes require confirmation; a demo works without tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to Apple Music tokens and personal listening, library, ratings, recommendations, and Replay data.

Mitigation: Install only if comfortable granting this access; use the token-free demo to evaluate first.

Risk: Playlist edits, ratings, favorites, or library additions can change the account.

Mitigation: Review previews and confirm only intended account changes.

Risk: Scheduled jobs continue making recurring music selections until removed.

Mitigation: Review the schedule before enabling cron and remove jobs when no longer needed.

## Reference(s):

- [Apple Music DJ on ClawHub](https://clawhub.ai/and3rn3t/skills/apple-music-dj)
- [Apple Music API reference](artifact/references/api-reference.md)
- [Authentication setup](artifact/references/auth-setup.md)
- [Playlist strategies](artifact/references/playlist-strategies.md)
- [Troubleshooting](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Conversational text and Markdown with commands; optional Apple Music playlists and SVG taste cards]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can preview account changes before confirmation and schedule recurring curation.]

## Skill Version(s):

3.3.1 (source: release metadata, skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
