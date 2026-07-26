## Description: <br>
Provides agent guidance for resolving YouTube channel identifiers, browsing recent or paginated uploads, and searching within a channel through TranscriptAPI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[therohitdas](https://clawhub.ai/user/therohitdas) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill when a YouTube channel is the focus, including resolving handles or channel URLs, reviewing recent uploads, paging through channel videos, and searching within a creator's channel. It is not intended for YouTube account management or channel creation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup flow can involve an agent handling and persisting a TranscriptAPI credential. <br>
Mitigation: Prefer that the user creates the TranscriptAPI account and supplies the key through an approved secret manager; before persistence, confirm the storage location and how to revoke or remove the key. <br>
Risk: The setup guide gives the agent broad authority to create a third-party account and process OTP or API secret material. <br>
Mitigation: Require explicit user approval for signup, avoid exposing tokens or API keys in chat or logs, and clean up temporary files that may contain credential material. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/therohitdas/skills/youtube-channels) <br>
- [TranscriptAPI homepage](https://transcriptapi.com) <br>
- [TranscriptAPI OpenAPI specification](https://transcriptapi.com/openapi.json) <br>
- [TranscriptAPI authentication setup](references/auth-setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls, JSON] <br>
**Output Format:** [Markdown guidance with inline curl examples and JSON API response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires internet access to transcriptapi.com and a TRANSCRIPT_API_KEY for API requests.] <br>

## Skill Version(s): <br>
1.5.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
