## Description:

Reach for this when structured YouTube data is the goal: video metadata, transcripts for analysis, channel upload history, search results or playlist contents, with no Google Cloud project and no quota units.

This skill is ready for commercial/non-commercial use.

## Publisher:

[artemchuikin](https://clawhub.ai/user/artemchuikin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to retrieve structured YouTube video metadata, transcripts, channel video lists, search results, and playlist contents through TranscriptOut.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: YouTube searches, video URLs or IDs, channel names, playlist IDs, and setup email addresses may be sent to TranscriptOut as a third-party processor.

Mitigation: Use the skill only for explicit YouTube data requests and avoid sending sensitive or unnecessary identifiers.

Risk: Account setup can involve one-time codes, API keys, and persistent credential storage.

Mitigation: Create the TranscriptOut account and API key yourself when possible, store the key in an approved secret store, and avoid pasting credentials into chat.

Risk: Bulk channel or playlist retrieval can send broad queries and consume paid or limited TranscriptOut credits.

Mitigation: Review the scope before bulk retrieval and check endpoint credit costs before running large requests.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/artemchuikin/skills/youtube-data)
- [TranscriptOut](https://transcriptout.com)
- [TranscriptOut API Documentation](https://transcriptout.com/docs)
- [TranscriptOut API Key Setup](references/auth-setup.md)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with curl examples and JSON or text API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires TRANSCRIPTOUT_API_KEY and internet access to api.transcriptout.com; requests consume TranscriptOut credits according to endpoint.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
