## Description: <br>
Monitors DingTalk unread conversations, sends AI-generated replies in the user's own employee voice for one-to-one chats, and sends WeChat notifications for group chats or configured contacts without auto-replying. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[noaheleven](https://clawhub.ai/user/noaheleven) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees who use DingTalk can deploy this skill to monitor unread chats, draft and send one-to-one replies in their own voice, and route higher-risk group or configured-contact messages to WeChat for manual handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run persistently and send DingTalk replies as the configured user. <br>
Mitigation: Review .env settings before live use, validate behavior with DRY_RUN or TEST_MODE, and enable Startup persistence only after accepting the watchdog behavior. <br>
Risk: The reply agent may access local tools, workplace data, and optional local code search paths. <br>
Mitigation: Leave CODE_SEARCH_ROOTS unset unless needed and restrict tool access with DINGTALK_AGENT_DISALLOWED_TOOLS, including Bash/Web/Read/Grep/Glob where appropriate. <br>
Risk: Work chat content, identity settings, and authentication material are sensitive. <br>
Mitigation: Keep .env private, avoid distributing generated runtime files, and review audit logs for auto-replies and skipped actions. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/noaheleven/skills/dingtalk-auto-reply) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [Tencent CodeBuddy](https://copilot.tencent.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [DingTalk messages, WeChat notification text, Markdown documentation, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May send messages as the configured user when live mode is enabled; DRY_RUN and TEST_MODE support validation without sending to the original sender.] <br>

## Skill Version(s): <br>
0.1.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
