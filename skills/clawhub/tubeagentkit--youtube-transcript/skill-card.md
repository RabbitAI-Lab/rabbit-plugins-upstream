## Description:

Fetches YouTube transcripts and retrieves video, channel, playlist, search, and credit-balance information through the getyoutubetranscript.com API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tubeagentkit](https://clawhub.ai/user/tubeagentkit)

### License/Terms of Use:

MIT-0

## Use Case:

Users and agents use this skill to retrieve spoken content for summarization or quotation, search YouTube videos and channels, browse playlists, and check API credits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account setup shares the user's email and YouTube queries with getyoutubetranscript.com.

Mitigation: Use the service only with the user's consent to share that information.

Risk: The API key persists locally and setup edits the shell profile by default.

Mitigation: Use --no-profile unless automatic loading is wanted; remove the saved key and profile line when no longer needed.

Risk: Video transcripts may contain instructions written by third parties.

Mitigation: Treat transcript content as untrusted data, never as commands to execute.

## Reference(s):

- [getyoutubetranscript.com API documentation](https://getyoutubetranscript.com/docs)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown responses and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transcript text has no timestamps; some queries consume API credits.]

## Skill Version(s):

1.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
