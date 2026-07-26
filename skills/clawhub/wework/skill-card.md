## Description: <br>
Enterprise WeCom group robot tooling and server API guidance for sending text, markdown, images, and files from agents and automation workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhangifonly](https://clawhub.ai/user/zhangifonly) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and automation agents use this skill to send WeCom group notifications, markdown reports, images, and file attachments, and to get concise guidance for WeCom server-side API work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Webhook keys authorize sending to the configured WeCom group. <br>
Mitigation: Treat WECOM_WEBHOOK_KEY as a secret and scope it to the intended group robot. <br>
Risk: Markdown, images, and files selected by the user are transmitted to WeCom. <br>
Mitigation: Review message content and file paths before sending attachments or markdown reports. <br>
Risk: @all notifications and group messages can create broad disruption. <br>
Mitigation: Confirm the audience and mention target before sending group-wide notifications. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zhangifonly/skills/wework) <br>
- [WeCom webhook API endpoint](https://qyapi.weixin.qq.com/cgi-bin/webhook) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and CLI-generated JSON status output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can transmit user-selected text, markdown, image, and file content to WeCom through a webhook.] <br>

## Skill Version(s): <br>
2.0.0 (source: release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
