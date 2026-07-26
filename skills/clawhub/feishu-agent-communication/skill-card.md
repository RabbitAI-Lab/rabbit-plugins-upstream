## Description: <br>
Guides agents through configuring Feishu group chat so multiple AI agents can collaborate by mutual @ mentions using text messages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhouxin121](https://clawhub.ai/user/zhouxin121) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to set up Feishu groups, bot apps, permissions, open_id discovery, text-format @ mentions, and troubleshooting for multi-agent collaboration in group chat. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Feishu App Secret and open_id values can expose bot access or user identity context if mishandled. <br>
Mitigation: Protect secrets and open_id values, share them only with the intended agents, and rotate credentials if they are exposed. <br>
Risk: Configured bots can post messages into the Feishu group. <br>
Mitigation: Limit each bot to the intended group and keep broad group-message permissions disabled unless explicitly needed. <br>
Risk: Incorrect message format or permission settings can cause agents to miss @ mentions or receive unintended group traffic. <br>
Mitigation: Use text messages with raw <at user_id="ou_xxx"> tags, verify event subscriptions, and keep group_msg disabled for @-only behavior. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/zhouxin121/skills/feishu-agent-communication) <br>
- [Server-resolved GitHub source](https://github.com/zhouxin121/feishu-agent-communication) <br>
- [Feishu developer documentation](https://open.feishu.cn/document/home/index) <br>
- [Feishu message content documentation](https://open.feishu.cn/document/server-docs/im-v1/message-content-description/create-content) <br>
- [Feishu send message API](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/message/send) <br>
- [Feishu event subscription guide](https://open.feishu.cn/document/server-docs/event-subscription-guide/overview) <br>
- [OpenClaw documentation](https://docs.openclaw.ai/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance with tables and inline API parameters] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Covers Feishu bot setup, permission choices, open_id handling, @ mention formatting, validation steps, and troubleshooting.] <br>

## Skill Version(s): <br>
0.1.0 (source: release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
