## Description:

Fetches timestamped caption data from YouTube videos through TranscriptAPI for reading, quoting, translating, accessibility, content review, and language-learning workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[therohitdas](https://clawhub.ai/user/therohitdas)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to retrieve YouTube captions or transcript text for accessibility, review, quotation, translation, and timing-aware analysis. It is not intended for uploading subtitles or managing YouTube accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a TranscriptAPI API key and includes setup guidance for creating and storing the credential.

Mitigation: Use a scoped secret manager or the agent platform's approved secret storage, and avoid broad persistent shell or environment storage.

Risk: YouTube URLs or IDs supplied to the skill are sent to TranscriptAPI.

Mitigation: Install and use the skill only when sharing those video identifiers with TranscriptAPI is acceptable for the intended workflow.

Risk: Server security evidence marks the release as suspicious because of credential handling behavior.

Mitigation: Review the skill before installation and confirm the authentication flow and persistent key storage are appropriate for the deployment environment.

## Reference(s):

- [TranscriptAPI](https://transcriptapi.com)
- [TranscriptAPI authentication setup](references/auth-setup.md)
- [ClawHub skill listing](https://clawhub.ai/therohitdas/skills/captions)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, API calls]

**Output Format:** [Markdown guidance with inline bash commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include timestamped transcript segments, plain transcript text, and video metadata returned by TranscriptAPI.]

## Skill Version(s):

1.5.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
