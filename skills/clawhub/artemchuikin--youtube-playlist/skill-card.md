## Description:

Helps agents list YouTube playlist videos, search within playlists, and collect playlist transcripts through TranscriptOut.

This skill is ready for commercial/non-commercial use.

## Publisher:

[artemchuikin](https://clawhub.ai/user/artemchuikin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill when they need to inspect a YouTube playlist, find videos inside a long playlist, or turn a course or series playlist into transcripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow can expose OTP codes and a long-lived TranscriptOut API key to the agent or local environment storage.

Mitigation: Create the TranscriptOut key yourself when practical, store it in a trusted secret manager, and provide only TRANSCRIPTOUT_API_KEY to the agent runtime.

Risk: Playlist URLs, video IDs, and transcript requests are sent to TranscriptOut.

Mitigation: Use the skill only for playlists whose metadata and video IDs can be shared with TranscriptOut, and avoid private or sensitive playlists unless that sharing is acceptable.

## Reference(s):

- [TranscriptOut](https://transcriptout.com)
- [TranscriptOut API Docs](https://transcriptout.com/docs)
- [TranscriptOut Auth Setup](references/auth-setup.md)
- [ClawHub Skill Page](https://clawhub.ai/artemchuikin/skills/youtube-playlist)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text, markdown]

**Output Format:** [Markdown with inline bash commands and API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires TRANSCRIPTOUT_API_KEY and internet access to api.transcriptout.com.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
