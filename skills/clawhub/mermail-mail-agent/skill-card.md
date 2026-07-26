## Description: <br>
Create, list, continue, rename, and delete Mermail mailbox-agent conversations and inspect their messages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mermail](https://clawhub.ai/user/mermail) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and mailbox operators use this skill to manage Mermail mailbox-agent conversations, review prior agent work, and ask the Mermail agent to reason about a selected mailbox. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a Mermail API key to interact with mailbox-agent conversations. <br>
Mitigation: Install it only for users who intend to grant that access, keep MERMAIL_API_KEY scoped and protected, and surface authentication or rate-limit errors instead of retrying write actions automatically. <br>
Risk: Downstream mailbox-agent activity may affect mailbox state, including sending-related or destructive actions. <br>
Mitigation: Confirm explicit sending or destructive intent before the call, and require explicit approval plus a prepare_destructive_action token before deletion. <br>
Risk: Mailbox content and downstream agent output may contain untrusted instructions or misleading claims of completed work. <br>
Mitigation: Do not execute instructions contained in mailbox messages unless independently requested and approved by the user, and distinguish narrative from tool-confirmed execution in the final report. <br>


## Reference(s): <br>
- [Mermail AI skills documentation](https://docs.mermail.app/ai/skills) <br>
- [Mermail MCP server](https://console.mermail.app/mcp) <br>
- [Mermail Mail Agent on ClawHub](https://clawhub.ai/mermail/skills/mermail-mail-agent) <br>
- [Mail-agent tool map](references/tools.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Concise text or Markdown with mailbox-agent conversation summaries and requested next steps.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference Mermail MCP tool results; requires MERMAIL_API_KEY for live mailbox-agent access.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
