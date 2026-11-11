## Description:

用钉钉给自己/同事发通知与私信：工作通知（应用消息）、机器人单聊私信、以本人身份私信，支持 text/markdown/文件，失败自动留痕。当需要「钉钉通知 / 钉钉私信 / 工作通知 / 机器人消息 / 把结果推到钉钉 / dingtalk notify / 配置钉钉企业内部应用 AppKey」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[hero81yf](https://clawhub.ai/user/hero81yf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to send work notifications, direct messages, and files to DingTalk colleagues through an enterprise app.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan marks the release suspicious because of a high-confidence concern that the DingTalk app secret in a request URL could be exposed in error logs; the scan was partial.

Mitigation: Follow the scanner guidance and review this concern before installing. If the app secret may have been exposed, rotate it and check relevant logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hero81yf/skills/dtflow-notify)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands]

**Output Format:** [Text, Markdown, or file notifications sent through DingTalk]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports work notifications, direct messages, and file attachments.]

## Skill Version(s):

0.1.0 (source: release evidence, frontmatter, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
