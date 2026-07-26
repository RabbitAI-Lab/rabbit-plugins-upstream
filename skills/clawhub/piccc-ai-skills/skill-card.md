## Description: <br>
Generate images, videos, and audio with Piccc AI, or query and download existing media tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xiaoyaocz](https://clawhub.ai/user/xiaoyaocz) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to have an agent create Piccc AI image, video, and audio tasks, monitor asynchronous task status, and download completed outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill accesses a Piccc AI account and can create paid media-generation tasks. <br>
Mitigation: Install it only when that access is intended, review generation requests before submission, and use task-status commands rather than creating replacement tasks while waiting. <br>
Risk: A local API key is saved after login. <br>
Mitigation: Use the provided logout command when access is no longer needed, or rotate the key in Piccc AI if the local environment is no longer trusted. <br>
Risk: Generated media files are written to local storage. <br>
Mitigation: Download outputs into a dedicated folder selected for the task. <br>
Risk: Special-offer models may be slower or less stable. <br>
Mitigation: Warn the user before creating a paid task when a selected model is marked as a special offer. <br>


## Reference(s): <br>
- [Piccc AI Media API](references/api.md) <br>
- [Piccc AI](https://picccai.cn) <br>
- [ClawHub Skill Page](https://clawhub.ai/xiaoyaocz/skills/piccc-ai-skills) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, JSON, Files, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON task responses, and downloaded media files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include generated image, video, or audio files downloaded to a user-selected directory.] <br>

## Skill Version(s): <br>
0.1.2 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
