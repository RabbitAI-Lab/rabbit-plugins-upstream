## Description:

Answer questions from the owner's Telegram history, and read or send messages in their personal account, through tg.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Telegram account owners and their agents use this skill to find answers in chat history, inspect message context, manage setup, and carry out explicitly requested account actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill's documented reach can extend from Telegram chats to notes, Drive content, task and contact metadata, and broad bot operations.

Mitigation: Enable only integrations needed for the task and review the MCP permission setup, including how approval is enforced.

Risk: Sending, editing, forwarding, or deleting content can affect a live Telegram account; approval prompts may depend on the MCP client.

Mitigation: Require the owner's explicit request for the specific action and target, and confirm that the client enforces any configured approval step.

Risk: The security scan is incomplete because two local references could not be resolved.

Mitigation: Resolve and review the missing references, then repeat the security review before deployment.

## Reference(s):

- [Tg Cli on ClawHub](https://clawhub.ai/wirecat/skills/wirecat-tg)
- [@wirecat/tg-cli package](https://www.npmjs.com/package/@wirecat/tg-cli)
- [Search guidance](artifact/references/search.md)
- [Message actions and boundaries](artifact/references/messages.md)
- [MCP and bot guidance](artifact/references/mcp-and-bots.md)
- [Setup and command behavior](artifact/references/setup.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Text or Markdown, with Telegram CLI command examples and message references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers may include message locators and dates; search coverage can be partial.]

## Skill Version(s):

1.0.8 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
