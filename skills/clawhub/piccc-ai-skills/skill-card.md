## Description: <br>
Generate images, videos, and audio with Piccc AI (皮可AI), or query and download existing media tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xiaoyaocz](https://clawhub.ai/user/xiaoyaocz) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to authorize a Piccc AI account, discover available media models or voices, create image, video, and audio tasks, monitor task status, and download completed outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses the user's Piccc AI account and credits for media generation. <br>
Mitigation: Review task cost settings before submission; the skill defaults to economy models and reports available credits after authorization. <br>
Risk: Authorization creates a local API key for future Piccc AI requests. <br>
Mitigation: Authorize only through the expected browser flow and use `auth logout` to remove the saved local API key when access is no longer wanted. <br>
Risk: Paid asynchronous media tasks may be slow, fail, or time out. <br>
Mitigation: Use task IDs to resume status checks, wait for `completed` status before claiming success, and warn users before using special-offer models. <br>


## Reference(s): <br>
- [Piccc AI media API reference](references/api.md) <br>
- [Piccc AI](https://picccai.cn) <br>
- [ClawHub skill release](https://clawhub.ai/xiaoyaocz/skills/piccc-ai-skills) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/xiaoyaocz) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON command results; generated media may be downloaded as files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live Piccc AI model responses and task status before reporting or downloading results.] <br>

## Skill Version(s): <br>
0.1.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
