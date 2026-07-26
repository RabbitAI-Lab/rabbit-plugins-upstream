## Description: <br>
Helps an agent send proactive text, image, file, and video messages through a configured WorkBuddy ClawBot WeChat bot channel using the documented ilink bot flow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[noaheleven](https://clawhub.ai/user/noaheleven) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill when an agent needs to prepare or run WorkBuddy ClawBot WeChat push workflows for a configured recipient. It is intended for sending messages and attachments through the user's own local WorkBuddy credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is designed to send WeChat messages and attachments externally using local WorkBuddy credentials. <br>
Mitigation: Install only for agents that should send through the configured ClawBot channel, keep local settings and cursor files private, and require explicit confirmation before sending. <br>
Risk: Server security evidence reports broad send triggers and no clear confirmation step. <br>
Mitigation: Gate message and attachment sends behind user approval and review the recipient, content, and attachment paths before execution. <br>
Risk: Server security guidance flags missing send.js provenance in the provided artifact. <br>
Mitigation: Verify the runtime script provenance and contents before deployment. <br>
Risk: Network access or sandbox bypass may be needed to reach WeChat and CDN endpoints. <br>
Mitigation: Allow outbound network access only after confirming the destination and operational need. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/NoahEleven/weixinclaw-proactive-push) <br>
- [ClawHub skill page](https://clawhub.ai/noaheleven/skills/weixinclaw-proactive-push) <br>
- [Tencent WeChat ilink bot API base](https://ilinkai.weixin.qq.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May describe WeChat text, image, file, and video send operations that rely on local WorkBuddy credentials.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
