## Description: <br>
Helps agents look up YouTube transcripts, videos, channel latest uploads, channel IDs, and topic search results through TranscriptAPI.com; it is not for uploads or account management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[therohitdas](https://clawhub.ai/user/therohitdas) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agents use this skill to retrieve YouTube transcripts, search YouTube content, inspect recent channel uploads, and resolve channel handles via TranscriptAPI.com. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: TranscriptAPI.com receives YouTube-related inputs submitted through the skill. <br>
Mitigation: Use the skill only when sharing those YouTube queries or URLs with TranscriptAPI.com is acceptable. <br>
Risk: The setup flow may involve sensitive account, OTP, token, and persistent API-key handling by the agent. <br>
Mitigation: Create the TranscriptAPI account yourself, store TRANSCRIPT_API_KEY through a trusted secret store, and avoid setup paths where the agent handles OTPs or works around token redaction. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/therohitdas/skills/yt) <br>
- [TranscriptAPI homepage](https://transcriptapi.com) <br>
- [TranscriptAPI OpenAPI spec](https://transcriptapi.com/openapi.json) <br>
- [TranscriptAPI auth setup](references/auth-setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with inline bash/curl commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires TRANSCRIPT_API_KEY and internet access to transcriptapi.com; transcript and search requests may consume TranscriptAPI credits.] <br>

## Skill Version(s): <br>
1.5.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
