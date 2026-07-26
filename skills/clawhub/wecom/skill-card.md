## Description: <br>
Send messages to WeCom (企业微信) via webhooks using MCP protocol. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qidu](https://clawhub.ai/user/qidu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to let an MCP-compatible agent send selected text or markdown updates to WeCom group chats through an incoming webhook. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Messages are sent to a configured WeCom webhook and may expose selected agent content outside the local agent session. <br>
Mitigation: Send only content approved for the destination WeCom chat, and avoid secrets, credentials, regulated data, and private prompts unless that use is explicitly approved. <br>
Risk: The WeCom webhook URL is a credential-like secret that can allow unauthorized posting if exposed. <br>
Mitigation: Keep WECOM_WEBHOOK_URL out of logs, screenshots, source control, and shared configuration files. <br>
Risk: Dependency hygiene needs review before deployment. <br>
Mitigation: Review dependency versions and the lockfile before installing or deploying the skill. <br>


## Reference(s): <br>
- [ClawHub Wecom Skill](https://clawhub.ai/qidu/skills/wecom) <br>
- [WeCom Group Chat Message API](https://developer.work.weixin.qq.com/document/path/99110) <br>
- [WeCom Apps](https://work.weixin.qq.com/#indexDownload) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API Calls] <br>
**Output Format:** [MCP tool responses and WeCom text or markdown webhook messages] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports plain text, markdown, and markdown_v2 messages; requires WECOM_WEBHOOK_URL.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact package metadata reports 1.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
