## Description: <br>
Use when a YouTube playlist is involved: pasted playlist links or IDs, requests to list playlist videos, browse playlist contents, or work through a playlist for transcripts or research. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[therohitdas](https://clawhub.ai/user/therohitdas) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to inspect YouTube playlist contents, page through playlist videos, and fetch transcripts for videos in a playlist or course collection through TranscriptAPI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup flow may ask an agent to handle account signup, OTPs, raw tokens, and persistent API-key storage. <br>
Mitigation: Prefer creating the TranscriptAPI account yourself, enter the API key through a secure secret manager, and avoid long-term shell-profile storage unless you know how to remove or revoke the key. <br>
Risk: Playlist and video targets are sent to TranscriptAPI. <br>
Mitigation: Install and use the skill only if you are comfortable sharing those YouTube playlist or video identifiers with TranscriptAPI. <br>


## Reference(s): <br>
- [TranscriptAPI](https://transcriptapi.com) <br>
- [TranscriptAPI OpenAPI specification](https://transcriptapi.com/openapi.json) <br>
- [TranscriptAPI auth setup](references/auth-setup.md) <br>
- [ClawHub skill page](https://clawhub.ai/therohitdas/skills/youtube-playlist) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON API response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires TRANSCRIPT_API_KEY and internet access to transcriptapi.com; API requests consume TranscriptAPI credits.] <br>

## Skill Version(s): <br>
1.5.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
