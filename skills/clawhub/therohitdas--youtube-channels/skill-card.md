## Description:

Helps agents resolve YouTube channel handles or URLs, browse recent uploads and channel feeds, search within a channel, and inspect channel profile or community data through TranscriptAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[therohitdas](https://clawhub.ai/user/therohitdas)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to inspect and monitor YouTube channels by resolving channel identifiers, checking recent uploads, listing videos, searching within a channel, and retrieving channel profile details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow asks agents to handle and persist a TranscriptAPI credential.

Mitigation: Create or retrieve the key yourself when possible, store it through the agent runtime's secure secret mechanism, and avoid broad shell-profile or global config persistence unless that reuse is intended.

Risk: YouTube channel identifiers and channel search terms are sent to TranscriptAPI.

Mitigation: Review requests before use and avoid sending sensitive monitoring targets or private research terms to the service.

## Reference(s):

- [TranscriptAPI](https://transcriptapi.com)
- [TranscriptAPI OpenAPI specification](https://transcriptapi.com/openapi.json)
- [Authentication setup](references/auth-setup.md)
- [ClawHub skill page](https://clawhub.ai/therohitdas/skills/youtube-channels)
- [ClawHub publisher profile](https://clawhub.ai/user/therohitdas)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with curl examples and JSON response shapes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires internet access and TRANSCRIPT_API_KEY; API calls send YouTube channel identifiers and search terms to TranscriptAPI.]

## Skill Version(s):

1.6.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
