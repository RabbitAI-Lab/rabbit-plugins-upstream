## Description: <br>
Audio Stream Upload helps agents prepare Python and curl workflows for batch audio uploads, chunked uploads, custom encoding settings, multi-quality HLS or DASH outputs, and metadata management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, platform operators, and professional audio teams use this skill to generate upload workflows for moving audio files and metadata into a streaming service with configurable quality profiles. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send local audio, metadata, and API secrets to a hardcoded third-party streaming service. <br>
Mitigation: Use it only when the user trusts the streaming service, intends to upload the selected files there, and is authorized to share the audio, metadata, and API credentials. <br>
Risk: Confidential, regulated, copyrighted, or internal audio may be uploaded outside the user's environment. <br>
Mitigation: Review selected files and metadata before execution and avoid using the skill for sensitive audio unless sharing with the service is approved. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/audio-stream-upload) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with Python and bash code blocks plus JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include upload configuration, API credential headers, metadata examples, status output, and troubleshooting guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
