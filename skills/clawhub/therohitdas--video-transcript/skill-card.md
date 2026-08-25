## Description: <br>
Extracts transcripts from YouTube videos and Shorts through TranscriptAPI.com so agents can summarize, quote, translate, or inspect video content as text. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[therohitdas](https://clawhub.ai/user/therohitdas) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, employees, and external users can use this skill when an agent needs to retrieve YouTube transcript text, timestamps, and metadata for summarization, quotation, translation, or information extraction. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Video URLs or IDs submitted through the skill are sent to TranscriptAPI.com. <br>
Mitigation: Use the skill only for video links you are comfortable sharing with TranscriptAPI.com, and avoid submitting private or sensitive video URLs. <br>
Risk: The setup flow can make a TranscriptAPI key available to the agent for reuse. <br>
Mitigation: Prefer entering the key through a secure secret mechanism, rotate or remove the key when it is no longer needed, and review where the agent persists environment variables. <br>
Risk: The account setup guide can involve sharing an OTP through the agent. <br>
Mitigation: Prefer creating the TranscriptAPI account yourself, or share one-time verification codes through the agent only when you accept that workflow. <br>


## Reference(s): <br>
- [TranscriptAPI](https://transcriptapi.com) <br>
- [TranscriptAPI Authentication Setup](references/auth-setup.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/therohitdas/skills/video-transcript) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, configuration, guidance] <br>
**Output Format:** [Markdown guidance with HTTP API examples; API responses are text or JSON transcripts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires TRANSCRIPT_API_KEY; sends requested YouTube video URLs or IDs to TranscriptAPI.com; successful requests consume 1 credit.] <br>

## Skill Version(s): <br>
1.5.0 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
