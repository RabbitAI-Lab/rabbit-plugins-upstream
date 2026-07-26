## Description: <br>
Monitors unread DingTalk conversations, uses AI to draft and send direct-message replies in the configured user's voice, and sends WeChat notifications for group or selected-message cases. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[noaheleven](https://clawhub.ai/user/noaheleven) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees or operators use this skill to run a personal DingTalk assistant that monitors unread chats, auto-replies to direct messages when configured, and escalates group or sensitive cases through WeChat notification. Developers may also use it as deployment guidance for configuring dws, CodeBuddy Agent SDK, environment variables, validation, and background startup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run as a persistent background DingTalk assistant that reads unread chats and sends replies as the user. <br>
Mitigation: Install it only when that behavior is intended, begin with DRY_RUN, confirm DingTalk send permissions, and review audit logs before enabling real automatic replies. <br>
Risk: Startup launcher or PATH changes can affect how the monitor runs and what local tools it can invoke. <br>
Mitigation: Verify the exact scripts from the server-resolved source repository and check any Startup launcher or PATH changes before enabling background execution. <br>
Risk: Automatic replies may be sent to inappropriate contacts or duplicate/self conversations if configuration is wrong. <br>
Mitigation: Use skip lists, identity configuration, delayed reply behavior, and audit logs before enabling live replies. <br>


## Reference(s): <br>
- [Server-resolved GitHub source](https://github.com/NoahEleven/dingtalk-auto-reply) <br>
- [ClawHub skill page](https://clawhub.ai/noaheleven/skills/dingtalk-auto-reply) <br>
- [Publisher profile](https://clawhub.ai/user/noaheleven) <br>
- [CodeBuddy console](https://copilot.tencent.com) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes operational guidance for dry-run validation, background startup, audit logs, DingTalk permissions, and optional notification/image handling.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
