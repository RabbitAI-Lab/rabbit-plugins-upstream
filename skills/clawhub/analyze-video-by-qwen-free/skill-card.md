## Description: <br>
Analyze Video By Qwen Free uses Qwen 3.5 Plus through Alibaba Cloud DashScope to summarize and describe local video files with fixed default analysis settings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Creators and agent users use this skill to get quick scene descriptions and content summaries for local video files. It is intended for default-parameter video overviews, not remote URL analysis, custom prompts, custom frame rates, high-precision action recognition, or content moderation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Analyzed video content may be sent to Alibaba Cloud DashScope. <br>
Mitigation: Use the skill only for videos whose confidentiality, privacy, and regulatory requirements are compatible with the provider's data handling terms. <br>
Risk: The documented API-key check could display or log the DashScope API key. <br>
Mitigation: Check configuration without printing the secret value, and avoid sharing API keys in chat, logs, or command output. <br>


## Reference(s): <br>
- [SkillHub homepage](https://skillhub.cn) <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/analyze-video-by-qwen-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON-shaped result examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require local DashScope API-key configuration and may send analyzed video content to Alibaba Cloud DashScope.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
