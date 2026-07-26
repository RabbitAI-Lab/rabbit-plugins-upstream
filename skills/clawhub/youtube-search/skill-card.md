## Description: <br>
Searches YouTube videos and channels and helps agents discover relevant creators, tutorials, talks, expert discussions, and transcripts through TranscriptAPI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[therohitdas](https://clawhub.ai/user/therohitdas) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and research agents use this skill to search YouTube globally for videos or channels, resolve channel identifiers, and retrieve transcripts for YouTube-based research workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may create or use a TranscriptAPI account and handle a long-lived TRANSCRIPT_API_KEY. <br>
Mitigation: Prefer supplying an existing key through an approved platform secret manager, confirm where the key is stored, and revoke or rotate it when the skill is no longer used. <br>
Risk: YouTube search queries and transcript requests are sent to TranscriptAPI. <br>
Mitigation: Avoid sensitive queries and confirm that third-party API use is acceptable for the user's research task before sending requests. <br>
Risk: Authentication setup can persist credentials across future sessions. <br>
Mitigation: Store credentials only in the correct secret mechanism for the agent environment, avoid printing tokens or keys, and clean up temporary authentication files. <br>


## Reference(s): <br>
- [TranscriptAPI homepage](https://transcriptapi.com) <br>
- [TranscriptAPI OpenAPI specification](https://transcriptapi.com/openapi.json) <br>
- [TranscriptAPI authentication setup](references/auth-setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON API response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires TRANSCRIPT_API_KEY and internet access to transcriptapi.com; API calls return YouTube video, channel, and transcript data.] <br>

## Skill Version(s): <br>
1.5.0 (source: evidence release and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
