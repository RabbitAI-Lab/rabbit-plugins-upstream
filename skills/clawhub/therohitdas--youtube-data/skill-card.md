## Description: <br>
Use when structured YouTube data is needed: pasted video/channel/playlist links, transcripts for analysis, video metadata, channel upload history, search results, or playlist contents - without Google API quotas or OAuth. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[therohitdas](https://clawhub.ai/user/therohitdas) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and agents use this skill to retrieve structured YouTube transcripts, metadata, search results, channel uploads, and playlist contents through TranscriptAPI. It is not intended for uploads, account management, or written-source-only research. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup flow can involve account signup, OTP handling, API keys, and persistent environment changes. <br>
Mitigation: Create or retrieve the TranscriptAPI account yourself when possible, enter the key through a dedicated secret manager, confirm where it will be stored, and remove temporary files after setup. <br>
Risk: The skill sends YouTube URLs, creator names, topic searches, and playlist or channel identifiers to TranscriptAPI. <br>
Mitigation: Avoid submitting sensitive, private, or confidential URLs and search terms, and review requests before execution. <br>
Risk: TranscriptAPI availability, Cloudflare requirements, credit limits, and endpoint behavior can affect results. <br>
Mitigation: Use the required Authorization and User-Agent headers, monitor remaining credits, and verify important outputs against source material. <br>


## Reference(s): <br>
- [TranscriptAPI homepage](https://transcriptapi.com) <br>
- [TranscriptAPI OpenAPI specification](https://transcriptapi.com/openapi.json) <br>
- [TranscriptAPI authentication setup](references/auth-setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Shell commands, Configuration instructions, JSON, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires TRANSCRIPT_API_KEY and internet access to transcriptapi.com; responses may consume TranscriptAPI credits depending on endpoint.] <br>

## Skill Version(s): <br>
1.5.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
