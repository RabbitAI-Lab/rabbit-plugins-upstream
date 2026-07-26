## Description: <br>
Azure Ai Transcription Py Free guides agents through batch speech-to-text transcription with Azure AI Speech, Blob audio URLs, locale selection, and subscription-key authentication. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to configure Azure AI transcription resources, submit batch transcription jobs for Blob-hosted audio, choose a recognition locale, and retrieve transcript results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audio recordings and generated transcripts can contain sensitive content. <br>
Mitigation: Treat recordings and transcripts as sensitive data, limit access to them, and delete temporary blobs or transcripts when they are no longer needed. <br>
Risk: Public audio URLs or broad SAS URLs can expose source recordings beyond the intended transcription workflow. <br>
Mitigation: Prefer private Blob containers and use short-lived, read-only SAS URLs instead of public access where possible. <br>
Risk: Azure transcription subscription keys could be leaked through source control, prompts, logs, or copied commands. <br>
Mitigation: Keep TRANSCRIPTION_KEY out of source control and rotate the key promptly if exposure is suspected. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/azure-ai-transcription-py-free) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands, Python code examples, and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include environment variable setup, Azure batch transcription code, result-handling guidance, troubleshooting steps, and JSON-shaped output examples.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
