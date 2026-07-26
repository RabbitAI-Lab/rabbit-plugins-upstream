## Description: <br>
Smart Message Plus is a cross-platform enterprise messaging skill for sending user-provided DingTalk, Feishu/Lark, and WeCom webhook messages with aliases, templates, media, recall, onboarding, and configurable safety gates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[songhonglei](https://clawhub.ai/user/songhonglei) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operations teams, and agent users use this skill to configure enterprise messaging providers and send user-supplied P2P, group, media, card, and broadcast messages through a unified CLI. It is suited for controlled operational notifications where dry-run previews, contact aliases, and approval gates are needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send and recall enterprise messages, create some chat groups, and perform broad broadcasts through configured messaging providers. <br>
Mitigation: Use dry-run before broad sends, keep safety_gate enabled, configure approval admins carefully, and require force or approval codes above the configured thresholds. <br>
Risk: Messaging credentials, local configuration, approval codes, and send logs with message previews may be sensitive. <br>
Mitigation: Protect the data directory, restrict filesystem access to credential and log files, and avoid placing secrets or confidential message content in shared workspaces. <br>
Risk: Approval workflows can expose message previews to configured administrators. <br>
Mitigation: Send confidential content through approval workflows only when those administrators are authorized to view the preview, or reduce message sensitivity before requesting approval. <br>
Risk: AI-generated or modified outbound message content could create unauthorized communications. <br>
Mitigation: Require the user to provide message content explicitly; allow autonomous test content only when the user authorizes self-testing to the user's own account. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/songhonglei/skills/smart-message-plus) <br>
- [Provider Capability Matrix](references/provider-matrix.md) <br>
- [Console Setup Guide](references/console-setup.md) <br>
- [Org Lookup Contract](references/org-lookup-contract.md) <br>
- [Design Document](docs/design.md) <br>
- [Add Channel Guide](docs/add-channel.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI command examples, configuration snippets, terminal text, and JSONL send or audit logs when executed.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill can execute messaging API actions through configured provider credentials; dry-run previews are available before broad sends.] <br>

## Skill Version(s): <br>
2.1.0 (source: server release metadata, target metadata, and SKILL.md) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
