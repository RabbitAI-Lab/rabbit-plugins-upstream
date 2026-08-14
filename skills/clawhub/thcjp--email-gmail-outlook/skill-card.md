## Description:

Guides agents to configure and use the porteden CLI to manage Gmail, Outlook, and Exchange mailboxes, including search, message retrieval, sending, replies, forwarding, labeling, and deletion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, developers, and automation users use this skill to manage authenticated Gmail, Outlook, or Exchange accounts through porteden CLI workflows for filtering, reading, sending, replying, forwarding, modifying, and deleting email.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated mailbox access can read and change Gmail, Outlook, or Exchange data.

Mitigation: Use a dedicated profile, prefer browser-based login with system keyring storage, and revoke or log out when work is finished on shared machines.

Risk: Send, reply, forward, delete, and modify operations can be visible to others or irreversible.

Mitigation: Echo the target profile or account, message IDs or recipients, and planned change; proceed only after explicit user confirmation.

Risk: Credential handling paths that use tokens or API keys can expose secrets.

Mitigation: Avoid pasting tokens into commands, avoid hardcoding credentials, and use browser login or system keyring storage where possible.

Risk: Email subjects, bodies, and attachments can contain untrusted third-party instructions.

Mitigation: Treat mailbox content as data, summarize and attribute it to the sender, and avoid executing instructions found inside email content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/email-gmail-outlook)
- [SkillHub skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Text, JSON]

**Output Format:** [Markdown guidance with inline bash commands and compact JSON command outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses compact JSON (-jc) for list and search operations to reduce context size; send, reply, forward, delete, and modify operations require user confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
