## Description:

Monitors unread DingTalk conversations and uses AI to send one-to-one replies as the user while routing group chats and configured contacts to WeChat notifications instead of auto-sending.

This skill is ready for commercial/non-commercial use.

## Publisher:

[noaheleven](https://clawhub.ai/user/noaheleven)

### License/Terms of Use:

MIT-0

## Use Case:

Employees who use DingTalk can use this skill to monitor unread direct messages, generate in-character replies, notify through WeChat for group or skipped conversations, and validate or recover missed messages during setup and operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent operation can auto-send DingTalk messages as the user.

Mitigation: Start with DRY_RUN or TEST_MODE, review generated replies and audit logs, and enable live sending only after confirming the account behavior is acceptable.

Risk: Chat-triggered agents can receive broad local and account access through configured DingTalk, CodeBuddy, gbrain, PATH, and Startup integrations.

Mitigation: Keep optional code search and group reply preview features disabled unless needed, confirm all requested DingTalk permissions and persistence changes, and avoid disabling sandboxing.

Risk: Local persona, environment, and private few-shot files may contain sensitive identity or organizational context.

Mitigation: Review local dingtalk-helper.md, .env, and private few-shot files before deployment or redistribution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/noaheleven/skills/dingtalk-auto-reply)
- [CodeBuddy Console](https://copilot.tencent.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated chat reply text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can run persistently and may send DingTalk messages when configured for live operation.]

## Skill Version(s):

0.1.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
