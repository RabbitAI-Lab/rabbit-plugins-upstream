## Description:

Reach for this when a YouTube playlist is in play: a pasted playlist link or PL... id, listing a course or series, finding one video inside a long playlist, or turning a whole playlist into transcripts. Skip it for creating playlists or account chores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[artemchuikin](https://clawhub.ai/user/artemchuikin)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use this skill to list or search videos in a YouTube playlist and retrieve transcripts for a video, course, or series through TranscriptOut.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional account setup instructions may turn supplied text into unintended local commands.

Mitigation: Review the setup commands before use; create the API key yourself and enter it through the runtime's secret interface when available.

Risk: Signup shares an email with TranscriptOut, stored keys persist across sessions, and transcript requests spend credits.

Mitigation: Use private runtime secret storage for the key, and consider the service's account and credit use before creating an account or submitting transcripts.

Risk: The remote TranscriptOut service is outside the supplied security inspection.

Mitigation: Send the API key only to api.transcriptout.com and review the service's current terms and data practices before use.

## Reference(s):

- [TranscriptOut API documentation](https://transcriptout.com/docs?utm_source=youtube-skills&utm_medium=clawhub&utm_content=youtube-playlist)
- [TranscriptOut](https://transcriptout.com)
- [API key setup guide](artifact/references/auth-setup.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Playlist metadata and transcript text from TranscriptOut API responses in JSON envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires internet access and TRANSCRIPTOUT_API_KEY; transcript requests consume credits.]

## Skill Version(s):

1.2.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
