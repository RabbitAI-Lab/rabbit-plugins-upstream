## Description:

Operates existing DingTalk documents specified by a user URL or docKey, including reading, overwriting, inserting, modifying, and deleting content blocks while excluding document creation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shyzhen](https://clawhub.ai/user/shyzhen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill to let agents manage existing DingTalk documents through an enterprise DingTalk app. Operations are scoped to documents identified by the user and to the current user's DingTalk permissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents can overwrite full documents or delete content blocks.

Mitigation: Review the exact document URL and block structure before overwrite or delete operations, and confirm ambiguous targets before execution.

Risk: The local operator fallback can execute under an unintended identity if used in production.

Mitigation: Do not configure DINGTALK_OPERATOR_ID in production; rely on OPENCLAW_SENDER_ID or DINGTALK_SENDER_ID for the current user identity.

Risk: DingTalk credentials with write permission can modify documents the current user can access.

Mitigation: Protect the enterprise app credentials, grant only required DingTalk permissions, and review agent actions before enabling write operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/shyzhen/skills/dingtalk-doc-enterprise)
- [DingTalk OpenClaw connector issue 456](https://github.com/DingTalk-Real-AI/dingtalk-openclaw-connector/issues/456)
- [DingTalk connector Docs and MCPDocs reference](https://github.com/DingTalk-Real-AI/dingtalk-openclaw-connector?tab=readme-ov-file#%E9%92%89%E9%92%89%E6%96%87%E6%A1%A3docs%E4%B8%8E-mcpdocs)
- [Whitelist-controlled DingTalk document skill](https://clawhub.ai/shyzhen/dingtalk-doc)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with Node.js command examples and DingTalk document operation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and DingTalk enterprise app credentials in DINGTALK_CLIENTID and DINGTALK_CLIENTSECRET.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
