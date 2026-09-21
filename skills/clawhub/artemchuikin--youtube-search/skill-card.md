## Description:

Searches YouTube videos and channels through TranscriptOut so agents can find relevant videos, creators, tutorials, talks, and reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[artemchuikin](https://clawhub.ai/user/artemchuikin)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search for YouTube videos or channels on a topic, identify creators or reviews, and choose candidates for follow-up transcript retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow may expose a TranscriptOut API key or one-time login code in chat or local files.

Mitigation: Prefer creating and storing the API key in a secure secret manager, avoid pasting credentials into normal chat, and delete temporary credential files after setup.

Risk: Persisting TRANSCRIPTOUT_API_KEY broadly for future sessions can make the credential available beyond the immediate task.

Mitigation: Scope the environment variable to the agent runtime or project where possible and review persistent shell profiles or runtime secret stores before installation.

Risk: The skill depends on an external API and spends TranscriptOut credits for search pages.

Mitigation: Review requests before execution, set conservative limits, and monitor the returned credit balance header.

## Reference(s):

- [TranscriptOut](https://transcriptout.com)
- [TranscriptOut API Documentation](https://transcriptout.com/docs)
- [TranscriptOut API Key Setup](references/auth-setup.md)
- [ClawHub YouTube Search Skill](https://clawhub.ai/artemchuikin/skills/youtube-search)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Markdown, Guidance]

**Output Format:** [Markdown with JSON response examples and inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a TranscriptOut API key in TRANSCRIPTOUT_API_KEY and internet access to api.transcriptout.com.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
