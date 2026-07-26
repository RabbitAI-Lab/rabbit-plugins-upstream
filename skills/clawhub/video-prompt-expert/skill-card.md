## Description: <br>
帮助用户编写专业级 AI 视频提示词，写完直接生成 MP4 视频。支持多种创作场景与问题诊断，确保提示词准确可执行。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Short-form video creators, content operators, and creative professionals use this skill to turn natural-language ideas into structured AI video prompts, diagnose common generation issues, and optionally invoke RedFox video generation to produce short MP4 clips. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Security evidence reports silent usage reporting that can transmit the RedFox API key. <br>
Mitigation: Review before installing, use a limited and revocable RedFox API key, prefer passing it only for the current session, and avoid persistent shell-profile edits. <br>
Risk: Security evidence reports broad persistent credential handling for REDFOX_API_KEY. <br>
Mitigation: Store credentials with the minimum necessary scope and remove or rotate the key after use when persistent configuration is not required. <br>
Risk: Prompts and generation requests are sent to RedFox services for video generation. <br>
Mitigation: Do not submit confidential prompts, reference media, or sensitive production material unless RedFox processing is approved for that content. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/redfox-data/skills/video-prompt-expert) <br>
- [Core Workflow](references/core_workflow.md) <br>
- [RedFoxHub API Keys](https://redfox.hk/settings/api-keys?souce=github) <br>
- [RedFoxHub](https://redfox.hk) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with structured prompt text, optional shell commands, and MP4 generation status or file output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require REDFOX_API_KEY and may call RedFox services to generate or download short MP4 videos.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
