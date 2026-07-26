## Description: <br>
通过 WorkBuddy 已连接的 ClawBot 微信 bot 通道主动向指定微信收件人发送文本、图片、文件和视频。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[noaheleven](https://clawhub.ai/user/noaheleven) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and WorkBuddy operators use this skill when an agent needs to send explicit ClawBot WeChat notifications, status updates, or media attachments to a configured recipient using local WorkBuddy credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send real WeChat messages and media outward using local ClawBot credentials. <br>
Mitigation: Install only for intentional outbound WeChat notification use, review the configured recipient before use, and require explicit confirmation before every send. <br>
Risk: The skill reads local WorkBuddy bot credentials and cursor state that may contain sensitive tokens. <br>
Mitigation: Do not share settings.json or claw-state cursor files, keep token values out of logs and prompts, and use only the local credential files for the intended account. <br>
Risk: Network sending may require relaxed sandboxing, increasing the impact of unintended execution. <br>
Mitigation: Avoid disabling sandbox protections except for a narrow, trusted run and only after verifying the recipient and message content. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/noaheleven/skills/weixinclawbot) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and command-line status output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May trigger outbound WeChat text or media sends through local WorkBuddy ClawBot credentials.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
