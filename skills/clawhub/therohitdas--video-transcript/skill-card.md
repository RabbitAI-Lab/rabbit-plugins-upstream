## Description:

Use when video content needs to be extracted as text: pasted YouTube links or IDs, requests to transcribe, summarize, quote, translate, convert video to text, or extract information from video content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[therohitdas](https://clawhub.ai/user/therohitdas)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and users use this skill to retrieve YouTube video transcripts, metadata, timestamps, and related text outputs for summarization, quoting, translation, or information extraction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions give the agent substantial control over account creation, OTP handling, and long-term API key storage.

Mitigation: Prefer user-managed signup through the provider site and store TRANSCRIPT_API_KEY in the agent platform's secure secret store rather than pasting API keys or OTP codes into chat.

## Reference(s):

- [TranscriptAPI homepage](https://transcriptapi.com)
- [TranscriptAPI auth setup](references/auth-setup.md)
- [ClawHub skill page](https://clawhub.ai/therohitdas/skills/video-transcript)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and text or JSON transcript responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires TRANSCRIPT_API_KEY and internet access to transcriptapi.com. Transcript responses may include timestamps and video metadata when requested.]

## Skill Version(s):

1.5.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
