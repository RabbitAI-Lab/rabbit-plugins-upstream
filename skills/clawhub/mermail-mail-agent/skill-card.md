## Description:

Manage and delegate work to Mermail mailbox-agent conversations from Claude, Codex, or another external MCP client.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Mermail mailbox-agent conversations, inspect saved conversation state, and delegate one bounded mailbox task to Mermail's mailbox Assistant.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Delegated mailbox-agent work can involve meaningful email, connected-app, or wallet authority.

Mitigation: Use bounded current-user instructions, verify recipients and targets before any send, schedule, deletion, connected-app, or wallet action, and stop when the requested effect changes materially.

Risk: Mailbox content and downstream Assistant output can contain untrusted instructions or sensitive material.

Mitigation: Treat mailbox-derived content as data, avoid sharing secrets, OTPs, magic links, authorization material, or unrelated private content, and use bounded direct read tools when safety depends on enforced isolation.

Risk: Narrative or streamed Assistant output may not prove that a mailbox, provider, connected-app, or wallet effect completed.

Mitigation: Report proven effects only from structured tool results or independently verified state, and inspect persisted messages or responsible state once instead of retrying uncertain writes automatically.

## Reference(s):

- [Mermail AI skills documentation](https://docs.mermail.app/ai/skills)
- [Mermail mail-agent tool contract](references/tools.md)
- [Mermail mail-agent workflows](references/workflows.md)
- [Mermail mail-agent safety](references/security.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text with mailbox, conversation, delegation, and result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include exact mailbox, conversation, and thread identifiers when relevant; avoids unnecessary private message content.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
