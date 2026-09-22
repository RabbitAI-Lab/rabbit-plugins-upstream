## Description:

Use when a YouTube playlist is involved: pasted playlist links or IDs, requests to list playlist videos, browse playlist contents, or work through a playlist for transcripts or research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[therohitdas](https://clawhub.ai/user/therohitdas)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and external users use this skill to browse YouTube playlist contents, find videos in a series or course, and retrieve transcripts through TranscriptAPI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow may ask an agent to create a TranscriptAPI account, handle an email verification code, and persist a long-lived API key.

Mitigation: Prefer creating the account and storing TRANSCRIPT_API_KEY yourself through a trusted secret manager before using the skill.

Risk: The authentication guide describes writing raw token responses to temporary files, which can expose credentials if files are retained or broadly readable.

Mitigation: Avoid writing raw credential responses to general temporary files; if temporary storage is unavoidable, restrict permissions and delete the files immediately after use.

## Reference(s):

- [TranscriptAPI homepage](https://transcriptapi.com)
- [TranscriptAPI OpenAPI specification](https://transcriptapi.com/openapi.json)
- [TranscriptAPI authentication setup](references/auth-setup.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls]

**Output Format:** [Markdown with inline bash commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires TRANSCRIPT_API_KEY and internet access to transcriptapi.com.]

## Skill Version(s):

1.6.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
