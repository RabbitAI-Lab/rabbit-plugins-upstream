## Description:

Provides agent guidance for retrieving YouTube transcripts, video and channel metadata, channel upload history, search results, and playlist contents through TranscriptAPI without Google API quotas or OAuth.

This skill is ready for commercial/non-commercial use.

## Publisher:

[therohitdas](https://clawhub.ai/user/therohitdas)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and external agent users use this skill when they need structured YouTube content for analysis, including transcripts, metadata, channel videos, search results, and playlist contents. It is not intended for uploads, account management, or research limited to written sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow asks the agent to handle a TranscriptAPI credential and persist it for future sessions.

Mitigation: Create or retrieve the API key yourself, provide it through a protected secret mechanism, and avoid storing it in shell profiles or temporary files unless that matches the agent runtime's approved secret-storage practice.

Risk: The skill depends on an external TranscriptAPI service and API credits for most YouTube data requests.

Mitigation: Confirm network access, configure a valid TRANSCRIPT_API_KEY, monitor credit usage, and review request parameters before large channel or playlist jobs.

## Reference(s):

- [TranscriptAPI](https://transcriptapi.com)
- [TranscriptAPI OpenAPI Specification](https://transcriptapi.com/openapi.json)
- [TranscriptAPI Auth Setup](references/auth-setup.md)
- [ClawHub Skill Page](https://clawhub.ai/therohitdas/skills/youtube-data)
- [Publisher Profile](https://clawhub.ai/user/therohitdas)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text, json]

**Output Format:** [Markdown guidance with curl examples and JSON response shapes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires TRANSCRIPT_API_KEY and internet access to transcriptapi.com; API responses may consume TranscriptAPI credits.]

## Skill Version(s):

1.5.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
