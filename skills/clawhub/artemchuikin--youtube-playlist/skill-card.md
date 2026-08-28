## Description:

Helps agents list YouTube playlist videos, search within playlists, and fetch bulk transcripts through TranscriptOut.

This skill is ready for commercial/non-commercial use.

## Publisher:

[artemchuikin](https://clawhub.ai/user/artemchuikin)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill when a YouTube playlist, course, or series needs to be listed, searched, or converted into transcripts. It is suited for playlist discovery and transcript retrieval, not for creating playlists or account management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow may place account signup, email OTPs, API keys, temporary secret files, and persistent credential storage under agent control.

Mitigation: Create the TranscriptOut API key yourself in the provider dashboard when possible, then store it through the approved secret manager for the agent platform.

Risk: Playlist and video metadata may be sent to TranscriptOut during playlist and transcript requests.

Mitigation: Avoid private or sensitive playlists unless the data sharing is acceptable for the intended use.

## Reference(s):

- [TranscriptOut](https://transcriptout.com)
- [TranscriptOut API documentation](https://transcriptout.com/docs)
- [TranscriptOut authentication setup](references/auth-setup.md)
- [ClawHub skill page](https://clawhub.ai/artemchuikin/skills/youtube-playlist)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown with inline bash commands and JSON API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires internet access to api.transcriptout.com and a TRANSCRIPTOUT_API_KEY secret for API requests.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
