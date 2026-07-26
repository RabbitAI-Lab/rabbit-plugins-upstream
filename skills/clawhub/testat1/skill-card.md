## Description: <br>
Use when you need to control Slack from Clawdbot via the slack tool, including reacting to messages or pinning/unpinning items in Slack channels or DMs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chaunceyliu](https://clawhub.ai/user/chaunceyliu) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to let an agent perform Slack workspace actions such as reacting to, reading, sending, editing, deleting, pinning, and unpinning messages, plus fetching member and emoji information. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent Slack message-changing powers, including sending, editing, deleting, pinning, and unpinning messages. <br>
Mitigation: Require explicit user confirmation before message-changing actions and restrict the bot to intended channels where possible. <br>
Risk: The skill can read Slack messages and member details that may contain sensitive workspace information. <br>
Mitigation: Use a least-privilege Slack bot token and require explicit confirmation before reading sensitive Slack messages or member details. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chaunceyliu/skills/testat1) <br>
- [Publisher profile](https://clawhub.ai/user/chaunceyliu) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Configuration] <br>
**Output Format:** [Markdown with JSON action examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces Slack action payloads for the configured slack tool; explicit confirmation is recommended for message-changing or sensitive read actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
