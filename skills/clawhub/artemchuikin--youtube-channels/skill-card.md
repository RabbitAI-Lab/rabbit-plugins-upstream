## Description:

Reach for this when a YouTube channel is the subject: a pasted @handle or channel URL, a creator's recent uploads, their full catalogue, or a search inside one channel.

This skill is ready for commercial/non-commercial use.

## Publisher:

[artemchuikin](https://clawhub.ai/user/artemchuikin)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to look up recent uploads, full video catalogues, and channel-scoped search results for YouTube channels through TranscriptOut.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup may involve account signup, one-time codes, API keys, and persistent secret storage.

Mitigation: Create the TranscriptOut account and API key yourself when possible, and store the key in a platform-managed secret store instead of pasting credentials into chat.

Risk: Channel names, channel URLs, search terms, and usage metadata are sent to TranscriptOut for lookup.

Mitigation: Avoid sensitive channel searches unless you accept sharing those lookup details with TranscriptOut.

## Reference(s):

- [TranscriptOut](https://transcriptout.com)
- [TranscriptOut API Documentation](https://transcriptout.com/docs)
- [TranscriptOut API Key Setup](references/auth-setup.md)
- [ClawHub Skill Page](https://clawhub.ai/artemchuikin/skills/youtube-channels)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, JSON, Guidance]

**Output Format:** [Markdown guidance with inline bash commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires TRANSCRIPTOUT_API_KEY and internet access to api.transcriptout.com.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
