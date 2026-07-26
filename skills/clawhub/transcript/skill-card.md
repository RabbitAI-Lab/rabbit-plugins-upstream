## Description: <br>
Fetches YouTube video transcripts from TranscriptAPI for summarization, quoting, translation, fact-checking, research, and learning workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[therohitdas](https://clawhub.ai/user/therohitdas) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and agents use this skill to retrieve YouTube transcript text, timestamps, and metadata for downstream analysis or content transformation. It is intended for transcript retrieval, not video uploads or account management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup flow can let an agent create a TranscriptAPI account, handle OTP verification, store an API key, and persist environment changes. <br>
Mitigation: Prefer creating the account yourself and storing the API key through a trusted secret manager; avoid letting the agent handle OTPs or persist secrets broadly unless you understand where the key will be stored and how to revoke it. <br>
Risk: Using the skill sends YouTube video identifiers and related request data to TranscriptAPI. <br>
Mitigation: Use it only for videos and request metadata you are comfortable sharing with TranscriptAPI, and review the service's terms and privacy expectations before sensitive use. <br>


## Reference(s): <br>
- [TranscriptAPI](https://transcriptapi.com) <br>
- [TranscriptAPI auth setup](references/auth-setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance with curl examples and TranscriptAPI responses as timestamped text or JSON] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires TRANSCRIPT_API_KEY and a User-Agent header for API requests; long transcripts may be summarized before providing full text.] <br>

## Skill Version(s): <br>
1.5.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
