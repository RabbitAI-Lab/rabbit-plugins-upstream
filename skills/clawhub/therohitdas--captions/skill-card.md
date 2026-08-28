## Description: <br>
Fetches timestamped caption data from YouTube videos via TranscriptAPI for reading, quoting, translating, accessibility, content review, and language learning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[therohitdas](https://clawhub.ai/user/therohitdas) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when an agent needs the spoken text, captions, subtitles, timestamps, or metadata from a YouTube video. It supports accessibility workflows, content review, language learning, quoting, translation, and transcript-based analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup flow can give the agent control over TranscriptAPI account creation and persistent API-key storage. <br>
Mitigation: Create the TranscriptAPI account yourself, provide the key through a trusted secret manager, and avoid persistent shell or profile storage unless the storage location and removal process are clear. <br>
Risk: Using the skill sends YouTube video URLs or IDs to TranscriptAPI and requires an API key available to the agent. <br>
Mitigation: Use the skill only for videos you are comfortable sharing with TranscriptAPI, scope access to the required TRANSCRIPT_API_KEY, and rotate or revoke the key if exposure is suspected. <br>


## Reference(s): <br>
- [TranscriptAPI](https://transcriptapi.com) <br>
- [Authentication Setup](references/auth-setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON or plain-text transcript responses from TranscriptAPI] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires TRANSCRIPT_API_KEY and internet access to transcriptapi.com; API requests include a User-Agent header.] <br>

## Skill Version(s): <br>
1.5.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
