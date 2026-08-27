## Description:

TranscriptOut helps agents retrieve YouTube transcripts, video metadata, search results, channel and playlist listings, and bulk transcript jobs through the TranscriptOut API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[artemchuikin](https://clawhub.ai/user/artemchuikin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to ask an agent for YouTube transcript retrieval, video and channel research, playlist inspection, creator monitoring, and batch transcript collection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an agent to handle and persist a TranscriptOut API key.

Mitigation: Use a dedicated key with limited value, store it through a trusted secret manager, and avoid pasting it into chat.

Risk: YouTube searches, channel or playlist requests, and bulk jobs are sent to TranscriptOut.

Mitigation: Avoid processing sensitive queries or collections unless the user intends to share those inputs with TranscriptOut.

## Reference(s):

- [TranscriptOut Skill Page](https://clawhub.ai/artemchuikin/skills/transcriptout)
- [TranscriptOut Homepage](https://transcriptout.com)
- [TranscriptOut API Documentation](https://transcriptout.com/docs)
- [Authentication Setup](references/auth-setup.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown with API request examples, shell commands, and JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include TranscriptOut API calls and guidance for handling YouTube transcripts, search results, channel data, playlist data, and bulk jobs.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
