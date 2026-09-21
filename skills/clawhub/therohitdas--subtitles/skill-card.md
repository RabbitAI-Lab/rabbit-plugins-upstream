## Description:

Fetches timestamped subtitles and spoken text from YouTube videos through TranscriptAPI for reading, translation, accessibility, and language-learning workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[therohitdas](https://clawhub.ai/user/therohitdas)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve YouTube subtitles or spoken text for reading, translation, accessibility, and language-learning workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead an agent to collect, handle, and persist TranscriptAPI credentials.

Mitigation: Prefer creating the account and API key yourself, then store the key only through a trusted secret manager or scoped environment mechanism.

Risk: Sensitive API keys or OTPs may be exposed if pasted into chat or printed through tool output.

Mitigation: Avoid pasting sensitive keys or OTPs into chat unless you understand the storage and exposure implications, and avoid printing token values during setup.

Risk: The skill depends on an external TranscriptAPI service and sends YouTube identifiers or URLs to that service.

Mitigation: Review the external request target before use and send only video identifiers or URLs appropriate for the workflow.

## Reference(s):

- [TranscriptAPI](https://transcriptapi.com)
- [TranscriptAPI auth setup](references/auth-setup.md)
- [ClawHub skill page](https://clawhub.ai/therohitdas/skills/subtitles)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with bash examples and JSON or plain-text API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires TRANSCRIPT_API_KEY and internet access to transcriptapi.com.]

## Skill Version(s):

1.5.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
