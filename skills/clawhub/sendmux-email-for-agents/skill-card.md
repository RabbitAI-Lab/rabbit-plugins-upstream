## Description: <br>
Give OpenClaw agents a Sendmux inbox to receive, triage, route, reply to, and send email with owner approval and scoped credentials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sendmux.ai](https://clawhub.ai/user/sendmux.ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to route agent-email tasks to the right Sendmux setup, mailbox, sending, attachment, CLI, MCP, or token-efficiency workflow while preserving approval and credential boundaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive email, mailbox access, API keys, agent tokens, and one-time registration credentials. <br>
Mitigation: Use secure credential storage, scoped tokens, and the skill's instruction not to paste secrets into chat, logs, files, screenshots, or memory-only state. <br>
Risk: Outbound email or destructive mailbox changes could occur without the intended owner's approval. <br>
Mitigation: Require explicit user confirmation before sending email, changing labels or read state, deleting mail, revoking keys, suspending mailboxes, or resuming mailboxes. <br>
Risk: Attachments can expose sensitive content or consume excessive context if copied into chat. <br>
Mitigation: Use Sendmux attachment workflows with local paths, presigned URLs, CLI or SDK helpers, and documented size limits instead of placing attachment bytes or long base64 in chat. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sendmux.ai/skills/sendmux-email-for-agents) <br>
- [Sendmux skills repository](https://github.com/Sendmux/skills) <br>
- [Sendmux agent auth discovery](https://app.sendmux.ai/auth.md) <br>
- [Sendmux API resource](https://smtp.sendmux.ai/api/v1) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown guidance with route recommendations, scoped credential notes, API call names, and command references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user approval before outbound sends or destructive mailbox changes.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter reports 1.3.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
