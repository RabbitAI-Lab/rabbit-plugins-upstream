## Description:

Monitors selected Feishu, WeCom, or DingTalk conversations and wakes an agent when matching messages arrive, with setup, style-learning, health-check, and recovery guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[buger-gif](https://clawhub.ai/user/buger-gif)

### License/Terms of Use:

MIT

## Use Case:

External users and teams can use this skill to monitor selected workplace chats and have an agent draft or send replies as the account holder. It also guides setup, style learning from selected conversations, and troubleshooting for the supported messaging platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Contact lookup can read unrelated chats.

Mitigation: Supply exact conversation IDs for monitoring.

Risk: Authorization safeguards can overlook or misrepresent added permissions.

Mitigation: Before automatic reauthorization, correct the permission-discovery handling and authorization-card text, then verify permissions on the provider's consent screen.

Risk: Chat-derived profiles persist locally until deleted.

Mitigation: Review stored profiles and delete local chat-derived data when it is no longer needed.

Risk: Replies sent as the account holder can have external consequences.

Mitigation: Keep reply approval enabled and set a stop time for monitoring.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/buger-gif/skills/cyber-im-avatar)
- [GitHub source at the server-resolved release commit](https://github.com/buger-gif/cyber-im-avatar/tree/7fe66acb0c424b07e93780baeb841b93102a9c17)
- [Feishu setup and platform notes](https://github.com/buger-gif/cyber-im-avatar/blob/7fe66acb0c424b07e93780baeb841b93102a9c17/references/feishu.md)
- [WeCom setup and platform notes](https://github.com/buger-gif/cyber-im-avatar/blob/7fe66acb0c424b07e93780baeb841b93102a9c17/references/wecom.md)
- [DingTalk setup and platform notes](https://github.com/buger-gif/cyber-im-avatar/blob/7fe66acb0c424b07e93780baeb841b93102a9c17/references/dingtalk.md)
- [Troubleshooting guide](https://github.com/buger-gif/cyber-im-avatar/blob/7fe66acb0c424b07e93780baeb841b93102a9c17/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Text]

**Output Format:** [Markdown guidance, shell commands, configuration examples, JSON message events, and draft replies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Replies are drafted for review by default; automatic sending requires explicit authorization.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
