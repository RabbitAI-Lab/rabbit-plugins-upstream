## Description: <br>
Guides an agent through Feishu Open Platform workflows for sending messages, finding chats and members, and uploading message images or files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jypjypjypjyp](https://clawhub.ai/user/jypjypjypjyp) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to have an agent prepare Feishu API calls for finding chats or members, sending text messages, and uploading images or files to Feishu. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Messages, images, or files can be sent to Feishu recipients when examples are executed with live credentials. <br>
Mitigation: Confirm the recipient, message text, and exact file path before any send or upload action. <br>
Risk: Feishu app secrets may be exposed if credentials are pasted into shared chats or logs. <br>
Mitigation: Keep app secrets out of shared agent conversations and logs, and provide them only through the user's approved secret-handling mechanism. <br>
Risk: Chat and member lookup workflows can expose Feishu workspace data. <br>
Mitigation: Use least-privilege Feishu app scopes and only enable the read scopes needed for the intended workflow. <br>


## Reference(s): <br>
- [Feishu Open Platform API documentation](https://open.feishu.cn/document/server-docs/api-call-guide/server-api-list) <br>
- [ClawHub release page](https://clawhub.ai/jypjypjypjyp/skills/feishu-messaging) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, configuration] <br>
**Output Format:** [Markdown with Python code blocks and Feishu API parameters] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-provided Feishu app credentials, scopes, recipient identifiers, message content, and file paths before execution.] <br>

## Skill Version(s): <br>
0.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
